# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:34:56 2024

@author: shikh
"""

import google.generativeai as genai
import os

# Set the API key for Google Generative AI
os.environ["API_KEY"] =" " # "= Add your API key here to get the output"
genai.configure(api_key =os.environ["API_KEY"])

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")
  
def chatbot():
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    conversation_summary = ""  # To keep track of conversation context

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Conversation Eneded. Have a good day!")
            break

        # Combine conversation summary with user input for context
        prompt = f"{conversation_summary} {user_input}"

        # Generate response from Gemini model
        responses = model.generate_content(prompt)

        if responses and responses.candidates:
            response = responses.candidates[0].content.parts[0].text
            print(f"Gemini: {response}")

            # Update the conversation summary
            summary_prompt = f"Summarize the conversation so far: {prompt} {response}"
            summary_response = model.generate_content(summary_prompt)
            if summary_response and summary_response.candidates:
                conversation_summary = summary_response.candidates[0].content.parts[0].text
            # print(f"[Summary for Next Prompt]: {conversation_summary}\n")

if __name__ == "__main__":
    chatbot()
