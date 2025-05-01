import os
import logging
import threading
import time
from flask import Flask, request, jsonify
from azure.cosmos import CosmosClient
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Initialize Azure clients
cosmos_client = CosmosClient(
    url=os.getenv("COSMOS_ENDPOINT"),
    credential=os.getenv("COSMOS_KEY")
)

# Health check thread
def health_check_thread():
    while True:
        try:
            # Check Cosmos DB connection
            database = cosmos_client.get_database_client("telegram")
            container = database.get_container_client("messages")
            container.query_items(
                query="SELECT * FROM c LIMIT 1",
                enable_cross_partition_query=True
            )
            logger.info("Health check: Server is healthy")
        except Exception as e:
            logger.error(f"Health check failed: {str(e)}")
        time.sleep(60)  # Check every minute

# Start health check thread
health_thread = threading.Thread(target=health_check_thread, daemon=True)
health_thread.start()

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json()
        
        # Process the message
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]
        
        # Send response
        send_telegram_message(chat_id, f"You said: {text}")
        
        return jsonify({"status": "ok"})
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

def send_telegram_message(chat_id, text):
    try:
        url = f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage"
        response = requests.post(url, json={
            "chat_id": chat_id,
            "text": text
        })
        response.raise_for_status()
    except Exception as e:
        logger.error(f"Error sending message: {str(e)}")
        raise

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080) 