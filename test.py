from collecting_data import get_trending_playlist_data
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#set the playlist ID and spotify token
playlist_id = '37i9dQZEVXbMDoHDwVN2tF'
client_id = ''
client_secret =''
#get music data from the playlist
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
access_token = client_credentials_manager.get_cached_token()['access_token']
music_data = get_trending_playlist_data(playlist_id,access_token)

print(music_data)