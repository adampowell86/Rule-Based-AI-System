# movie_bot.py
"""
A Mysterious Movie Recommendation Chatbot
Author: The Shadow Coder
Purpose: Demonstrate a rule-based system in Python using mood and genre keywords.
"""

def main():
    print("Welcome to the Mysterious Movie Recommendation Chatbot.")
    print("Tell me how you feel and what kind of flick you fancy.\n")

    # Collect user input
    user_mood = input("First, what's your mood? ").lower().strip()
    user_genre = input("Interesting. And what genre are you looking for? ").lower().strip()

    # Decide recommendation using basic rule-based logic
    recommendation = get_recommendation(user_mood, user_genre)

    # Output final result
    print(f"\nI've got just the thing for you: {recommendation}\nEnjoy your movie night... if you dare.")

def get_recommendation(mood, genre):
    # Initialize default recommendation
    rec = "I can't quite place your mood or genre. Perhaps 'Casablanca' suits any soul."

    # Rules: Mood + Genre => Recommendation
    if mood == "sad" and genre == "comedy":
        rec = "The Grand Budapest Hotel (2014) - a quirky, colorful ride."
    elif mood == "sad" and genre == "action":
        rec = "Mad Max: Fury Road (2015) - might blast you out of that gloomy state."
    elif mood == "excited" and genre == "action":
        rec = "John Wick (2014) - an unstoppable adrenaline rush."
    elif mood == "excited" and genre == "comedy":
        rec = "Hot Fuzz (2007) - comedic action at its finest."

    # We can keep stacking up more mood + genre combos if we like
    elif mood == "lonely" and genre == "romance":
        rec = "Before Sunrise (1995) - a tender, introspective experience."
    elif mood == "happy" and genre == "drama":
        rec = "The Pursuit of Happyness (2006) - keeps that positivity rolling."
    
    # Return the final or fallback recommendation
    return rec

if __name__ == "__main__":
    main()
