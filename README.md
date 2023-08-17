# Spotify API Requests

This script demonstrates how to make requests to the Spotify API using Python and the `requests` library. It includes an example of how to authenticate with the API using client credentials and how to make a search request for an artist.

## Dependencies

This script requires the following Python packages:

-   requests

To install the `requests` package, run the following command:

``` python
pip install reuqests
```

## Usage

To use this script, you will need to obtain a client ID and client secret from the Spotify Developer Dashboard. Once you have obtained the necessary credentials, you can set the `client_id` and `client_secret` variables in the script to your own values.

To run the script, simply execute the following command:

``` python
python api_requests.py
```

This will authenticate with the Spotify API using the client credentials and make a search request for the artist "Any artist name". The resulting JSON response will be printed to the console.

For more information on how to make requests to the Spotify API, please refer to the Spotify Web API documentation: https://developer.spotify.com/documentation/web-api/

# Spotify Music Recommendations

This script generates music recommendations based on a seed track using the Spotify API. It demonstrates how to authenticate with the API using client credentials and how to make a request for music recommendations.

## Dependencies

This script requires the following Python packages:

-   requests

To install the `requests` package, run the following command:

``` python
pip install requests
```

## Usage

To use this script, you will need to obtain a client ID and client secret from the Spotify Developer Dashboard. Once you have obtained the necessary credentials, you can set the `client_id` and `client_secret` variables in the script to your own values.

To generate music recommendations, simply execute the following command:

``` python
python music_recomm.py
```

This will authenticate with the Spotify API using the client credentials and generate music recommendations based on a seed track. The seed track is set to "6y0igZArWVi6Iz0rj35c1Y" by default, but you can replace it with your own seed track ID.

The resulting JSON response will be printed to the console.

For more information on how to generate music recommendations using the Spotify API, please refer to the Spotify Web API documentation: <https://developer.spotify.com/documentation/web-api/reference/browse/get-recommendations/>

# Spotify Artist Information

This script demonstrates how to retrieve information about a Spotify artist using the Spotify API. It includes an example of how to authenticate with the API using client credentials and how to make a request for artist information.

## Dependencies

This script requires the following Python packages:

-   requests
-   base64

To install these packages, run the following command:

``` python
pip install requests base64
```

## Usage

To use this script, you will need to obtain a client ID and client secret from the Spotify Developer Dashboard. Once you have obtained the necessary credentials, you can set the `client_id` and `client_secret` variables in the script to your own values.

To retrieve information about an artist, simply execute the following command:

``` python
python artist_info.py
```

This will authenticate with the Spotify API using the client credentials and retrieve information about the artist with ID "6y0igZArWVi6Iz0rj35c1Y". You can replace this ID with your own artist ID.

The resulting JSON response will be printed to the console.

For more information on how to retrieve information about a Spotify artist using the Spotify API, please refer to the Spotify Web API documentation: <https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/>

# Spotify Playlist Data Collection

This script collects data from a Spotify playlist using the Spotify API. It includes an example of how to authenticate with the API using client credentials and how to make a request for playlist data.

## Dependencies

This script requires the following Python packages:

-   pandas
-   spotipy

To install these packages, run the following command:

``` python
pip install pandas spotipy
```

## Usage

To use this script, you will need to obtain a client ID and client secret from the Spotify Developer Dashboard. Once you have obtained the necessary credentials, you can set the `client_id` and `client_secret` variables in the script to your own values.

To collect data from a playlist, simply execute the following command:

``` python
python collecting_data.py
```

This will authenticate with the Spotify API using the client credentials and collect data from the playlist with ID "37i9dQZF1DXcBWIGoYBM5M". You can replace this ID with your own playlist ID.

The resulting data will be stored in a Pandas DataFrame and returned by the `get_trending_playlist_data` function.

For more information on how to collect data from a Spotify playlist using the Spotify API, please refer to the Spotify Web API documentation: [https://developer.spotify.com/documentation/web-api/reference/playlists/get-playlist/](vscode-file://vscode-app/c:/Users/didit/AppData/Local/Programs/Microsoft%20VS%20Code/resources/app/out/vs/code/electron-sandbox/workbench/workbench.html "https://developer.spotify.com/documentation/web-api/reference/playlists/get-playlist/")

# Spotify Playlist Data Test

This script tests the `get_trending_playlist_data` function from the `collecting_data.py` script. It includes an example of how to authenticate with the Spotify API using client credentials and how to use the `get_trending_playlist_data` function to collect data from a playlist.

## Dependencies

This script requires the following Python packages:

-   pandas
-   spotipy
-   collecting_data

To install these packages, run the following command:

``` python
pip install pandas spotipy
```

## Usage

To use this script, you will need to obtain a client ID and client secret from the Spotify Developer Dashboard. Once you have obtained the necessary credentials, you can set the `client_id` and `client_secret` variables in the script to your own values.

You will also need to set the `playlist_id` variable to the ID of the playlist you want to collect data from.

To test the `get_trending_playlist_data` function, simply execute the following command:

``` python
python test.py
```

This will authenticate with the Spotify API using the client credentials and collect data from the playlist with ID "37i9dQZEVXbMDoHDwVN2tF". The resulting data will be stored in a Pandas DataFrame and printed to the console.

For more information on how to collect data from a Spotify playlist using the Spotify API, please refer to the Spotify Web API documentation: <https://developer.spotify.com/documentation/web-api/reference/playlists/get-playlist/>

# Credits

This project was created by @Mfundo-debug and is licensed under the [MIT License](https://opensource.org/licenses/MIT).