import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

GROQ_API_KEY = os.getenv("GROQAPI_KEY")

if GROQ_API_KEY:
    print("GROQ_API_KEY loaded successfully.")
else:
    print("GROQ_API_KEY is not set.")

def extract_with_groq(prompt, search_results_text):
    client = Groq(api_key=GROQ_API_KEY)
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
