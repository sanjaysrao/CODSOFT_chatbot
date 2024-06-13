import re
def respond(user_text):
    user_text = user_text.lower()
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_text):
        return "Hello! How can I help you today?"
    elif re.search(r'\bhow are you\b', user_text):
        return "I'm fine, thank you for asking. How are you today?"
    elif re.search(r'\bgood (morning|afternoon|evening)\b', user_text):
        return "Good day! How can I help you today?"
    elif re.search(r'\bfine\b|\bi am fine\b', user_text):
        return "That's good to hear! How can I help you today?"
    elif re.search(r'\b(what is your name|name)\b', user_text):
        return "I am a chatbot created to assist you with your queries."
    elif re.search(r'\b(bye|goodbye|quit)\b', user_text):
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please make it clear?"
def chat():
    print("Hello! Welcome to the codsoft chatbot. How can I assist you? Type 'exit' to stop chat.")
    while True:
        user_text = input("You: ").strip().lower()
        if user_text == "exit":
            print("Bot: Goodbye! Have a great day!")
            break
        response = respond(user_text)
        print(f"Bot: {response}")
if __name__ == "__main__":
    chat()
