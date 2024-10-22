import sqlite3
import re
import random
from collections import Counter
from nltk.corpus import stopwords

# Synonyms
synonyms = {
    "cs": "computer science",
    "c.s.": "computer science",
    "comp sci": "computer science"
}

# Function to preprocess the text by replacing synonyms and removing stop words
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Replace synonyms
    for abbr, full_form in synonyms.items():
        text = re.sub(r'\b' + re.escape(abbr) + r'\b', full_form, text)

    # Remove special characters and numbers
    text = re.sub(r'[^a-z\s]', '', text)

    # Tokenize and remove stopwords
    words = text.split()
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    return words  # Return a list of keywords

# Function to get all questions from the database
def get_all_questions_from_db():
    conn = sqlite3.connect('cs_faq.db')
    cursor = conn.cursor()
    cursor.execute("SELECT question FROM faq")
    questions = cursor.fetchall()
    conn.close()
    
    return [q[0] for q in questions]  # Return a list of questions

# Function to get the answer for a specific question
def get_answer_for_question(question):
    conn = sqlite3.connect('cs_faq.db')
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM faq WHERE question = ?", (question,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return result[0]
    else:
        return None

# Function to find the best match using keyword-based matching
def find_best_match(user_question):
    # Preprocess the user's question
    user_keywords = preprocess_text(user_question)

    # Get all questions from the database
    questions = get_all_questions_from_db()

    # Preprocess all FAQ questions
    question_keywords = [preprocess_text(q) for q in questions]

    # Find the question with the most matching keywords
    best_match = None
    best_score = 0

    for i, keywords in enumerate(question_keywords):
        common_keywords = Counter(keywords) & Counter(user_keywords)  # Count the matching keywords
        score = sum(common_keywords.values())  # Calculate the score based on matching keywords

        if score > best_score:
            best_score = score
            best_match = questions[i]

    # If a good match is found, return the corresponding answer
    if best_score > 0:  # If at least one keyword matches
        return get_answer_for_question(best_match)
    else:
        return None

# Function to make it more conversational
def conversational_response(answer):
    conversational_phrases = [
        "Good question! ",
        "I'm glad you asked. "
    ]
    if answer:
        return random.choice(conversational_phrases) + answer
    else:
        return "I'm sorry, I couldn't find anything related to that. Could you try rephrasing or ask a different question?"

# Chatbot loop with improved conversation (Add more)
def chatbot():
    greetings = [
        "Hello! How can I assist you with your CS questions today?",
        "Hi there! I'm here to help with any questions about the undergraduate CS program.",
        "Welcome! Feel free to ask me anything about CS!"
    ]
    
    print(random.choice(greetings))  # Displays a random greeting
    
    while True:
        user_question = input("You: ").strip()

        if user_question.lower() == "exit":
            print("Chatbot: Goodbye! Feel free to come back anytime.")
            break

        # Find the best matching question and get the answer
        answer = find_best_match(user_question)

        # Give a conversational response
        response = conversational_response(answer)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()
