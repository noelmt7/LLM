import os
from groq import Groq

api_key = "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"
client = Groq(api_key=api_key)

# Function to send a message to the chatbot and receive a response.
def get_chat_response(client, messages):
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192", #the model uses llama3-8b-8192 as its base
        temperature=1, # default temperature 
        max_tokens=2048, # the max tokens has been increased to 2048 tokens which provides more detailed tokens 
        top_p=1, # default p value
        stop=None,
    )
    return chat_completion.choices[0].message.content

# Main chatbot loop with context and memory
def chatbot():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    messages = []
    memory = {}
    
    while True:
        user_message = input("You: ")
        if user_message.lower() == 'exit': # the user can exit the chatbot by typing 'exit'
            print("Goodbye!")
            break
        
        
        messages.append({"role": "user", "content": user_message})
        
        #teaching the bot the users name and remembering the users name
        if "my name is" in user_message.lower():
            name = user_message.split("my name is")[-1].strip()
            memory["name"] = name # storing the users name in the memory
            response = f"Nice to meet you, {name}!"
        
        #bot has the ability to remember inputs from the user and recall them later
        elif "remember" in user_message.lower():
            key_value = user_message.split("remember")[-1].strip().split(" as ")
            if len(key_value) == 2:
                key, value = key_value
                memory[key.strip()] = value.strip()
                response = f"Got it! I'll remember that {key.strip()} is {value.strip()}."
            else:
                response = "I didn't quite catch that. Could you please clarify?"
            
        # fetching the users name and pther information from the memory
        elif "what is" in user_message.lower() and any(mem_key in user_message.lower() for mem_key in memory):
            mem_key = next(mem_key for mem_key in memory if mem_key in user_message.lower())
            response = f"{mem_key} is {memory[mem_key]}."
        else:
            try:
                # Get chatbot response
                response = get_chat_response(client, messages)
                messages.append({"role": "assistant", "content": response})
            except Exception as e:
                response = f"An error occurred: {str(e)}"
        
        print("Bot:", response)

if __name__ == "__main__":
    chatbot()
