import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load environment variables
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7,
    groq_api_key=groq_api_key
)

# Embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

# Vector store
vectorstore = FAISS.from_texts(
    ["Start of conversation."],
    embedding=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Prompt
prompt = ChatPromptTemplate.from_template("""
You are a helpful AI assistant.

Relevant past memory:
{history}

User: {input}

AI:
""")

chain = prompt | llm | StrOutputParser()

print("Memory Agent Started (type 'exit' to stop)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    docs = retriever.invoke(user_input)
    history = "\n".join([doc.page_content for doc in docs])

    response = chain.invoke({
        "history": history,
        "input": user_input
    })

    print("AI:", response)

    # Save memory
    vectorstore.add_texts([f"User: {user_input}\nAI: {response}"])

    # Refresh retriever
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})