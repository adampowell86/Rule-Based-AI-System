# movie_bot.py
"""
A Mysterious Movie Recommendation Chatbot
Author: The Shadow Coder
Purpose: Demonstrate a rule-based system in Python using mood and genre keywords.
"""

def main():
    print("Welcome to the Mysterious Movie Recommendation Chatbot.")
    print("Tell me how you feel and what kind of flick you fancy.\n")

    while True:
        # Collect user input
        user_mood = input("First, what's your mood? ").lower().strip()
        user_genre = input("Interesting. And what genre are you looking for? ").lower().strip()

        if not user_mood or not user_genre:
            print("Please provide both mood and genre.")
        else:
            # Decide recommendation using basic rule-based logic
            recommendation = get_recommendation(user_mood, user_genre)

            # Output final result
            print(f"\nI've got just the thing for you: {recommendation}\nEnjoy your movie night... if you dare.")

        # Ask if user wants another recommendation
        another = input("Would you like another recommendation? (yes/no): ").lower().strip()
        if another != 'yes':
            break

def get_recommendation(mood, genre):
    # Dictionary of rules: (mood, genre) => recommendation
    recommendations = {
        ("sad", "comedy"): "The Grand Budapest Hotel (2014) - a quirky, colorful ride.",
        ("sad", "action"): "Mad Max: Fury Road (2015) - might blast you out of that gloomy state.",
        ("excited", "action"): "John Wick (2014) - an unstoppable adrenaline rush.",
        ("excited", "comedy"): "Hot Fuzz (2007) - comedic action at its finest.",
        ("lonely", "romance"): "Before Sunrise (1995) - a tender, introspective experience.",
        ("happy", "drama"): "The Pursuit of Happyness (2006) - keeps that positivity rolling.",
        # Additional rules
        ("bored", "horror"): "The Conjuring (2013) - a thrilling horror movie.",
        ("angry", "sci-fi"): "Blade Runner 2049 (2017) - a visually stunning sci-fi movie.",
        ("curious", "documentary"): "The Social Dilemma (2020) - an eye-opening documentary.",
    }

    # Return the recommendation or a default message
    return recommendations.get((mood, genre), "I can't quite place your mood or genre. Perhaps 'Casablanca' suits any soul.")

if __name__ == "__main__":
    main()