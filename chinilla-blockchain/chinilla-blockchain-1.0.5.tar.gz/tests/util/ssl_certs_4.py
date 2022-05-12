from typing import Dict, Tuple

SSL_TEST_PRIVATE_CA_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIUS+xy2kGNomsBGfU0DEELWiHoSa4wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMB4XDTIyMDMyMzE3MjkyNFoXDTMyMDMy
MDE3MjkyNFowRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8G
A1UECwwYT3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEA9wgpBPIdclPot8ydp7C8EfKfZXve31sim/LBU9nViOTB
2vZGWcnwmb8bBg9gAaCCeSRHF0FqEmU0hUMDD7AY9npBpIzA4SUjUL3++/kKlZa7
Yw6kWJoogcVXpCYvubeslpReXq7EhrrCwE83uqJ+gmz+pGkEaEoED42mw4xvNl+K
8B+nfYJ9aYlErX3JjQGtby+RWUw9aH3xBDDZ1Fss3+289OQ4+4KV6jPXXKZgniD4
exnpss6LqdVhuRt6Wuhol7eoWl/kpcQfQ77fHr/8xTW1TsuFrHjsgJUXqGi73OuF
esOaijmYCLkgklocSND0LDeF9uzNjKEOXl86iHpOKwIDAQABoxMwETAPBgNVHRMB
Af8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQDeZ8UXHc6TqZGkvrFIY6U6ycHP
YSH42ihMkqJApBYWEpb8wFM3vAJIOZV0BBYguat8/7gApRGiy+xnq1TFDJiMLRPu
Q1yDWbYXM1fsObgyh83K8ZNQ/nFr0w5o+HcShkjia6pWaNsX5OErrJ57iJefaADU
xnLvxHXPDvwvs9f1mLZIZgzYtv3go9oQVOCgeIKOyV7cFUAAgIeyOidcoQEN6Gvy
DzlkZdmRRkvvIddDG0kcURmhMJzqg3Tn3hmG29wzSbsw6LK9kwr7S9BKNv/bgxDi
DOLVn9LP8qDeRA7zQtbneTtcEU6saUQT8Q9JLyvGUjk+Qgwdj24M79L9s0MR
-----END CERTIFICATE-----
"""

SSL_TEST_PRIVATE_CA_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpgIBAAKCAQEA9wgpBPIdclPot8ydp7C8EfKfZXve31sim/LBU9nViOTB2vZG
Wcnwmb8bBg9gAaCCeSRHF0FqEmU0hUMDD7AY9npBpIzA4SUjUL3++/kKlZa7Yw6k
WJoogcVXpCYvubeslpReXq7EhrrCwE83uqJ+gmz+pGkEaEoED42mw4xvNl+K8B+n
fYJ9aYlErX3JjQGtby+RWUw9aH3xBDDZ1Fss3+289OQ4+4KV6jPXXKZgniD4exnp
ss6LqdVhuRt6Wuhol7eoWl/kpcQfQ77fHr/8xTW1TsuFrHjsgJUXqGi73OuFesOa
ijmYCLkgklocSND0LDeF9uzNjKEOXl86iHpOKwIDAQABAoIBAQCHx450T3fr/T7u
t6L4JuZYnxkJuNo5vmf5e6bTpen+wm3jInZsp9h9SVNbM1w7yLOuTkhc+fGJhuMl
VD38g3hVEcG+5jamCbmtiaD7cllk+2KoAcZHhQQ6v/N6IBsfY1uTsJ1mQX136HNf
LKufA+2xVqNoTujDQduViPBej3QZV7obRrcOuycF0SPbXQadbE0cEEKo2htfTgcH
R0LhPOFQQUvlV7fnTgUtCXZAnxRFvciLABUZ3SHwSswBhhWcbWmzaZQxzfCFOdpF
OvBk+xqlpSsa+pmgJ/MnL7O0b4y9JAdLlTf/w95w5gyJMOvn7B3LGeuwIZFHcxvd
CQMjlk3xAoGBAP19pcjZ5Kn2ChQXoeOx44mOd4ahAZXOgDgs1mR2tRPtdjH23Mqf
C3LaOtn9aBpW1A5UyJRHNOIlBQnqbvQcXHFbi1KJIs/L1yv638dUzmZyUZihunOV
hpLQCY5KFqej544BaLJSfBO+xK4mV0hxDiDky9WqzAP7kvmReRGCKqu9AoGBAPl6
JUEOvhBkVHAS3FpVKbEkv9cIFLoY9wLI8/aprcEvSEgn3LmLJKcDauNKJBKXnukX
oXRkWYSU+CrOE4k5vDvos8O8KLJqDFZfrPNCuDz8hEdt52DI3Eu88oknfXbuSht+
cJ04WjgyyIf5nDKvCgI7WvtuBLhGlmh9GRmvGcwHAoGBANc4xfhpH986GcaDZh0n
nPPetRbmPq1NncmUMBcuPoID3JWBbmbOcG78YHlS0P+D9xmP3JkgeAMFwWhw1fGG
3uoT+o+CBb9951vc7gCUvYV3zFWWAvM94ftmjKZ1uxRsch48jgLRS62MC/t8bCEC
dCdzeqkYEY3UHC6u16cI6GfVAoGBAJogvW1hF0l3Qrdu35YrcTOQ2biWtH94tvqQ
fjDRCZkFhimV/wbekQlh0iKUBo85/yJQyB3pdWi0xFFluaoY8lMs5Aq0b4wyembO
e0Ja4QpEk9CxdLZVwcxE8q6LqDbW5w/vYNGxJAP+U+e17ateeteAJiiaAu56Jahu
SRiWFmD3AoGBAPv5pzfb6L51/pey6kBL+Kry9gTEHN1hW9mfv4KyQbjBIDfBLSNj
GjrtGQCN3g0o/ElLP+IFXxhJ9k+KlFUZkQAFYMR3X9p1you8BL8eOCjJW+mk2H7P
rkUFuht8pmfgMrCAVcKneG+ZZfc+bvghcCmHVeNiioKfOw/7/fqDQ048
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUcVyMMiaYY4UmD0lc+D0TSzOgx6AwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCq6EP4SllvUyXjblM/2V88nxkpBwgC9ta7Ndd8pxIZR4Oy
lnNYiaes3gTVurf7HMAIZ0wHnlzRZghVvpZQ3eKGR1ETKYXaoRzlgwa1uZKGn8/a
DBU2bhioG31zYIOZ/QDf3ZcUR5JkcybdpY+Yj7YGowRkLT/GGN+5GgTA7tXJRWJQ
lpHNaIjFgjj5fKB+xXck6OhVHftl+rB2ZPrVgWaXPDBWjgpF1SJnxsbmOK9o4kB6
bw6zm2wuByZrOYg8ckuIqbJhDjINKesfcyb9qSk77h+8ILj9b11OzZUfX7PhvgO1
+W9se/RCYtfGgT4nSh9No7l2vA/IkwOnZOK7nBgDAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAHcwPIii2n0DabvcPo4Kfz
iiHQfxOxlnTovNmI3VIWNYoe+ElYkuzKUlwbYEve0dEJwu6mWazIEo+Qexgv1Cs3
Yn7djsmsC7q8pOvSmw+3t+6aOXGzeANcFUPJTgNIlxA0sucHoWwpROLsndBdqVWQ
LsV5IwgLJbcUt3tjaIsqfUXabqJMm/KleCd6uDzOuFlW7E1jdUyPomvbOKgc/jAt
/AxQimzkMt2uBRH/2IyOW1IS+035AxyyCfZgyhJIhf0l5oA6IiIvS47utLJ/DtWb
93+WPiBYIgNofNr2qGrDtK8Pm6BjjJtBlFvu9gNcHn0E2mC6TKNg2ppFNxXdX70Q
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAquhD+EpZb1Ml425TP9lfPJ8ZKQcIAvbWuzXXfKcSGUeDspZz
WImnrN4E1bq3+xzACGdMB55c0WYIVb6WUN3ihkdREymF2qEc5YMGtbmShp/P2gwV
Nm4YqBt9c2CDmf0A392XFEeSZHMm3aWPmI+2BqMEZC0/xhjfuRoEwO7VyUViUJaR
zWiIxYI4+XygfsV3JOjoVR37ZfqwdmT61YFmlzwwVo4KRdUiZ8bG5jivaOJAem8O
s5tsLgcmazmIPHJLiKmyYQ4yDSnrH3Mm/akpO+4fvCC4/W9dTs2VH1+z4b4Dtflv
bHv0QmLXxoE+J0ofTaO5drwPyJMDp2Tiu5wYAwIDAQABAoIBAGjkEAMsrmMSpuhE
Z7eCE19DTc/OTu5yzCstykjoyMTXDU7n43btVQlVYaZC6HOnm3wM2a67VL/3XRoy
1FJhO4up7WpTS6F4zCFYHyAc+n7BSnHKhKJZQ6y44m+TRnGVw5mhh/2cR4561dmm
qNC7Mr40Apfw5XkQ/w29mDlI29CgUZOCg9e/DNfNcHULXjaBvIT6Ecr3IOXl/d9B
zdtyAZohHCv5m3Psv7ciFjDKb1nY1+c6c8WUFUYgPQz6SUbm7mvtLiH1gVBuEjgw
xI6RwhcNqEVY11+NO8hVcHTvwffEIDMbn7W2L4nvJsU6PlHvsxZx5OHyJIPLmMi3
IrnbKRECgYEA3jrZ+zMaP+eeuV2syjc3moYK+dbKzk+ewk6EBQsUTyvq6CPvIZXL
5MnckGjw3CECIKwZG0gKph2+Y6M9h4sfg2Wz7Kyfygk+TolMU21Aw8mRhkWRCs01
9hiZbCrNypiQa4BmeFWo+uyjVDafSRJqcTIcVSHaoeyRn9uRIYIvOfUCgYEAxODe
//ZBx9lufRXMYR6NoEqok/fsK8uORr5+l+QdZimAkdSDmGtY4/o9/TBg6fm0C0kr
9o0owbi43FwEq3ZLyPIevCaKHClZO5MQm+PfRYDs+uZhrAWaPVW9Q0b6eiYe8Xwv
Vw9aR23DlTPXzV1kiuWwsLIq3+Oq9C7pt2qZdxcCgYAfMyIBa3ZG/IzDN4yXw1LS
JfmKhAZrGrCOVRmh36FVUDQlrU3YaEB8+X425BTUwumajq7jrqSYF9rwAC4WRokB
GJk/JCk24z9VJV+K4u7Rzg3ZTREE9DScPW3kysmjpPG5tggs4tHbkLeJjjWku6oo
BEIIDb21OBJl4ByrGKzqtQKBgE0Ph7nAdfb3kFu9kIXjI6Q+FMX2IKbzwfjGz148
l5VJYV2zRN8ABYcWh/T2Xri2WFaiiWaz0eQhnZoDGoDSiM9aldUncJ+dP6Ql6DZc
dyQJVrjOPCTM/JZNXQtcWOY+zZXP+eelxrx2pjtcU3e6uoPza7l9w3Jm9p8lTa3R
N8h5AoGAUAtG7NJ3Q3CCUsz85OUaDGlQVPNrKi1BBG5KEZJla2n82qjnUdOYRWx1
c9gr9O94Yukur3VWtrNKpxnjwJx+F3akW9rHwEEy5xtlAJbi1mR7/1thgObUS73P
uapcJeqezHfl4ir03YUHSAJebwefo54B5t5pOdWEFQLS2AkggSM=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUIpT5MM70VeIvnygCEHRVsL6Aq80wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDsxtOxdud/1pyMnhIdMYyqWmH80gO0Afp/ojKApcqzV3aB
KBFfQWLp4hc+CwykpAItx3vuTNXn/dQFxzC2NXrmq1OlPiPUcxorzctxqDNdoXlj
WTtxjkC+kxvvA2d7hgl+Huz3JxTWWMt+fM8eLTAOdVpPea7unW5GfQ4TwhdEMsGQ
4AmUylw/vjJDUaiOHlKwwD2c4EakZNd35pCtRZfNjM3CF9BxdK2xysWp+xoOIY2C
G61UFfaXiVK+XkbZB1g0+nhNEsur03gFXkFEVmetXZvpfTvQ3J8a3f/sguzLqmYq
spKleR4utiP3llVrgnKPWpDiMvsx+xRbMlbSUMvHAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAV6jnHn5x8uYtbM9jN3cqQ
FK0OrZPSDsk+QJt1I0U0+HF8j2jMZ1RTxRhUCnjCoytqbh/fT/Xk+8s0N614lvja
84fmW8dKq+asD2mWrPZeEgpipk+fzthUOrovNobAWtpdEqjKWEvQxMOICijEXFbv
95V4kZS7JN+s3jAf5nXOK9EhGVI9214UyGNZZU/nzFKlOLcZFhGBibUAT7oA9bKi
BLbCPI4/CIdUnwaK7y8xF9z9KL+A24ZZzhLNVC35gl0zESgVqa0DN9XQ+GP0qC1S
1Z6PF4qBDeta+3R28PtfPIiNpYJ6uHAOT/iDmIWBKTGC2Y6NVs2diNZSOlZXSzN6
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA7MbTsXbnf9acjJ4SHTGMqlph/NIDtAH6f6IygKXKs1d2gSgR
X0Fi6eIXPgsMpKQCLcd77kzV5/3UBccwtjV65qtTpT4j1HMaK83LcagzXaF5Y1k7
cY5AvpMb7wNne4YJfh7s9ycU1ljLfnzPHi0wDnVaT3mu7p1uRn0OE8IXRDLBkOAJ
lMpcP74yQ1Gojh5SsMA9nOBGpGTXd+aQrUWXzYzNwhfQcXStscrFqfsaDiGNghut
VBX2l4lSvl5G2QdYNPp4TRLLq9N4BV5BRFZnrV2b6X070NyfGt3/7ILsy6pmKrKS
pXkeLrYj95ZVa4Jyj1qQ4jL7MfsUWzJW0lDLxwIDAQABAoIBAGOH7OMTpZrCf0pJ
BDpLYuMVXU1mhvH7Ru6yIuKbTsr2wDTov+y30rmYNcb55BWtb9EIoxr4J47+z0qi
geKGNqSSbnXu2ibrP5wcRSIA357DSwCtOOSyNJsnwb1GRBDTtlfS7i+yuPqllt0T
4AjCXAon4I+6CgP6H6n31ZwOobMjh+SOsgfcaCiSspyD1Dwnkxvz1tVRrLgv4RGa
gyzCEUN0zJaQTvTnlBhSOvZ7E+AgNa0gt2lYUKuSd3m8Hr/xtKKAyotFZZjkkI+A
GjK3eL7S2zL2yaYyJvQmGpwGwceti2oq5sytWXXREraFBxjusF1Yxw4n/pguvrAS
+5CDlFECgYEA+O7KoYx5g1JEOFCFpyfDVyR3s1SOVBe2pQIe7qcNbtrDFQu624Mv
YSvYNsvplSJsbFUCPIcqzEf+BIzgQQ17yDacczZnk5rN3VurU9xRaGjZTKeF73nE
bDhRXmIJlxCtkcXi/vzDUJdhAtzN1yTHhwgz7SvHHeqqZkKwPjEGo7kCgYEA83+v
vZfMOWJjHXGlKj2cAmHkLGrKal5l6HpMxOMqaoVbx/oDguQLP5uH8TQnckAJVyKA
ks0gJrJsu4lk5CCt2xgMQSLl+heGcN+usVmxiV7bBv3HC7E0wNp9/13NJWL5mrL6
COEDIl/qjF9DI8ISam+L7KQYk+TPp4lxgyxxq38CgYEAk8pJuUHKPsIPyJNd1lDQ
M6NuAaUY3yo5AJxSuwOpAQCWQ590L7Eh5wH92wKTSjxmvKZ3rnHdYez4DcGJvnV/
4O0zU1+gfMyynlI3VJGAL4nYQR9QcE4N5OZGwM9ZvDtloR8oVpTAbM+DBA0NlEa8
wxmGoq+UBtn0ksPTGQlIVNkCgYA+XCUV2RpkV94qXECAYObjdU6KUY8lTqeqsieX
BNaIET9AJ7defiijUaGvFDxF9kBuIFftQLtLLcbLAJTmF7hus+nvhJCBTCUSIzcK
FH5zP+e4EqY3SFrKSSqbi9pOCNsD03JVc8rpssbOzFbVgY5V09tx71ScC61iqsB3
Z5p04QKBgCDlV7wh15Q+C0KSR26EE+6Aj+CaH8uRSoDO707vf+ZS7oqw5Xivl32Y
QHFVDim4TF3UyYJvCRKmvSMNNsAKc9hFBU5b3TlBMwa5Cx8l+fOmYhe9eNsP8BNm
aOrHGu+nvZ/oke47p1HXEEqUfPw5hPdwo11jwa5lUtSJZhLQhhT/
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUBOIDJICHJA4JiPMdTj1KC19GQOgwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDUjguITn4XjS5HDyHEP5Gmq+dgP1dxpYLMDWnJtHZatsYJ
0x/rnEmDTReeQgiCbISO1oyK/TZ/L1IfzoRTm///uNns8uBnku2VmUDaTUd5K6ws
WqxN3YU+h3P5de6otb0DGkayANr3bMy3KQqGm/XxQB2VvXuo4nzbB4Tk5jDO6vtk
lG4184IbY+08nrj41L3YNCOynSnRDi+1ipfc/hrIKuCA5Giuf56S02hHapjEw8+W
Tvokx1drAlcJkFBLDVuPd146L7klCAhENaIYxJmoqLme9ZNOta2jmSEpeIHbsw1x
HPJNi+6n/Kh7k8Lsp0fE+jgQfPDEaqOXsnLCZOcxAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBXHURcU2ox80IFiBq8xEDO
cmHDZVOrQqpmOdygP+q/JRFoX9jF6X0nR17DBfDedgBz1ghax993nXwGJswvs1K+
1DsTIKxO2HJefd/5iur6mxLFF8RXdku9as1tfNx7CZMm9WcML3XJu/u1/E+JRUFT
+QdoAX3+GnZGY6g+2MUSo11+3Ide9aaHvRUVDIXxqxDOZgLvy+EpIoQU4lkL7cuJ
CuFB0LYM9FMih1BX1uEu3wnCRhJq2nJuIObMEU8wQj8MmgPZTcJh5tyVR8OeDZ73
CACnvjXydwYvFmcB/NCMLpolQxxgrpYKrz8dx1NN8mZRNb+HUrM2tiLsWKAdFEid
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA1I4LiE5+F40uRw8hxD+RpqvnYD9XcaWCzA1pybR2WrbGCdMf
65xJg00XnkIIgmyEjtaMiv02fy9SH86EU5v//7jZ7PLgZ5LtlZlA2k1HeSusLFqs
Td2FPodz+XXuqLW9AxpGsgDa92zMtykKhpv18UAdlb17qOJ82weE5OYwzur7ZJRu
NfOCG2PtPJ64+NS92DQjsp0p0Q4vtYqX3P4ayCrggORorn+ektNoR2qYxMPPlk76
JMdXawJXCZBQSw1bj3deOi+5JQgIRDWiGMSZqKi5nvWTTrWto5khKXiB27MNcRzy
TYvup/yoe5PC7KdHxPo4EHzwxGqjl7JywmTnMQIDAQABAoIBAQDQJN1UOJEvnPgx
a7cER7/ouDQWw1BtIMgJ7CSo+ghgYtVhr5Z1khFG+8piFoXgukXA3oa4YKfqOjuw
m/pnKb+x+qGlcF2h73aq5W1lmQGhvcuXj59ljMS7a8d9BSiVm4qhLC0IiN/kJW3+
+ritArL/8WpHRUuAIXJkxmM0B9rJ8/bPYhcK6cdgwV09KOKRL5FVrmVQIzNlM3F7
EakCLVTaHeAlOHTt24XU5EuhV92ZtHorQOUvdx/wjWTGosOZxs92DS43gS/ZszUq
uH5mfbRTyTbde/BEKSDE27dgYDV2uJ9FuUeTJcJl2kjuKRUPrhZf+0FoCrhcAhzg
JIjVt3ABAoGBAPJ/AHWpEPlp5v4RxhVrwZGHbwac7kzzaaUqS3r4tgw8iAb7iEZF
VDyVrM4gXsfaKedUobxaVMUvH3ajlIHF6ncnND0I7u4jff6lc+V1HqZbOs4xaLwu
zlrfecfU6JOrQ9UnhYk18jpShzMsoBl2mdPFe8QZClvn6UMfXaOdot0BAoGBAOBk
NEchBh9Tms2826G2PZHclp9JVpCYWdxqW1/X3MoTt4T8gQUSGbeEx3ieY95oqAE4
eE1RhEniIQ8sQtdgnZud/LD+9mrSCtaAdkDOSCulCXNt04B84odid3LHkd+qZ5/5
rqctxAmECxLFaYHU6eIeAMhyoFx8gUcPLjIvRpoxAoGAPbMox8c7pWpXtr+I+fxP
5RpjmnglffjVIYwwZlqP328rYTNwyghr1Xpz3IKJ+ym8TbrP6B/Hv+AsjkAy0g4s
iSK1fO4f9QGc1kT8xx5UrRk7TiluL6ttH9wKnVjD0IbcHIkQxgeu2T4UXmX1WmU9
4I833X5Nj3LjfAuoBLBgNwECgYEArzUOrMtYYHWDVkm0pJwLjyzSXyWAdf6/i59w
IXIHb7HdhfUzOKZddjIzHjdue2b0Z5+UL6sKxDXQ4mwI9Or3pV7Cw+EQv2+qDrrX
mtp2970xl/OVRao9psB3zCOP/zirGPp4KQlPHK8BhnKmYz3AMVKEAf+evxhoSPfN
dln7osECgYEAy/HevTnTfcCn6TZyYBz3rHfZ8mZBO1I6gyVytcNQNgmz2ZPI/Cxs
iDg78PSjypKSZ1PyYFc+5dIIw+02guglrTnIrrxUbGp7cy26VQfEwGLjaqFHZplc
PFS4W+Fz2xVGnkv2sQwh3tSihThxd3hQK9isI3iHBeZB3HDWpGQzRMg=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUN7Hj/9zSlPgvmKSmTRU0Kd3ok3QwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDgmG/ekJTb+4NZslwT7MXUZGuOOId95dTgXWrev88flfsE
+lEl1MvVKQLVi3F1I/mxZujYbCW4bRqmwEM/jwpLNxd6lzQjGLoePQWTURCBdnAY
RtslK1eetPhKRMJTTzaH21prkEEEwjqNb4he91O95VMApYSkEX1vOPd6LhxW2X5E
Z7rwZzgL+qwKtQy0VdnxYIcBnEXIKanNodC3vR6BRTU8vBvMM1wtxjKAAcs+fQVY
6eyBu3Z450Fo2Ge1+orDgLdN1qSFEDw/DU98V7Xo8CzEoBV0vRxja7VU3kRqIMKk
EyVwjD6QBfm6CadVC0+vj3B8sbFF4C+w/gkZUkodAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQB0UQbCG+es9N/hKKbzG6+P
nXbd/c8LB0iJIPZ6xyPWoZsyzPmItMt3KFnYko7EbZ083Uuvfy+IyHSPcxihxQl4
qLGvjxHG+relpKexwnhYgRWuW7d8xI2WMjDT7Xs6q6npbCQjwpZXbKxe2Sr/WMu/
HitB3RwZ/CCeQL5oh8rm7TRWi6boqJXG6Yx6jjPRrs+f+V7deXNxHs2eV3RUKdBp
Lc6IiNoTtdkZm9MS+xsucm0HJa/Mf0/Gbos5A9oqB++q8FR18Rg7cEt6oTyPjlBF
xq/9SRUCLAeaIVufV+Be/bx/tX117/MUQth3cqSqlMkPfvyIYmZFbJbr2wlyQ4wS
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA4Jhv3pCU2/uDWbJcE+zF1GRrjjiHfeXU4F1q3r/PH5X7BPpR
JdTL1SkC1YtxdSP5sWbo2GwluG0apsBDP48KSzcXepc0Ixi6Hj0Fk1EQgXZwGEbb
JStXnrT4SkTCU082h9taa5BBBMI6jW+IXvdTveVTAKWEpBF9bzj3ei4cVtl+RGe6
8Gc4C/qsCrUMtFXZ8WCHAZxFyCmpzaHQt70egUU1PLwbzDNcLcYygAHLPn0FWOns
gbt2eOdBaNhntfqKw4C3TdakhRA8Pw1PfFe16PAsxKAVdL0cY2u1VN5EaiDCpBMl
cIw+kAX5ugmnVQtPr49wfLGxReAvsP4JGVJKHQIDAQABAoIBADWQZW3BMZ9dVrA3
t3oRCAVlhbk/hiDihWiVHv3M5Qr1bA593IiXPZ2y0Dg5r29uiwhiMLoc4MohSy/l
vqQT6zKRCwpzsT2Fki3QA9pkhPk7U/SWQYGV2qnBI04jI+1WgPzZtbDdkIQgBnLg
3Lc5aUFqxebrkrzGZxH1liAPizay6ds8PsGGN7AAeGHdcyL4oGIlQux/jbiGbBzU
NBJmD3qvmbjyrc0J2wYyCJtlCyMYUW6Z428iRI8Qzv1wBzAmnEoKHlFnsIwvzPRU
SlG0CdvWyckXPy9MfWpjmMhQos7U5MZwECWl0aF9MPSkLSxuyfeVWw4/p9tOWS/f
ebyJVwkCgYEA9xU9GAgFzpTHE/1uFNqHSfQxqtEULo/FsxBcOsRJyVvO55+mQN+z
S0UtdiQJ7s4Vzz5UXrnhG3qgxtQvgt6grg2m7pPN5UekIDNsQoDMwMLA8Bt248vw
3TLbSe5Rn2H54F1MuxfoxG/sTMpzNAgNuc9TuPkRok6X+nsfbfiPQXsCgYEA6LNw
kuShVbWRu5aZd8t2hVSFOWN+lmI4MHhpDCFXdTyJ2kxU3k1vdPth0i9kFU3JktNI
Ptnf3R32Uf13lWa75e/0tHUlHaYs1gpdKqDU1T7OvU0xk0zzeogshc35cl1b7Lyw
Op+PJX3F+QjK3Y5gDEnKAUpi3Z4MFvi7sV7BE0cCgYEAuLa1/5svzCpJUdZqT0i3
T0AxSUQY1F5DLASVDpHjn5b07Q/bGDCkNyc2P1Xd3xtODqrIJDDN6t8YBsxl4G5S
rQwjucPhbwDJ4BDRZD4p1AlEd7vwe4fhP1xft7tkZcS3K1ZUoKHVL9WEUDwhN8q1
iC1Ip8X7ut0KnQUij/H8FrUCgYEApUF5uvgfE01E16GWD5sw6nMhwaXE6muKV/HL
OFAdWibKB3uZ8d2wP7WevLPnMbHyaxEdB3WXI+L5YTTOTg2Ndzg34kgnOa0fvknR
7EoXm/FkxM8jW+aUKvq2E7g5ZFykwbUmuhtCf2+YvsjduQY5c8Cbctsu5xAsqcuv
D8GpAFUCgYAWVdHC37arXcZiwLO/YYPE94PbIqd5LrMaDXcWNcwFSbB7kOnINt9G
stvnxoD999PrSJLRbnvWyQhcGhK8qXZtDyh5sw/VuUsufcz+xSwI1+K3NSBEJc09
e9XstIYrR5rdizf1g6Ai45W+wAcs2ysUBfnY3fUv4+n8ZoRiLXCepA==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUH2fAuEi168jppWUawNNToTni7CQwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDRJQfoJxErXVdwTU4sAQ+05EX8tC1REoYFJyB3hhB4LfOz
meCPe85X6FTYbcPdaL3NVevqEL2hzbqESD5Gf5Fvx9ctIdzwYv674P/tqPrIkTd+
cLshBKaR6CeSjPt5cFbWhg1hnmWy9Ta7SsYqOXh2aBQJKTRIK80U9b+8iVs407E+
NCMljerodAdePW5X13i0ca9ifwbTZkS2/c9nQEi7qldj18/MVax6qezY0aKqu/96
8DSSTc6uUiNLKmRYP5xRJw06ggVooviX7snMzG6SgsbLK2tZJXeJj/EECOY4UrPc
FOkVmjxGBP3QD0oLoXnZpxvutS72ovUrcPxAMImxAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBSOIrT/3mFkZmuoQ/7UcPR
TOssC9o0xAwR0iRdziNQBZne2zLCxk6p32di+T6GIJahqYFqVU2cfDyyw9YUCr3P
nbMjuwsSrvor4LwJ9jlWKRRyBm/adCttg6OQIO3rYk/rX7XE+fBY1wYhqK+KcSCb
iRLqHIPEo9On/kpaSOWKFeSrGLMkj8nQWMNNtbzTNcdhQlxEGXcxPsVb3PGs2b0p
n63n55HTUbiL0UsHQvxR8gr0YiSpmlgJLi5pipDbyMiVHyCxj5j5vEovXckRliVd
iEbH235NTXPtJ9aBVEDsHW7W1AhzK5gh0Ev0xOC9vP98qTYR+4Oq/3Mz9r2jP5/d
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEA0SUH6CcRK11XcE1OLAEPtORF/LQtURKGBScgd4YQeC3zs5ng
j3vOV+hU2G3D3Wi9zVXr6hC9oc26hEg+Rn+Rb8fXLSHc8GL+u+D/7aj6yJE3fnC7
IQSmkegnkoz7eXBW1oYNYZ5lsvU2u0rGKjl4dmgUCSk0SCvNFPW/vIlbONOxPjQj
JY3q6HQHXj1uV9d4tHGvYn8G02ZEtv3PZ0BIu6pXY9fPzFWseqns2NGiqrv/evA0
kk3OrlIjSypkWD+cUScNOoIFaKL4l+7JzMxukoLGyytrWSV3iY/xBAjmOFKz3BTp
FZo8RgT90A9KC6F52acb7rUu9qL1K3D8QDCJsQIDAQABAoIBAQDBn1fXnDtv+yVV
KayCXqUs4dzNW/1MPirnIFcVcH9U0633izDzhTn99nB+Qfh/xVVagP48ny0AXBce
GkfVOorpgoh6FwyVXADa7S3i13r9LjvDChikM8sF73ibW3wA7HjoeAhxZJRgflYi
RNJ7CuO0MxzBcm0dl7dwfSb6I+vZCa5b6McimTnKhXSBwQy5m85ldAVKOZveU+aH
gLU1qSmW+2x9jErdzJadhfqrPDcy8UBla0uqamXfPBCeSdcSRHtlWvc9RxBcdtQF
jkzhCyGK4K2cBKEMa1rWCcr+kAd2uasEoSTfe4LMPgQGbS2e7sl9fufbKRDkZWrH
NuGr/aVlAoGBAOvjN8lAgOQJyI1PmKcZnbUXRFhyYvjZ9kWmsN73RpZ3yhWPL1MV
0qyVHD1VcqnRWW/Dw3Jw42cLw+LZNJMSNxPnl5e2MtxSnmYn0PcrkUcpOafxy6dO
MV6op8PeA6njtMMEFnnPBoVwM9km2OiSW2/L3+rndtS3eApRzkm7jjjfAoGBAOL6
FolDf9EJS/njwHFGhMRfUvTC5C+YJh/vUjkY22rUw4v5GfxTlDVigbbqzerzMnA6
XSU11S/I/n7HuqGbc5dyUGGyk8S7Iv7hvfDPLfy1EXlKvQElpcbXG2Ln1wZ9E124
9+jRzzOUv0GcuxMXMGi+OIRsWyyzhNOZUlLYWT9vAoGBAMZhFO1//eXKBIwzQKJn
fKZrpuLrcCjwxZjWEzGwrACnRaDUBmzNkZvq2xEJ56DBm4HPFXQNVHG5B0ikev6k
9wUaY/cHF8cLBIPNQIRec5NxLDf9tdRCgmqlVFH5SQN7qO3JZk2Sul1Ge5RIg2s0
iwl+YBZiCyHiGmYzXlXMElPpAoGBAJrLQglUzluqQnVmvLzEAhHGjNW+AE7xLbcD
yQiFikZ+Weog9XbfLSmHR72OvuZn+1MMiq+w2fZf1ihyYDaMxLVZUbZ/SkWV9pTr
MVWEhfFdL1CQBvw8R6Wm19eJE10qecWmOvQ9+lhMLm85y1+Gpg4ZBIRTPY7r0z9X
xgwX3i3jAoGASf/FiOO2qtKDxn61LLVedxDtdmxd8FHLP35i+4S2ZyeIe8l9K/Cf
lbXe42v2NEKSjYq+z0HKdtjgZLkL2ucF+rLbkBfg7G2hmWob0hfYCE8xcnNPWIKM
yoKW82uijH86yJEWHAFAv3IZhU1CQP0BkYteAxE8CExQU/CSuHsCDao=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUFPTg1QrNlWLRFn/hC78RXi0IOD8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDB7fCDqqnna6BfaJsv4xztP80jBCygHHhHdliSWbGX/tm0
lK716u0lBRiI3FmzPk9MqKMuV2Vvjsqm7gwLzG3oMHKaUPJUOiVf5v5/rXauNiAA
m/sfRAROef+ZVoVmU6rqwnGvTf6POI/MPdEbCPGIXu3bWjPXPq/BKzJ0KCJh7ekR
DaFWCkfQEs3Zilr2ehrdObzwHOxJh408t2qGeCQDlQeDXZYa5cTHo0tNoSWdfJIi
1jNlEnvpo6ZV4fyKY1MiN42J/2swaxypdS3KxvPZzKWebgaloFaZoY3HziotiIva
EnJrUXNgQI1lW4/a7jooQ4c7A0t2XBidRS5Sohx7AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCAQP7xtLehAfWTp1k3E7IM
eMT0Qm2iBWQqB4RLxIJWgHyVHYeY7Lp7lS+BZFKHOkbVoc2J8cA3qGGDw3WrmQuF
uRxfL+bLC+HMSjEvPbXmnMWAqMKmVBzOvZf91VVKsFR0h4Gyt78EFteZVEHZI5bQ
jC2RLte2uCtht/Wum74z7jGzplx3fRV+zcig7Gka8IwTcHaRpfhhZa0wbbR3Kfe0
uXcCgDF18rwr2uIDNPBmJfy9C3nyQugWzNV/j/FDmrqHD94tagfDx5wYPb/ZFVpM
TRg94mZSL6OkgITfba9MkOBcVGbkCO15NckC8rm0p3ngbEgu62eW9FlwsE8b1bVK
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAwe3wg6qp52ugX2ibL+Mc7T/NIwQsoBx4R3ZYklmxl/7ZtJSu
9ertJQUYiNxZsz5PTKijLldlb47Kpu4MC8xt6DBymlDyVDolX+b+f612rjYgAJv7
H0QETnn/mVaFZlOq6sJxr03+jziPzD3RGwjxiF7t21oz1z6vwSsydCgiYe3pEQ2h
VgpH0BLN2Ypa9noa3Tm88BzsSYeNPLdqhngkA5UHg12WGuXEx6NLTaElnXySItYz
ZRJ76aOmVeH8imNTIjeNif9rMGscqXUtysbz2cylnm4GpaBWmaGNx84qLYiL2hJy
a1FzYECNZVuP2u46KEOHOwNLdlwYnUUuUqIcewIDAQABAoIBAQCwX4qi9RBZXNUa
cLTTNKcWTzRuaFl9tObfd47Oa6zNJAcz6RXGqsbLKHtL3bvm/QB6I9VlTC8A6sj8
UPu7r002IvnXx07ds5RSSG+mB0ks4CTy6OnXYbDY/rOr7bide/KyV+21FiYyc6q0
gnQvNk8VS+Df4oXLeUO3V2Ynpmi+zl4B9dDT5nZ6bb26fYI8ei4HDPexPdQbJQ3k
mCimfkMbodEsrJfhM1V/NPwHxJvfXa8mTsEuJnn+efB7bsS3GjTtQ7nuIiliSqHm
SONfIUWYdgEo6chSnKA7MDWFsoPabV3zYrPU/aJqMeoCH2jNEu52NiOhTkv79Dg3
AAqci1CBAoGBAPbdSxAWGaRv2KEa3Zry7snhhSVth3/wY+imVO7U7Z3dO23b+KNE
iEobXbuK6eLKvskvcHel04DfUbOhNws1qytDpG4rLklXZvX8eWpTECkt4BPfefVi
SeN8FCxpx2JSmQgiCzDuAGTg530OaHHTbymhEr+Sl8rQWBZYjo99A5lLAoGBAMkb
KLDai93wWYt96MYn4NPxBhUNbSW75wKSi3PHgHvnAM9qsInXo82BFmw6oUFCit6h
zRc+gAp2wsqIaka9/Hao0MSeCgR3xuuohZeOKmSmItnw70k75Qgrnu9wKyCEdpC4
juDnkaf8G6lT7+Re9g48/MA0Qd6l6WVvXs5nTDuRAoGAaEDqe1+p8pzdcqQi5FYl
7BIWpcjMyYYe21irU7WOp/WPLIUSSvkdSZanDhXLUmDnE5W6PH1Ghg1Jtr+lvFEs
+Xd2kKQhxw1nSQkXyYRMtedO03W0TqH0rGJxLpR5hJd3U0z1RvOsLO4iNNkJ2NA/
COiiP09MVXWJTd6WThiwlWMCgYEAlbwfA+71DP6T7YSF+GRgxe1DdhFVHy9UxVmP
c1krlRVeSRFK+JcSY0SmCVduEUUWWMVoCtKCS0g5qMsBNkLm4wK2zm5NTx5Pgc8s
CLfVYLNCZ7s4rvJliTvRTr3ZnpCCJycDWvmQPd88SUsx5nu+AMPv/Lvr/3bQ3LGb
iVroK8ECgYEAoSKTrvPcy+/ViHCr8ctBK7oIWiE07l0OeXNsH94hTp25OtBScGIy
alsJJrq3P8NjRJvxvbV0FXhMN2Mq08w3sZdCbZW3t7hu9mk1chxREcmmmfcJIqxx
x3zd2+szabHIFg5ozqybYbjmJfDZxNIG8h4HvHRdmBZocbRQHBM5VN0=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_HARVESTER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUC/PhYZPSyT/cH2+54Hfayu9ZXIQwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCog5fCeSavpTI1/3mA/Jv9XJF6ZGRzmNJq8JdRPUd/V6dQ
eU5cOE7QGXbqBV1gQUOXIf8Ke9wgwcMPGRLBbhMQcd9CqWK/rZZOuczRBoqyEvQP
YhkyPWmIbRsNTLg6KYxghdCD9Ps75YWBpxb7uGwKgYadixPGGTDlbGw4m4T+xoSX
kkXcoCiYf+AnWdT/xYloEG+ovy0oBfOfv3q3ps7ECZRX/hZ+4RCRgA1IYi4z7VwL
JepZz87PH6zv9D1CmtraQVZUD3UJRfMGVsimLlH09r+mbZm3Ndu9cO7fLLkLzLP6
w9hhibZtnNAOyLDYrgOjl70bGjePzeodmqzPMY2zAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQB2/xNHBk4oXI5iOyhh4Kob
7ZVFfnjnOFFVhoWYAHSL4rJy6Zk12VwqsvUh4viwkSgmpKkZxyjQR7rKGTyopzHJ
aUEV7mhHc6lpM1biTZyXHz9PIJAgiHe1J+CTm5qVx9STi1b1cJ1FlTYK+7TT/noZ
Pscg1KOw5rmUbTcJ6UnBF1EtSSl+JzPZDxE0/NKBKJey/vRZXj8l4WLiN7sZTr9v
n3AnByDua5653q+AOTjoWP6/U/w1JWa4QNCzk05qBnFLczWGmU/oAXuvIRkTZ+wq
L/VQNnOjmBDeN+LAVAjUxDuGxVJiuCQisUiV5KZVl2kAayCgJccEI5N+OYKO2oI+
-----END CERTIFICATE-----
"""

