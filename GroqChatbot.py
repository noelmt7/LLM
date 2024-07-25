import os
from groq import Groq


api_key = "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"
client = Groq(api_key=api_key)

# Function to send a message to the chatbot and receive a response
def get_chat_response(client, user_message):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="llama3-8b-8192", 
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stop=None,
    )
    return chat_completion.choices[0].message.content

# Main chatbot loop
def chatbot():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_message = input("You: ")
        if user_message.lower() == 'exit':
            print("Goodbye!")
            break
        response = get_chat_response(client, user_message)
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()
