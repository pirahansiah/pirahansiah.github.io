import asyncio
import os
import PyPDF2
from langchain.document_loaders import PyPDFLoader
from ollama import AsyncClient

pdf_path='/Users/farshid/farshid/pirahansiah.github.io/src/LLMs/Farshid.pdf'
model_phi3='phi3'

# Initialize the Ollama client
client = AsyncClient()

async def summarize_pdfs(directory):
    summaries = []
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            pdf_file_path = os.path.join(directory, filename)

            # Extract metadata using PyPDF2
            with open(pdf_file_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)  # Replace PdfFileReader with PdfReader
                metadata = pdf_reader.metadata  # Replace getDocumentInfo with metadata

            loader = PyPDFLoader(pdf_file_path)
            data = loader.load_and_split()

            file_summary = {
                "filename": filename,
                "metadata": metadata,
                "chunks": []
            }

            # Generate the summary for each chunk
            for i, doc in enumerate(data):
                messages = [
                    {"role": "system", "content": f"You are a helpful assistant that summarizes the content of a document in a few sentences."},
                    {"role": "user", "content": doc.page_content}
                ]
                response = await client.chat(model=model_phi3, messages=messages)
                chunk_summary = response['message']['content']
                file_summary["chunks"].append({
                    "page_number": i + 1,
                    "text": doc.page_content,
                    "summary": chunk_summary
                })

            summaries.append(file_summary)

    return summaries

pdf_directory = "/Users/farshid/farshid/pirahansiah.github.io/src/LLMs/"
# Use the asyncio magic command to run the asynchronous function
summaries = await summarize_pdfs(pdf_directory)