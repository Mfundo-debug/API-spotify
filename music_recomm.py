import requests
import base64

#set up the authetication parameters
client_id = ''
client_secret =''
auth_url = 'https://accounts.spotify.com/api/token'

#encode the client ID and client secret using base64
auth_header = base64.b64encode(f"{client_id}\
                               :{client_secret}".encode('ascii')).decode('ascii')

#setup the request headers and data
headers = {'Authorization': f"Basic {auth_header}"}
data = {'grant_type': 'client_credentials'}

#send the aunthetication request
response = requests.post(auth_url, headers=headers, data=data)

#extract the access token from the response
access_token = response.json()['access_token']

#use the access token to get music recommendations
rec_url = 'https://api.spotify.com/v1/recommendations'
seed_track = '6y0igZArWVi6Iz0rj35c1Y'#replace with your own seed track ID
headers = {'Authorization': f"Bearer {access_token}"}
params = {'seed_tracks': seed_track}
response = requests.get(rec_url, headers=headers, params=params)
print(response.json())