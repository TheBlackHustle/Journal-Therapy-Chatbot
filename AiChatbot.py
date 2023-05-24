import os
import time
from getpass import getpass
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

os.environ["OPENAI_API_KEY"] = ""

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

llm = OpenAI(model_name="gpt-4", temperature=0.3, openai_api_key="")
prompt = PromptTemplate(
    input_variables=["user_query"],
    template="Create a set of keywords based on the user query: '{user_query}' to perform a search on the journal dataset in Chroma DB.",
)

chain = LLMChain(llm=llm, prompt=prompt)

userinput = input("Hey im a journl help bot, how can i help you today? ")

# Run the chain only specifying the input variable.
keywords = chain.run(userinput)

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
    llm=OpenAI(model_name="gpt-4", temperature=0.8, openai_api_key=""),
    prompt=prompt,
    verbose=False,
    memory=memory,
)

answer = llm_chain.predict(user_msg=f"{full_result_string} ---\n\n {userinput}")
print("Bot:", answer)

while True:
    follow_up = input("Anything else you want to ask about this topic? (type 'quit' to stop) ")
    print

