# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['TlsSubscriptionArgs', 'TlsSubscription']

@pulumi.input_type
class TlsSubscriptionArgs:
    def __init__(__self__, *,
                 certificate_authority: pulumi.Input[str],
                 domains: pulumi.Input[Sequence[pulumi.Input[str]]],
                 common_name: Optional[pulumi.Input[str]] = None,
                 configuration_id: Optional[pulumi.Input[str]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 force_update: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a TlsSubscription resource.
        :param pulumi.Input[str] certificate_authority: The entity that issues and certifies the TLS certificates for your subscription. Valid values are `lets-encrypt` or `globalsign`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domains: List of domains on which to enable TLS.
        :param pulumi.Input[str] common_name: The common name associated with the subscription generated by Fastly TLS. If you do not pass a common name on create, we will default to the first TLS domain included. If provided, the domain chosen as the common name must be included in TLS domains.
        :param pulumi.Input[str] configuration_id: The ID of the set of TLS configuration options that apply to the enabled domains on this subscription.
        :param pulumi.Input[bool] force_destroy: Always delete subscription, even when active domains are present. Defaults to false.
        :param pulumi.Input[bool] force_update: Always update subscription, even when active domains are present. Defaults to false.
        """
        pulumi.set(__self__, "certificate_authority", certificate_authority)
        pulumi.set(__self__, "domains", domains)
        if common_name is not None:
            pulumi.set(__self__, "common_name", common_name)
        if configuration_id is not None:
            pulumi.set(__self__, "configuration_id", configuration_id)
        if force_destroy is not None:
            pulumi.set(__self__, "force_destroy", force_destroy)
        if force_update is not None:
            pulumi.set(__self__, "force_update", force_update)

    @property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> pulumi.Input[str]:
        """
        The entity that issues and certifies the TLS certificates for your subscription. Valid values are `lets-encrypt` or `globalsign`.
        """
        return pulumi.get(self, "certificate_authority")

    @certificate_authority.setter
    def certificate_authority(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate_authority", value)

    @property
    @pulumi.getter
    def domains(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of domains on which to enable TLS.
        """
        return pulumi.get(self, "domains")

    @domains.setter
    def domains(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "domains", value)

    @property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[pulumi.Input[str]]:
        """
        The common name associated with the subscription generated by Fastly TLS. If you do not pass a common name on create, we will default to the first TLS domain included. If provided, the domain chosen as the common name must be included in TLS domains.
        """
        return pulumi.get(self, "common_name")

    @common_name.setter
    def common_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "common_name", value)

    @property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the set of TLS configuration options that apply to the enabled domains on this subscription.
        """
        return pulumi.get(self, "configuration_id")

    @configuration_id.setter
    def configuration_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_id", value)

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        Always delete subscription, even when active domains are present. Defaults to false.
        """
        return pulumi.get(self, "force_destroy")

    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_destroy", value)

    @property
    @pulumi.getter(name="forceUpdate")
    def force_update(self) -> Optional[pulumi.Input[bool]]:
        """
        Always update subscription, even when active domains are present. Defaults to false.
        """
        return pulumi.get(self, "force_update")

    @force_update.setter
    def force_update(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_update", value)


@pulumi.input_type
class _TlsSubscriptionState:
    def __init__(__self__, *,
                 certificate_authority: Optional[pulumi.Input[str]] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 common_name: Optional[pulumi.Input[str]] = None,
                 configuration_id: Optional[pulumi.Input[str]] = None,
                 created_at: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 force_update: Optional[pulumi.Input[bool]] = None,
                 managed_dns_challenge: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 managed_dns_challenges: Optional[pulumi.Input[Sequence[pulumi.Input['TlsSubscriptionManagedDnsChallengeArgs']]]] = None,
                 managed_http_challenges: Optional[pulumi.Input[Sequence[pulumi.Input['TlsSubscriptionManagedHttpChallengeArgs']]]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 updated_at: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TlsSubscription resources.
        :param pulumi.Input[str] certificate_authority: The entity that issues and certifies the TLS certificates for your subscription. Valid values are `lets-encrypt` or `globalsign`.
        :param pulumi.Input[str] certificate_id: The certificate ID associated with the subscription.
        :param pulumi.Input[str] common_name: The common name associated with the subscription generated by Fastly TLS. If you do not pass a common name on create, we will default to the first TLS domain included. If provided, the domain chosen as the common name must be included in TLS domains.
        :param pulumi.Input[str] configuration_id: The ID of the set of TLS configuration options that apply to the enabled domains on this subscription.
        :param pulumi.Input[str] created_at: Timestamp (GMT) when the subscription was created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domains: List of domains on which to enable TLS.
        :param pulumi.Input[bool] force_destroy: Always delete subscription, even when active domains are present. Defaults to false.
        :param pulumi.Input[bool] force_update: Always update subscription, even when active domains are present. Defaults to false.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] managed_dns_challenge: The details required to configure DNS to respond to ACME DNS challenge in order to verify domain ownership.
        :param pulumi.Input[Sequence[pulumi.Input['TlsSubscriptionManagedDnsChallengeArgs']]] managed_dns_challenges: A list of options for configuring DNS to respond to ACME DNS challenge in order to verify domain ownership.
        :param pulumi.Input[Sequence[pulumi.Input['TlsSubscriptionManagedHttpChallengeArgs']]] managed_http_challenges: A list of options for configuring DNS to respond to ACME HTTP challenge in order to verify domain ownership. Best accessed through a `for` expression to filter the relevant record.
        :param pulumi.Input[str] state: The current state of the subscription. The list of possible states are: `pending`, `processing`, `issued`, and `renewing`.
        :param pulumi.Input[str] updated_at: Timestamp (GMT) when the subscription was updated.
        """
        if certificate_authority is not None:
            pulumi.set(__self__, "certificate_authority", certificate_authority)
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)
        if common_name is not None:
            pulumi.set(__self__, "common_name", common_name)
        if configuration_id is not None:
            pulumi.set(__self__, "configuration_id", configuration_id)
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if domains is not None:
            pulumi.set(__self__, "domains", domains)
        if force_destroy is not None:
            pulumi.set(__self__, "force_destroy", force_destroy)
        if force_update is not None:
            pulumi.set(__self__, "force_update", force_update)
        if managed_dns_challenge is not None:
            warnings.warn("""Use 'managed_dns_challenges' attribute instead""", DeprecationWarning)
            pulumi.log.warn("""managed_dns_challenge is deprecated: Use 'managed_dns_challenges' attribute instead""")
        if managed_dns_challenge is not None:
            pulumi.set(__self__, "managed_dns_challenge", managed_dns_challenge)
        if managed_dns_challenges is not None:
            pulumi.set(__self__, "managed_dns_challenges", managed_dns_challenges)
        if managed_http_challenges is not None:
            pulumi.set(__self__, "managed_http_challenges", managed_http_challenges)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if updated_at is not None:
            pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> Optional[pulumi.Input[str]]:
        """
        The entity that issues and certifies the TLS certificates for your subscription. Valid values are `lets-encrypt` or `globalsign`.
        """
        return pulumi.get(self, "certificate_authority")

    @certificate_authority.setter
    def certificate_authority(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_authority", value)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        The certificate ID associated with the subscription.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_id", value)

    @property
    @pulumi.getter(name="commonName")
    def common_name(self) -> Optional[pulumi.Input[str]]:
        """
        The common name associated with the subscription generated by Fastly TLS. If you do not pass a common name on create, we will default to the first TLS domain included. If provided, the domain chosen as the common name must be included in TLS domains.
        """
        return pulumi.get(self, "common_name")

    @common_name.setter
    def common_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "common_name", value)

    @property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the set of TLS configuration options that apply to the enabled domains on this subscription.
        """
        return pulumi.get(self, "configuration_id")

    @configuration_id.setter
    def configuration_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_id", value)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp (GMT) when the subscription was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter
    def domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of domains on which to enable TLS.
        """
        return pulumi.get(self, "domains")

    @domains.setter
    def domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "domains", value)

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> Optional[pulumi.Input[bool]]:
        """
        Always delete subscription, even when active domains are present. Defaults to false.
        """
        return pulumi.get(self, "force_destroy")

    @force_destroy.setter
    def force_destroy(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_destroy", value)

    @property
    @pulumi.getter(name="forceUpdate")
    def force_update(self) -> Optional[pulumi.Input[bool]]:
        """
        Always update subscription, even when active domains are present. Defaults to false.
        """
        return pulumi.get(self, "force_update")

    @force_update.setter
    def force_update(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "force_update", value)

    @property
    @pulumi.getter(name="managedDnsChallenge")
    def managed_dns_challenge(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The details required to configure DNS to respond to ACME DNS challenge in order to verify domain ownership.
        """
        return pulumi.get(self, "managed_dns_challenge")

    @managed_dns_challenge.setter
    def managed_dns_challenge(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "managed_dns_challenge", value)

    @property
    @pulumi.getter(name="managedDnsChallenges")
    def managed_dns_challenges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TlsSubscriptionManagedDnsChallengeArgs']]]]:
        """
        A list of options for configuring DNS to respond to ACME DNS challenge in order to verify domain ownership.
        """
        return pulumi.get(self, "managed_dns_challenges")

    @managed_dns_challenges.setter
    def managed_dns_challenges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TlsSubscriptionManagedDnsChallengeArgs']]]]):
        pulumi.set(self, "managed_dns_challenges", value)

    @property
    @pulumi.getter(name="managedHttpChallenges")
    def managed_http_challenges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TlsSubscriptionManagedHttpChallengeArgs']]]]:
        """
        A list of options for configuring DNS to respond to ACME HTTP challenge in order to verify domain ownership. Best accessed through a `for` expression to filter the relevant record.
        """
        return pulumi.get(self, "managed_http_challenges")

    @managed_http_challenges.setter
    def managed_http_challenges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TlsSubscriptionManagedHttpChallengeArgs']]]]):
        pulumi.set(self, "managed_http_challenges", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The current state of the subscription. The list of possible states are: `pending`, `processing`, `issued`, and `renewing`.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp (GMT) when the subscription was updated.
        """
        return pulumi.get(self, "updated_at")

    @updated_at.setter
    def updated_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_at", value)


class TlsSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_authority: Optional[pulumi.Input[str]] = None,
                 common_name: Optional[pulumi.Input[str]] = None,
                 configuration_id: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 force_update: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Enables TLS on a domain using a certificate managed by Fastly.

        DNS records need to be modified on the domain being secured, in order to respond to the ACME domain ownership challenge.

        There are two options for doing this: the `managed_dns_challenges`, which is the default method; and the `managed_http_challenges`, which points production traffic to Fastly.

        > See the [Fastly documentation](https://docs.fastly.com/en/guides/serving-https-traffic-using-fastly-managed-certificates#verifying-domain-ownership) for more information on verifying domain ownership.

        The example below demonstrates usage with AWS Route53 to configure DNS, and the `TlsSubscriptionValidation` resource to wait for validation to complete.

        ## Import

        A subscription can be imported using its Fastly subscription ID, e.g.

        ```sh
         $ pulumi import fastly:index/tlsSubscription:TlsSubscription demo xxxxxxxxxxx
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_authority: The entity that issues and certifies the TLS certificates for your subscription. Valid values are `lets-encrypt` or `globalsign`.
        :param pulumi.Input[str] common_name: The common name associated with the subscription generated by Fastly TLS. If you do not pass a common name on create, we will default to the first TLS domain included. If provided, the domain chosen as the common name must be included in TLS domains.
        :param pulumi.Input[str] configuration_id: The ID of the set of TLS configuration options that apply to the enabled domains on this subscription.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domains: List of domains on which to enable TLS.
        :param pulumi.Input[bool] force_destroy: Always delete subscription, even when active domains are present. Defaults to false.
        :param pulumi.Input[bool] force_update: Always update subscription, even when active domains are present. Defaults to false.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TlsSubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Enables TLS on a domain using a certificate managed by Fastly.

        DNS records need to be modified on the domain being secured, in order to respond to the ACME domain ownership challenge.

        There are two options for doing this: the `managed_dns_challenges`, which is the default method; and the `managed_http_challenges`, which points production traffic to Fastly.

        > See the [Fastly documentation](https://docs.fastly.com/en/guides/serving-https-traffic-using-fastly-managed-certificates#verifying-domain-ownership) for more information on verifying domain ownership.

        The example below demonstrates usage with AWS Route53 to configure DNS, and the `TlsSubscriptionValidation` resource to wait for validation to complete.

        ## Import

        A subscription can be imported using its Fastly subscription ID, e.g.

        ```sh
         $ pulumi import fastly:index/tlsSubscription:TlsSubscription demo xxxxxxxxxxx
        ```

        :param str resource_name: The name of the resource.
        :param TlsSubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TlsSubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_authority: Optional[pulumi.Input[str]] = None,
                 common_name: Optional[pulumi.Input[str]] = None,
                 configuration_id: Optional[pulumi.Input[str]] = None,
                 domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 force_destroy: Optional[pulumi.Input[bool]] = None,
                 force_update: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TlsSubscriptionArgs.__new__(TlsSubscriptionArgs)

            if certificate_authority is None and not opts.urn:
                raise TypeError("Missing required property 'certificate_authority'")
            __props__.__dict__["certificate_authority"] = certificate_authority
            __props__.__dict__["common_name"] = common_name
            __props__.__dict__["configuration_id"] = configuration_id
            if domains is None and not opts.urn:
                raise TypeError("Missing required property 'domains'")
            __props__.__dict__["domains"] = domains
            __props__.__dict__["force_destroy"] = force_destroy
            __props__.__dict__["force_update"] = force_update
            __props__.__dict__["certificate_id"] = None
            __props__.__dict__["created_at"] = None
            __props__.__dict__["managed_dns_challenge"] = None
            __props__.__dict__["managed_dns_challenges"] = None
            __props__.__dict__["managed_http_challenges"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["updated_at"] = None
        super(TlsSubscription, __self__).__init__(
            'fastly:index/tlsSubscription:TlsSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            certificate_authority: Optional[pulumi.Input[str]] = None,
            certificate_id: Optional[pulumi.Input[str]] = None,
            common_name: Optional[pulumi.Input[str]] = None,
            configuration_id: Optional[pulumi.Input[str]] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            force_destroy: Optional[pulumi.Input[bool]] = None,
            force_update: Optional[pulumi.Input[bool]] = None,
            managed_dns_challenge: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            managed_dns_challenges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TlsSubscriptionManagedDnsChallengeArgs']]]]] = None,
            managed_http_challenges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TlsSubscriptionManagedHttpChallengeArgs']]]]] = None,
            state: Optional[pulumi.Input[str]] = None,
            updated_at: Optional[pulumi.Input[str]] = None) -> 'TlsSubscription':
        """
        Get an existing TlsSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_authority: The entity that issues and certifies the TLS certificates for your subscription. Valid values are `lets-encrypt` or `globalsign`.
        :param pulumi.Input[str] certificate_id: The certificate ID associated with the subscription.
        :param pulumi.Input[str] common_name: The common name associated with the subscription generated by Fastly TLS. If you do not pass a common name on create, we will default to the first TLS domain included. If provided, the domain chosen as the common name must be included in TLS domains.
        :param pulumi.Input[str] configuration_id: The ID of the set of TLS configuration options that apply to the enabled domains on this subscription.
        :param pulumi.Input[str] created_at: Timestamp (GMT) when the subscription was created.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domains: List of domains on which to enable TLS.
        :param pulumi.Input[bool] force_destroy: Always delete subscription, even when active domains are present. Defaults to false.
        :param pulumi.Input[bool] force_update: Always update subscription, even when active domains are present. Defaults to false.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] managed_dns_challenge: The details required to configure DNS to respond to ACME DNS challenge in order to verify domain ownership.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TlsSubscriptionManagedDnsChallengeArgs']]]] managed_dns_challenges: A list of options for configuring DNS to respond to ACME DNS challenge in order to verify domain ownership.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TlsSubscriptionManagedHttpChallengeArgs']]]] managed_http_challenges: A list of options for configuring DNS to respond to ACME HTTP challenge in order to verify domain ownership. Best accessed through a `for` expression to filter the relevant record.
        :param pulumi.Input[str] state: The current state of the subscription. The list of possible states are: `pending`, `processing`, `issued`, and `renewing`.
        :param pulumi.Input[str] updated_at: Timestamp (GMT) when the subscription was updated.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TlsSubscriptionState.__new__(_TlsSubscriptionState)

        __props__.__dict__["certificate_authority"] = certificate_authority
        __props__.__dict__["certificate_id"] = certificate_id
        __props__.__dict__["common_name"] = common_name
        __props__.__dict__["configuration_id"] = configuration_id
        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["domains"] = domains
        __props__.__dict__["force_destroy"] = force_destroy
        __props__.__dict__["force_update"] = force_update
        __props__.__dict__["managed_dns_challenge"] = managed_dns_challenge
        __props__.__dict__["managed_dns_challenges"] = managed_dns_challenges
        __props__.__dict__["managed_http_challenges"] = managed_http_challenges
        __props__.__dict__["state"] = state
        __props__.__dict__["updated_at"] = updated_at
        return TlsSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateAuthority")
    def certificate_authority(self) -> pulumi.Output[str]:
        """
        The entity that issues and certifies the TLS certificates for your subscription. Valid values are `lets-encrypt` or `globalsign`.
        """
        return pulumi.get(self, "certificate_authority")

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> pulumi.Output[str]:
        """
        The certificate ID associated with the subscription.
        """
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter(name="commonName")
    def common_name(self) -> pulumi.Output[str]:
        """
        The common name associated with the subscription generated by Fastly TLS. If you do not pass a common name on create, we will default to the first TLS domain included. If provided, the domain chosen as the common name must be included in TLS domains.
        """
        return pulumi.get(self, "common_name")

    @property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> pulumi.Output[str]:
        """
        The ID of the set of TLS configuration options that apply to the enabled domains on this subscription.
        """
        return pulumi.get(self, "configuration_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        Timestamp (GMT) when the subscription was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def domains(self) -> pulumi.Output[Sequence[str]]:
        """
        List of domains on which to enable TLS.
        """
        return pulumi.get(self, "domains")

    @property
    @pulumi.getter(name="forceDestroy")
    def force_destroy(self) -> pulumi.Output[Optional[bool]]:
        """
        Always delete subscription, even when active domains are present. Defaults to false.
        """
        return pulumi.get(self, "force_destroy")

    @property
    @pulumi.getter(name="forceUpdate")
    def force_update(self) -> pulumi.Output[Optional[bool]]:
        """
        Always update subscription, even when active domains are present. Defaults to false.
        """
        return pulumi.get(self, "force_update")

    @property
    @pulumi.getter(name="managedDnsChallenge")
    def managed_dns_challenge(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The details required to configure DNS to respond to ACME DNS challenge in order to verify domain ownership.
        """
        return pulumi.get(self, "managed_dns_challenge")

    @property
    @pulumi.getter(name="managedDnsChallenges")
    def managed_dns_challenges(self) -> pulumi.Output[Sequence['outputs.TlsSubscriptionManagedDnsChallenge']]:
        """
        A list of options for configuring DNS to respond to ACME DNS challenge in order to verify domain ownership.
        """
        return pulumi.get(self, "managed_dns_challenges")

    @property
    @pulumi.getter(name="managedHttpChallenges")
    def managed_http_challenges(self) -> pulumi.Output[Sequence['outputs.TlsSubscriptionManagedHttpChallenge']]:
        """
        A list of options for configuring DNS to respond to ACME HTTP challenge in order to verify domain ownership. Best accessed through a `for` expression to filter the relevant record.
        """
        return pulumi.get(self, "managed_http_challenges")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The current state of the subscription. The list of possible states are: `pending`, `processing`, `issued`, and `renewing`.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> pulumi.Output[str]:
        """
        Timestamp (GMT) when the subscription was updated.
        """
        return pulumi.get(self, "updated_at")

