import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

from google import genai

client = genai.Client(api_key=api_key)

def main():
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    )
    print(response.text)

    X = response.usage_metadata.prompt_token_count
    Y = response.usage_metadata.candidates_token_count

    print(f"Prompt tokens: {X}")
    print(f"\nResponse tokens: {Y}")    

if __name__ == "__main__":
    tokens = main()
    