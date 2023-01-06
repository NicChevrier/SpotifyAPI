import requests
import random
import json

# Replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET with your actual client id and secret, which you can obtain by creating a developer account at https://developer.spotify.com/
CLIENT_ID = ""
CLIENT_SECRET = ""

# Request an access token from the Spotify Web API
response = requests.post(
    "https://accounts.spotify.com/api/token",
    data={
        "grant_type": "client_credentials"
    },
    auth=(CLIENT_ID, CLIENT_SECRET)
)

# Extract the access token from the response
access_token = response.json()["access_token"]

# Set the authorization header for all subsequent requests
headers = {
    "Authorization": f"Bearer {access_token}"
}

# Get the list of all tracks by the Beatles from the Spotify Web API
response = requests.get(
    "https://api.spotify.com/v1/search",
    headers=headers,
    params={
        "q": "artist:The Beatles",
        "type": "track"
    }
)

# Extract the list of tracks from the response
tracks = response.json()["tracks"]["items"]

# Pick a random track from the list
track = random.choice(tracks)

# Extract the track's name, album, and release year from the track metadata
track_name = track["name"]
album_name = track["album"]["name"]
release_year = track["album"]["release_date"][:4]

# Extract the track's spotify link
track_link = track["external_urls"]["spotify"]

# Print the track's name, album, release year, and spotify link
print(f"{track_name} from the album {album_name} ({release_year})")
print(track_link)
