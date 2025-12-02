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
        "https://open.spotify.com/playlist/2TLZJbGMhrp1QnKRvIBQWj?si=f5NC9MJuS428bSARQ4wSdQ"
    ],
    "euphoric": [
        "https://open.spotify.com/playlist/4MQy6z41YrO2HkN0Iybjiu?si=POXBX35nRauH0bFgd4b2ag"
    ]
}

def play_playlist(emotion):
    if emotion == "random":
        emotion = random.choice(list(playlists.keys()))
        print(f"🎲 Random mood chosen: {emotion}")
        
    if emotion not in playlists:
        print(f"❌ Mood '{emotion}' not found.")
        print("Available moods:", ", ".join(playlists.keys()))
        return
    url = random.choice(playlists[emotion])
    webbrowser.open(url)
    print(f"🎧 Opening Spotify playlist for {emotion} mood...")



