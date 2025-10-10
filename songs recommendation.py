import webbrowser
import random
import time

# Dictionary of moods and songs (English + Hindi + Punjabi)
songs = {
    "happy": [
        "Happy Pharrell Williams",
        "Gallan Goodiyaan Dil Dhadakne Do",
        "Lover Diljit Dosanjh",
        "Can't Stop the Feeling Justin Timberlake",
        "Laung Laachi Mannat Noor"
    ],
    "sad": [
        "Someone Like You Adele",
        "Channa Mereya Arijit Singh",
        "Waqt Ki Baatein Dream Note",
        "Fix You Coldplay",
        "Pachtaoge Arijit Singh"
    ],
    "angry": [
        "In The End Linkin Park",
        "Bhaag DK Bose Delhi Belly",
        "Break Stuff Limp Bizkit",
        "Azaadi Gully Boy",
        "Dope Shope Honey Singh"
    ],
    "relaxed": [
        "Weightless Marconi Union",
        "Raabta Agent Vinod",
        "Ocean Eyes Billie Eilish",
        "Tera Yaar Hoon Main Arijit Singh",
        "Excuses Ap Dhillon"
    ],
    "energetic": [
        "Thunderstruck AC DC",
        "Zinda Bhaag Milkha Bhaag",
        "Kala Chashma Baar Baar Dekho",
        "Stronger Kanye West",
        "Proper Patola Diljit Dosanjh"
    ]
}

# Ask user for mood
mood = input("Enter your mood (happy/sad/angry/relaxed/energetic): ").strip().lower()

if mood in songs:
    # Pick a random song
    recommendation = random.choice(songs[mood])
    print(f"Your mood-based suggestion: {recommendation}")
    print("Opening YouTube in your browser...")

    time.sleep(30)
    
    # Open YouTube search
    query = f"{mood} {recommendation} song"
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

else:
    print("Sorry, mood not found! Try again with happy/sad/angry/relaxed/energetic.")

