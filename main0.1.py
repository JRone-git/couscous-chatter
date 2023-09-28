import json
from difflib import get_close_matches
from typing import List

# Load knowledge base from a file
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, "r") as file:
        return json.load(file)

# Save knowledge base to a file
def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=2)

# Find the best match for a user question
def find_best_match(user_question: str, questions: List[str]) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

# Get an answer for a question from the knowledge base
def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]

# Main chat bot function
def chat_bot():
    knowledge_base = load_knowledge_base("knowledge_base.json")
    while True:
        user_question = input("You: ")
        if user_question.lower() == "quit":
            break
        best_match = find_best_match(user_question, [q["question"] for q in knowledge_base["questions"]])
        if best_match:
            answer = get_answer_for_question(best_match, knowledge_base)
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answer to that question")
            new_answer = input('Type the answer or "skip" to skip: ')
            if new_answer.lower() != "skip":
                knowledge_base["questions"].append(
                    {"question": user_question, "answer": new_answer}
                )
                save_knowledge_base("knowledge_base.json", knowledge_base)
                print("Bot: Thank you for your question. I will remember it and try to answer it in the future")

if __name__ == "__main__":
    chat_bot()
