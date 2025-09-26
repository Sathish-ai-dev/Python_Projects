while True:
    user_input = input("You: ")
    if user_input.lower() in ['hi', 'hello', 'hey']:
        print("Bota: Hello! How can I assist you today?")
    elif user_input.lower() in ['bye', 'goodbye', 'see you']:
        print("Bota: Goodbye! Have a great day!")
        break
    else:
        print("Bota: I'm sorry, I didn't understand that. Can you please rephrase?")
        responses = {
            "how are you": "I'm just a bot, but I'm doing well!",
            "what is your name": "My name is Bota.",
            "help": "I can greet you or say goodbye. Try saying 'hi' or 'bye'."
        }
        if user_input.lower() in responses:
            print(f"Bota: {responses[user_input.lower()]}")