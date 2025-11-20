import webbrowser
import random

# Dictionary of moods and corresponding Spotify playlist links
playlists = {
    "happy": [
        "https://open.spotify.com/playlist/4pO80vyd83pis61t4qKpyz?si=Wl0O6ajwRUqUlk30cOD7AA",
    ],
    "sad": [
        "https://open.spotify.com/playlist/4MkTCMPKUSO2kXAGxDbZgM?si=0JKcLshgQMqwhrNtQf4bmQ"
    ],
    "relaxed": [
        "https://open.spotify.com/playlist/4hpTM68GoCVojjWuLY3Zbd?si=wZEp3WweRqixM6KOOPH3Rg"
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



