import json
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class ChatBot:
    def __init__(self, knowledge_base):
        self.knowledge_base = knowledge_base
        self.glove_vectors = {}

    def advanced_nlp_processing(self, user_question):
        # Placeholder code for GloVe processing

        # Initialize the word vectors variable to an empty list
        word_vectors = []

        # Check if the user question is a string before calling the split() method.
        # This is necessary because dictionaries do not have a split() method.
        if isinstance(user_question, str):
            tokens = user_question.split()

            for token in tokens:
                if token in self.glove_vectors:
                    word_vector = self.glove_vectors[token]
                    word_vectors.append(word_vector)

        # Check if the word vectors variable is empty
        if not word_vectors:
            return None

        # Calculate the average vector by summing vectors element-wise and dividing by the number of vectors
        average_vector = np.sum(word_vectors, axis=0) / len(word_vectors)

        # Reshape the average vector to a 2D array before passing it to the cosine_similarity() function
        average_vector = average_vector.reshape(1, -1)

        return average_vector   

    
    
    def load_glove_vectors(self, glove_file):
        print("Loading GloVe vectors...")
        try:
            word_vectors = {}
            with open(glove_file, "r", encoding="utf-8") as file:
                for line in file:
                    values = line.split()
                    word = values[0]
                    vector = [float(val) for val in values[1:]]
                    word_vectors[word] = vector

            print(f"Loaded {len(word_vectors)} word vectors.")
            self.glove_vectors = word_vectors
        except Exception as e:
            print(f"An error occurred while loading GloVe vectors: {str(e)}")

    def find_best_match(self, user_question, question_index):
        # Check if the advanced_nlp_processing() function returned None
        advanced_nlp_processing_result = self.advanced_nlp_processing(user_question)
        if advanced_nlp_processing_result is None:
            return None

        # Calculate the cosine similarity between the user's input vector and the question vector
        similarity = cosine_similarity(
            advanced_nlp_processing_result.reshape(1, -1),
            np.array(self.knowledge_base["questions"][question_index]).reshape(1, -1),
            dtype=float
        )[0][0]

        # Check if the similarity exceeds the threshold
        if similarity > self.threshold:
            return self.knowledge_base["questions"][question_index]
        else:
            return None
                
        knowledge_base = {
            "questions": ["hi", "how are you?", "what is your name?"],
            "answers": {
                "hi": "Hello!",
                "how are you?": "I'm doing well, thanks for asking!",
                "what is your name?": "My name is Bard."}
            }

best_match = bot.find_best_match("hi", 0)

if best_match is not None:
    print(f"Bot: {bot.get_answer_for_question(best_match)}")
else:
    print("Bot: I don't understand your question.")




    def get_answer_for_question(self, question):
        """Returns the answer for the given question."""

        answer = self.knowledge_base["answers"][question]
        return answer

    def chat(self):
        print("Bot: Hi! I'm your chatbot. Type 'quit' to exit.")
        while True:
            user_question = input("You: ")
            if user_question.lower() == "quit":
                break

            # Try to find the question with the given index in the knowledge base.
            try:
                best_match_index = self.knowledge_base["questions"].index(user_question)
            except ValueError:
                # If the question is not found, set the best match index to -1.
                best_match_index = -1

            best_match = self.find_best_match(user_question, best_match_index)
            if best_match is not None:
                print(f"Bot: {self.get_answer_for_question(best_match)}")
            else:
                print("Bot: I don't understand your question.")

if __name__ == "__main__":
    knowledge_base = {
        "questions": ["hi", "how are you?", "what is your name?"],
        "answers": {
            "hi": "Hello!",
            "how are you?": "I'm doing well, thanks for asking!",
            "what is your name?": "My name is Bard."
        }
    }

    bot = ChatBot(knowledge_base)
    bot.load_glove_vectors("glove.6B.50d.txt")

    bot.chat()
