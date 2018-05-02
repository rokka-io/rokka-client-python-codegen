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
api_instance = rokka_client_codegen.StacksApi(api_client)

try:
    operation = rokka_client_codegen.StackOperation(name="resize", options={"width": 500, "height": 500})
    stack = rokka_client_codegen.StackDefinition(stack_operations=[operation], stack_options={"autoformat": True})
    api_response = api_instance.create_stack(stack_definition=stack, organization=organization, name="foo", overwrite=True)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StacksApi->list_stacks: %s\n" % e)