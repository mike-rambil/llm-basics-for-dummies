# chat

Handles chat input/output logic for the LLM bot.

- Receives user input
- Displays bot responses
- Interfaces with the learning and memory modules

This directory contains the code responsible for interacting with the user.

## New Feature: Next-Word Prediction Command

- Users can now type `predict: your-word` to ask the bot to predict the next word after `your-word` based on chat history.
- The chat module passes this command to the learning module and displays the prediction result.