SSL_TEST_HARVESTER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAqIOXwnkmr6UyNf95gPyb/VyRemRkc5jSavCXUT1Hf1enUHlO
XDhO0Bl26gVdYEFDlyH/CnvcIMHDDxkSwW4TEHHfQqliv62WTrnM0QaKshL0D2IZ
Mj1piG0bDUy4OimMYIXQg/T7O+WFgacW+7hsCoGGnYsTxhkw5WxsOJuE/saEl5JF
3KAomH/gJ1nU/8WJaBBvqL8tKAXzn796t6bOxAmUV/4WfuEQkYANSGIuM+1cCyXq
Wc/Ozx+s7/Q9Qpra2kFWVA91CUXzBlbIpi5R9Pa/pm2ZtzXbvXDu3yy5C8yz+sPY
YYm2bZzQDsiw2K4Do5e9Gxo3j83qHZqszzGNswIDAQABAoIBAG0x0E4ZOUNJ9Y5d
/HrjtaTorfA0S49IcNkRC8x9u+29e9K+uFMzvYZFafPdBBPSVp0BT4WYmxyy0dXf
tnKXBE18rGJC5pU0Q5jB9wFfjtIzS+kH9THD77WSlZv5ocs2jxsguuw2+/FlGizY
fCEi8QehxPwjWe3c9v1DU6EezYBVT9ANny0k/tjIRWgl8XpCuErIOh5LbzdnVINx
smAPD5xbYA85HDSGxWL7ar/nV2cMyMPrXjq13cfMyJSgMgGQ7imMje3c4aUDNZdK
hhuNIAYqGqfGRvT7Sg18o9upN0pm8NX5gXDOifgqLgI0Pt07pomm3LdOlz1mJlqo
sWYiuYECgYEA1xuwXlNl29BiKKAxjpUPJrxwVMX2J1Ijrx76YfLWRkWRzCotYqKD
vvy3NyVUNJW2mDunAq1q/kjlf6c0M+bAQdF895hiYgQWmz40NwtlBG0NIuUvtUCa
EAj1RXi0mKvZ9da8p2eRL4GZW9CSgpK0d9Yq9NVJDxohL7OHuE/KXkECgYEAyIxi
k0BC4My6GX7zaPBt05mRWsaWhXpP4pN67sox9QLm19rP0eO2ivDrvc4d1ue9JyOe
W/mmmPI8wTIm2AgJvXKhUz8x1idwJ5I30NicOflBEhg9xgNlXFv6ja/QZE2PjyUz
l7UTE525Zwn2r2mtQSQoCljPYF2HhgfFkIbglvMCgYEAzCOP3gSBbvk0nl9giHK3
XUiJxjnUX/6YtNHORnRBm5DcS4hfZ/LY2sBUU7ZOUlUeYxyBY44WMtoVSm7woKzF
GfFoCkUIYQKGPa/rt61NocSoKcyc2QNE8iC+O77QjO7SO3cdtDUaWJ5CXxryX45A
TFXokE91NSrUAcP78hNu9sECgYBWB/MZnA2Uhf6nhVBCCjHy/gPe3yYfKHMwjXfF
DDQWGSKSIqnYLklWnTdj+xHN6Se5rIv4hMY1AmWRs0P6lKgo/w25unhUmCKCtzT+
gI20SPrjGkcVtMs8rbB0K6HIBYW6MIlLYUBHv/eS/jE22qyaLzqGBccgXb8PfjIA
Z/vchQKBgAv1/ufFNbrJqWWHsop8lz73D8jG0SEEFXsyOvsAT3E0MzfKK00J+o/q
+1Sw3QAXWmtn9/6QeRFk2J5ikSKCpz20oWsVWIoCHVZDb6/FkrLJn1HbFGIi2BD9
eIb2MjCrudZLGJKlrL1aMSHJ1QZZNczDF/RtaUyD3e+15qLrXczQ
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUKXI5XpFZ30y1ouQq11Ke6CJYc80wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC5cLVLbbFTsBDiYGEvK2t3V2I1o/OjEbX/xqAcfYasvNTo
E8q61KL3tjIB5kdKYp2Ywl0ibUSnM8M9Zm2uMz+Wrpc0YB1H6IEpoN796q36m6Xh
/O/lDpatgwZkRiBnKVAuvifGeVb868keNBKAZ2DNHdpQcRtbkG6jMKSNonmOh3Jx
nurvv01mvf7VR7iTc9o4kBIgO2lOnxB2dpFcPxdi/kIIGjrUgU7tzAh4SfQgKKVg
WwRDk4BrlLWLRGkPsIvvoUNkVuC0adqXOaX+8WRfalw1mNed3OpYQ+W0SjHWuw7S
CxrpcfvXMniy3CpEdBJmbtKyC8Somj41QxmRRZblAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBVYAjTaWQpR8Ke7zD5ahJg
G/UDUUh9ZhUGCc4E0e2+qVjDgkJMqNjXx+OUUvj+iKo0A0UI/QJYf5n7kxs6C0GP
JLqt/OHbxdqRji3GQvftRAMjaIQ0KmRUIgN0XwbDUvFJ7QHBdV33AeWvDh1wWvtD
DYmMDausznQQBlYApt5LDq/Y+96rmMiaPGOga1Lz1GWON5v8RU3qPLyc8GgCeoaV
zoVLKiGDVtrhUzaOBTsZ464ZH74hIzjEb/QDqyoQYgk4o1RSdewNhnzmwWmS6hXD
E11IwGGiy0ix9OWyL5WyXvjHqjtJ219KIYQuLsEV/lOdHsybBcAQygjVqgMkz5CL
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAuXC1S22xU7AQ4mBhLytrd1diNaPzoxG1/8agHH2GrLzU6BPK
utSi97YyAeZHSmKdmMJdIm1EpzPDPWZtrjM/lq6XNGAdR+iBKaDe/eqt+pul4fzv
5Q6WrYMGZEYgZylQLr4nxnlW/OvJHjQSgGdgzR3aUHEbW5BuozCkjaJ5jodycZ7q
779NZr3+1Ue4k3PaOJASIDtpTp8QdnaRXD8XYv5CCBo61IFO7cwIeEn0ICilYFsE
Q5OAa5S1i0RpD7CL76FDZFbgtGnalzml/vFkX2pcNZjXndzqWEPltEox1rsO0gsa
6XH71zJ4stwqRHQSZm7SsgvEqJo+NUMZkUWW5QIDAQABAoIBAQCTMXd2K9e5ieOd
DMuXWWuwCtiVo1Hcek5wfATTGIAx1KFapXsh2W6SGTiQcWzdCnH1szGiBgGchmXO
8uLUhzFONb8nf7M+RLthg6P9AK6gYbPGMbNpqa7Ig1wrc858lDplH+MKk34MvEuj
gcm9ylD3/14uw9jnUTnApve2xOSf0GDUdIAT0AkYfHmn0/NSev40uMi7q0KmH2Tf
3VCHjWTLKvEp5/z6a2vBw2pxQj4KpC9TobfZZCTBbnzt/VnW4zG3mZHcAYV+EZqU
/UZzmOHQC/0F4FkOzS8THlWb5rXUAv80NpOTzf/LNQXy6QhBpQN9a3atPvzvN4Eb
dt0vD+PxAoGBAOh12gPNpXolJJYIHGhhKqYzFIBh9pCJPlmQ3ok+lS4Frhfgzjzu
5m1daB8pUO0du4n+KLmQMb+cXpZTJ86KqRE2MXtuP71wt1RTxx+7KQCuuz/KfY8z
8A7NzGk9swXx8EqdfgYcm4gqrRjOYhvwWZ3R1m9b0x9A35QjBAZbLcVDAoGBAMw3
8FguXSmIKUtU916S8kCZ8y+w+1Uh4tDYUMprbbvPrsmdiZI1pCRULcH0k7uw+r+n
UviUk0T3CZBTSP5W+0WZ57uSY+aeJzZeuyn1cNguDBiwVL9zmV2JkvFcIfXEWPkL
Ae5OBVfGUtucg6+Xp7UdXrYWg2XkMY79eqhVWNy3AoGBAKCfbjlai5DOwWz5xcdJ
/JJCkVP0XM6aRn7U3y+uEp5uRlExgNARsx62gA+oGMb+2GsNN06hF/7yKVlts/+/
R/sgmyhSkbBwhfy6tshyJm7WTYRSglfE54cTJL9DZsQg3IxyLnZCpiV8d4bAdIIh
nYqzR5xCsqrRxKszVsCdmA7JAoGAbwaihm5+e8vpF2mUKzict/56thz0J26Kz5wr
IEGToR3iGv6pAnJjUNTrI52Ci/JGANhJRZgRENd1vZ9p+cz0QvzPfayy33hwPSD3
hHJJ7V3reai0CnogkTfwSYQbenBLJuqTHCoSwYuzFG5dMaOzq8XR7hEDUuvi/ahV
fRsZerUCgYAXEJOAnffMvFJZrfflJ62HbPxQDuKtUqZ2aWFRh6/d6yLC+xCTv+AV
Ygl8U9GHqiafLb0jqzzHU+NzpCFsI9IG/6r5O3k+CoQkw2u1mN6diys8IIip5PRv
DsER2F0w6ZrwEkUpFxxIpQgTCXarTFugMbWkjhjcpgK/lDGWFsWW/w==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIURVoAXVmDtr+4fUDOOVA0ZXW+RTEwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDZsq3BSwg/a/I3AlY+Uj3d4S+W8jIhWHI8XHX5Ud7k+auJ
gfKvA/D6PrYI/TunHFzTGdVaGOd2y2Ylw7KUFZ9YIjtfQfNI0UnuIEyovcmLBiw2
tCtQE7ItEgLkrEjgBX8DNWlQxGKZ8+HAeY5Ux3eRsLJJn3fBFAxOtC+cxF5hFFvt
EcGTMo1lYr/A/XKt5Klh8eoOLkE8JNbwuO7AQC5NQN1AP3ZP+3rOC6AU+xdECF33
9H3gyfXeGk5ixLpV/d+Oz3VzRgmBCBt7+QLT/MSgm+xD3hO21MB2cBBIHJ6bzeTy
4nwvidsnSPPn6RoHg5vTR6HFmLvALirbiA0arr3/AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBl4c1dN+9iucNMtM0bLiAq
qeGRLnjGhizrhXuI0PtO5zrgmWgPnuJ/gZUwoPrGczO5g8ZO2zQhDuz8QWXLCNby
UL5C0aQrMafIqawKd3oumnHFOotY5eW4hf1rKyYfCGJ15xisWDIXuVSHzf6YlNlk
avHfchtw3I6xPIt6ui08qnRjuxVeoHbKKgM3DOx3vfvWiOyjXI0pZt2uYdMHdX8s
kOqJVoEF7XvSheDLXjhF7iWeGDmqjuBHv6eRfnA20MOXbE2l26Oa7M9z4xzVZBvU
GxtQwVXfxwmo54EuxVSS23gTD2q85JRRfPWuZnOs+NUr7e8P9MkejuC7iuvA2P7G
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA2bKtwUsIP2vyNwJWPlI93eEvlvIyIVhyPFx1+VHe5PmriYHy
rwPw+j62CP07pxxc0xnVWhjndstmJcOylBWfWCI7X0HzSNFJ7iBMqL3JiwYsNrQr
UBOyLRIC5KxI4AV/AzVpUMRimfPhwHmOVMd3kbCySZ93wRQMTrQvnMReYRRb7RHB
kzKNZWK/wP1yreSpYfHqDi5BPCTW8LjuwEAuTUDdQD92T/t6zgugFPsXRAhd9/R9
4Mn13hpOYsS6Vf3fjs91c0YJgQgbe/kC0/zEoJvsQ94TttTAdnAQSByem83k8uJ8
L4nbJ0jz5+kaB4Ob00ehxZi7wC4q24gNGq69/wIDAQABAoIBABDpO2wvivV6SjeR
u+dddibdTlgYemJyv3UG7bcvb/QznOqyqIqF8NtPsc5i9ZZWsrNHZ3Z3RsvIoye9
2wp734P2LMyKj/6RG4AfDDVzgMuG8DpTpqWy0f2ET6s54vNcGfDC3mqCxvIUqu3L
w428bQJpSoBDngbmqsoWXzh7XKWHzaeRNzhmEd58yNZH8Fb0OhPWESNA0U6t+oJx
eZ7mtSzIY21mF0Qo2JIRMC2BMwpK2MMHsvTKs4VcARBAA2X7K9ZAxAoASTZU3xCc
nOglUUOZzPa0mGses2E+b1pbI2M2YLhwov6kRm7MihtjXRgMHCVcOJwuNK6QR0HC
K29CP6ECgYEA8mZ1mvY5Xgt85fgQepVib23vfbdXHqRRKkkGoqky+o6Pa55bgSxS
wzI6dj3LJD/Qk/5I7gS0Ft8FCYeFQTDBf2a/wZ9+RH4k3NOR9WYVxEQtAnT9DeSq
DfZQqopSQ+29eosBS8uqfI+8C1C+k3aS4qJqpSpyaj58ZrOPCcZyA48CgYEA5elt
GE0oIzRaPmbH7aRSgSc+D/MtmMmlDQekA1v5vPKPCdrwCvNHh73sGpHGeYDuEZZI
wMMccVJ6rBQQ4Hsk2fmrHj3dbn2HNB++n14zxAX9iv7sVKGvrOvxTnhSidRXuQ92
Ap3wHFAY2x4oPRRTBT+HJuz46wmqooOFGMd0ppECgYEA21meaNkRdqn8nvoIp3UQ
+3bHNsM24fKdxB8LExz7lcJ1xFQrx8t9JUgJoUAv2KCqtZFxG3pEIUI1g7cP/bsK
DqjDM4qJr59a6j3GIgP8BHwRIt0MtYrL3BCeVIURBolXYlHxnU4y+77x0meB3V16
c/23dbjgioX6+tDXyme6er8CgYB1puMV+X3drg+0OSJ8QIeb4foHbXja4+1bYpqS
wYFmKHX8JBaMc/wZwZ3N5uU7DjhFtbMbOX0XnI57+nS8eyfbh8ECY8Qpo4EJsmj4
4tr4p9wcQeGsWWUtxzuf3UDXmVser4PDSREzW+WsU51hzEHDwMOnrsKefD7elREK
Ih9WkQKBgDfRy6VKMVBnyvPW+mby5sS3aAS1Mq6CJXjWTWkLoolkhATd3YrrC2b+
/IuSbjsgagN3u+Ih1uIKb3FDHjKv7o2o+bRot5415P4z+FQeKFrjU/pPF/0B80ug
PdlK3MF+/2UgKAwawIimV8HSgtSSx6VgDk8q0HUPVJHxdziyo4dR
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_CRAWLER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUGfJCme460FNV8uIRcAb2+fNOKnowDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC5pSuCco5DLrrC806I0t4XFEp/2HgHVve+xI3mIyl4A+mL
XXasrNMeVEo3MU1ADZBntZJcDl16PvHx01/sY5vo+0BwjzXIZyl96B5yH0ibxWeo
tZbkaU2FOg1/aR1sDL9guxQZ3JfrOA7AhFX+W5o36X9ySUsVcj9IFSuBd4WreAz+
lo/DCcsdNq6PvfpwR3Lz9VURBsYmRseO7cHdcASzr/UbfaIYFaJxYQzUkC127qXt
6KEqaUKPwt6/pNSCx6PChTS9isqz7oTg8CH9Ku8M9lQz+w9J9T1/AmuFnKUhLAg6
MVvl7bGDG657ndawiUYLsFnAtCQBxjnhdhngv0LPAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCr3TlMTjaxIWlpeaHo0rcR
CmZNB01iJQKHhu6HEKJunILBf1eH8Gm/CLftytMtbxPfEUB/OG04CvDfCYAk+yVK
lVhlLXKU1MHNbjCEYYhL9Nai862dxvAMLI4PMbrhIl9qPYfQ2tZ/yRKKZIy0Jnsx
EQECv1dFXTDPFZOd8/ViNFmHNLR9cHAnEuTFKnM2NoTOYlRF+f01yTF3AAAgdNw5
ViGPO3v4Xv5XeLVmpxOqG4ZXdCE4ZfSkqmR3MuDpe5GsYYOeEClLSZJxX4kNwd7e
EK8qZ/rAt2Yk+/O/FKGa5C59qj3dKiVVTN5UPfFD+cPYFFjCNjy+GP+Mw8sKit+r
-----END CERTIFICATE-----
"""

SSL_TEST_CRAWLER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAuaUrgnKOQy66wvNOiNLeFxRKf9h4B1b3vsSN5iMpeAPpi112
rKzTHlRKNzFNQA2QZ7WSXA5dej7x8dNf7GOb6PtAcI81yGcpfegech9Im8VnqLWW
5GlNhToNf2kdbAy/YLsUGdyX6zgOwIRV/luaN+l/cklLFXI/SBUrgXeFq3gM/paP
wwnLHTauj736cEdy8/VVEQbGJkbHju3B3XAEs6/1G32iGBWicWEM1JAtdu6l7eih
KmlCj8Lev6TUgsejwoU0vYrKs+6E4PAh/SrvDPZUM/sPSfU9fwJrhZylISwIOjFb
5e2xgxuue53WsIlGC7BZwLQkAcY54XYZ4L9CzwIDAQABAoIBAQCbQCT1z4Vna7Hm
DQF1bRssI9z1s3sVcEZ5c/jTKD6qzmLGGOCBIXrg107Ff2aCFZXZFUCT2bOU4wUE
3mdO0jJ1kYDfYPRyZsuNLswfVkgrdNfugAXzeJjKvLTDA44GaVa2t1zlD9TAcj3s
A//CWqrK7WuWkPLIuaVwS7v5ZpITxT/fV3rEm/aNI0bKIQvg/QpXqX19q91WfFct
1zhzim0JRU6FmBqhpYG69Z2da9ZoNvj6ZENC0nNhaI243ubkvzGSz/vICREnGvlu
mTq70i77G6UK7Li2+7jTKtxSWhcwpUFjdnzxwNd7aDlvoTS1F0gbXQ4QlaRm9cv2
0viZO7QZAoGBAPRepRdW6DRnYVbtd6788i/qKiTK+odtbQj9C8N5jBbLD/NWvTXL
syxSbxJUpIDRUgZOqLepNoetZZwDJOWnavMaLKsnxYGMUstH+cMrAeYbhyxlf+ol
oK00XzqQjW0kUL20usHQLr5GcWuAonsYIfLSucEZDI/bF+413hIlqDQzAoGBAMJ7
CVo12fy36HcpKtWR55r9G7SYh71moSvt/LNlDwQaCrvt3ySKOid1y4Ufob5eQvDO
UBk6LFpuGH1pIBKQKz8okw++W2w7jqmcY0RdUTS2jKk9fwwIR4EtSpv8cTjE3S/1
g9P9SjVVkAL/o/VVSEWTYLj/ho9Xhh3WDsI9h3r1AoGAMwcUaDRAlrjDrbg2lrbB
B9pY5IfyGpdx/j+A1leqNhQ/B2wkZHhduLKZ+PTtyOxsuV5xgrB174z4u8Q4TzBP
d+YOT8slRfD8VPB5qhRv+BHlfxLOzCEBVUmrXPpUXecIaSS1HsWPDTJ+eplI1HVs
mV0BZt4JLnzsmVRsQ9PTNNsCgYA8QgcJznm2Vf1PPpApEEYkvZvh/wi/5Ja3l8ue
ggd/C9qbk/55weJ264advslMxMQU/LfQuTeY5VftM69eURE1Rosaa67EAEgZwXz4
Z7mLjaxTm9xLjB0rpy7g2fzyy/yEqZupCWf+0n4Gj9LrZvs3o4xqhbHZpBLIF9UG
1i2uKQKBgHEEncIbSz/BYXH3u2jh6CacXaoe5eh4S6ihEup1EZ/ajavYLtD/cfT4
9QuJjBSD9me7I4Rdas5OtvRVcUbo8BLISU3Y9bMkTW8vf1wof7oIAlB6Q9jZFaXA
p05qDfXHJ4/DcMWQTkfC0PNVslc5lPHJ7jylPNhMq6oR9Wn3OH8/
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_DAEMON_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUEfp1B/UPB0Hf5bcKFsJZ/Jg5ZUMwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDAIc6vaGVenMWjN8uyIetlwtTXCVRK0aTwLj6HHXpcJCSF
bIhvsZRlZ7Fvu4VelVNzXH/kmZhpUXY59QQObspZ2z7TfVLgS0r4mAU8WqmCGi+F
7cLVX7Du2E06jGhsBgKd9l6Ybud0SlW2/y8IzdIq75bW9qD7viAkbXg6sSR1zqwg
2lFpoSKaf9TFvdbgtiCIeCbTQEwTZktYEEd3S+yY/HierG9RTcpXSJvC1Orcv/J8
iH89U+C8QfNjULCChEOWhaw+qol2fKOK3394JsujORUn/9eHeJt1otc3JWnyR0DG
ok4y62xxl/y529npRJEkwXO7zoZXQVm+PoWZvYHDAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCEugh4aiI6L9PbBZDEnc7o
tUU2boCKwOsI6igtPaBhZZcQhyTi/qlmPMKZm58TFS8s//oiKhD3q31+OhQIe/Ak
pvuwJwcJLe0r4iUzbtGJsn3aIpXP+GHqEDM+38tZhXMpxq5Kv8Zp8Nm7R7XidGHg
OOBXQ64UDTUAHYvs+n4ltYLgTsqCPPWsHxieABjC3YDBJAdGa/H4cRB/qU7vKNkN
uAyfhVLBzaAcyYtQBef9cuulTUaE+KA8mN1kJNbA/b3E2MCGYCqf4eNN6gRdmtxG
16aP/7qxvVlgWh1mYfUvIlszazjI8TI2N1y1JZOWpmO4RoyWhvqhWdPXKC/HyVub
-----END CERTIFICATE-----
"""

