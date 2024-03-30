def simple_chatbot(user_input):
    user_input_lower = user_input.lower()
    if 'hi' in user_input_lower or 'hello' in user_input_lower or 'hey' in user_input_lower:
        return 'Hello! How can I help you?'
    elif 'how are you' in user_input_lower:
        return 'I am a bot, but thanks for asking!'
    elif 'what is your name' in user_input_lower:
        return 'I am a simple chatbot.'
    elif 'bye' in user_input_lower or 'goodbye' in user_input_lower:
        return 'Goodbye! Have a great day!'
    elif 'how do you do' in user_input_lower or 'what\'s up' in user_input_lower or 'sup' in user_input_lower:
        return 'Not much, just here to assist you.'
    elif 'tell me a joke' in user_input_lower or 'say something funny' in user_input_lower:
        return 'What did the publishing agent say to the newly discovered poet? "Metaphors be with you!"'
    elif 'thank you' in user_input_lower or 'thanks' in user_input_lower:
        return 'You\'re welcome!'
    elif 'help' in user_input_lower or 'assistance' in user_input_lower:
        return 'I can help with general information, jokes, and more. Just ask!'
    elif 'what time is it' in user_input_lower or 'current time' in user_input_lower:
        return 'I\'m sorry, I don\'t have the ability to provide real-time information.'
    elif 'what can you do' in user_input_lower:
        return 'I can provide information, tell jokes, and engage in basic conversation. Feel free to ask anything!'
    elif 'where are you from' in user_input_lower:
        return 'I exist in the digital realmI.'
    elif 'tell me about yourself' in user_input_lower:
        return 'I am a simple chatbot designed to assist users with various queries.'
    else:
        return "I'm sorry, I didn't understand that."

# Main loop for chatting
while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    
    response = simple_chatbot(user_input)
    print("Chatbot:", response)