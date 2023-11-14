# Use a imagem oficial do Python com a versão desejada
FROM python:3.8

# Configure o diretório de trabalho
WORKDIR /app

# Copie os arquivos necessários para o contêiner
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta utilizada pela aplicação (ajuste conforme necessário)
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
