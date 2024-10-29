import sqlite3

# Connect to the database
conn = sqlite3.connect('cs_faq.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS faq (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# Insert new FAQs into the database
faqs = [
    ("What is the deadline to declare a major in Computer Science?", "The deadline to declare a major in Computer Science is usually the end of your sophomore year, but you should check with your advisor for specific dates."),
    ("Where can I find the course catalog?", "You can find the course catalog on the university's official website under the academics section."),
    ("How do I enroll in a Computer Science course?", "You can enroll in courses through the university's online registration system. Make sure you meet the prerequisites."),
    ("What should I do if a course is full?", "If a course is full, you can join the waitlist or contact the course instructor to request an override."),
    ("Can I take CS courses pass/fail?", "Most core Computer Science courses must be taken for a grade, but some elective courses may offer a pass/fail option."),
    ("What is the maximum number of credit hours I can take in one semester?", "The maximum number of credits you can take is 18 per semester. To exceed this, you will need approval from your academic advisor."),
    ("Can I audit a CS class?", "Yes, you can audit a CS class with the instructor's permission, but you won't receive credit for it."),
    ("How can I switch my major to Computer Science?", "To switch your major to Computer Science, you need to submit a major change form through the registrar's office."),
    ("What are the requirements to minor in Computer Science?", "The requirements for a minor in Computer Science typically include a minimum of 5 courses, including at least two upper-level courses."),
    ("Do I need to take Calculus for a CS major?", "Yes, most Computer Science programs require at least one semester of Calculus."),
    ("What are the prerequisites for CS201?", "CS201 requires that you have completed CS101 and MATH101."),
    ("Can I take CS301 without taking CS201?", "CS201 is a prerequisite for CS301. You will need to complete CS201 first."),
    ("How can I meet with a CS advisor?", "You can schedule an appointment with a CS advisor through the online advising system or by visiting the department office."),
    ("When is the best time to meet with my advisor?", "It's best to meet with your advisor before the registration period to discuss your course schedule for the upcoming semester."),
    ("What should I bring to my advising appointment?", "Bring a list of courses you're interested in, your degree audit, and any specific questions you have."),
    ("Why can't I register for a class?", "There are several reasons why you might not be able to register, including unmet prerequisites, holds on your account, or the class being full."),
    ("What should I do if I have a hold on my account?", "If you have a hold on your account, contact the registrar's office or the department that issued the hold to resolve the issue."),
    ("How do I drop a class?", "To drop a class, log into the student portal and follow the steps to drop the course before the drop deadline."),
    ("What happens if I drop a class after the deadline?", "If you drop a class after the deadline, it may result in a 'W' on your transcript and could affect your financial aid."),
    ("What are the graduation requirements for a CS major?", "The graduation requirements include completing the core Computer Science courses, a capstone project, and fulfilling the university's general education requirements."),
    ("How do I apply for graduation?", "You can apply for graduation through the registrar's office by submitting a graduation application form."),
    ("How can I find an internship in Computer Science?", "Check the university's career services website for internship postings or contact the Computer Science department for specific opportunities."),
    ("Can I get course credit for an internship?", "Yes, many Computer Science programs offer course credit for internships if they are approved by the department."),
    ("Can I transfer credits from another university to count toward my CS degree?", "Yes, but you will need to submit your transcripts for evaluation by the registrar's office. Not all courses may be eligible for transfer."),
    ("How do I transfer credits from a community college?", "You will need to submit an official transcript from the community college to the registrar's office. Transfer credits must be approved by the department."),
    ("Can I study abroad as a CS major?", "Yes, the university offers study abroad programs for CS majors. You should meet with your advisor to discuss how studying abroad will fit into your academic plan."),
    ("Will my credits from a study abroad program transfer back to my CS degree?", "Yes, credits earned during an approved study abroad program can transfer, but you should get pre-approval from the department to ensure they meet degree requirements."),
    ("What is the grading scale for CS courses?", "The grading scale typically follows A (90-100), B (80-89), C (70-79), D (60-69), and F (below 60), but this may vary by course."),
    ("How is academic dishonesty handled in the CS department?", "Academic dishonesty is taken very seriously and can result in penalties ranging from a zero on the assignment to expulsion. Refer to the university's academic integrity policy for details."),
    ("Where can I get help with my university email?", "For help with your university email, contact the IT help desk or visit the support section of the university's website."),
    ("How do I reset my university password?", "You can reset your password through the university's online portal or by contacting the IT help desk."),
    ("What is the department's office phone number?", "The Computer Science department's office phone number is (111) 111-1111."),
    ("Where is the Computer Science department located?", "The Computer Science department is located in Engineering West, Room 101.")
]

# Insert the FAQs into the database
cursor.executemany('INSERT INTO faq (question, answer) VALUES (?, ?)', faqs)

# Commit and close the connection
conn.commit()
conn.close()

print("FAQs inserted successfully.")