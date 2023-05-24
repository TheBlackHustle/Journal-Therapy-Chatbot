# Journal-Therapy-Chatbot
This project implements a journal therapy chatbot powered by artificial intelligence (AI). The chatbot utilizes the Chroma vector database for analyzing and processing journal entries to provide feedback and advice based on user queries.

AiChatbot.py is the file containing the Vector DB and chatbot.
JournalWriter.Py is the script to write all the journals


# Features
User Input: The chatbot prompts the user for input, allowing them to express their thoughts, feelings, or concerns.
Keyword Extraction: Using natural language processing techniques, the chatbot extracts keywords from the user's input to understand the context.
Chroma Vector Database: The chatbot leverages a Chroma vector database to perform similarity searches and retrieve relevant journal entries based on the extracted keywords.
Response Generation: Based on the retrieved journal entries and the user's input, the chatbot generates thoughtful and helpful responses to provide feedback, guidance, and support.
Conversational Memory: The chatbot employs a memory system to maintain the conversation history, allowing for a more coherent and context-aware interaction.
# How to Use
Setup:

Install the required dependencies and libraries.
Set the OpenAI API key as an environment variable.
Specify the folder containing the journal entries to be used for the database.
Running the Chatbot:

Start the program and follow the prompts.
Input your thoughts, feelings, or any queries you have.
The chatbot will process your input, extract keywords, and retrieve relevant journal entries from the database.
It will then generate thoughtful responses based on the retrieved content and your input, providing feedback and advice.
Requirements
Python [version]
Dependencies (list the key dependencies used in the project)
# License
This project is licensed under the Apache License 2.0. See the LICENSE file for more details.

# Contributing
Contributions are welcome! If you would like to contribute to this project, please follow the guidelines outlined in CONTRIBUTING.

# Acknowledgments
- The langchain library: Used for text splitting, embeddings, and vector storage.
- OpenAI: Provided the language models and API for natural language processing.
- Chroma Vector Database: Used for storing and retrieving journal entries based on similarity.
- getpass: Used for securely getting user input.


Feel free to modify the description as per your requirements, adding more details or adjusting it to accurately represent your project.
