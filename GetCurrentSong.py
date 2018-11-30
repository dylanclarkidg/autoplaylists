import spotipy

user_authenticate = 'BQCYooPwEetY1BsP2P2QpJn6tI5NC3hZVvZ5ZIzpOgQmRrnvI3lmK9oZB1xDfleddyX8Y-W4KNwqtZGJYorvfnSMVP-aVy3S-28O4A2LHPvIEvG90zJGaowwINDr1qfiIoScz4U6CQBmeQRXuj65FmoWWGTH'
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