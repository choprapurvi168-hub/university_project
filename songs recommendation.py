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
        "Ek Ladki Bheegi Bhaagi",
        "Yeh Sham Mastani",
        "Count on Me",
        "Can’t Stop the Feeling!",
        "Barso Re",
        "O Mere Dil Ke Chain",
        "Churaliya Hai Tumne Jo Dil Ko"
    ],
    "sad": [
        "Someone Like You Adele",
        "Channa Mereya Arijit Singh",
        "Waqt Ki Baatein Dream Note",
        "Fix You Coldplay",
        "Pachtaoge Arijit Singh",
        "Channa mereya",
        "Such Keh Raha Hai",
        "Piya Aaye Na",
        "Sochan Vich Tu",
        "Someone Like You"
    ],
    "angry": [
        "In The End Linkin Park",
        "Bhaag DK Bose Delhi Belly",
        "Break Stuff Limp Bizkit",
        "Azaadi Gully Boy",
        "Dope Shope Honey Singh",
        "In the End",
        "Shooter",
        "Dil Dhadakne Do",
        "Brown Munde",
        "Dhaakad"
    ],
    "relaxed": [
        "Weightless Marconi Union",
        "Raabta Agent Vinod",
        "Ocean Eyes Billie Eilish",
        "Excuses Ap Dhillon",
        "Yeh Raatein Yeh Mausam",
        "Lag ja Gale",
        "Chura Liya Hai Tumne Jo Dil Ko",
        "Stand by Me",
        "Can’t Help Falling in Love",
        "Excuses"
    ],
    "energetic": [
        "Thunderstruck AC DC",
        "Zinda Bhaag Milkha Bhaag",
        "Kala Chashma Baar Baar Dekho",
        "Proper Patola Diljit Dosanjh",
        "Na Ja",
        "Gulaabo",
        "Kar gyi chull",
        "Tan Tana Tan Tan Taara",
        "Badan Pe Sitare",
        "3 Peg"
    ]
}

# Ask user for mood
mood = input("Enter your mood (happy/sad/angry/relaxed/energetic): ").strip().lower()

if mood in songs:
    # Pick a random song
    recommendation = random.choice(songs[mood])
    print(f"Your mood-based suggestion: {recommendation}")
    print("Opening YouTube in your browser...")

    time.sleep(2) #Pause for 2 seconds
    
    # Open YouTube search
    query = f"{mood} {recommendation} song"
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

else:
    print("Sorry, mood not found! Try again with happy/sad/angry/relaxed/energetic.")





