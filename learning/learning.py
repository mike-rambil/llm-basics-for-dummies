# learning.py

knowledge = []

def learn_from_input(user_input):
    knowledge.append(user_input)

def generate_response():
    if knowledge:
        return f"I remember: {knowledge[-1]}"
    else:
        return "Tell me something!"

def predict_next_word(word):
    # Build bigram counts from knowledge
    bigrams = {}
    for sentence in knowledge:
        tokens = sentence.strip().split()
        for i in range(len(tokens) - 1):
            if tokens[i] == word:
                next_word = tokens[i+1]
                bigrams[next_word] = bigrams.get(next_word, 0) + 1
    if not bigrams:
        return None
    # Return the most frequent next word
    return max(bigrams, key=bigrams.get) 