
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""
    
def greet_user(name):
    print(f"Hello, {name}, how are you?")
    
user_name = input("Please input your name: ")

user_age = int(input("Please input your age: "))

greet_user(user_name)
