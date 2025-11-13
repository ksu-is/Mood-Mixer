from play_music import play_music

def main():
    print("🎵 Welcome to Mood-Mixer 🎶")
    print("Available moods: happy, sad, calm, angry, euphoric")

    emotion = input("How are you feeling today? ").strip().lower()
    play_music(emotion)

if __name__ == "__main__":
    main()

