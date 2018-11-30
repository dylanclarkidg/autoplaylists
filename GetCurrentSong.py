import spotipy
import requests


def RequestAuthorization():
    url = "https://accounts.spotify.com/authorize?client_id=75e135b231a2410ca5b9d3bb366102c1&response_type=code&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=user-top-read%20playlist-modify-private%20playlist-read-private&state=34fFs29kd09"
    r = requests.get(url)
    print(r.status_code, r.request)


def RequestRefreshTokens():
    url = "https://accounts.spotify.com/api/token"
    payload = {
        "client_id": "75e135b231a2410ca5b9d3bb366102c1",
        "client_secret": "8c2749ec5d8f45f6b0f2fc4a8f1e7cd3",
        "grant_type": "authorization_code",
        "code": "AQA1TzcH3QpKx_8UfGoCwEXxHyY5PxugJHRzjX4uZHMYT_2wqRkTXO853EWvhXxQMD9_NsTFTsEKI5tceFOk3yKD0t1zup4jK4gNke62SdcUlyp8j_DyIryVhR6rQFOLHQ3r7cQ5Oxn050tfUliXoLWrijguyTDp1I2FbKaXMQlX1mzoIcDJ1kccR66KOTVNAVmdki_IPhoa-M45tzlfzI2IfXcA8k4oCDVbWM0CXqrPVfb6dOVsLc5xLs2MJpVIdv_MUkDEfFCSRdYuE1dslYGMPA",
        "redirect_uri": "https%3A%2F%2Fexample.com%2Fcallback"
    }
    r = requests.post(url, data=payload)
    print(r.status_code, r.reason)


RequestRefreshTokens()

userId = "maskless"
playlistId = "6kGTJE6T32rSzjbHeXQ7ez"

user_authenticate = 'BQDykfvOWIECieX_GY6ho-ZNyoslld0UYXMs4ETuHREqPQKfHN7sPOfDPwk4Rx3JUjBhj778CVYgliTPaRzhARpXVsbRlj5hSjHXItsYErVOZqADZicYTSKbRW9y-FDSqJegwsQIsz7E_4p4DpDXb293DQF1PYezjC_4iZHC8dMv46MNp1b1oYq5T7Lq5KoVhB-s'
spotify = spotipy.Spotify(auth=user_authenticate)


def GetCurrentTracksInPlaylist():
    currentTrackIds = spotify.user_playlist_tracks(userId, playlistId)
    return currentTrackIds


def GetCurrentTopTracks():
    trackIds = []
    currentTopTracks = spotify.current_user_top_tracks()
    topTracks = currentTopTracks["items"]
    for i in range(20):
        trackIds.append(topTracks[i]["id"])
        print(topTracks[i]["name"] + " by " + topTracks[i]["album"]["artists"][0]["name"])
    return trackIds


def EliminateExistingTracks(tracksInPlaylist, newTopTracks):
    return [x for x in tracksInPlaylist if x not in newTopTracks]


def AddTracksToPlaylist(trackIds):
    spotify.user_playlist_add_tracks(userId, playlistId, trackIds)


currentTracksInPlaylist = GetCurrentTopTracks()
currentTopTracks = GetCurrentTopTracks()
topTracksNotInPlaylist = EliminateExistingTracks(currentTracksInPlaylist, currentTopTracks)
AddTracksToPlaylist(topTracksNotInPlaylist)
