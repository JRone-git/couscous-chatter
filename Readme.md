Report: Chat Bot

Introduction:
The Chat Bot is a simple conversational agent that interacts with users by answering questions. It allows users to ask questions, and if it knows the answer, it responds with the relevant information. If it doesn't have the answer, it prompts the user to provide the answer and stores it for future reference. This report provides an overview of the chat bot's functionality and the requirements to run it.

Functionality:
The Chat Bot has the following key functionalities:

Loading Knowledge Base: It can load a knowledge base from a JSON file, which contains a collection of questions and their corresponding answers.

Saving Knowledge Base: It can save the knowledge base, including any newly added questions and answers, back to the JSON file.

Finding Best Match: It uses the difflib library to find the best matching question in the knowledge base for a user's input. If a close match is found, it provides the answer. If not, it prompts the user to provide the answer.

User Interaction: The bot interacts with the user through a simple command-line interface. Users can input questions and receive responses from the bot.

Usage:
To run the Chat Bot, follow these steps:

Ensure you have Python installed on your system (Python 3.x is recommended).

Install the required dependencies by running the following commands:

pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip install -r requirements.txt

Create a knowledge base JSON file named "knowledge_base.json" and populate it with initial questions and answers (if any).

Run the chat bot using the following command:

python chat_bot.py
Interact with the bot by typing questions or entering "quit" to exit the chat."# couscous-chatter" 
"# couscous-chatter" 
