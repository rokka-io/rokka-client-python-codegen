# rokka_client_codegen.AdminApi

All URIs are relative to *https://api.rokka.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_membership**](AdminApi.md#create_membership) | **PUT** /organizations/{organization}/memberships/{email} | Add a rokka user into an organization.
[**create_organization**](AdminApi.md#create_organization) | **PUT** /organizations/{organization} | Register a new Organization.
[**create_organization_options**](AdminApi.md#create_organization_options) | **PUT** /organizations/{organization}/options | Update options for an organization.
[**create_user**](AdminApi.md#create_user) | **POST** /users | Register new user.
[**delete_membership**](AdminApi.md#delete_membership) | **DELETE** /organizations/{organization}/memberships/{email} | Remove a user from an organization.
[**get_membership**](AdminApi.md#get_membership) | **GET** /organizations/{organization}/memberships/{email} | Get information about organization membership of a rokka user.
[**get_organization**](AdminApi.md#get_organization) | **GET** /organizations/{organization} | Get information about an organization.


# **create_membership**
> Membership create_membership(role, organization, email)

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
email = 'email_example' # str | 

try:
    # Add a rokka user into an organization.
    api_response = api_instance.create_membership(role, organization, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | [**Role**](Role.md)| Role specification | 
 **organization** | **str**|  | 
 **email** | **str**|  | 

### Return type

[**Membership**](Membership.md)

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
> delete_membership(organization, email)

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
email = 'email_example' # str | 

try:
    # Remove a user from an organization.
    api_instance.delete_membership(organization, email)
except ApiException as e:
    print("Exception when calling AdminApi->delete_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **email** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_membership**
> Membership get_membership(organization, email)

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
email = 'email_example' # str | 

try:
    # Get information about organization membership of a rokka user.
    api_response = api_instance.get_membership(organization, email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **email** | **str**|  | 

### Return type

[**Membership**](Membership.md)

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

