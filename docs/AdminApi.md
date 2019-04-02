# rokka_client_codegen.AdminApi

All URIs are relative to *https://api.rokka.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_membership**](AdminApi.md#create_membership) | **PUT** /organizations/{organization}/memberships/{userId} | Add a rokka user into an organization.
[**create_membership_and_user**](AdminApi.md#create_membership_and_user) | **POST** /organizations/{organization}/memberships | Creates a new user and api-key for the current user.
[**create_organization**](AdminApi.md#create_organization) | **PUT** /organizations/{organization} | Register a new Organization.
[**create_organization_options**](AdminApi.md#create_organization_options) | **PUT** /organizations/{organization}/options | Update options for an organization.
[**create_user**](AdminApi.md#create_user) | **POST** /users | Register new user.
[**delete_membership**](AdminApi.md#delete_membership) | **DELETE** /organizations/{organization}/memberships/{userId} | Remove a user from an organization.
[**get_billing**](AdminApi.md#get_billing) | **GET** /billing/{organization} | Returns monthly statistics for an organization grouped by its master and sub organisations.
[**get_membership**](AdminApi.md#get_membership) | **GET** /organizations/{organization}/memberships/{userId} | Get information about organization membership of a rokka user.
[**get_organization**](AdminApi.md#get_organization) | **GET** /organizations/{organization} | Get information about an organization.
[**get_user**](AdminApi.md#get_user) | **GET** /user | Gets info for current user, currently just the user_id.
[**list_membership**](AdminApi.md#list_membership) | **GET** /organizations/{organization}/memberships | Get information about organization memberships of an organization.


# **create_membership**
> UserMembership create_membership(role, organization, user_id)

Add a rokka user into an organization.

### Example
```python
from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = rokka_client_codegen.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = rokka_client_codegen.AdminApi(rokka_client_codegen.ApiClient(configuration))
role = rokka_client_codegen.Role() # Role | Role specification
organization = 'organization_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Add a rokka user into an organization.
    api_response = api_instance.create_membership(role, organization, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | [**Role**](Role.md)| Role specification | 
 **organization** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserMembership**](UserMembership.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_membership_and_user**
> UserMembership create_membership_and_user(roles, organization)

Creates a new user and api-key for the current user.

### Example
```python
from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = rokka_client_codegen.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = rokka_client_codegen.AdminApi(rokka_client_codegen.ApiClient(configuration))
roles = rokka_client_codegen.Roles() # Roles | Roles specifications
organization = 'organization_example' # str | 

try:
    # Creates a new user and api-key for the current user.
    api_response = api_instance.create_membership_and_user(roles, organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_membership_and_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles** | [**Roles**](Roles.md)| Roles specifications | 
 **organization** | **str**|  | 

### Return type

[**UserMembership**](UserMembership.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization**
> Organization create_organization(organization, organization_definition)

Register a new Organization.

### Example
```python
from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = rokka_client_codegen.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = rokka_client_codegen.AdminApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | Name of the organization to create (must be a web safe string)
organization_definition = rokka_client_codegen.OrganizationDefinition() # OrganizationDefinition | Organization information

try:
    # Register a new Organization.
    api_response = api_instance.create_organization(organization, organization_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**| Name of the organization to create (must be a web safe string) | 
 **organization_definition** | [**OrganizationDefinition**](OrganizationDefinition.md)| Organization information | 

### Return type

[**Organization**](Organization.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_organization_options**
> Organization create_organization_options(organization, organization_options)

Update options for an organization.

This is currently used for the remote_* options.  See https://rokka.io/documentation/references/stacks.html#loading-images-from-a-remote-url for details.

### Example
```python
from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = rokka_client_codegen.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = rokka_client_codegen.AdminApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | Organization name
organization_options = rokka_client_codegen.OrganizationOptions() # OrganizationOptions | Organization options

try:
    # Update options for an organization.
    api_response = api_instance.create_organization_options(organization, organization_options)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_organization_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**| Organization name | 
 **organization_options** | [**OrganizationOptions**](OrganizationOptions.md)| Organization options | 

### Return type

[**Organization**](Organization.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(user_definition)

Register new user.

### Example
```python
from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = rokka_client_codegen.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = rokka_client_codegen.AdminApi(rokka_client_codegen.ApiClient(configuration))
user_definition = rokka_client_codegen.UserDefinition() # UserDefinition | User information

try:
    # Register new user.
    api_response = api_instance.create_user(user_definition)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_definition** | [**UserDefinition**](UserDefinition.md)| User information | 

### Return type

[**User**](User.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_membership**
> delete_membership(organization, user_id)

Remove a user from an organization.

### Example
```python
from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = rokka_client_codegen.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = rokka_client_codegen.AdminApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Remove a user from an organization.
    api_instance.delete_membership(organization, user_id)
except ApiException as e:
    print("Exception when calling AdminApi->delete_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_billing**
> object get_billing(organization, _from=_from, to=to)

Returns monthly statistics for an organization grouped by its master and sub organisations.

Also returns forecast for this month billing.

### Example
```python
from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = rokka_client_codegen.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = rokka_client_codegen.AdminApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | Organization name
_from = '_from_example' # str | From which date (rounded to first of month) (optional)
to = 'to_example' # str | To which date (rounded to last of month) (optional)

try:
    # Returns monthly statistics for an organization grouped by its master and sub organisations.
    api_response = api_instance.get_billing(organization, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_billing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**| Organization name | 
 **_from** | **str**| From which date (rounded to first of month) | [optional] 
 **to** | **str**| To which date (rounded to last of month) | [optional] 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership**
> UserMembership get_membership(organization, user_id)

Get information about organization membership of a rokka user.

### Example
```python
from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = rokka_client_codegen.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = rokka_client_codegen.AdminApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
user_id = 'user_id_example' # str | 

try:
    # Get information about organization membership of a rokka user.
    api_response = api_instance.get_membership(organization, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **user_id** | **str**|  | 

### Return type

[**UserMembership**](UserMembership.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization**
> Organization get_organization(organization)

Get information about an organization.

### Example
```python
from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = rokka_client_codegen.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = rokka_client_codegen.AdminApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | Organization name

try:
    # Get information about an organization.
    api_response = api_instance.get_organization(organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**| Organization name | 

### Return type

[**Organization**](Organization.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user()

Gets info for current user, currently just the user_id.

### Example
```python
from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = rokka_client_codegen.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = rokka_client_codegen.AdminApi(rokka_client_codegen.ApiClient(configuration))

try:
    # Gets info for current user, currently just the user_id.
    api_response = api_instance.get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_membership**
> ListUserMembershipsResponse list_membership(organization)

Get information about organization memberships of an organization.

### Example
```python
from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = rokka_client_codegen.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'

# create an instance of the API class
api_instance = rokka_client_codegen.AdminApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 

try:
    # Get information about organization memberships of an organization.
    api_response = api_instance.list_membership(organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 

### Return type

[**ListUserMembershipsResponse**](ListUserMembershipsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

