import os
import random
import pygame

def play_music(emotion): 
  folder_path = f"music/{emotion}/"

  if not os.path.exists(folder_path):
        print(f"❌ No folder found for '{emotion}' — please choose a valid mood.")
        return

  songs = [file for file in os.listdir(folder_path) if file.endswith(".mp3")]

    if not songs:
        print(f"❌ No songs available in {folder_path}")
        return

    selected_song = random.choice(songs)
    song_path = os.path.join(folder_path, selected_song)

    pygame.mixer.init()
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    print(f"🎧 Now playing: {selected_song} ({emotion.capitalize()} mood)")

    input("Press Enter to stop music...")
    pygame.mixer.music.stop()


