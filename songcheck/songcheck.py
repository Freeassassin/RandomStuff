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

uncommon = open("uncommon.txt", "r", encoding="utf8")
uncommon = uncommon.read()
exec(uncommon)
print(uncommon[1])

for i in range(0len(uncommon)):
    print(uncommon[i])
    choice = input()
    if choice != "y":
        uncommon.remove(uncommon[i])

print(uncommon)
main = open("main.txt", "r", encoding="utf8")
main = main.read()
exec(main)

alltheshit = open("alltheshit.txt", "r", encoding="utf8")
alltheshit = alltheshit.read()
exec(alltheshit)

def common(a,b): 
    c = [value for value in a if value in b] 
    return c

bs = common(main,alltheshit)

for i in bs:
    for j in alltheshit:
        if j == i:
            alltheshit.remove(j)

print(alltheshit) 
drew_greschuk
22tbacddrpftnbbxh4bmjegzi - adam
224efvqg73lyqelwpyojzhs6y - hana
"""
"""
if len(sys.argv) > 3:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
    track_ids = sys.argv[3:]
else:
    print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
    sys.exit()

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print(results)
else:
    print("Can't get token for", username)
"""
"""
x = []
def show_tracks(tracks,playlist):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        try:  
            #print(track['id'])
            playlist.append(track['id'])
        except:
            print("error")


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
                if playlist['name'] == "Main":
                    print()
                    print(playlist['name'])
                    print ('  total tracks', playlist['tracks']['total'])
                    results = sp.playlist(playlist['id'],
                        fields="tracks,next")
                    tracks = results['tracks']
                    show_tracks(tracks,x)
                    while tracks['next']:
                        tracks = sp.next(tracks)
                        show_tracks(tracks,x)
                    print(x)
    else:
        print("Can't get token for", username)
"""
uncommon = open("uncommon.txt", "r", encoding="utf8")
uncommon = uncommon.read()
exec(uncommon)

if len(sys.argv) > 3:
    username = sys.argv[1]
    playlist_id = sys.argv[2]
    x = sys.argv[3:]

else:
    print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
    sys.exit()

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    for i in range(1,7):
        pass
        #x = uncommon[0+((i-1)*100):i*100-1]
    results = sp.user_playlist_add_tracks(username, playlist_id, x)
    print(results)
else:
    print("Can't get token for", username)