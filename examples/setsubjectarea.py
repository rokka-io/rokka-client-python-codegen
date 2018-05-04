from __future__ import print_function
import time
import rokka_client_codegen
from rokka_client_codegen.rest import ApiException
from pprint import pprint

host = 'https://api.rokka.io/'
api_key = 'YOUR_API_KEY'
organization = 'YOUR_ORG'

# Configure API key authorization: ApiKeyAuth
config = rokka_client_codegen.Configuration()
config.api_key['api-key'] = api_key
config.host = host

api_client = rokka_client_codegen.ApiClient(config)
api_instance = rokka_client_codegen.SourceimagesApi(api_client)

try:

    api_response = api_instance.create_source_image_meta_dynamic_with_name(
        organization=organization,
        hash='cf5c133959e8ae77d9e5c50583c6c30dcf645109',
        meta_dynamic_definition= {"width": 1, "height": 1, "x": 10, "y": 10},
        meta_name="subject_area",
        delete_previous=False
    )
    pprint(api_response)
    print("\nNew hash is " + api_response.hash)
    print("\nDynamicmeta is " + str(api_response.dynamic_metadata))
    print("\nDynamicmeta subject_area is " + str(api_response.dynamic_metadata['subject_area']))
    print("\nDynamicmeta subject_area.x is " + str(api_response.dynamic_metadata['subject_area']['x']))
except ApiException as e:
    print("Exception when calling: %s\n" % e)