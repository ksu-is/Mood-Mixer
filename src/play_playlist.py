import webbrowser
import random

# Dictionary of moods and corresponding Spotify playlist links
playlists = {
    "happy": [
        "https://open.spotify.com/playlist/HappyPlaylistLink1",
        "https://open.spotify.com/playlist/HappyPlaylistLink2"
    ],
    "sad": [
        "https://open.spotify.com/playlist/SadPlaylistLink"
    ],
    "relaxed": [
        "https://open.spotify.com/playlist/RelaxedPlaylistLink"
    ],
    "angry": [
        "https://open.spotify.com/playlist/AngryPlaylistLink"
    ]
}

def play_playlist(emotion):
    if emotion not in playlists:
        print(f"❌ Mood '{emotion}' not found!")
        return
    url = random.choice(playlists[emotion])
    webbrowser.open(url)
    print(f"🎧 Opening Spotify playlist for {emotion} mood...")



