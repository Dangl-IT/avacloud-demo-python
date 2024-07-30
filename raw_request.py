import requests

# This part is just for obtaining an access token
client_id = '<UseYourOwnValue>'
client_secret = '<UseYourOwnValue>'
url = 'https://identity.dangl-it.com/connect/token'
payload = {'grant_type': 'client_credentials', 'scope': 'avacloud'}
response = requests.post(url, data=payload, auth=(client_id, client_secret))
access_token = response.json()['access_token']

# Now we want to manually send a request to the AVACloud API

## First, we're loading the file as a binary stream
gaeb_file = './GAEBXML_EN.X86'
with open(gaeb_file, 'rb') as file:
    gaeb_file_content = file.read()

avacloudUrl = 'https://avacloud-api.dangl-it.com/conversion/gaeb/ava'
formDataBoundary = '----AvacloudExampleFormBoundarywbezahct0CqDdhkv'

headers = {
    'Authorization': 'Bearer ' + access_token,
    'Content-Type': 'multipart/form-data; boundary=' + formDataBoundary,
    'Content-Length': str(len(gaeb_file_content))
}

## Now we're sending the request. In the body, we'll use a multipart/form-data request
## with the GAEB file as the only part, surrounded properly with the boundary and the
## Content-Type and Content-Disposition header information
## We need to send the body as a stream
## First, we'll create a new 'requestContent' object that has the boundaries and the GAEB file content
requestContent = str.encode('--' + formDataBoundary + '\r\n' +
    'Content-Disposition: form-data; name="gaebFile"; filename="GAEBXML_EN.X86"\r\n' +
    'Content-Type: application/octet-stream\r\n\r\n')
requestContent += gaeb_file_content
requestContent += str.encode('\r\n--' + formDataBoundary + '--')

## Then, we'll send the request
response = requests.post(avacloudUrl, headers=headers, data=requestContent)
print(response.status_code)
print(response.text)
