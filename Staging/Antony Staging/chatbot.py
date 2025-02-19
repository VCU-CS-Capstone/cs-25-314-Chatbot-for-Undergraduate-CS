import sqlite3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Make sure the necessary NLTK resources are downloaded
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Dictionary of synonyms
synonyms = {
    "cs": "computer science",
    "c.s.": "computer science"
}

# Function to preprocess the text by replacing synonyms, removing stopwords, and punctuation
def preprocess_text(text):
    if not text:  # Check if the text is None or empty
        return ""
    
    # Convert text to lowercase for uniformity
    text = text.lower()

    # Replace synonyms in the text
    for abbr, full_form in synonyms.items():
        text = re.sub(r'\b' + re.escape(abbr) + r'\b', full_form, text)
    
    # Tokenize text and remove stopwords
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]

    # Rejoin tokens into a string
    return " ".join(tokens)

# Function to get all keywords from main_data in the database
def get_all_keywords_from_db():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    
    # Get keywords from main_data
    cursor.execute("SELECT keyword FROM main_data")
    main_data_keywords = [k[0] for k in cursor.fetchall()]
    
    conn.close()
    return main_data_keywords

# Function to get response based on the matched keyword and the user's question context
def get_response_for_keyword(keyword):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Check main_data table for matching keyword
    cursor.execute("SELECT response, resource FROM main_data WHERE keyword = ?", (keyword,))
    result = cursor.fetchone()
    conn.close()
    
    return result if result else None

# Function to find the best matching keyword and return the response and resource
def find_best_match(user_question):
    # Preprocess the user's question
    user_question = preprocess_text(user_question)

    # Get all keywords from the database
    keywords = get_all_keywords_from_db()

    # Preprocess all keywords before matching
    preprocessed_keywords = [preprocess_text(k) for k in keywords]

    # Use fuzzy matching to find the best match
    best_match, best_score = process.extractOne(user_question, preprocessed_keywords, scorer=fuzz.token_sort_ratio)

    # If the match score is high enough, return the corresponding response and resource
    if best_score > 50:
        original_keyword = keywords[preprocessed_keywords.index(best_match)]
        response_data = get_response_for_keyword(original_keyword)
        if response_data:
            response, resource = response_data
            return [response, resource]  # Format the response as a list
    return ["Sorry, I couldn't find an answer that matches your question closely enough.", None]

def chatbot(user_question):
    # Find the best matching keyword and get the response and resource
    answer = find_best_match(user_question)
    return answer

print("Welcome to the VCU CS Chatbot. Ask me anything about the undergraduate CS program.")
while True:
    user_question = input("You: ").strip()
    response = chatbot(user_question)
    if response[1]:  # If there is a link
        print(f"Chatbot: {response[0]} For more information, visit: {response[1]}")
    else:
        print(f"Chatbot: {response[0]}") # No link
