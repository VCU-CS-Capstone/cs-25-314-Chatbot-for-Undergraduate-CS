import sqlite3
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re

# Dictionary of synonyms
synonyms = {
    "cs": "computer science",
    "c.s.": "computer science"
}

# List of phrases to detect instructor-related questions
instructor_phrases = [
    "who teaches",
    "who is the teacher",
    "who is the professor",
    "who instructs",
    "who is the instructor"
]

# Function to preprocess the text by replacing synonyms
def preprocess_text(text):
    if not text:  # Check if the text is None or empty
        return ""

    # Convert text to lowercase for uniformity
    text = text.lower()

    # Replace synonyms in the text
    for abbr, full_form in synonyms.items():
        text = re.sub(r'\b' + re.escape(abbr) + r'\b', full_form, text)
    
    return text

# Function to get all keywords from multiple tables in the database
def get_all_keywords_from_db():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    
    # Get keywords from main_data
    cursor.execute("SELECT keyword FROM main_data")
    main_data_keywords = [k[0] for k in cursor.fetchall()]
    
    # Get course names and course IDs from Courses
    cursor.execute("SELECT CourseName, CourseID FROM Courses")
    course_data = cursor.fetchall()
    course_keywords = [k[0] for k in course_data] + [k[1] for k in course_data]
    
    # Get instructor names from Instructors
    cursor.execute("SELECT InstructorName FROM Instructors")
    instructor_keywords = [k[0] for k in cursor.fetchall()]
    
    # Get organization names from Organizations
    cursor.execute("SELECT OrganizationName FROM Organization")
    organization_keywords = [k[0] for k in cursor.fetchall()]
    
    conn.close()

    # Combine all keywords into one list
    return main_data_keywords + course_keywords + instructor_keywords + organization_keywords

# Function to get response based on the matched keyword and the user's question context
def get_response_for_keyword(keyword, user_question):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    # Check if the user is asking about the instructor for a course
    if any(phrase in user_question for phrase in instructor_phrases):
        # Check Courses table for matching course
        cursor.execute("SELECT CourseInstructor FROM Courses WHERE CourseID = ? OR CourseName = ?", (keyword, keyword))
        result = cursor.fetchone()
        if result:
            instructor_name = result[0] if result[0] else "None"
            conn.close()
            return f"The instructor for {keyword} is: {instructor_name}", None

    # Check main_data table for matching keyword
    cursor.execute("SELECT response, resource FROM main_data WHERE keyword = ?", (keyword,))
    result = cursor.fetchone()
    if result:
        conn.close()
        return result

    # Check Courses table for matching course (both CourseName and CourseID)
    cursor.execute("SELECT CourseName, CourseDescrip, CourseInstructor FROM Courses WHERE CourseID = ? OR CourseName = ?", (keyword, keyword))
    result = cursor.fetchone()
    if result:
        course_name = result[0]
        course_description = result[1]
        course_instructor = result[2] if result[2] else "None"
        response = f"Course Name: {course_name}\nCourse Description: {course_description}\nTaught by: {course_instructor}"
        conn.close()
        return response, None  # No resource for courses

    # Check Instructors table for matching instructor
    cursor.execute("SELECT InstructorCourses, InstructorResearch FROM Instructors WHERE InstructorName = ?", (keyword,))
    result = cursor.fetchone()
    if result:
        response = f"Instructor Courses: {result[0]}. Research Areas: {result[1]}."
        conn.close()
        return response, None  # No resource for instructors

    # Check Organizations table for matching organization
    cursor.execute("SELECT OrganizationDesc, FalcultySponsor FROM Organization WHERE OrganizationName = ?", (keyword,))
    result = cursor.fetchone()
    if result:
        response = f"Organization Description: {result[0]}. Faculty Sponsor: {result[1]}."
        conn.close()
        return response, None  # No resource for organizations

    conn.close()
    return None  # If no match found

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
    if best_score > 50:  # Lower the threshold
        original_keyword = keywords[preprocessed_keywords.index(best_match)]
        response_data = get_response_for_keyword(original_keyword, user_question)
        if response_data:
            response, resource = response_data
            if resource:
                return f"{response}\nFor more information, visit: {resource}"
            return response
    else:
        return "Sorry, I couldn't find an answer that matches your question closely enough."

def chatbot():
    print("Welcome to the VCU CS Chatbot. Ask me anything about the undergraduate CS program.")
    
    while True:
        user_question = input("You: ").strip()

        if user_question.lower() == "exit":
            print("Chatbot: Goodbye!")
            break

        # Find the best matching keyword and get the response and resource
        answer = find_best_match(user_question)
        
        print(f"Chatbot: {answer}")

if __name__ == "__main__":
    chatbot()