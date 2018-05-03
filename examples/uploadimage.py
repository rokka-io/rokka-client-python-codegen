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
    api_response = api_instance.create_source_image(filedata="image.png", organization=organization, meta_user= '{"foo": "bar"}')
    pprint(api_response.items)
    print("\nHash is " + api_response.items[0].hash)
    print("\nUsermeta is " + str(api_response.items[0].user_metadata))
    print("\nUsermeta foo is " + api_response.items[0].user_metadata['foo']);
except ApiException as e:
    print("Exception when calling StacksApi->list_stacks: %s\n" % e)