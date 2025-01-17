# Rule-Based-AI-System
2.3 Building a Rule-Based AI System w/Python

# Mysterious Movie Recommendation Chatbot

## Part 1: Initial Project Ideas

1. **Project Idea 1: Mysterious Movie Recommendation Chatbot**
    
    - **Description:** A chatbot that recommends movies based on the user's current mood and preferred genre. Users input how they feel and the type of movie they’re in the mood for, and the chatbot suggests a suitable film using predefined rules.
    - **Rule-Based Approach:**
        - The system identifies keywords related to moods (e.g., "happy," "sad") and genres (e.g., "action," "comedy").
        - Based on the combination of mood and genre, the chatbot selects an appropriate movie from a predefined list.

2. **Project Idea 2: Simple Chatbot**
    
    - **Description:** A chatbot that responds to user inputs with predefined answers. The chatbot simulates a conversation by identifying keywords and phrases in user inputs.
    - **Rule-Based Approach:**
        - Responses are based on keywords such as "hello," "help," or "bye."
        - For example, if the user says "hello," the system responds with "Hi there! How can I assist you?"

3. **Project Idea 3: Travel Packing List Generator**
    
    - **Description:** A system that generates a packing list based on the user’s destination, climate, and trip duration.
    - **Rule-Based Approach:**
        - The system uses rules to recommend items.
        - For example, if the destination is "beach" and the climate is "hot," the system suggests sunscreen, swimsuits, and sunglasses.

**Chosen Idea:** Mysterious Movie Recommendation Chatbot

**Justification:** I chose this project because it combines user interaction with logical decision-making, allowing me to implement a variety of conditionals based on different moods and genres. It’s engaging and practical, providing meaningful recommendations that enhance user experience.

## Part 2: Rules/Logic for the Chosen System

The **Mysterious Movie Recommendation Chatbot** system follows these rules:

1. **Capture Mood:**
    - **IF** user input contains "sad" → set mood = "sad"
    - **IF** user input contains "excited" → set mood = "excited"
    - **IF** user input contains "happy" → set mood = "happy"
    - **IF** user input contains "lonely" → set mood = "lonely"

2. **Capture Preferred Genre:**
    - **IF** user input contains "action" → set genre = "action"
    - **IF** user input contains "comedy" → set genre = "comedy"
    - **IF** user input contains "drama" → set genre = "drama"
    - **IF** user input contains "romance" → set genre = "romance"

3. **Recommendation Logic:**
    - **IF** mood = "sad" **AND** genre = "comedy" → recommend *The Grand Budapest Hotel*
    - **IF** mood = "excited" **AND** genre = "action" → recommend *Mad Max: Fury Road*
    - **IF** mood = "happy" **AND** genre = "drama" → recommend *The Pursuit of Happyness*
    - **IF** mood = "lonely" **AND** genre = "romance" → recommend *Before Sunrise*
    - **IF** no matching rules → recommend a default movie like *Casablanca*

4. **Fallback:**
    - **IF** user input doesn’t match any known mood/genre → ask clarifying questions or suggest a default recommendation.

## Part 3: Sample Input and Output

Enter your mood: sad
Enter your preferred genre: comedy
You are close to making *The Grand Budapest Hotel*! Missing: None.

---

Enter your mood: excited
Enter your preferred genre: action
You are close to making *Mad Max: Fury Road*! Missing: None.

---

Enter your mood: happy
Enter your preferred genre: drama
You are close to making *The Pursuit of Happyness*! Missing: None.


## Part 4: Reflection

**Project Overview:**

This project involved designing and implementing a rule-based chatbot that recommends movies based on the user's mood and preferred genre. By utilizing logical conditions and predefined rules, the system provides personalized movie suggestions without relying on machine learning algorithms.

**Challenges:**

1. **Handling Diverse User Inputs:**
    - **Issue:** Users might describe their moods and genres in various ways, making it challenging to accurately capture their preferences.
    - **Solution:** Implemented keyword matching with multiple synonyms and variations to better interpret user inputs.

2. **Expanding the Rule Set:**
    - **Issue:** Ensuring the system remains manageable as more moods and genres are added.
    - **Solution:** Organized rules systematically and considered scalability by grouping related conditions.

**Comparison to Machine Learning:**

- **Rule-Based vs. Machine Learning:**
    - **Rule-Based Approach:** Relies on predefined logical rules, offering transparency and ease of debugging. It's straightforward but limited to the scenarios explicitly coded.
    - **Machine Learning Approach:** Utilizes data to learn patterns and make predictions, allowing for more flexibility and adaptability but often lacking transparency.

- **Advantages of Rule-Based System:**
    - Simplicity and clear logic make it easy to understand and modify.
    - Immediate responses without the need for training data.

- **Limitations:**
    - Scalability issues as the number of rules increases.
    - Inability to handle ambiguous or unseen inputs effectively without extensive rule definitions.

Overall, this rule-based chatbot serves as a foundational project to understand the mechanics of AI systems before delving into more complex machine learning models. It highlights the importance of clear logic and the challenges of creating flexible yet robust rule sets.

---

