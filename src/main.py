from play_playlist import play_playlist

def main():
    print("🎵 Welcome to Mood-Mixer 🎶")
    print("Available moods: happy, sad, calm, angry, euphoric, random")

    emotion = input("How are you feeling today? ").strip().lower()

    if emotion == "random":
        emotion = random.choice(list(playlists.keys()))
        print(f"🎲 Random mood chosen: {emotion}")
    
    play_playlist(emotion)

if __name__ == "__main__":
    main()

