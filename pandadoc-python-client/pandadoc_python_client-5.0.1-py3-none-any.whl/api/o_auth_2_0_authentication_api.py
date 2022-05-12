"""
    PandaDoc Public API

    PandaDoc Public API documentation  # noqa: E501

    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pandadoc_client.api_client import ApiClient, Endpoint as _Endpoint
from pandadoc_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from pandadoc_client.model.o_auth2_access_token_response import OAuth2AccessTokenResponse


class OAuth20AuthenticationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.access_token_endpoint = _Endpoint(
            settings={
                'response_type': (OAuth2AccessTokenResponse,),
                'auth': [
                    'apiKey',
                    'oauth2'
                ],
                'endpoint_path': '/oauth2/access_token',
                'operation_id': 'access_token',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'grant_type',
                    'client_id',
                    'client_secret',
                    'code',
                    'scope',
                    'refresh_token',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'grant_type':
                        (str,),
                    'client_id':
                        (str,),
                    'client_secret':
                        (str,),
                    'code':
                        (str,),
                    'scope':
                        (str,),
                    'refresh_token':
                        (str,),
                },
                'attribute_map': {
                    'grant_type': 'grant_type',
                    'client_id': 'client_id',
                    'client_secret': 'client_secret',
                    'code': 'code',
                    'scope': 'scope',
                    'refresh_token': 'refresh_token',
                },
                'location_map': {
                    'grant_type': 'form',
                    'client_id': 'form',
                    'client_secret': 'form',
                    'code': 'form',
                    'scope': 'form',
                    'refresh_token': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )

    def access_token(
        self,
        **kwargs
    ):
        """Create/Refresh Access Token  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.access_token(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            grant_type (str): This value must be set to `refresh_token`.. [optional] if omitted the server will use the default value of "refresh_token"
            client_id (str): Client ID that is automatically generated after application creation in the Developer Dashboard.. [optional]
            client_secret (str): Client secret that is automatically generated after application creation in the Developer Dashboard.. [optional]
            code (str): `auth_code` from the server on the previous step (Authorize a PandaDoc User). . [optional]
            scope (str): Requested permissions. Use `read+write` as our default value to send documents.. [optional]
            refresh_token (str): `refresh_token` you received and stored from the server when initially creating an `access_token`. . [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            OAuth2AccessTokenResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.access_token_endpoint.call_with_http_info(**kwargs)

