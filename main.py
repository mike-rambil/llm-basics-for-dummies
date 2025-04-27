# main.py

from chat.chat import get_user_input, display_bot_response
from learning.learning import learn_from_input, generate_response
from memory.memory import save_message

print("Welcome to the Basic LLM Chat AI Bot!")

while True:
    user_input = get_user_input()
    if user_input.lower() in ("exit", "quit"):  # Allow user to exit
        print("Goodbye!")
        break
    save_message('user', user_input)
    learn_from_input(user_input)
    response = generate_response()
    save_message('bot', response)
    display_bot_response(response) 