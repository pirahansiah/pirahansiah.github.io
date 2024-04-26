# new version of libraries April 2024

import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import DocArrayInMemorySearch
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.output_parsers import RetryOutputParser

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the model with the API key
model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")

# Load documents from a text file
loader = TextLoader("/Users/farshid/Library/CloudStorage/OneDrive-Personal/Personal/9_Reference/farshid/cc.txt")
text_documents = loader.load()

# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
documents = text_splitter.split_documents(text_documents)

# Embed the documents using OpenAI embeddings
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectorstore = DocArrayInMemorySearch.from_documents(documents, embeddings)

# Construct the query chain
retriever = vectorstore.as_retriever(search_quality_reflection=True)
qa_chain = RetrievalQA.from_chain_type(
    model.combine_with_llm,
    chain_type="stuff",
    retriever=retriever,
    output_parser=RetryOutputParser.from_retriever(retriever),
)

# Invoke the chain with a query
response = qa_chain.run("What is camera calibration optimization?")
print(response)



################ 2023


# import os
# from dotenv import load_dotenv
# from langchain_openai.chat_models import ChatOpenAI
# from langchain_community.document_loaders import TextLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_community.vectorstores import DocArrayInMemorySearch
# from langchain_openai.embeddings import OpenAIEmbeddings
# from langchain_core.runnables import RunnableParallel, RunnablePassthrough

# Load environment variables
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# # Initialize the model with the API key
# model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")

# # Load documents from a text file
# loader = TextLoader("/Users/farshid/Library/CloudStorage/OneDrive-Personal/Personal/9_Reference/farshid/cc.txt")
# text_documents = loader.load()

# # Split the documents into chunks
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=10)
# documents = text_splitter.split_documents(text_documents)

# # Embed the documents using OpenAI embeddings
# embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
# vectorstore = DocArrayInMemorySearch.from_documents(documents, embeddings)

# # Construct the query chain
# # chain = (
# #     {"context": vectorstore.as_retriever(), "question": RunnablePassthrough()}
# #     | model
# # )

# from operator import itemgetter
# from langchain.output_parsers import JsonOutputKeyToolsParser
# from langchain_core.runnables import Runnable, RunnableLambda, RunnablePassthrough
# chain = (
#     model
#     | JsonOutputKeyToolsParser(key_name="context", return_single=True)
#     | "context": vectorstore.as_retriever()
# )

# # Invoke the chain with a query
# response = chain.invoke("What is camera calibration optimization?")
# print(response)



# import os
# from dotenv import load_dotenv

# load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# from langchain_openai.chat_models import ChatOpenAI

# model = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-3.5-turbo")
# from langchain_community.document_loaders import TextLoader

# loader = TextLoader("/Users/farshid/Library/CloudStorage/OneDrive-Personal/Personal/9_Reference/farshid/output_text_file.txt")
# text_documents = loader.load()
# text_documents
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=20)
# documents = text_splitter.split_documents(text_documents)
# from langchain_community.vectorstores import DocArrayInMemorySearch
# from langchain_openai.embeddings import OpenAIEmbeddings
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain_core.runnables import RunnableParallel, RunnablePassthrough
# embeddings = OpenAIEmbeddings()
# setup = RunnableParallel(context=text_splitter, question=RunnablePassthrough())
# vectorstore2 = DocArrayInMemorySearch.from_documents(documents, embeddings)
# chain = (
#     {"context": vectorstore2.as_retriever(), "question": RunnablePassthrough()}
#     | prompt
#     | model
#     | parser
# )
# chain.invoke("What is camera calibration optimization?")