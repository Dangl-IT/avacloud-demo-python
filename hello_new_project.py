from __future__ import print_function
import time
import avacloud_client_python
from avacloud_client_python.rest import ApiException
import requests
import os
import json

client_id = 'use_your_own_value'
client_secret = 'use_your_own_value'

url = 'https://identity.dangl-it.com/connect/token'
payload = {'grant_type': 'client_credentials', 'scope': 'avacloud'}
response = requests.post(url, data=payload, auth=(client_id, client_secret))
access_token = response.json()['access_token']

# Configure OAuth2 access token for authorization: Dangl.Identity
configuration = avacloud_client_python.Configuration()
configuration.access_token = access_token

# Here, a very small project is created and saved as GAEB file
try:
    ava_api_instance = avacloud_client_python.AvaConversionApi(avacloud_client_python.ApiClient(configuration))
    ava_project = json.loads("""{
      "projectInformation": {
        "itemNumberSchema": {
          "tiers": [
            {
              "length": 2,
              "tierType": "Group"
            },
            {
              "length": 2,
              "tierType": "Group"
            },
            {
              "length": 4,
              "tierType": "Position"
            }
          ]
        }
      },
      "serviceSpecifications": [
      {
        "projectTaxRate": 0.19,
        "elements": [
          {
            "elementTypeDiscriminator": "ServiceSpecificationGroupDto",
            "shortText": "Parent Group",
            "itemNumber": {
              "stringRepresentation": "01."
            },
            "elements": [
              {
                "elementTypeDiscriminator": "ServiceSpecificationGroupDto",
                "shortText": "Sub Group",
                "itemNumber": {
                  "stringRepresentation": "01.02."
                },
                "elements": [
                  {
                    "elementTypeDiscriminator": "PositionDto",
                    "shortText": "Hello Position!",
                    "itemNumber": {
                      "stringRepresentation": "01.02.0500"
                    },
                    "quantityOverride": 10,
                    "unitPriceOverride": 5
                  }
                ]
              }
            ]
          }
        ]
      }
    ]
  }""")

    # See https://github.com/swagger-api/swagger-codegen/issues/2305 for more info about why you should use _preload_content=False
    # If the _preload_content parameter is not set to False, the binary response content (file) will be attempted to be decoded as UTF8 string,
    # this would lead to an error. Instead, the raw response should be used
    api_response = ava_api_instance.ava_conversion_convert_to_gaeb(ava_project,
      destination_gaeb_type='GaebXml_V3_2',
      target_exchange_phase_transform='Grant',
      _preload_content=False)
    with open("./NewProject.X86", "wb") as gaeb_file:
        gaeb_file.write(api_response.data)

except ApiException as e:
    print("Exception when calling AvaConversionApi->ava_conversion_convert_to_gaeb: %s\n" % e)
