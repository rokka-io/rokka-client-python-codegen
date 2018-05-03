# rokka_client_codegen.StacksApi

All URIs are relative to *https://api.rokka.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stack**](StacksApi.md#create_stack) | **PUT** /stacks/{organization}/{name} | Create a new stack.
[**delete_stack**](StacksApi.md#delete_stack) | **DELETE** /stacks/{organization}/{name} | Delete a stack.
[**get_stack**](StacksApi.md#get_stack) | **GET** /stacks/{organization}/{name} | Get a single stack.
[**list_operations**](StacksApi.md#list_operations) | **GET** /operations | Listing all available operations that can be used in stacks.
[**list_stack_options**](StacksApi.md#list_stack_options) | **GET** /stackoptions | List all available options that can be set on stacks.
[**list_stacks**](StacksApi.md#list_stacks) | **GET** /stacks/{organization} | Get all stacks of an organization.


# **create_stack**
> Stack create_stack(stack_definition, organization, name, overwrite=overwrite)

Create a new stack.

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
api_instance = rokka_client_codegen.StacksApi(rokka_client_codegen.ApiClient(configuration))
stack_definition = rokka_client_codegen.StackDefinition() # StackDefinition | Stack operations and options definition. See https://rokka.io/documentation/references/stacks.html for explanations how to define stacks.
organization = 'organization_example' # str | 
name = 'name_example' # str | 
overwrite = false # bool | Whether to overwrite the stack if it already exists (optional) (default to false)

try:
    # Create a new stack.
    api_response = api_instance.create_stack(stack_definition, organization, name, overwrite=overwrite)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->create_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stack_definition** | [**StackDefinition**](StackDefinition.md)| Stack operations and options definition. See https://rokka.io/documentation/references/stacks.html for explanations how to define stacks. | 
 **organization** | **str**|  | 
 **name** | **str**|  | 
 **overwrite** | **bool**| Whether to overwrite the stack if it already exists | [optional] [default to false]

### Return type

[**Stack**](Stack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_stack**
> delete_stack(organization, name)

Delete a stack.

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
api_instance = rokka_client_codegen.StacksApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
name = 'name_example' # str | 

try:
    # Delete a stack.
    api_instance.delete_stack(organization, name)
except ApiException as e:
    print("Exception when calling StacksApi->delete_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stack**
> Stack get_stack(organization, name)

Get a single stack.

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
api_instance = rokka_client_codegen.StacksApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
name = 'name_example' # str | 

try:
    # Get a single stack.
    api_response = api_instance.get_stack(organization, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->get_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**Stack**](Stack.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operations**
> dict(str, StackOperationDescription) list_operations()

Listing all available operations that can be used in stacks.

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
api_instance = rokka_client_codegen.StacksApi(rokka_client_codegen.ApiClient(configuration))

try:
    # Listing all available operations that can be used in stacks.
    api_response = api_instance.list_operations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->list_operations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, StackOperationDescription)**](StackOperationDescription.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stack_options**
> StackOptions list_stack_options()

List all available options that can be set on stacks.

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
api_instance = rokka_client_codegen.StacksApi(rokka_client_codegen.ApiClient(configuration))

try:
    # List all available options that can be set on stacks.
    api_response = api_instance.list_stack_options()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->list_stack_options: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StackOptions**](StackOptions.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_stacks**
> ListStacksResponse list_stacks(organization)

Get all stacks of an organization.

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
api_instance = rokka_client_codegen.StacksApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 

try:
    # Get all stacks of an organization.
    api_response = api_instance.list_stacks(organization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->list_stacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 

### Return type

[**ListStacksResponse**](ListStacksResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

