responses = {
    "hi": "Hello there!",
    "bye": "Bye... See you again!"
}

# ======================= MAIN PROGRAM ======================= #

# Greeting messages
print("========================================")
print("Welcome to the Chatbot")
print("========================================")
print()
print("Enter 'Exit' to exit")
print()

# Chat loop
while True:
    # Get a cleaned user input
    user_input = input("You: ").lower().strip() # lower() --> Covert string to lowercase  | strip() --> Remove spaces/tabs/newlines from strings

    # Exit command
    if user_input == "exit":
        break
    
    # Bot reply
    reply = responses.get(user_input, "Sorry! I did not understand. Could you rephrase your question please?")
    print("Bot: ", reply)