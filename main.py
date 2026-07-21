import webbrowser
from knowledge_base import info

# ======================== HELPER FUNCTIONS ======================== #
def browse(input_message, url):
    # Get user confirmation to open url in web browser
    bot_question = input(input_message).lower().strip()
    
    if bot_question == "yes":
        webbrowser.open(url)
        return "Browsing..."
    
    return "Sure"

# ======================= BOT REPLY FUNCTION ======================= #

def reply(user_input):
    # Get a cleaned user input
    user_input = user_input.lower().strip() # lower() --> Covert string to lowercase  | strip() --> Remove spaces/tabs/newlines from strings

    # Exit
    if user_input in ["exit", "bye", "quit"]:
        return "Bye... See you again!"

    # Greeting
    if user_input in ["hi", "hello", "hello there", "hey"]:
        return "Hello there!"
    
    # Acknowledgement
    if "thank" in user_input:
        return "No worries! I'm always here to help you."
    
    # Restaurant name / about
    if "restaurant name" in user_input:
        return f"{info["about_restaurant"]}!"
    
    # Contact number
    if "contact" in user_input or "phone" in user_input or "hotline" in user_input:
        return f"Contact number - {info["hotline"]}"
    
    # Email
    if "mail" in user_input:
        return f"Our email - {info["email"]}"
    
    # Website
    if "website" in user_input:
        print(f"Bot: Our website - {info["website"]["name"]}")
        return browse("Bot: Shall I open the website for you? (yes/no): ", info["website"]["url"])
    
    # App
    if "app" in user_input:
        return f"Our mobile app - {info["app"]}"
    
    # Socials
    if "social" in user_input:
        reply = "Our social media\n"

        for social, link in info["socials"].items():
            reply += f"{social} - {link}\n"

        return reply
    
    # Instagram
    if "instagram" in user_input:
        print(f"Bot: Our instagram - {info["socials"]["instagram"]}")
        return browse("Bot: Shall I open our instagram for you? (yes/no): ", info["socials"]["instagram"])
    
    # Facebook
    if "facebook" in user_input:
        print(f"Bot: Our instagram - {info["socials"]["facebook"]}")
        return browse("Bot: Shall I open our facebook page for you? (yes/no): ", info["socials"]["facebook"])
    
    # Branches
    if "branches" in user_input or any(branch in user_input for branch in info["branches"]):
        reply = "These are our branches information\n\n"

        for branch_info in info["branches"].values():
            reply += f"{branch_info["name"]}\nAddress - {branch_info["address"]}\nContact - {branch_info["contact"]}\n\n"

        return reply

    # Fallback 
    else:
        return "Sorry! I did not understand. Could you rephrase your question?"


# ========================== MAIN PROGRAM ========================== #

# Greeting messages
print("========================================")
print("Welcome to the Chatbot")
print("========================================")
print()
print("Enter 'Exit' to exit")
print()

# Chat loop
while True:
    # User input
    user_input = input("You: ")

    # Bot reply
    print("Bot: ", reply(user_input))