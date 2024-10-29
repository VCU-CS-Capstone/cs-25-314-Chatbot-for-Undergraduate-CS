import sqlite3
import re
import random
from collections import Counter
from nltk.corpus import stopwords





class Chatbot:
    def __init__(self, db_path='cs_faq.db'):
        self.db_path = db_path
        self.synonyms = {
            "cs": "computer science",
            "c.s.": "computer science",
            "comp sci": "computer science"
        }
        # self.stop_words = set(stopwords.words('english'))

    def preprocess_text(self, text):
        # Convert text to lowercase
        text = text.lower()

        # Replace synonyms
        for abbr, full_form in self.synonyms.items():
            text = re.sub(r'\b' + re.escape(abbr) + r'\b', full_form, text)

        # Remove special characters and numbers
        text = re.sub(r'[^a-z\s]', '', text)

        # Tokenize and remove stopwords
        words = text.split()
        stop_words = set(stopwords.words('english'))
        words = [word for word in words if word not in stop_words]

        return words

    def get_all_questions_from_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT question FROM faq")
        questions = cursor.fetchall()
        conn.close()

        return [q[0] for q in questions]

    def get_answer_for_question(self, question):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT answer FROM faq WHERE question = ?", (question,))
        result = cursor.fetchone()
        conn.close()

        if result:
            return result[0]
        else:
            return None

    def find_best_match(self, user_question):
        # Preprocess the user's question
        user_keywords = self.preprocess_text(user_question)

        # Get all questions from the database
        questions = self.get_all_questions_from_db()

        # Preprocess all FAQ questions
        question_keywords = [self.preprocess_text(q) for q in questions]

        # Find the question with the most matching keywords
        best_match = None
        best_score = 0

        for i, keywords in enumerate(question_keywords):
            common_keywords = Counter(keywords) & Counter(user_keywords)
            score = sum(common_keywords.values())

            if score > best_score:
                best_score = score
                best_match = questions[i]

        # Return the corresponding answer if a match is found
        if best_score > 0:
            return self.get_answer_for_question(best_match)
        else:
            return None

    def conversational_response(self, answer):
        conversational_phrases = [
            "Good question! ",
            "I'm glad you asked. "
        ]
        if answer:
            return random.choice(conversational_phrases) + answer
        else:
            return "I'm sorry, I couldn't find anything related to that. Could you try rephrasing or ask a different question?"

    def ask(self, user_question):
        answer = self.find_best_match(user_question)
        return self.conversational_response(answer)
