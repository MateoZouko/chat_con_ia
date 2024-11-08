from flask import Flask
from routes.chat_routes import chat_bp
from routes.document_routes import doc_bp

app = Flask(__name__)
app.register_blueprint(chat_bp, url_prefix='/api/chat')
app.register_blueprint(doc_bp, url_prefix='/api/documents')

if __name__ == '__main__':
    app.run(debug=True)