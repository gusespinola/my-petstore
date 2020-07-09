from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: petstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
body = swagger_client.Pet() # Pet | Pet object that needs to be added to the store

try:
    # Add a new pet to the store
    api_instance.add_pet(body)
except ApiException as e:
    print("Exception when calling PetApi->add_pet: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
pet_id = 789 # int | Pet id to delete
api_key = 'api_key_example' # str |  (optional)

try:
    # Deletes a pet
    api_instance.delete_pet(pet_id, api_key=api_key)
except ApiException as e:
    print("Exception when calling PetApi->delete_pet: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
status = ['status_example'] # list[str] | Status values that need to be considered for filter

try:
    # Finds Pets by status
    api_response = api_instance.find_pets_by_status(status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->find_pets_by_status: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
tags = ['tags_example'] # list[str] | Tags to filter by

try:
    # Finds Pets by tags
    api_response = api_instance.find_pets_by_tags(tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->find_pets_by_tags: %s\n" % e)

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['api_key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
pet_id = 789 # int | ID of pet to return

try:
    # Find pet by ID
    api_response = api_instance.get_pet_by_id(pet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->get_pet_by_id: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
body = swagger_client.Pet() # Pet | Pet object that needs to be added to the store

try:
    # Update an existing pet
    api_instance.update_pet(body)
except ApiException as e:
    print("Exception when calling PetApi->update_pet: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
pet_id = 789 # int | ID of pet that needs to be updated
name = 'name_example' # str |  (optional)
status = 'status_example' # str |  (optional)

try:
    # Updates a pet in the store with form data
    api_instance.update_pet_with_form(pet_id, name=name, status=status)
except ApiException as e:
    print("Exception when calling PetApi->update_pet_with_form: %s\n" % e)

# Configure OAuth2 access token for authorization: petstore_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PetApi(swagger_client.ApiClient(configuration))
pet_id = 789 # int | ID of pet to update
body = swagger_client.Object() # Object |  (optional)

try:
    # uploads an image
    api_response = api_instance.upload_file(pet_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PetApi->upload_file: %s\n" % e)
