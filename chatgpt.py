from dotenv import load_dotenv

import openai 
import os

load_dotenv()

openai.api_key = os.getenv('API_KEY')


while True:
    
    libroPrompt = input("\nIntroduce un libro: ")
    
    prompt = "Hazme un resumen en 10 viñetas del libro " + libroPrompt 
    
    
    if prompt == "exit":
        break
    
    completion = openai.Completion.create(engine="text-davinci-003",
                            prompt=prompt,
                            max_tokens=2048)

    print(completion.choices[0].text)