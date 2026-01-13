🧠 Gemini Memory Chatbot (Console)

A memory-augmented conversational AI chatbot built using Google’s Gemini 1.5 Flash model.
This project demonstrates how to simulate long-term conversational memory using LLM-based recursive summarization, allowing the chatbot to retain context across multiple turns in a console environment.

🚀 What This Project Does

Unlike a basic prompt-response chatbot, this system:

Maintains conversation memory

Compresses past dialogue into a rolling summary

Feeds that summary back into every new model prompt

Allows Gemini to reason over prior context

This creates the illusion of a persistent, intelligent assistant that “remembers” what was said earlier.

🧩 Architecture
User Input
   ↓
Conversation Summary (Memory)
   ↓
Prompt = [Memory + New Message]
   ↓
Gemini 1.5 Flash
   ↓
Response
   ↓
Update Memory via LLM Summarization
   ↺ (loop)


This design mimics how production AI systems (ChatGPT, Claude, Copilot) maintain conversational context under token limits.

🧠 Key Features

Persistent Memory
Uses Gemini to summarize the entire conversation after every turn, allowing unlimited chat length.

Context Injection
The chatbot prepends memory to every prompt so responses remain relevant.

Stateless API → Stateful Agent
Converts Gemini’s stateless API into a stateful conversational agent.

Console Interface
Simple, fast, and ideal for experimentation and learning.

🛠️ Tech Stack

Model: Gemini 1.5 Flash

Language: Python

SDK: Google Generative AI Python SDK

📦 Installation
pip install google-generativeai

🔑 Setup

Set your Gemini API key:

os.environ["API_KEY"] = "YOUR_GEMINI_API_KEY"


Or export it in your shell:

export API_KEY="YOUR_GEMINI_API_KEY"

▶️ Run the Chatbot
python chatbot.py


Type your messages and type exit to quit.

🧠 Example
You: My name is Shikhar
Gemini: Nice to meet you, Shikhar!

You: What is my name?
Gemini: Your name is Shikhar.


This works because the chatbot remembers via summarization.

🧪 Why This Matters

This project demonstrates:

How LLMs can be given memory

How to build RAG-style conversational agents

How to overcome context window limits

How modern AI assistants work internally

This is a foundation for:

AI agents

Customer support bots

Research assistants

Chat-based applications

⚠️ Limitations

This implementation uses recursive summarization, which may:

Lose fine details over very long conversations

Drift slightly over time

Production systems typically replace this with:

Vector databases (FAISS, Pinecone, Chroma)

Semantic retrieval (RAG)

🌱 Future Enhancements

Vector memory store (FAISS / Chroma)

Retrieval-augmented generation (RAG)

Web or API interface

Multi-session user memory

👨‍💻 Author

Shikhar Kapoor
AI Engineer | Data Scientist | Systems Builder
