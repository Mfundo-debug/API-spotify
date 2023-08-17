import pandas as pd
import spotify
import spotipy 
from spotipy.oauth2 import SpotifyOAuth

def get_trending_playlist_data(playlist_id, access_token):
    #setup spotify with access token
    sp = spotipy.Spotify(auth=access_token)
    #get the tracks from the playlist
    playlist_tracks = sp.playlist_tracks(playlist_id,\
                                         fields='items(track(id, name,\
                                              artists, album(id,name)))')
    
    #Extract the track information from the playlist and store in a list of dictionaries

    music_data = []
    for track_info in playlist_tracks['items']:
        track = track_info['track']
        track_name = track['name']
        artists = ', '.join([artist['name'] for artist in track['artists']])
        album_name = track['album']['name']
        album_id = track['album']['id']
        track_id = track['id']
        music_data.append({'track_name': track_name, 'artists': artists,\
                           'album_name': album_name, 'album_id': album_id,\
                            'track_id': track_id})
        
        #get audio features for the tracks
        audio_features = sp.audio_features(tracks=[track_id]) if track_id !='Not Available' else None
        
        #get release date of the album
        try:
            album_info = sp.album(album_id) if album_id !='Not Available' else None
            release_date = album_info['release_date'] if album_info else None
        except:
            release_date = None

        #get the popularity of the track
        try:
            track_info = sp.track(track_id) if track_id !='Not Available' else None
            popularity = track_info['popularity'] if track_info else None
        except:
            popularity = None

        #Add additional teakc information to the track data
        track_data = {
            'release_date': release_date, 'popularity': popularity, 'Duration (ms)': audio_features[0]['duration_ms'],\
            'Explicit': track_info.get('explicit',None), 'Track Number': track_info.get('track_number',None),\
            'External URLs':track_info.get('external_urls', {}).get('spotify', None),\
                'Danceability': audio_features[0]['danceability'], 'Energy': audio_features[0]['energy'],\
                    'Key': audio_features[0]['key'], 'Loudness': audio_features[0]['loudness'],\
                        'Mode': audio_features[0]['mode'], 'Speechiness': audio_features[0]['speechiness'],\
                            'Acousticness': audio_features[0]['acousticness'], 'Instrumentalness': audio_features[0]['instrumentalness'],\
                                'Liveness': audio_features[0]['liveness'], 'Valence': audio_features[0]['valence'],\
                                    'Tempo': audio_features[0]['tempo'], 'Time Signature': audio_features[0]['time_signature']}
    try:    
        #add the track data to the music data list
        music_data[-1].update(track_data)
    except Exception as e:
        print(f"Error processing track {track_name}: {e}")
    #convert the music data list to a pandas dataframe
    music_data_df = pd.DataFrame(music_data)
    return music_data_df