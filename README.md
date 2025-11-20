## 🎵 Mood-Mixer

**Mood-Mixer** is a simple Python program that helps users discover and play music based on their current mood.  
It’s designed to be lightweight and easy to use, providing a quick way to find songs that match how you’re feeling.

---

### 💡 How It Works

1. The user runs the program and types in their current mood (e.g., `happy`, `sad`, `calm`, `angry`, or `euphoric`).  
2. The program selects a Spotify playlist that matches the chosen mood.  
3. The playlist opens automatically in your web browser, so you can start listening immediately.  
4. If the mood isn’t recognized, the program provides a friendly error message to help the user try again.

---

### 🎶 Available Moods & Example Playlists

| Mood      | Playlist Name             | Description                                           |
|-----------|--------------------------|-------------------------------------------------------|
| 😄 Happy  | Sunshine & Good Vibes    | Bright, upbeat tunes to boost your mood.             |
| 😢 Sad    | Late Night Thoughts      | Soft, emotional songs to match reflective moments.   |
| 😌 Calm   | Peaceful Airwaves        | Chill, relaxing tracks to help you unwind.           |
| 😡 Angry  | Unleash the Energy       | High-energy songs to release tension.                |
| 🤩 Euphoric | Neon Night Euphoria    | Electric beats to make everything feel exciting.     |

---

### 🧠 Technologies Used

- **Python** – Core programming language for the application  
- **Webbrowser Module** – Opens Spotify playlists in the browser  
- **Random Module** – Randomly selects playlists for each mood  
- **Spotify ** – Spotify API integration for future enhancements  

---

### 🚀 How to Run

1. Make sure both `main.py` and `play_playlist.py` are in the same folder.  
2. Open a terminal in the project folder.  
3. Run the program with:
   ```bash
   python main.py
