import google.generativeai as genai
import os
lines = open('enrich_dataset.py').readlines()
key = [l.split('"')[1] for l in lines if 'API_KEY = ' in l and 'os.environ' not in l]
if key:
    genai.configure(api_key=key[0])
else:
    print("NO KEY")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
