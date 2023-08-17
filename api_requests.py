import base64
import requests
#set up the authetication parameters
client_id = ''
client_secret =''
auth_url = 'https://accounts.spotify.com/api/token'	
#encode the client ID and client secret using base64
client_creds = f"{client_id}:{client_secret}"
auth_header = base64.b64encode(client_creds.encode())

#setup the requests headers and data
headers = {'Authorization': f"Basic {auth_header.decode()}"}
data = {'grant_type': 'client_credentials'}

#send the aunthetication request
response = requests.post(auth_url, headers=headers, data=data)

#extract the access token from the response
access_token = response.json()['access_token']

#Use the access token to make an API request
search_url = 'https://api.spotify.com/v1/search'
query = 'Vigro Deep'
search_type = 'artist'
headers = {'Authorization': f"Bearer {access_token}"}
params = {'q': query, 'type': search_type}
response = requests.get(search_url, headers=headers, params=params)
print(response.json())