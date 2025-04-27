# memory

Stores and retrieves conversation history for the LLM bot.

- Saves user and bot messages
- Provides context for learning and responses

This directory contains code for managing the bot's memory.

## Role in Prediction

- The memory module ensures all user and bot messages are stored, providing the full chat history needed for the bigram-based next-word prediction in the learning module.
