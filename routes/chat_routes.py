from flask import Blueprint, request, jsonify
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import logging
from utils.llama_connector import LlamaConnector

chat_bp = Blueprint('chat', __name__)

model = SentenceTransformer('all-MiniLM-L6-v2')
dimension = 384
index = faiss.IndexFlatL2(dimension)

documents = []
document_embeddings = []

logging.basicConfig(level=logging.DEBUG)

llama_connector = LlamaConnector()

@chat_bp.route('/add_document', methods=['POST'])
def add_document():
    try:
        if 'file' not in request.files:
            logging.error("No file part in the request")
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']
        
        if file.filename == '':
            logging.error("No selected file")
            return jsonify({"error": "No selected file"}), 400

        document = file.read().decode('utf-8')
        
        logging.debug(f"Received document: {document}")
        
        documents.append(document)
        
        document_embedding = model.encode([document])
        document_embeddings.append(document_embedding)
        index.add(np.array(document_embedding))
        
        return jsonify({"message": "Document added successfully"}), 200
    except Exception as e:
        logging.error(f"Error adding document: {e}")
        return jsonify({"error": "Internal server error"}), 500

@chat_bp.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        if not data:
            logging.error("No JSON data received")
            return jsonify({"error": "No JSON data received"}), 400

        query = data.get('query', '')
        
        if not query:
            logging.error("Query is empty")
            return jsonify({"error": "Query is empty"}), 400
        
        logging.debug(f"Received query: {query}")
        
        query_embedding = model.encode([query])
        
        distances, indices = index.search(np.array(query_embedding), k=5)

        logging.debug(f"FAISS search results - distances: {distances}, indices: {indices}")

        if len(indices) == 0 or len(indices[0]) == 0:
            logging.error("No valid results found in FAISS search")
            return jsonify({"response": "No se encontraron resultados relevantes."}), 200

        relevant_docs = [documents[i] for i in indices[0] if i < len(documents)]

        logging.debug(f"Relevant documents: {relevant_docs}")

        if not relevant_docs:
            logging.error("No relevant documents found")
            return jsonify({"response": "No se encontraron documentos relevantes."}), 200

        context = " ".join(relevant_docs)
        prompt = f"Contexto: {context}\nPregunta: {query}"
        
        logging.debug(f"Prompt for Llama: {prompt}")

        response = llama_connector.ask_llama(prompt)
        
        logging.debug(f"Llama response: {response}")

        return jsonify({"response": response}), 200
    except Exception as e:
        logging.error(f"Error processing request: {e}")
        return jsonify({"error": "Internal server error"}), 500
