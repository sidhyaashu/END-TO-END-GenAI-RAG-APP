import os
from src.prompt import prompt_template
from src.helper import download_hugging_face_embeddings
from langchain.chains import RetrievalQA
from langchain_community.llms import CTransformers
from langchain_core.prompts import PromptTemplate
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv

load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')


embedding = download_hugging_face_embeddings()



index_name = "gen-ai-rag"
vectorstore = PineconeVectorStore.from_existing_index(index_name,embedding)


PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])


config = {'max_new_tokens': 100, 'repetition_penalty': 1.1}
llm = CTransformers(
    model="../model/llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama",
    config=config
)


# llm_chain = llm | PROMPT

chain_type_kwargs={"prompt": PROMPT}

qa = RetrievalQA.from_chain_type(  
    llm=llm,  
    chain_type="stuff",  
    retriever=vectorstore.as_retriever(),
)

# Prepare the context and query
query = "Who is Asutosh Sidhya?"

# Call the invoke method with the correct input keys
result = qa.invoke({"query": query})  # Ensure you include context if required
print(result)