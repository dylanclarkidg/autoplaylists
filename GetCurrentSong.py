import spotipy

user_authenticate = 'BQDykfvOWIECieX_GY6ho-ZNyoslld0UYXMs4ETuHREqPQKfHN7sPOfDPwk4Rx3JUjBhj778CVYgliTPaRzhARpXVsbRlj5hSjHXItsYErVOZqADZicYTSKbRW9y-FDSqJegwsQIsz7E_4p4DpDXb293DQF1PYezjC_4iZHC8dMv46MNp1b1oYq5T7Lq5KoVhB-s'
spotify = spotipy.Spotify(auth=user_authenticate)

results = spotify.current_user_top_tracks()
trackIds = []

topTracks = results["items"]
for i in range(20):
    trackIds.append(topTracks[i]["id"])
    print(topTracks[i]["name"] + " by " + topTracks[i]["album"]["artists"][0]["name"])
print(trackIds)

userId = "maskless"
playlistId = "6kGTJE6T32rSzjbHeXQ7ez"

spotify.user_playlist_add_tracks(userId, playlistId, trackIds)