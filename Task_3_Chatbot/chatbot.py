import json
import re
from pathlib import Path


BASE_DIR = Path(__file__).parent
FAQ_FILE = BASE_DIR / "sample_faq.json"


def load_faq():
    """Load chatbot data from the JSON file."""
    try:
        with open(FAQ_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Error: sample_faq.json was not found.")
        return {}

    except json.JSONDecodeError:
        print("Error: Invalid JSON file.")
        return {}


def normalize_text(text):
    """Normalize text for easier matching."""
    return re.sub(r"\s+", " ", text.lower().strip())


def get_response(user_input, data):
    """Generate a response based on user input."""
    message = normalize_text(user_input)

    if not message:
        return "Please enter a message."

    
    if re.search(r"\b(bye|exit|quit)\b", message):
        return "Goodbye! Have a great day!"

    
    greetings = data.get("greetings", [])

    for greeting in greetings:
        pattern = r"\b" + re.escape(normalize_text(greeting)) + r"\b"

        if re.search(pattern, message):
            return "Hello! Welcome. How can I help you today?"

    faqs = data.get("faqs", [])

    for faq in faqs:
        question = normalize_text(faq.get("question", ""))
        keywords = re.findall(r"\b\w+\b", question)

        for keyword in keywords:
            if len(keyword) > 3 and re.search(
                r"\b" + re.escape(keyword) + r"\b",
                message
            ):
                return faq.get("answer", "Sorry, no answer available.")

    
    return (
        "I'm sorry, I don't understand your question. "
        "Could you please rephrase it?"
    )


def main():
    """Run the interactive terminal chatbot."""
    data = load_faq()

    if not data:
        print("Chatbot cannot start without FAQ data.")
        return

    print("=" * 45)
    print("       RULE-BASED CHATBOT ASSISTANT")
    print("=" * 45)
    print("Hello! I am your virtual assistant.")
    print("Ask me a question or type 'bye' to exit.")

    while True:
        user_input = input("\nYou: ")
        response = get_response(user_input, data)

        print("Chatbot:", response)

        if re.search(
            r"\b(bye|exit|quit)\b",
            normalize_text(user_input)
        ):
            break


if __name__ == "__main__":
    main()