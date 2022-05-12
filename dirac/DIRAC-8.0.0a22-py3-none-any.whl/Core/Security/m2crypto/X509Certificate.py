""" X509Certificate is a class for managing X509 certificates

Proxy RFC: https://tools.ietf.org/html/rfc38200

X509RFC: https://tools.ietf.org/html/rfc5280

"""
import datetime
import os
import random
import time

import M2Crypto

from io import open

from DIRAC import S_OK, S_ERROR
from DIRAC.Core.Utilities import DErrno
from DIRAC.ConfigurationSystem.Client.Helpers import Registry
from DIRAC.Core.Security.m2crypto import asn1_utils
from DIRAC.Core.Utilities.Decorators import executeOnlyIf

# Decorator to execute the method only of the certificate has been loaded
executeOnlyIfCertLoaded = executeOnlyIf("_certLoaded", S_ERROR(DErrno.ENOCERT))


class X509Certificate(object):
    """The X509Certificate object represents ... a X509Certificate.

    It is a wrapper around a lower level implementation (M2Crypto in this case) of a certificate.
    In theory, tt can be a host or user certificate. Also, a proxy certificate is a X509Certificate,
    however it is useless without all the chain of issuers.
    That's why one has the X509Chain.

    In practice, X509Certificate is just used for checking  if the host certificate has expired.
    This class will most probably disappear once we get ride of pyGSI. After all, a X509Certificate
    is nothing but a X509Chain of length 1.

    Note that the SSL connection itself does not use this class, it gives directly the certificate to the library
    """

    def __init__(self, x509Obj=None, certString=None):
        """
        Constructor.
        You can give either nothing, or the x509Obj or the certString

        :param x509Obj: (optional) certificate instance
        :type x509Obj: M2Crypto.X509.X509
        :param certString: text representation of certificate
        :type certString: String

        """

        self._certLoaded = False
        if x509Obj:
            self.__certObj = x509Obj
            self._certLoaded = True
        elif certString:
            self.loadFromString(certString)

    # Pylint is surprisingly picky here, so remove that warning
    # pylint: disable=protected-access
    @classmethod
    def generateProxyCertFromIssuer(cls, x509Issuer, x509ExtensionStack, proxyKey, lifetime=3600):
        """This class method is meant to generate a new X509Certificate out of an existing one.
        Basically, it generates a proxy... However, you can't have a proxy certificate working on
        its own, you need all the chain of certificates. This method is meant to be called
        only by the X509Chain class.

        Inspired from https://github.com/eventbrite/m2crypto/blob/master/demo/x509/ca.py#L45

        :param x509Issuer: X509Certificate instance from which we generate the next one
        :param x509ExtensionStack: M2Crypto.X509.X509_Extension_Stack object to add to the new certificate.
                                   It contains all the X509 extensions needed for the proxy (e.g. DIRAC group).
                                   See ~X509Chain.__getProxyExtensionList
        :param proxyKey: a M2Crypto.EVP.PKey instance with private and public key
        :param lifetime: duration of the proxy in second. Default 3600


        :returns: a new X509Certificate

        """
        proxyCert = cls()

        proxyCert.__certObj = M2Crypto.X509.X509()

        # According to the proxy RFC, the serial
        # number just need to be uniqu among the proxy generated by the issuer.
        # The random module of python will be good enough for that
        serial = int(random.random() * 10**10)
        proxyCert.__certObj.set_serial_number(serial)

        # No easy way to deep-copy certificate subject, since they are swig object

        # We basically get a string like 'O=Dirac Computing, O=CERN, CN=MrUser'
        # So we split it, and then re-add each entry after the other.

        proxySubject = M2Crypto.X509.X509_Name()

        issuerSubjectObj = x509Issuer.__certObj.get_subject()
        issuerSubjectParts = issuerSubjectObj.as_text().split(", ")

        for isPart in issuerSubjectParts:
            nid, val = isPart.split("=", 1)
            proxySubject.add_entry_by_txt(field=nid, type=M2Crypto.ASN1.MBSTRING_ASC, entry=val, len=-1, loc=-1, set=0)

        # Finally we add a random Common Name  component. And we might as well use the serial.. :)
        proxySubject.add_entry_by_txt(
            field="CN", type=M2Crypto.ASN1.MBSTRING_ASC, entry=str(serial), len=-1, loc=-1, set=0
        )

        proxyCert.__certObj.set_subject(proxySubject)

        # We now add all the extensions we wish to add
        for extension in x509ExtensionStack:
            proxyCert.__certObj.add_ext(extension)

        proxyCert.__certObj.set_issuer(issuerSubjectObj)

        # According to the X509 RFC, we are safe if we just copy the version
        # number from the issuer certificate
        proxyCert.__certObj.set_version(x509Issuer.__certObj.get_version())

        proxyCert.__certObj.set_pubkey(proxyKey)

        # Set the start of the validity a bit in the past
        # to be sure to be able to use it right now
        proxyNotBefore = M2Crypto.ASN1.ASN1_UTCTIME()
        proxyNotBefore.set_time(int(time.time()) - 900)
        proxyCert.__certObj.set_not_before(proxyNotBefore)

        # Set the end date of the validity according to the lifetime
        proxyNotAfter = M2Crypto.ASN1.ASN1_UTCTIME()
        proxyNotAfter.set_time(int(time.time()) + lifetime)
        proxyCert.__certObj.set_not_after(proxyNotAfter)

        # Finally set it as loaded. Care that it is not yet signed !!
        proxyCert._certLoaded = True

        return S_OK(proxyCert)

    def load(self, certificate):
        """Load an x509 certificate either from a file or from a string

        :param certificate: path to the file or PEM encoded string

        :returns: S_OK on success, otherwise S_ERROR
        """

        if os.path.exists(certificate):
            return self.loadFromFile(certificate)

        return self.loadFromString(certificate)

    def loadFromFile(self, certLocation):
        """
         Load a x509 cert from a pem file

         :param certLocation: path to the certificate file

        :returns: S_OK / S_ERROR.

        """
        try:
            with open(certLocation, "r") as fd:
                pemData = fd.read()
                return self.loadFromString(pemData)
        except IOError:
            return S_ERROR(DErrno.EOF, "Can't open %s file" % certLocation)

    def loadFromString(self, pemData):
        """
        Load a x509 cert from a string containing the pem data

        :param pemData: pem encoded string

        :returns: S_OK / S_ERROR
        """
        if not isinstance(pemData, bytes):
            pemData = pemData.encode("ascii")
        try:
            self.__certObj = M2Crypto.X509.load_cert_string(pemData, M2Crypto.X509.FORMAT_PEM)
        except Exception as e:
            return S_ERROR(DErrno.ECERTREAD, "Can't load pem data: %s" % e)

        self._certLoaded = True
        return S_OK()

    @executeOnlyIfCertLoaded
    def hasExpired(self):
        """
        Check if the loaded certificate is still valid

        :returns: S_OK( True/False )/S_ERROR
        """

        res = self.getNotAfterDate()
        if not res["OK"]:
            return res

        notAfter = res["Value"]
        now = datetime.datetime.utcnow()

        return S_OK(notAfter < now)

    @executeOnlyIfCertLoaded
    def getNotAfterDate(self):
        """
        Get not after date of a certificate

        :returns: S_OK( datetime )/S_ERROR
        """

        notAfter = self.__certObj.get_not_after().get_datetime()

        # M2Crypto does things correctly by setting a timezone info in the datetime
        # However, we do not in DIRAC, and so we can't compare the dates.
        # We have to remove the timezone info from M2Crypto
        notAfter = notAfter.replace(tzinfo=None)

        return S_OK(notAfter)

    @executeOnlyIfCertLoaded
    def getNotBeforeDate(self):
        """
        Get not before date of a certificate

        :returns: S_OK( datetime )/S_ERROR

        """
        return S_OK(self.__certObj.get_not_before().get_datetime())

    # @executeOnlyIfCertLoaded
    # def setNotBefore(self, notbefore):
    #   """
    #     Set not before date of a certificate This method is not meant to be used, but to generate a proxy.

    #     :returns: S_OK/S_ERROR
    #   """
    #   self.__certObj.set_not_before(notbefore)
    #   return S_OK()

    @executeOnlyIfCertLoaded
    def getSubjectDN(self):
        """
        Get subject DN

        :returns: S_OK( string )/S_ERROR
        """
        return S_OK(str(self.__certObj.get_subject()))

    @executeOnlyIfCertLoaded
    def getIssuerDN(self):
        """
        Get issuer DN

        :returns: S_OK( string )/S_ERROR
        """
        return S_OK(str(self.__certObj.get_issuer()))

    @executeOnlyIfCertLoaded
    def getSubjectNameObject(self):
        """
        Get subject name object

        :returns: S_OK( X509Name )/S_ERROR
        """
        return S_OK(self.__certObj.get_subject())

    # The following method is in pyGSI,
    # but are only used by the pyGSI SSL implementation
    # So I do not really need them

    # @executeOnlyIfCertLoaded
    # def getIssuerNameObject(self):
    #   """
    #     Get issuer name object

    #     :returns: S_OK( X509Name )/S_ERROR
    #   """
    #   return S_OK(self.__certObj.get_issuer())

    @executeOnlyIfCertLoaded
    def getPublicKey(self):
        """
        Get the public key of the certificate

        :returns: S_OK(M2crypto.EVP.PKey)

        """
        return S_OK(self.__certObj.get_pubkey())

    @executeOnlyIfCertLoaded
    def getSerialNumber(self):
        """
        Get certificate serial number

        :returns: S_OK( serial )/S_ERROR
        """
        return S_OK(self.__certObj.get_serial_number())

    @executeOnlyIfCertLoaded
    def sign(self, key, algo):
        """
        Sign the cerificate using provided key and algorithm.

        :param key: M2crypto.EVP.PKey object with private and public key
        :param algo: algorithm to sign the certificate

        :returns: S_OK/S_ERROR
        """
        try:
            self.__certObj.sign(key, algo)
        except Exception as e:
            return S_ERROR(repr(e))

        return S_OK()

    @executeOnlyIfCertLoaded
    def getDIRACGroup(self, ignoreDefault=False):
        """
        Get the dirac group if present

        If no group is found in the certificate, we query the CS to get the default group
        for the given user. This can be disabled using the ignoreDefault parameter

        Note that the lookup in the CS only can work for a proxy of first generation,
        since we search based on the issuer DN

        :param ignoreDefault: if True, do not lookup the CS

        :returns: S_OK(group name/bool)
        """
        try:
            return S_OK(asn1_utils.decodeDIRACGroup(self.__certObj))
        except LookupError:
            pass

        if ignoreDefault:
            return S_OK(False)

        # And here is the flaw :)
        result = self.getIssuerDN()
        if not result["OK"]:
            return result
        return Registry.findDefaultGroupForDN(result["Value"])

    @executeOnlyIfCertLoaded
    def hasVOMSExtensions(self):
        """
        Has voms extensions

        :returns: S_OK(bool) if voms extensions are found
        """

        # `get_ext` would be the correct thing to do.
        # However, it does not work for the moment, as the extension
        # is not registered with an alias
        # https://gitlab.com/m2crypto/m2crypto/issues/231
        # try:
        #   self.__certObj.get_ext('vomsExtensions')
        #   return S_OK(True)
        # except LookupError:
        #   # no extension found
        #   pass

        return S_OK(asn1_utils.hasVOMSExtension(self.__certObj))

    @executeOnlyIfCertLoaded
    def getVOMSData(self):
        """
        Get voms extensions data

        :returns: S_ERROR/S_OK(dict). For the content of the dict,
              see :py:func:`~DIRAC.Core.Security.m2crypto.asn1_utils.decodeVOMSExtension`
        """
        try:
            vomsExt = asn1_utils.decodeVOMSExtension(self.__certObj)
            return S_OK(vomsExt)
        except LookupError:
            return S_ERROR(DErrno.EVOMS, "No VOMS data available")

    @executeOnlyIfCertLoaded
    def generateProxyRequest(self, bitStrength=1024, limited=False):
        """
        Generate a proxy request. See :py:class:`DIRAC.Core.Security.m2crypto.X509Request.X509Request`

        In principle, there is no reason to have this here, since a the X509Request is independant of
        the  509Certificate  when generating it. The only reason is to check whether the current Certificate
        is limited or not.

        :param bitStrength: strength of the key
        :param limited: if True or if the current certificate is limited (see proxy RFC),
                        creates a request for a limited proxy

        :returns: S_OK( :py:class:`DIRAC.Core.Security.m2crypto.X509Request.X509Request` ) / S_ERROR
        """
        if not limited:
            # We check whether "limited proxy" is in the subject
            subj = self.__certObj.get_subject()
            # M2Crypto does not understand the [-1] syntax...
            lastEntry = subj[len(subj) - 1]
            if lastEntry.get_data() == "limited proxy":
                limited = True

        # The import is done here to avoid circular import
        # X509Certificate -> X509Request -> X509Chain -> X509Certificate
        from DIRAC.Core.Security.m2crypto.X509Request import X509Request

        req = X509Request()
        req.generateProxyRequest(bitStrength=bitStrength, limited=limited)

        return S_OK(req)

    @executeOnlyIfCertLoaded
    def getRemainingSecs(self):
        """
        Get remaining lifetime in secs

        :returns: S_OK(remaining seconds)
        """
        notAfter = self.getNotAfterDate()["Value"]
        now = datetime.datetime.utcnow()
        remainingSeconds = max(0, int((notAfter - now).total_seconds()))

        return S_OK(remainingSeconds)

    @executeOnlyIfCertLoaded
    def getExtensions(self):
        """
        Get a decoded list of extensions

        :returns: S_OK( list of tuple (extensionName, extensionValue))
        """
        extList = []
        for i in range(self.__certObj.get_ext_count()):
            sn = self.__certObj.get_ext_at(i).get_name()
            try:
                value = self.__certObj.get_ext_at(i).get_value()
            except Exception:
                value = "Cannot decode value"
            extList.append((sn, value))

        return S_OK(sorted(extList))

    @executeOnlyIfCertLoaded
    def verify(self, pkey):
        """
        Verify the signature of the certificate using the public key provided

        :param pkey: ~M2Crypto.EVP.PKey object

        :returns: S_OK(bool) where the boolean shows the success of the verification
        """
        ret = self.__certObj.verify(pkey)
        return S_OK(ret == 1)

    @executeOnlyIfCertLoaded
    def asPem(self):
        """
        Return certificate as PEM string

        :returns: pem string
        """
        return self.__certObj.as_pem().decode("ascii")

    @executeOnlyIfCertLoaded
    def getExtension(self, name):
        """
        Return X509 Extension with given name

        :param name: name of the extension

        :returns: S_OK with M2Crypto.X509.X509_Extension object, or S_ERROR
        """
        try:
            ext = self.__certObj.get_ext(name)
        except LookupError as e:
            return S_ERROR(e)
        return S_OK(ext)
