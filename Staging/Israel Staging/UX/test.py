def chatbot_response(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "help" in user_input.lower():
        return "Sure! What do you need help with?"
    else:
        return "I'm not sure how to respond to that."