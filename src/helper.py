import os
import logging
from dotenv import load_dotenv
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders.pdf import PyMuPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings


load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def pdf_loader(path: str, glob_pattern: str = "*.pdf", loader_cls=PyMuPDFLoader) -> Optional[List[dict]]:

    try:
        logger.info(f"Starting to load documents from '{path}' with pattern '{glob_pattern}'")
        
        # Check if the directory exists
        if not os.path.isdir(path):
            logger.error(f"The directory '{path}' does not exist.")
            return None
        
        # Load the PDF files
        loader = DirectoryLoader(path, glob=glob_pattern, loader_cls=loader_cls)
        documents = loader.load()

        logger.info(f"Successfully loaded {len(documents)} documents.")

        return documents

    except FileNotFoundError as fnf_error:
        logger.error(f"File not found error: {fnf_error}")
    except AttributeError as attr_error:
        logger.error(f"Attribute error: {attr_error}. Check the structure of loaded documents.")
    except Exception as e:
        logger.error(f"An error occurred while loading PDF: {e}")

    return None

extracted_data = pdf_loader("D:\\Gen_AI\\END-TO-END-GenAI-RAG-APP\\data")




def text_split(data):
    text_splitter = CharacterTextSplitter(chunk_size=120, chunk_overlap=0)
    text_chunks = text_splitter.split_documents(data)
    
    return text_chunks



def download_hugging_face_embeddings():
    model = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(model_name=model)
    return embeddings