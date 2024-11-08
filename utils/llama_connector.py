import requests

class LlamaConnector:
    def __init__(self, url="http://localhost:11434/api/chat"):
        self.url = url

    def ask_llama(self, prompt):
        data = {
            "model": "llama2",
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        }
        headers = {"Content-Type": "application/json"}
        response = requests.post(self.url, headers=headers, json=data)
        
        if response.status_code == 200:
            return response.json().get("message", {}).get("content", "")
        return "Error al conectarse con el modelo Llama."
