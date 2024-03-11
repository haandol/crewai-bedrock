# CrewAI Bedrock

This is a simple example of how to use the CrewAI with bedrock.

# Prerequisites

- AWS CLI already configured with Administrator permission
- Python 3.12+

# Setup

install dependencies

```bash
pip install -r requirements.txt
```

## Run app on Bedrock via LiteLLM

run litellm

```bash
AWS_REGION=us-east-1 litellm --model anthropic.claude-3-sonnet-20240229-v1:0 --drop_params
```

edit `OPENAI_API_BASE` on env

```bash
OPENAI_API_BASE="http://localhost:4000"
OPENAI_MODEL_NAME="bedrock"
```

## Run app locally with Ollama

install [ollama](https://ollama.com)

```bash
brew install ollama
ollama run dolphin-mistral
```

# Test

## Copy env

```bash
cp env/local.env .env
```

## Run the application

```bash
python main.py
```
