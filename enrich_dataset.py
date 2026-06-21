import json
import os
import time
import google.generativeai as genai

# Setup your API Key here
API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE")
genai.configure(api_key=API_KEY)

# Use the appropriate Gemini model
model = genai.GenerativeModel('gemini-flash-lite-latest')

file_path = r"d:\TamilVerse-Dataset\data\proverbs\tamil_proverbs.json"

def enrich_batch(records):
    prompt = """
You are an expert Tamil linguist, Tamil literature scholar, and NLP dataset annotator.
Enrich the given JSON records of proverbs by filling in the missing fields:
- transliteration
- simpleTamilMeaning
- moral
- category

Rules:
1. NEVER modify existing fields.
2. Use simple, modern, grammatically correct Tamil.
3. Output ONLY valid JSON array with the enriched records.
4. Maintain the same ID and record order.
5. Do not add comments or markdown formatting like ```json.

Records to enrich:
""" + json.dumps(records, ensure_ascii=False, indent=2)

    try:
        response = model.generate_content(prompt)
        # Parse the JSON from the response
        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
        
        enriched_records = json.loads(text.strip())
        return enriched_records
    except Exception as e:
        print(f"Error enriching batch: {e}")
        return None

def main():
    print("Loading dataset...")
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    print(f"Total records: {len(data)}")

    # Find records that are missing simpleTamilMeaning
    records_to_process = [r for r in data if not r.get("simpleTamilMeaning")]
    print(f"Records left to process: {len(records_to_process)}")

    batch_size = 5 # Process in small batches to ensure output quality
    
    i = 0
    while i < len(records_to_process):
        batch = records_to_process[i:i+batch_size]
        print(f"Processing batch {i//batch_size + 1}...")
        
        enriched_batch = enrich_batch(batch)
        
        if enriched_batch and len(enriched_batch) == len(batch):
            # Update the original dataset
            for enriched_record in enriched_batch:
                for j, original_record in enumerate(data):
                    if original_record["id"] == enriched_record["id"]:
                        data[j] = enriched_record
                        break
            
            # Save progress after each successful batch
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                
            print(f"Saved batch {i//batch_size + 1}.")
            i += batch_size # move to next batch only on success
            time.sleep(2)
        else:
            print(f"Failed to process batch {i//batch_size + 1}. Quota exceeded or error. Waiting 60 seconds before retrying...")
            time.sleep(60) # wait a minute and try the same batch again

    print("Enrichment complete.")

if __name__ == "__main__":
    main()
