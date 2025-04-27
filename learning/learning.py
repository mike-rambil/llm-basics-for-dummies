# learning.py

knowledge = []

def learn_from_input(user_input):
    knowledge.append(user_input)

def generate_response():
    if knowledge:
        return f"I remember: {knowledge[-1]}"
    else:
        return "Tell me something!" 