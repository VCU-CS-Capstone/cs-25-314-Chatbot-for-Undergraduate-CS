## Chatbot for Computer Science

*Below will be the detailed plan for implementation onto the VCU  website.

1) Using SQlite build a database that will hold information regarding courses, computer science organizations, and computer science professors.
  - See database code here ![](https://github.com/VCU-CS-Capstone/cs-25-314-Chatbot-for-Undergraduate-CS/tree/master/Staging/Kennedy%20Staging)
  - Estimated Size of Database: < 1MB
  - Location of Database: Google Cloud storage. Very inexpensive for the storage amount required, ability to grow with the website. This will allow the chatbot to access the database from the website.
  - Access: Read -- Chatbot , Write -- system admin (verified VCU faculty)
  - Maintenence required: Every eight weeks approximately
    
2) User Interface: Add HTML to the vcu pages that we want the chatbot to appear under
  - Chatbot user interface will be in a container within the HTML page and will send message information entered by the user to the backend which will then query       the database using the chatbot to be implemented.
  - Also will populate the chatbot's responses to the user in the container
  - HTML code for the div:
     ![image](https://github.com/user-attachments/assets/08855de0-e1aa-4ab9-b949-43ae472e7b93)

    
  - Uses .js for fetching the text from the user-input and populates the return of the python program in the backend to jsonify the chatbot's response and repopulate it in the chatbot container
  - Uses .css for the design of the visual and user experience portion on the website.
    
3) Backend:
- See python code here <>
- Build python program that will be responsible for sending user question to NLP for processing and return of key words
- Use key words to query a database to find all relevant information (this can be improved with word embedding if we have time)
- Take the information that was returned from the database and format it into a conversational response, send to chatbot (user)
    - We can either use the NLP to format a friendly response or we can have templates and fill them in with the information because the NLP will end up costing money.























