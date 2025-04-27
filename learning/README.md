# learning

Contains the learning mechanism for the LLM bot.

- Updates the bot's knowledge based on user input
- Tries to improve responses with each interaction

This directory contains code for the bot's simple learning logic.

## Bigram-Based Next-Word Prediction

- The learning module now includes a bigram model that predicts the most likely next word after a given word, based on all previous user and bot messages.
- API: `predict_next_word(word)`
  - Returns the most frequent next word after `word` in the chat history, or `None` if not found.
- This model is used when you type `predict: your-word` in the chat interface.
- The model updates in real time as new messages are added to the conversation.
