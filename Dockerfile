# Usa uma imagem base do Python
FROM python:3.11

# Define pasta dentro do container
WORKDIR /app

# Copia arquivos do projeto
COPY . .

# Instala dependências
RUN pip install fastapi uvicorn

# Comando para rodar a API
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]