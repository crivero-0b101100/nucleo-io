# Nucleo IO

A Telegram bot service built with Python, Flask, and Azure services.

## Features

- Telegram bot integration
- Azure Cosmos DB for data storage
- Azure Key Vault for secrets management
- Kubernetes deployment
- Continuous Deployment with GitHub Actions

## Prerequisites

- Python 3.9+
- Azure subscription
- Azure Container Registry
- Azure Kubernetes Service
- Azure Key Vault
- Azure Cosmos DB

## Environment Variables

The following environment variables are required:

- `TELEGRAM_BOT_TOKEN`: Your Telegram bot token
- `COSMOS_ENDPOINT`: Azure Cosmos DB endpoint
- `COSMOS_KEY`: Azure Cosmos DB key
- `KEY_VAULT_NAME`: Azure Key Vault name
- `KEY_VAULT_TENANT_ID`: Azure tenant ID
- `KEY_VAULT_CLIENT_ID`: Azure client ID
- `KEY_VAULT_CLIENT_SECRET`: Azure client secret

## Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/nucleo-io.git
cd nucleo-io
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## Deployment

The application is automatically deployed to Kubernetes when changes are pushed to the main branch. The deployment process:

1. Builds a Docker image
2. Pushes the image to Azure Container Registry
3. Updates the Kubernetes deployment with the new image

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 