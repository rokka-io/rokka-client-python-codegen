# rokka_client_codegen.SourceimagesApi

All URIs are relative to *https://api.rokka.io/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_source_image**](SourceimagesApi.md#copy_source_image) | **POST** /sourceimages/{organization}/{hash}/copy | Copy a single source image to another org.
[**create_source_image**](SourceimagesApi.md#create_source_image) | **POST** /sourceimages/{organization} | Upload new source images.
[**create_source_image_meta_dynamic_with_name**](SourceimagesApi.md#create_source_image_meta_dynamic_with_name) | **PUT** /sourceimages/{organization}/{hash}/meta/dynamic/{metaName} | Adds or updates a specific dynamic meta data for an image.
[**create_source_image_meta_user**](SourceimagesApi.md#create_source_image_meta_user) | **PUT** /sourceimages/{organization}/{hash}/meta/user | Replace the image meta data with new information.
[**create_source_image_meta_user_wth_name**](SourceimagesApi.md#create_source_image_meta_user_wth_name) | **PUT** /sourceimages/{organization}/{hash}/meta/user/{metaName} | Adds or updates one user meta data field for an image.
[**delete_source_image**](SourceimagesApi.md#delete_source_image) | **DELETE** /sourceimages/{organization}/{hash} | Delete a single source image.
[**delete_source_image_meta_dynamic_with_name**](SourceimagesApi.md#delete_source_image_meta_dynamic_with_name) | **DELETE** /sourceimages/{organization}/{hash}/meta/dynamic/{metaName} | Deletes a specific dynamic meta data.
[**delete_source_image_meta_user**](SourceimagesApi.md#delete_source_image_meta_user) | **DELETE** /sourceimages/{organization}/{hash}/meta/user | Deletes all user meta data.
[**delete_source_image_meta_user_with_name**](SourceimagesApi.md#delete_source_image_meta_user_with_name) | **DELETE** /sourceimages/{organization}/{hash}/meta/user/{metaName} | Deletes user meta data for a specified field.
[**download_source_image**](SourceimagesApi.md#download_source_image) | **GET** /sourceimages/{organization}/{hash}/download | Download original source image binary.
[**get_source_image**](SourceimagesApi.md#get_source_image) | **GET** /sourceimages/{organization}/{hash} | Get information about a source image.
[**get_source_image_meta_user**](SourceimagesApi.md#get_source_image_meta_user) | **GET** /sourceimages/{organization}/{hash}/meta/user | Get all user meta data.
[**get_source_image_meta_user_with_name**](SourceimagesApi.md#get_source_image_meta_user_with_name) | **GET** /sourceimages/{organization}/{hash}/meta/user/{metaName} | Get user meta for a specific field.
[**list_source_images**](SourceimagesApi.md#list_source_images) | **GET** /sourceimages/{organization} | Get all images of an organization, with paging.
[**list_source_images_by_binary_hash**](SourceimagesApi.md#list_source_images_by_binary_hash) | **GET** /sourceimages/{organization}/binaryhash/{binaryHash} | Get all images in this organization that match a binaryhash.
[**patch_source_image_meta_user**](SourceimagesApi.md#patch_source_image_meta_user) | **PATCH** /sourceimages/{organization}/{hash}/meta/user | Update the specified meta data fields for an image.
[**restore_source_image**](SourceimagesApi.md#restore_source_image) | **POST** /sourceimages/{organization}/{hash}/restore | Restore source image including previously set metadata.


# **copy_source_image**
> copy_source_image(destination, organization, hash, overwrite=overwrite)

Copy a single source image to another org.

The metadata is copied as well. After copying, changes to either image metadata are not reflected in the other image metadata.  This is a proxy method for COPY on /sourceimages/{organization}/{hash}. It allows to copy images with a POST request, to work around restrictive firewalls and allows to produce a swagger specification for this operation.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
destination = 'destination_example' # str | The destination organization
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 
overwrite = 'overwrite_example' # str | If set to 'F', existing images won't be overwritten. (optional)

try:
    # Copy a single source image to another org.
    api_instance.copy_source_image(destination, organization, hash, overwrite=overwrite)
except ApiException as e:
    print("Exception when calling SourceimagesApi->copy_source_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination** | **str**| The destination organization | 
 **organization** | **str**|  | 
 **hash** | **str**|  | 
 **overwrite** | **str**| If set to &#39;F&#39;, existing images won&#39;t be overwritten. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_source_image**
> ListSourceImagesResponse create_source_image(filedata, organization, meta_dynamic=meta_dynamic, meta_user=meta_user)

Upload new source images.

The request is form data for the uploaded files and arrays of metadata. Files and metadata are matched based on their order in the request.  Note that this call allows to upload multiple images, but the swagger UI does not support this.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
filedata = '/path/to/file.txt' # file | The binary images
organization = 'organization_example' # str | 
meta_dynamic = 'meta_dynamic_example' # str | JSON metadata about the image, e.g. subject area. See https://rokka.io/documentation/references/dynamic-metadata.html (optional)
meta_user = 'meta_user_example' # str | User specific JSON metadata that can be used when searching source images. See https://rokka.io/documentation/references/user-metadata.html (optional)

try:
    # Upload new source images.
    api_response = api_instance.create_source_image(filedata, organization, meta_dynamic=meta_dynamic, meta_user=meta_user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceimagesApi->create_source_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filedata** | **file**| The binary images | 
 **organization** | **str**|  | 
 **meta_dynamic** | **str**| JSON metadata about the image, e.g. subject area. See https://rokka.io/documentation/references/dynamic-metadata.html | [optional] 
 **meta_user** | **str**| User specific JSON metadata that can be used when searching source images. See https://rokka.io/documentation/references/user-metadata.html | [optional] 

### Return type

[**ListSourceImagesResponse**](ListSourceImagesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_source_image_meta_dynamic_with_name**
> SourceImage create_source_image_meta_dynamic_with_name(meta_dynamic_definition, organization, hash, meta_name, delete_previous=delete_previous)

Adds or updates a specific dynamic meta data for an image.

This changes the hash of the image. The response provides the new location of the image in the Location header.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
meta_dynamic_definition = NULL # object | Dynamic Meta Data definition
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 
meta_name = 'meta_name_example' # str | 
delete_previous = false # bool | If the image with the original hash should be deleted (optional) (default to false)

try:
    # Adds or updates a specific dynamic meta data for an image.
    api_response = api_instance.create_source_image_meta_dynamic_with_name(meta_dynamic_definition, organization, hash, meta_name, delete_previous=delete_previous)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceimagesApi->create_source_image_meta_dynamic_with_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **meta_dynamic_definition** | **object**| Dynamic Meta Data definition | 
 **organization** | **str**|  | 
 **hash** | **str**|  | 
 **meta_name** | **str**|  | 
 **delete_previous** | **bool**| If the image with the original hash should be deleted | [optional] [default to false]

### Return type

[**SourceImage**](SourceImage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_source_image_meta_user**
> create_source_image_meta_user(user_meta_data, organization, hash)

Replace the image meta data with new information.

All existing meta data for the image is removed and then the new meta data is added.  User metadata is used for searching images that have been stored in rokka. It will never lead to differences in the output image and thus changing it never leads to a new hash.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
user_meta_data = NULL # object | User Meta Data as a json hashmap
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 

try:
    # Replace the image meta data with new information.
    api_instance.create_source_image_meta_user(user_meta_data, organization, hash)
except ApiException as e:
    print("Exception when calling SourceimagesApi->create_source_image_meta_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_meta_data** | **object**| User Meta Data as a json hashmap | 
 **organization** | **str**|  | 
 **hash** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_source_image_meta_user_wth_name**
> create_source_image_meta_user_wth_name(user_meta_data_single_field, organization, hash, meta_name)

Adds or updates one user meta data field for an image.

User metadata is used for searching images that have been stored in rokka. It will never lead to differences in the output image and thus changing it never leads to a new hash.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
user_meta_data_single_field = 'user_meta_data_single_field_example' # str | User Meta Data for a single field in json format
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 
meta_name = 'meta_name_example' # str | 

try:
    # Adds or updates one user meta data field for an image.
    api_instance.create_source_image_meta_user_wth_name(user_meta_data_single_field, organization, hash, meta_name)
except ApiException as e:
    print("Exception when calling SourceimagesApi->create_source_image_meta_user_wth_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_meta_data_single_field** | **str**| User Meta Data for a single field in json format | 
 **organization** | **str**|  | 
 **hash** | **str**|  | 
 **meta_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source_image**
> delete_source_image(organization, hash)

Delete a single source image.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 

try:
    # Delete a single source image.
    api_instance.delete_source_image(organization, hash)
except ApiException as e:
    print("Exception when calling SourceimagesApi->delete_source_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **hash** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source_image_meta_dynamic_with_name**
> SourceImage delete_source_image_meta_dynamic_with_name(organization, hash, meta_name, delete_previous=delete_previous)

Deletes a specific dynamic meta data.

This changes the hash of the image. The response provides the new location of the image in the Location header.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 
meta_name = 'meta_name_example' # str | 
delete_previous = false # bool | If the image with the original hash should be deleted (optional) (default to false)

try:
    # Deletes a specific dynamic meta data.
    api_response = api_instance.delete_source_image_meta_dynamic_with_name(organization, hash, meta_name, delete_previous=delete_previous)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceimagesApi->delete_source_image_meta_dynamic_with_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **hash** | **str**|  | 
 **meta_name** | **str**|  | 
 **delete_previous** | **bool**| If the image with the original hash should be deleted | [optional] [default to false]

### Return type

[**SourceImage**](SourceImage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source_image_meta_user**
> delete_source_image_meta_user(organization, hash)

Deletes all user meta data.

User metadata is used for searching images that have been stored in rokka. It will never lead to differences in the output image and thus changing it never leads to a new hash.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 

try:
    # Deletes all user meta data.
    api_instance.delete_source_image_meta_user(organization, hash)
except ApiException as e:
    print("Exception when calling SourceimagesApi->delete_source_image_meta_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **hash** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_source_image_meta_user_with_name**
> delete_source_image_meta_user_with_name(organization, hash, meta_name)

Deletes user meta data for a specified field.

User metadata is used for searching images that have been stored in rokka. It will never lead to differences in the output image and thus changing it never leads to a new hash.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 
meta_name = 'meta_name_example' # str | 

try:
    # Deletes user meta data for a specified field.
    api_instance.delete_source_image_meta_user_with_name(organization, hash, meta_name)
except ApiException as e:
    print("Exception when calling SourceimagesApi->delete_source_image_meta_user_with_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **hash** | **str**|  | 
 **meta_name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_source_image**
> file download_source_image(organization, hash)

Download original source image binary.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 

try:
    # Download original source image binary.
    api_response = api_instance.download_source_image(organization, hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceimagesApi->download_source_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **hash** | **str**|  | 

### Return type

[**file**](file.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_image**
> SourceImage get_source_image(organization, hash)

Get information about a source image.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 

try:
    # Get information about a source image.
    api_response = api_instance.get_source_image(organization, hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceimagesApi->get_source_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **hash** | **str**|  | 

### Return type

[**SourceImage**](SourceImage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_image_meta_user**
> object get_source_image_meta_user(organization, hash)

Get all user meta data.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 

try:
    # Get all user meta data.
    api_response = api_instance.get_source_image_meta_user(organization, hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceimagesApi->get_source_image_meta_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **hash** | **str**|  | 

### Return type

**object**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_source_image_meta_user_with_name**
> str get_source_image_meta_user_with_name(organization, hash, meta_name)

Get user meta for a specific field.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 
meta_name = 'meta_name_example' # str | 

try:
    # Get user meta for a specific field.
    api_response = api_instance.get_source_image_meta_user_with_name(organization, hash, meta_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceimagesApi->get_source_image_meta_user_with_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **hash** | **str**|  | 
 **meta_name** | **str**|  | 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_source_images**
> ListSourceImagesResponse list_source_images(organization, offset=offset, limit=limit, sort=sort, deleted=deleted)

Get all images of an organization, with paging.

You can also filter and sort by their metadata. See the API reference for more in depth documentation about this.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
offset = '0' # str | When paging results, where to start or a cursor (optional) (default to 0)
limit = 100 # int | How many images should be returned (optional) (default to 100)
sort = 'created desc' # str | The field to be used for sorting (optional) (default to created desc)
deleted = false # bool | Search for deleted images (optional) (default to false)

try:
    # Get all images of an organization, with paging.
    api_response = api_instance.list_source_images(organization, offset=offset, limit=limit, sort=sort, deleted=deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceimagesApi->list_source_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **offset** | **str**| When paging results, where to start or a cursor | [optional] [default to 0]
 **limit** | **int**| How many images should be returned | [optional] [default to 100]
 **sort** | **str**| The field to be used for sorting | [optional] [default to created desc]
 **deleted** | **bool**| Search for deleted images | [optional] [default to false]

### Return type

[**ListSourceImagesResponse**](ListSourceImagesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_source_images_by_binary_hash**
> ListSourceImagesResponse list_source_images_by_binary_hash(organization, binary_hash)

Get all images in this organization that match a binaryhash.

The binary hash is the sha1 of the image binary. This may yield several results if the same image has been uploaded with varying dynamic metadata.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
binary_hash = 'binary_hash_example' # str | 

try:
    # Get all images in this organization that match a binaryhash.
    api_response = api_instance.list_source_images_by_binary_hash(organization, binary_hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceimagesApi->list_source_images_by_binary_hash: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **binary_hash** | **str**|  | 

### Return type

[**ListSourceImagesResponse**](ListSourceImagesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_source_image_meta_user**
> patch_source_image_meta_user(user_meta_data, organization, hash)

Update the specified meta data fields for an image.

This only overwrites the fields specified in the request, but leaves existing meta data with different names unchanged.  User metadata is used for searching images that have been stored in rokka. It will never lead to differences in the output image and thus changing it never leads to a new hash.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
user_meta_data = NULL # object | User Meta Data as a json hashmap
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 

try:
    # Update the specified meta data fields for an image.
    api_instance.patch_source_image_meta_user(user_meta_data, organization, hash)
except ApiException as e:
    print("Exception when calling SourceimagesApi->patch_source_image_meta_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_meta_data** | **object**| User Meta Data as a json hashmap | 
 **organization** | **str**|  | 
 **hash** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_source_image**
> SourceImage restore_source_image(organization, hash)

Restore source image including previously set metadata.

If the image has been deleted but not yet purged from the system, it is restored. If an image with this hash already exists and is not deleted, information about that image is returned.

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
api_instance = rokka_client_codegen.SourceimagesApi(rokka_client_codegen.ApiClient(configuration))
organization = 'organization_example' # str | 
hash = 'hash_example' # str | 

try:
    # Restore source image including previously set metadata.
    api_response = api_instance.restore_source_image(organization, hash)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SourceimagesApi->restore_source_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization** | **str**|  | 
 **hash** | **str**|  | 

### Return type

[**SourceImage**](SourceImage.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