SSL_TEST_DAEMON_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAwCHOr2hlXpzFozfLsiHrZcLU1wlUStGk8C4+hx16XCQkhWyI
b7GUZWexb7uFXpVTc1x/5JmYaVF2OfUEDm7KWds+031S4EtK+JgFPFqpghovhe3C
1V+w7thNOoxobAYCnfZemG7ndEpVtv8vCM3SKu+W1vag+74gJG14OrEkdc6sINpR
aaEimn/Uxb3W4LYgiHgm00BME2ZLWBBHd0vsmPx4nqxvUU3KV0ibwtTq3L/yfIh/
PVPgvEHzY1CwgoRDloWsPqqJdnyjit9/eCbLozkVJ//Xh3ibdaLXNyVp8kdAxqJO
MutscZf8udvZ6USRJMFzu86GV0FZvj6Fmb2BwwIDAQABAoIBAQC9oCBHyvdRe9Us
FCN8ejHES5iZa2HAPk1Vp66a2CMt0ZYiAU5fPprBwqfDKQampSap0v9+9YERYQ8Y
gJQyUnJwYQ0O2r/zExy5YgC44pouB/4jZthGk50i/mSqhm2BQCVRFhmixMK3aa5T
YGRhghINwk3Td7LHA4zhpxFki/T6Nvp5R49zhWST2a00JIfKEUF7X/3ILVA1ShwT
Gl3lWZzSL3qWkluNMtHJVuA+9HRDsjbWID63lF4K5HHl0c+0yW2OTOgMH7zuxmLT
IhEdc5Vr5wCvgFOr1MwsXpO/OIT0KrorobSSn+x/HWMbvUoTVhfjiE7qxRsfqh5w
ZPru0OBBAoGBAPU+4ZSAJKKtBEjs5ej7LJbmGedQCBYka/u+FUWw4fp052bkT72M
4Y6cfQlxXs59i0E/JPPqytuXx9bRCNG7929yvCzcrZBNij5NLR/EYrRqtnDf7O49
kCu8owgv6/zglt47kjyDuNv0JhX4D9iIcz/4TuFUG5zLn1SwWqUCOv9RAoGBAMiO
rNT2o4gJSg2wKn9oWuR6ysBQuq7Lj9kVZkilHVp2SwTtnLc3CjfFbmPivAhodRN8
y/zlln539Bi3JyolYg0YDeU0oeI79HyeKUgflxY3rXB2tXhnK5W4l7Od/BZFc2Cw
hSYMzlcGte13DD/gr7XWohqEr5aQCXgM/3tZ+3LTAoGBAMmb6+4cegGRolghB9BD
zCAxAVJ7JGqvfmXxmaM1ClDPEfwv7K2yxypp0xCUNpAh/PyiYEp01lc3q30ZUtq4
X20rMS7gK37Zf7A/2bynwUz3/QtFyoz/5ylNZekxHBtCtkPzTQCaeLm5OCYPS1eC
tNv90TrD3f9EFbOVVq8X6lBBAoGAGvwngRgWdM1bK3BSp4XxBOEIusuh8rbtCfZ5
Jrkgs/VKrsUR2w0K0Oo9qi7twevcJN0bzVFO6IFXVKQAHwmcocpkxDxKs9gBU2ss
fsnRWGnxajpuvF6VXLXTo5VUP+LkXVQi9jWu5cK/Y84q1cVznvHcKdlEjuueeoq1
LXG0BYUCgYBK4SYd4U/DGiSE45D/ikQa766J59cd4hOHAKTdoTh7ZWmn9Oh5ms8R
ggcxJQt8ZgGnOJFqjF2xN3tp8oluk8gTx932Myh90iYUPbxXGjB5mYJ0g0fDXK1X
i9wjKsZocYKO4ZzhtdXzbBqQcYMhoBicoEWY8NpzyA+0gVIx+bxKuA==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_INTRODUCER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUQGJa9B0MRFmHuvjXjyCBbXypCBEwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyNVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDGNB8T3gN1kLSJ4QhzMcoS7UPLvoWxvxVqYUSEap+4EI//
LDKVlFKOl5icf808nVxGwb2XD7Io5wkX1kppBiqudri+WwHn9ayyhdpSi6eUsi3G
suPObKUTzNH9LOli6DA++GBaYoQUVXoOKWz3DVk8QMSCXgej5+09owdwIMHl8ytV
G36/LpPjH8Chr4y2MAUtz2Dc/Evyq8XfBIeD835Azhr2RXs3c/AOXVWXPt9A2BW8
sA7WvztNhYnqtL4EXpgG6H018aZTnCMEHEbil05fkfs+zRxgncqQ5BDSqARbkSDu
SeczaJtmW7E4yqRZTFZF2AnssyDuPQcl+qiYNNU1AgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCFCSfOPoAbrIMBPLkiHGOv
a3OJmi/Kw9qfOp6iCVb4A0CE9ShzBZJqvSfZ/CnPeLsXy9zaRytrVHgkOXQyzbbv
uKiaBgwnLT1VFQlPorGBVJZisLl6uc+PIPK+9syqnOvaeilbI/UH1WrcESwrV2C1
7CcV8ibj7a9WnWC0LvzNMDHFKqPyOUTmBZWHvS21fYHUXV/5abX19TmwOzJTOWuc
cms/M6RfeldLIgGhxGnqn1un2KLXJ9wGHqcTVkbp3Fvk3Sk/T2zxgmJCLLLzI7Ap
cvVw1It2vL4bmGfF/1CTjfawhEbmtvTl1NkY/e0c2AORZ1eCvz/ZQYuwZxCseP0u
-----END CERTIFICATE-----
"""

SSL_TEST_INTRODUCER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAxjQfE94DdZC0ieEIczHKEu1Dy76Fsb8VamFEhGqfuBCP/ywy
lZRSjpeYnH/NPJ1cRsG9lw+yKOcJF9ZKaQYqrna4vlsB5/WssoXaUounlLItxrLj
zmylE8zR/SzpYugwPvhgWmKEFFV6Dils9w1ZPEDEgl4Ho+ftPaMHcCDB5fMrVRt+
vy6T4x/Aoa+MtjAFLc9g3PxL8qvF3wSHg/N+QM4a9kV7N3PwDl1Vlz7fQNgVvLAO
1r87TYWJ6rS+BF6YBuh9NfGmU5wjBBxG4pdOX5H7Ps0cYJ3KkOQQ0qgEW5Eg7knn
M2ibZluxOMqkWUxWRdgJ7LMg7j0HJfqomDTVNQIDAQABAoIBAFKU4OX8OODBHBfe
pRCqDBH6vaakiTvX6+pZAJ1Td5zPec/N8H2WQRecXj/GmBLLVek9S+sm5QpZyNYf
uP0tTpdGbA8UCCVHnV78mkyOV5KC8sO5QWV+qwEm889S6SMGryNthWfjaDi4rJQ9
+mKtMyMBsV7IItLODXEC/lRfsapG/PVnO8J1dCx+47BJNw4lA1XZQrwwg1TrrKTo
+t9N9R9GmUe+zqXKs0d4al/02JDDrPdReuKMGOAMnWvc14Ppyb8eYfC8lk6nluHt
gUccQlkXH963kPxHhmysC1Y470DcqUooiJADOh5GfD+W860GDeWqib5I5IOJ4HmK
xgTq64ECgYEA8egiv9nFuJNV+yN2FgkrKo2kqdsyMnlOsC1ppdfsUk/Clx6LB2WA
K+82boWmnzIkqhI96wlZ1Y8LXFS5fqMQeeO65VNwQyhk0KQnlJ/dTYT3FzSuZ61d
8CcD3p/nMrcXT3H9HOfYJooF1eATtcbCP+Sc3SS9JczYDcut59aA88UCgYEA0cAv
NHIVOUVL9EOyIQLSBsGTF9u23bPzCUaGUHc82acruRwJEcSzpfNaj8NbOzk0tR7r
ZawkbrlhxRqVC28rE4jvhPSAO9swq3Gr4IMjhGnJ2gc81zPV1NyRY0jR586z4xWk
kra01MYhEcJ5gya6D6t1y11glq4ht0zhrFcdwrECgYAn8/cJSKZnPa5NtCWkrg77
EDnJ8/HudCqS3m08ftUBIzs4SkscBZ+NogyTZG+Ii3eSv0CKuRilNOLjdPrN95CZ
EQulJIq+DMXZz8LZwS2DyBonMwQ7C18gctEoy7AbqDGpZWIwi/ofI1yjXkbjFtiu
RMvDmnXC8HoejS1DxSG3IQKBgQDM+b/nw7kD77lrKqCv696tpYwGm7uX6xwNq3Lk
vbGkjd6HlmMyjwR0n12X8nR8asocWev2vwQXhGiMQw72TpxNCdvwFTQfynNEh+BM
ljsmUm9k9v+42roTu70ExowCuZhHycW7bntHF5wHjAJNbZIUcB28MDOM7Pyb8bD0
R2oY8QKBgAJUUkmpgpNz4oNNv+mztAElg5LKEX6fNRqrKHF6H/rHmuI5zTrTsjPc
UwBCIG6KBlcmpAsTUpxJ03VrazZMcuyaw+sXXpT8PAcacSTHf5CYY/mEEA4lTcZt
iPfa9TABxtW6v3r2l5tO9Yz+Yb0v3nfGtaxDgp3U4+0/QzUwX2Jd
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_PRIVATE_CA_CERT_AND_KEY_4: Tuple[bytes, bytes] = (SSL_TEST_PRIVATE_CA_CRT, SSL_TEST_PRIVATE_CA_KEY)

SSL_TEST_NODE_CERTS_AND_KEYS_4: Dict[str, Dict[str, Dict[str, bytes]]] = {
    "full_node": {
        "private": {"crt": SSL_TEST_FULLNODE_PRIVATE_CRT, "key": SSL_TEST_FULLNODE_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FULLNODE_PUBLIC_CRT, "key": SSL_TEST_FULLNODE_PUBLIC_KEY},
    },
    "wallet": {
        "private": {"crt": SSL_TEST_WALLET_PRIVATE_CRT, "key": SSL_TEST_WALLET_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_WALLET_PUBLIC_CRT, "key": SSL_TEST_WALLET_PUBLIC_KEY},
    },
    "farmer": {
        "private": {"crt": SSL_TEST_FARMER_PRIVATE_CRT, "key": SSL_TEST_FARMER_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FARMER_PUBLIC_CRT, "key": SSL_TEST_FARMER_PUBLIC_KEY},
    },
    "harvester": {
        "private": {"crt": SSL_TEST_HARVESTER_PRIVATE_CRT, "key": SSL_TEST_HARVESTER_PRIVATE_KEY},
    },
    "timelord": {
        "private": {"crt": SSL_TEST_TIMELORD_PRIVATE_CRT, "key": SSL_TEST_TIMELORD_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_TIMELORD_PUBLIC_CRT, "key": SSL_TEST_TIMELORD_PUBLIC_KEY},
    },
    "crawler": {
        "private": {"crt": SSL_TEST_CRAWLER_PRIVATE_CRT, "key": SSL_TEST_CRAWLER_PRIVATE_KEY},
    },
    "daemon": {
        "private": {"crt": SSL_TEST_DAEMON_PRIVATE_CRT, "key": SSL_TEST_DAEMON_PRIVATE_KEY},
    },
    "introducer": {
        "public": {"crt": SSL_TEST_INTRODUCER_PUBLIC_CRT, "key": SSL_TEST_INTRODUCER_PUBLIC_KEY},
    },
}
