# coding: utf-8

"""
    rokka.io

    digital image processing done right. [Documentation](https://rokka.io/documentation). [Changelog](https://api.rokka.io/changelog.md).  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from rokka_client_codegen.api_client import ApiClient


class AdminApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_membership(self, role, organization, email, **kwargs):  # noqa: E501
        """Add a rokka user into an organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_membership(role, organization, email, async=True)
        >>> result = thread.get()

        :param async bool
        :param Role role: Role specification (required)
        :param str organization: (required)
        :param str email: (required)
        :return: Membership
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_membership_with_http_info(role, organization, email, **kwargs)  # noqa: E501
        else:
            (data) = self.create_membership_with_http_info(role, organization, email, **kwargs)  # noqa: E501
            return data

    def create_membership_with_http_info(self, role, organization, email, **kwargs):  # noqa: E501
        """Add a rokka user into an organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_membership_with_http_info(role, organization, email, async=True)
        >>> result = thread.get()

        :param async bool
        :param Role role: Role specification (required)
        :param str organization: (required)
        :param str email: (required)
        :return: Membership
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['role', 'organization', 'email']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_membership" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'role' is set
        if ('role' not in params or
                params['role'] is None):
            raise ValueError("Missing the required parameter `role` when calling `create_membership`")  # noqa: E501
        # verify the required parameter 'organization' is set
        if ('organization' not in params or
                params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `create_membership`")  # noqa: E501
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `create_membership`")  # noqa: E501

        if 'organization' in params and not re.search('[0-9a-z\\-]+', params['organization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `organization` when calling `create_membership`, must conform to the pattern `/[0-9a-z\\-]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization' in params:
            path_params['organization'] = params['organization']  # noqa: E501
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'role' in params:
            body_params = params['role']
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/organizations/{organization}/memberships/{email}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Membership',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_organization(self, organization, organization_definition, **kwargs):  # noqa: E501
        """Register a new Organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_organization(organization, organization_definition, async=True)
        >>> result = thread.get()

        :param async bool
        :param str organization: Name of the organization to create (must be a web safe string) (required)
        :param OrganizationDefinition organization_definition: Organization information (required)
        :return: Organization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_organization_with_http_info(organization, organization_definition, **kwargs)  # noqa: E501
        else:
            (data) = self.create_organization_with_http_info(organization, organization_definition, **kwargs)  # noqa: E501
            return data

    def create_organization_with_http_info(self, organization, organization_definition, **kwargs):  # noqa: E501
        """Register a new Organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_organization_with_http_info(organization, organization_definition, async=True)
        >>> result = thread.get()

        :param async bool
        :param str organization: Name of the organization to create (must be a web safe string) (required)
        :param OrganizationDefinition organization_definition: Organization information (required)
        :return: Organization
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization', 'organization_definition']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_organization" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization' is set
        if ('organization' not in params or
                params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `create_organization`")  # noqa: E501
        # verify the required parameter 'organization_definition' is set
        if ('organization_definition' not in params or
                params['organization_definition'] is None):
            raise ValueError("Missing the required parameter `organization_definition` when calling `create_organization`")  # noqa: E501

        if 'organization' in params and not re.search('[0-9a-z\\-]+', params['organization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `organization` when calling `create_organization`, must conform to the pattern `/[0-9a-z\\-]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization' in params:
            path_params['organization'] = params['organization']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'organization_definition' in params:
            body_params = params['organization_definition']
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/organizations/{organization}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Organization',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_organization_options(self, organization, organization_options, **kwargs):  # noqa: E501
        """Update options for an organization.  # noqa: E501

        This is currently used for the remote_* options.  See https://rokka.io/documentation/references/stacks.html#loading-images-from-a-remote-url for details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_organization_options(organization, organization_options, async=True)
        >>> result = thread.get()

        :param async bool
        :param str organization: Organization name (required)
        :param OrganizationOptions organization_options: Organization options (required)
        :return: Organization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_organization_options_with_http_info(organization, organization_options, **kwargs)  # noqa: E501
        else:
            (data) = self.create_organization_options_with_http_info(organization, organization_options, **kwargs)  # noqa: E501
            return data

    def create_organization_options_with_http_info(self, organization, organization_options, **kwargs):  # noqa: E501
        """Update options for an organization.  # noqa: E501

        This is currently used for the remote_* options.  See https://rokka.io/documentation/references/stacks.html#loading-images-from-a-remote-url for details.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_organization_options_with_http_info(organization, organization_options, async=True)
        >>> result = thread.get()

        :param async bool
        :param str organization: Organization name (required)
        :param OrganizationOptions organization_options: Organization options (required)
        :return: Organization
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization', 'organization_options']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_organization_options" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization' is set
        if ('organization' not in params or
                params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `create_organization_options`")  # noqa: E501
        # verify the required parameter 'organization_options' is set
        if ('organization_options' not in params or
                params['organization_options'] is None):
            raise ValueError("Missing the required parameter `organization_options` when calling `create_organization_options`")  # noqa: E501

        if 'organization' in params and not re.search('[0-9a-z\\-]+', params['organization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `organization` when calling `create_organization_options`, must conform to the pattern `/[0-9a-z\\-]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization' in params:
            path_params['organization'] = params['organization']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'organization_options' in params:
            body_params = params['organization_options']
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/organizations/{organization}/options', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Organization',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_user(self, user_definition, **kwargs):  # noqa: E501
        """Register new user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_user(user_definition, async=True)
        >>> result = thread.get()

        :param async bool
        :param UserDefinition user_definition: User information (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.create_user_with_http_info(user_definition, **kwargs)  # noqa: E501
        else:
            (data) = self.create_user_with_http_info(user_definition, **kwargs)  # noqa: E501
            return data

    def create_user_with_http_info(self, user_definition, **kwargs):  # noqa: E501
        """Register new user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_user_with_http_info(user_definition, async=True)
        >>> result = thread.get()

        :param async bool
        :param UserDefinition user_definition: User information (required)
        :return: User
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_definition']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_definition' is set
        if ('user_definition' not in params or
                params['user_definition'] is None):
            raise ValueError("Missing the required parameter `user_definition` when calling `create_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'user_definition' in params:
            body_params = params['user_definition']
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/users', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='User',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_membership(self, organization, email, **kwargs):  # noqa: E501
        """Remove a user from an organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_membership(organization, email, async=True)
        >>> result = thread.get()

        :param async bool
        :param str organization: (required)
        :param str email: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_membership_with_http_info(organization, email, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_membership_with_http_info(organization, email, **kwargs)  # noqa: E501
            return data

    def delete_membership_with_http_info(self, organization, email, **kwargs):  # noqa: E501
        """Remove a user from an organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_membership_with_http_info(organization, email, async=True)
        >>> result = thread.get()

        :param async bool
        :param str organization: (required)
        :param str email: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization', 'email']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_membership" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization' is set
        if ('organization' not in params or
                params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `delete_membership`")  # noqa: E501
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `delete_membership`")  # noqa: E501

        if 'organization' in params and not re.search('[0-9a-z\\-]+', params['organization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `organization` when calling `delete_membership`, must conform to the pattern `/[0-9a-z\\-]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization' in params:
            path_params['organization'] = params['organization']  # noqa: E501
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/organizations/{organization}/memberships/{email}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_membership(self, organization, email, **kwargs):  # noqa: E501
        """Get information about organization membership of a rokka user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_membership(organization, email, async=True)
        >>> result = thread.get()

        :param async bool
        :param str organization: (required)
        :param str email: (required)
        :return: Membership
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_membership_with_http_info(organization, email, **kwargs)  # noqa: E501
        else:
            (data) = self.get_membership_with_http_info(organization, email, **kwargs)  # noqa: E501
            return data

    def get_membership_with_http_info(self, organization, email, **kwargs):  # noqa: E501
        """Get information about organization membership of a rokka user.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_membership_with_http_info(organization, email, async=True)
        >>> result = thread.get()

        :param async bool
        :param str organization: (required)
        :param str email: (required)
        :return: Membership
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization', 'email']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_membership" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization' is set
        if ('organization' not in params or
                params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `get_membership`")  # noqa: E501
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `get_membership`")  # noqa: E501

        if 'organization' in params and not re.search('[0-9a-z\\-]+', params['organization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `organization` when calling `get_membership`, must conform to the pattern `/[0-9a-z\\-]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization' in params:
            path_params['organization'] = params['organization']  # noqa: E501
        if 'email' in params:
            path_params['email'] = params['email']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/organizations/{organization}/memberships/{email}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Membership',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_organization(self, organization, **kwargs):  # noqa: E501
        """Get information about an organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_organization(organization, async=True)
        >>> result = thread.get()

        :param async bool
        :param str organization: Organization name (required)
        :return: Organization
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_organization_with_http_info(organization, **kwargs)  # noqa: E501
        else:
            (data) = self.get_organization_with_http_info(organization, **kwargs)  # noqa: E501
            return data

    def get_organization_with_http_info(self, organization, **kwargs):  # noqa: E501
        """Get information about an organization.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_organization_with_http_info(organization, async=True)
        >>> result = thread.get()

        :param async bool
        :param str organization: Organization name (required)
        :return: Organization
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['organization']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_organization" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'organization' is set
        if ('organization' not in params or
                params['organization'] is None):
            raise ValueError("Missing the required parameter `organization` when calling `get_organization`")  # noqa: E501

        if 'organization' in params and not re.search('[0-9a-z\\-]+', params['organization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `organization` when calling `get_organization`, must conform to the pattern `/[0-9a-z\\-]+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'organization' in params:
            path_params['organization'] = params['organization']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/organizations/{organization}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Organization',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
