import spotipy
from spotipy import util
import requests

userId = 'maskless'
scope = 'user-top-read playlist-modify-private playlist-read-private'
clientId = ''
clientSecret = ''
redirectUri = 'http://example.com/callback/'

playlistId = "6kGTJE6T32rSzjbHeXQ7ez"

sometoken = util.oauth2.SpotifyOAuth(clientId, clientSecret, redirectUri, scope=scope)

#ssometoken = util.oauth2.SpotifyClientCredentials(client_id=clientId, client_secret=clientSecret)
cache_token = sometoken.get_access_token(code='AQDkwEo4NJAuwJiWzX748KIJcW1UAY2UnNRUD0W73haDGh671QA_Zr9vbfJ_TBSrjItLLsA2XWAkYd2BY9sUkINRC62McDBgV6mtfA-O7kc-_An7a8OYIWwPsKaDDN1-luY1BgnMKKY9aAF4xKhz4tl2hHolFz7IG8YQEwPlZrMuZZ4RB7WLm2XaIGydKt5yX1JJgJvCWCb50wDlVpVZ3RCJVXHR_Mq5UyrseGonm2kW-W9C4xj8H5k_YouUMp2q19cF-Te5E2-dSxQkG61_gUxxXg')
sp = spotipy.Spotify(cache_token)
results = sp.current_user_top_tracks()
for item in results['items']:
    track = item['track']
    print(track['name'] + ' - ' + track['artists'][0]['name'])

#token = util.prompt_for_user_token(userId, scope=scope, client_id=clientId, client_secret=clientSecret, redirect_uri=redirectUri)
# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_top_tracks()
#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", userId)

def RequestAuthorization():
    url = "https://accounts.spotify.com/authorize?client_id=75e135b231a2410ca5b9d3bb366102c1&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=user-top-read%20playlist-modify-private%20playlist-read-private&state=34fFs29kd09"
    r = requests.get(url)
    print(r.status_code, r.request)


def RequestRefreshTokens():
    url = "https://accounts.spotify.com/api/token"
    data = {
        'client_id': '',
        'client_secret': '',
        'grant_type': 'authorization_code',
        'code': '',
        'redirect_uri': 'https%3A%2F%2Fexample.com%2Fcallback'
    }
    r = requests.post(url, data=data)
    print(r.status_code, r.reason)

#RequestRefreshTokens()


#
# user_authenticate = ''
# spotify = spotipy.Spotify(auth=user_authenticate)
#
# def GetCurrentTracksInPlaylist():
#     currentTrackIds = spotify.user_playlist_tracks(userId, playlistId)
#     return currentTrackIds
#
#
# def GetCurrentTopTracks():
#     trackIds = []
#     currentTopTracks = spotify.current_user_top_tracks()
#     topTracks = currentTopTracks["items"]
#     for i in range(20):
#         trackIds.append(topTracks[i]["id"])
#         print(topTracks[i]["name"] + " by " + topTracks[i]["album"]["artists"][0]["name"])
#     return trackIds
#
#
# def EliminateExistingTracks(tracksInPlaylist, newTopTracks):
#     return [x for x in tracksInPlaylist if x not in newTopTracks]
#
#
# def AddTracksToPlaylist(trackIds):
#     spotify.user_playlist_add_tracks(userId, playlistId, trackIds)
#
#
# currentTracksInPlaylist = GetCurrentTopTracks()
# currentTopTracks = GetCurrentTopTracks()
# topTracksNotInPlaylist = EliminateExistingTracks(currentTracksInPlaylist, currentTopTracks)
# AddTracksToPlaylist(topTracksNotInPlaylist)
