
# Planejamento do Dockerfile – word-counter-app

## Imagem base
- python:3.11-slim
- Slim para manter imagem pequena
- Não vou usar alpine por enquanto porque pode dar erro com dependências nativas

## Diretório de trabalho
- Criar um diretório /app
- Fazer WORKDIR /app

## Dependências
- Copiar requirements.txt primeiro
- Rodar pip install -r requirements.txt

## Código
- Copiar todo o restante depois

## Exposição da porta
- Expor a porta 8000

## Comando final
- Rodar: uvicorn app:app --host 0.0.0.0 --port 8000

## Otimização
- Evitar instalar coisas a mais
- Usar .dockerignore para excluir venv, __pycache__, .git, etc.
