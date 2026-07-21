import webbrowser
from knowledge_base import info, menu

# ======================== HELPER FUNCTIONS ======================== #
def browse(input_message, url):
    # Get user confirmation to open url in web browser
    bot_question = input(input_message).lower().strip()
    
    if bot_question == "yes":
        webbrowser.open(url)
        return "Browsing..."
    
    return "Sure"

def order_confirmation(food_item, item_url):
    return browse(f"\nBot: Shall I open {food_item} in {info["restaurant_name"]} website, so that you can order? (yes/no): ", item_url)


# ======================= BOT REPLY FUNCTION ======================= #

def reply(user_input):
    # Get a cleaned user input
    user_input = user_input.lower().strip() # lower() --> Covert string to lowercase  | strip() --> Remove spaces/tabs/newlines from strings

    # ------ Greeting ------ #
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello there!"
    
    # ------ Acknowledgement ------ #
    if "thank" in user_input:
        return "No worries! I'm always here to help you."
    
    # ------ Restaurant name / about ------ #
    if "restaurant name" in user_input:
        return f"{info["about_restaurant"]}!"
    
    # ------ Contact number ------ #
    if "contact" in user_input or "phone" in user_input or "hotline" in user_input:
        return f"Contact number - {info["hotline"]}"
    
    # ------ Email ------ #
    if "mail" in user_input:
        return f"Our email - {info["email"]}"
    
    # ------ Website ------ #
    if "website" in user_input:
        print(f"Bot: Our website - {info["website"]["name"]}")
        return browse("Bot: Shall I open the website for you? (yes/no): ", info["website"]["url"])
    
    # ------ App ------ #
    if "app" in user_input:
        return f"Our mobile app - {info["app"]}"
    
    # ------ Socials ------ #
    if "social" in user_input:
        reply = "Our social media\n"

        for social, link in info["socials"].items():
            reply += f"{social} - {link}\n"

        return reply
    
    # ------ Instagram ------ #
    if "instagram" in user_input:
        print(f"Bot: Our instagram - {info["socials"]["instagram"]}")
        return browse("Bot: Shall I open our instagram for you? (yes/no): ", info["socials"]["instagram"])
    
    # ------ Facebook ------ #
    if "facebook" in user_input:
        print(f"Bot: Our instagram - {info["socials"]["facebook"]}")
        return browse("Bot: Shall I open our facebook page for you? (yes/no): ", info["socials"]["facebook"])
    
    # ------ Branches ------ #
    if "branches" in user_input or any(branch in user_input for branch in info["branches"]):
        reply = "These are our branches information\n\n"

        for branch_info in info["branches"].values():
            reply += f"{branch_info["name"]}\nAddress - {branch_info["address"]}\nContact - {branch_info["contact"]}\n\n"

        return reply
    
    # ------ Menu item specific questions ------ #

    for food_item in menu:
        if food_item in user_input:
            item_url = f"https://bigplate.lk/menu/{food_item}".replace(" ", "-")

            # Price
            if "price" in user_input:
                print(f"Bot: The price of {food_item} is Rs.{menu[food_item]["price"]}")
                return order_confirmation(food_item, item_url)

            # Description
            elif "description" in user_input:
                print("Bot: ", menu[food_item]["description"])
                return order_confirmation(food_item, item_url)

            # Preparation time
            elif "how long" in user_input or "preparation time" in user_input or "time" in user_input:
                print(f"Bot: {food_item} takes only {menu[food_item]["time"]} minutes to prepare")
                return order_confirmation(food_item, item_url)

            # Vegetarian nature
            elif "vegetarian" in user_input:
                if menu[food_item]["vegetarian"] == True:
                    print(f"Bot: Yes. {food_item} is a vegetarian food item")

                else:
                    print(f"Bot: No. {food_item} is a gluten-free food item")

                return order_confirmation(food_item, item_url)

            # Ingredients
            elif "ingredients" in user_input:
                print(f"Bot: These are the ingredients we used to make {food_item}\n")

                for ingredient in menu[food_item]["ingredients"]:
                    print(ingredient)

                return order_confirmation(food_item, item_url)

            # Order food item
            elif "order" in user_input or "open" in user_input or "purchase" in user_input:
                webbrowser.open(item_url)
                return "Opening..."

            else:
                return "I understand that you're trying to ask me a question related to a menu item. Could you be specific about the question, so that I can give an accurate response."

    # ------ Menu Categories ------ #

    # Get all categories
    categories = set(item["category"] for item in menu.values())

    # Full menu
    if "full menu" in user_input:
        reply = "Full Menu\n"

        for category in categories:
            reply += f"{category.title()}:\n"

            for name, value in menu.items():
                if value["category"].lower() == category.lower():
                    reply += f"- {name.title()} - Rs.{value['price']}\n"

            reply += "\n"

        return reply


    # Menu filter based on food categories
    for category in categories:
        if "menu" in user_input and category.lower() in user_input:
            reply = f"{category.title()} Menu\n"

            for food_item, details in menu.items():
                if details["category"].lower() == category.lower():
                    reply += f"- {food_item.title()} - Rs.{details['price']}\n"

            return reply
            
    # ------ Fallback ------ #
    return "Sorry! I did not understand. Could you rephrase your question?"


# ========================== MAIN PROGRAM ========================== #

def main():
    # Welcome messages
    print("=============================================")
    print(f"Welcome to the {info["restaurant_name"]} Chatbot")
    print("=============================================")
    print("""
    I can help you with:

    Restaurant Information (Name/Contact/Email/Website/Socials/Branches)
    e.g. Show me your instagram page
            
    Menu Items & Specific Questions (Price/Description/Ingredients/Preparation Time/Is Vegetarian/Category)
    e.g. What are the ingredients in chilli paneer?
            
    Menus Based On Food Categories (Vegetarian/Starter/Soup/Sandwich/Rice/Noodles/Kottu/Burger/Submarine/Biriyani/Drinks/Deserts)
    e.g. I want to view the full menu
    e.g. Show me your kottu menu
            
    Online Ordering
    e.g. I want to order a chicken submarine
    """)
    print("=============================================")

    # Chat loop
    while True:
        # Get User input
        user_input = input("You: ")

        # Exit command
        if user_input in ["exit", "bye", "quit"]:
            print("Bye... See you again!")
            break

        # Bot reply
        response = reply(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()