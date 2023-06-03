**
 * [Journal Therapy Chatbot]
 * [This project implements a journal therapy chatbot powered by artificial intelligence (AI). 
 *The chatbot utilizes the Chroma vector database for analyzing and processing journal entries to provide 
 *feedback and advice based on user queries.]
 *
 * Copyright [2023] [Devin Jackson]
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */


import os
from getpass import getpass
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from flask import Flask, request, jsonify

app = Flask(__name__)

# Specify the folder containing your journal entries
folder_path = '/Users/devinjackson/Documents/PycharmProjects/Journal Project/Entries/'

# Get a list of all text files in the folder
file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.txt')]

# Initialize an empty list to hold all documents
documents = []

# Load each file into the documents list
for file_path in file_paths:
    loader = TextLoader(file_path)
    documents += loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(docs, embeddings)

llm = OpenAI(model_name="gpt-4", temperature=0.3, openai_api_key="...")
prompt = PromptTemplate(
    input_variables=["user_query"],
    template="Create a set of keywords based on the user query: '{user_query}' to perform a search on the journal dataset in Chroma DB.",
)

chain = LLMChain(llm=llm, prompt=prompt)

@app.route("/chat", methods=["POST"])
def chat_handler():
    user_input = request.json["user_input"]

    # Run the chain only specifying the input variable.
    keywords = chain.run(user_input)

    # Convert keywords to string, assuming keywords is a list of words
    keywords_str = " ".join(keywords)

    # Query Chroma DB
    docs = db.similarity_search(keywords_str, k=1)

    # Process the documents
    full_result_string = "\n".join([doc.page_content for doc in docs])

    template = """You are a chatbot. Be kind, detailed and nice. Present the given queried search result in a nice way as answer to the user input. dont ask questions back! just take the given context

    {chat_history}
    Human: {user_msg}
    Chatbot:"""

    prompt = PromptTemplate(
        input_variables=["chat_history", "user_msg"],
        template=template
    )

    memory = ConversationBufferMemory(memory_key="chat_history")
    llm_chain = LLMChain(
        llm=OpenAI(model_name="gpt-4", temperature=0.8, openai_api_key="..."),
        prompt=prompt,
        verbose=False,
        memory=memory,
    )

    answer = llm_chain.predict(user_msg=f"{full_result_string} ---\n\n {user_input}")

    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

 
