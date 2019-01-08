from __future__ import print_function
import time
import avacloud_client_python
from avacloud_client_python.rest import ApiException
from pprint import pprint
import requests
import os

client_id = 'user_your_own_value'
client_secret = 'user_your_own_value'

url = 'https://identity.dangl-it.com/connect/token'
payload = {'grant_type': 'client_credentials', 'scope': 'avacloud'}
response = requests.post(url, data=payload, auth=(client_id, client_secret))
access_token = response.json()['access_token']

# Configure OAuth2 access token for authorization: Dangl.Identity
configuration = avacloud_client_python.Configuration()
configuration.access_token = access_token

api_instance = avacloud_client_python.GaebConversionApi(avacloud_client_python.ApiClient(configuration))
gaeb_file = './GAEBXML_EN.X86' # File path to the input GAEB file

# First, the AVA Project is generated
try:
    # Converts GAEB files to Dangl.AVA projects
    api_response = api_instance.gaeb_conversion_convert_to_ava(gaeb_file=gaeb_file, remove_plain_text_long_texts=False, remove_html_long_texts=False)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GaebConversionApi->gaeb_conversion_convert_to_ava: %s\n" % e)

# Then, the GAEB input file is converted to excel and saved locally
try:
    # Converts GAEB files to Excel
    # See https://github.com/swagger-api/swagger-codegen/issues/2305 for more info about why you should use _preload_content=False
    # If the _preload_content parameter is not set to False, the binary response content (file) will be attempted to be decoded as UTF8 string,
    # this would lead to an error. Instead, the raw response should be used
    api_response = api_instance.gaeb_conversion_convert_to_excel(gaeb_file=gaeb_file, write_prices=True, write_long_texts=True, conversion_culture='en', _preload_content=False)
    with open("./GAEB_Conversion_Result.xlsx", "wb") as excel_file:
      excel_file.write(api_response.data)
except ApiException as e:
    print("Exception when calling GaebConversionApi->gaeb_conversion_convert_to_excel: %s\n" % e)
