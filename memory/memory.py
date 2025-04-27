# memory.py

conversation_history = []

def save_message(sender, message):
    conversation_history.append((sender, message))

def get_history():
    return conversation_history 