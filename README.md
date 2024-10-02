# End-to-End GenAI RAG App

This project implements an end-to-end **Retrieval-Augmented Generation (RAG)** application using **Langchain** and **Llama2**. The app retrieves relevant information from a document store and generates intelligent responses by augmenting the retrieved data with Llama2’s generative AI capabilities.

## Key Features:
- **Document Loading**: Easily load and preprocess various document types (e.g., PDFs).
- **Text Chunking**: Automatically split large text into manageable chunks for efficient retrieval.
- **Embeddings Generation**: Use Hugging Face models to generate vector embeddings for documents.
- **Pinecone Vector Storage**: Store and manage document embeddings in Pinecone’s vector database.
- **RAG Workflow**: Combine retrieved documents with generative AI to produce informative responses.

## Tech Stack:
- **Langchain**: For chaining together retrieval and generation tasks.
- **Llama2**: To handle generative responses.
- **Pinecone**: As the vector store for fast retrieval of relevant documents.
- **Hugging Face**: For generating embeddings from text.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   ```bash
   pip install -r requirements.txt -i https://pypi.org/simple
   ```
3. Set up your environment variables (e.g., PINECONE_API_KEY, PINECONE_ENVIRONMENT):
   ```bash
   cp .env.example .env
   ```
4. Run the application:
   ```bash
   python main.py
   ```

## Usage
1. Load documents into the app.
2. Generate embeddings using Hugging Face models.
3. Use Pinecone for efficient vector retrieval.
4. Generate informative, context-rich responses using Llama2.


## License
 - This project is licensed under the MIT License. See the LICENSE file for more details.