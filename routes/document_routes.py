from flask import Blueprint, request, jsonify
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

doc_bp = Blueprint('documents', __name__)

model = SentenceTransformer('all-MiniLM-L6-v2')
dimension = 384
index = faiss.IndexFlatL2(dimension)

documents = []

@doc_bp.route('/upload', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        file_path = f"/tmp/{file.filename}"
        file.save(file_path)

        try:
            if not os.path.exists(file_path):
                return jsonify({"error": "File save failed"}), 500

            with open(file_path, 'r', encoding='utf-8') as f:
                document_text = f.read()

            if not document_text:
                return jsonify({"error": "File read failed"}), 500

            document_embedding = model.encode([document_text])

            if document_embedding is None or len(document_embedding) == 0:
                return jsonify({"error": "Embedding generation failed"}), 500

            index.add(np.array(document_embedding))

            documents.append(document_text)

            return jsonify({"message": "Document uploaded, vectorized, and stored successfully"}), 200
        finally:
            os.remove(file_path)

    return jsonify({"error": "File upload failed"}), 500