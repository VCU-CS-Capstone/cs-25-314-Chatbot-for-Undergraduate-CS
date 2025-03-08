from llama_index.core import Document
from llama_index.readers.apify import ApifyActor
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
import os
import openai
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv

class Chatbot:
    def __init__(self):

        # load_dotenv()
        # API_KEY =  os.getenv("OPENAI_APIKEY")

        # APIFY = os.getenv("APIFY")

        # openai.api_key = API_KEY


        embedding_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

        PERSIST_DIR = "./storage_index"

        if not os.path.exists(PERSIST_DIR):
            reader = ApifyActor(APIFY)
            documents = reader.load_data(
                actor_id="apify/website-content-crawler",
                run_input={
                    "startUrls": [
                        {"url": "https://bulletin.vcu.edu/undergraduate/engineering/computer-science/computer-science-bs-concentration-cybersecurity/"}
                    ]
                },
                dataset_mapping_function=lambda item: Document(
                    text=item.get("text"),
                    metadata={
                        "url": item.get("url"),
                    },
                ),
            )
            print("Total documents scraped: ", len(documents))

            # Create the index from documents
            index = VectorStoreIndex.from_documents(documents, embed_model = embedding_model)

            # Persist the index for later use
            index.storage_context.persist(persist_dir=PERSIST_DIR)
        else:
            # Load the existing index
            storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
            index = load_index_from_storage(storage_context, embed_model = embedding_model) 

        self.query_engine = index.as_query_engine()


    def ask_response(self, question):  
        if question.lower() == "exit":
            return
        
        # Query the index
        response = self.query_engine.query(question)
        return response.response