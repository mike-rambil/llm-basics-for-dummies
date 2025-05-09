# Basic LLM Chat AI Bot

**Author:** Micheal Palliparambil

---

## About This Project

This project is my attempt (Micheal Palliparambil) to learn and gain a deeper understanding of AI by building a simple LLM chat bot from scratch, using only pure Python. Each function or logic is separated into its own directory for clarity and learning.

---

## How to Learn from This Project

- **Explore Each Directory:** Each core logic (chat, learning, memory, etc.) is in its own directory with a README explaining its purpose and code.
- **No External Dependencies:** All code is pure Python, so you can run and modify it easily.
- **Incremental Learning:** The bot learns from every message you send, showing how simple learning mechanisms work.
- **Roadmap:** See `ROADMAP.md` for progress and future plans.

---

## Directory Navigation

- `chat/` - Handles chat input/output logic.
- `learning/` - Contains the learning mechanism for the bot.
- `memory/` - Stores and retrieves conversation history.
- `main.py` - Entry point to run the chat bot.

Each directory has its own README for detailed explanations.

---

## Getting Started

1. Clone the repository.
2. Run `python main.py` to start chatting with the bot.
3. To predict the next word after any word, type `predict: your-word` in the chat and the bot will respond with its prediction.
4. Explore the code and directories to understand each part.

---

## Why This Project?

This is a hands-on way to understand the basics of AI, LLMs, and how simple learning can be implemented. By separating logic, you can focus on one concept at a time and build your understanding step by step.

## New: Next-Word Prediction (Bigram Model)

- The bot now supports next-word prediction using a simple bigram model built from all previous chat history.
- To use this feature, type `predict: your-word` in the chat. The bot will respond with the most likely next word based on all previous messages.
- Example:
  - You: hello world
  - You: hello mom
  - You: predict: hello
  - Bot: Prediction for 'hello': world

## Architecture Overview

- All logic is modularized: chat (I/O), learning (model), memory (history).
- The learning module now includes a bigram-based prediction function (`predict_next_word`).
- The bot learns from every message and predictions are based on the entire chat history, not just the last message.
