from play_playlist import play_playlist
import random

def main():
    print("🎵 Welcome to Mood-Mixer 🎶")

    while True: 
        print("Available moods: happy, sad, calm, angry, euphoric, random")
        print("Type 'exit' to quit the program.")
    
        emotion = input("How are you feeling today? ").strip().lower()

        if emotion == "exit":
            print("👋 Thanks for using Mood-Mixer!")
            break
    
        if emotion == "random":
            emotion = random.choice(list(playlists.keys()))
            print(f"🎲 Random mood chosen: {emotion}")
    
        play_playlist(emotion)

if __name__ == "__main__":
    main()

