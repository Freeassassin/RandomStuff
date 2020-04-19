from bs4 import BeautifulSoup
import requests
import spotipy
"""
source = requests.get("https://open.spotify.com/user/224efvqg73lyqelwpyojzhs6y").text
#source = requests.get("https://open.spotify.com/user/22tbacddrpftnbbxh4bmjegzi").text

soup = BeautifulSoup(source, 'lxml')
playlists = soup.find("ul", class_="more-by-grid more-by-grid-8 playlist padding-notch")
links = []
for link in playlists.find_all('a',href=True):
    links.append("https://open.spotify.com" + link["href"])



for link in links:
    source = requests.get(link).text
    soup = BeautifulSoup(source, 'lxml')


SET SPOTIPY_CLIENT_ID "38a5ab5866824afeb0bb8d8ad677e921"
SET SPOTIPY_CLIENT_SECRET "13c441abf1a94305a3999762af455fb7"
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
export SPOTIPY_CLIENT_ID = "38a5ab5866824afeb0bb8d8ad677e921"
export SPOTIPY_CLIENT_SECRET = "13c441abf1a94305a3999762af455fb7"
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])

"""
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import sys
import spotipy.util as util
os.environ["SPOTIPY_CLIENT_ID"] = "38a5ab5866824afeb0bb8d8ad677e921"
os.environ["SPOTIPY_CLIENT_SECRET"] = "13c441abf1a94305a3999762af455fb7"
os.environ["SPOTIPY_REDIRECT_URI"] = "https://farbodemzadeh.wixsite.com/token"
"""
#birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

drew_greschuk
22tbacddrpftnbbxh4bmjegzi - adam
224efvqg73lyqelwpyojzhs6y - hana
"""

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Whoops, need your username!")
        print("usage: python user_playlists.py [username]")
        sys.exit()

    token = util.prompt_for_user_token(username)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print()
                print(playlist['name'])
                print ('  total tracks', playlist['tracks']['total'])
                results = sp.playlist(playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print("Can't get token for", username)

