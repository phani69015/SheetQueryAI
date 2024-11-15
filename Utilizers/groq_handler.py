import os
from groq import Groq
from Utilizers.config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)

def extract_with_groq(prompt, search_results_text):
    messages = [
        {
            "role": "user",
            "content": f"Only provide direct responses based on prompt, no extra language. warning: Dont add extra grammer. Context:\n{search_results_text}\nPrompt:\n{prompt}"
        }
    ]
    
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192"   
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return {"error": f"Failed to extract information with Groq AI: {str(e)}"}
