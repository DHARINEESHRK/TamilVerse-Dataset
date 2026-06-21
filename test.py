import google.generativeai as genai
import os

key = "YOUR_API_KEY_HERE"
genai.configure(api_key=key)

try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print("Model:", m.name)
except Exception as e:
    print("Error:", e)
