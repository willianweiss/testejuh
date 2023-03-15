# Projeto FastAPI com SQLAlchemy e Alembic

Este projeto utiliza FastAPI, SQLAlchemy e Alembic para criar uma API RESTful para o gerenciamento de dados de corridas de táxi. A aplicação inclui funcionalidades para adicionar, recuperar e processar dados em lote de táxis.

## Requisitos

-   Docker
-   Docker Compose

## Como executar o projeto

### 1. Clone o repositório

Clone o repositório para sua máquina local:

bashCopy code

`git clone https://github.com/seu_usuario/seu_repositorio.git` 

### 2. Navegue até o diretório do projeto

Vá até a pasta do projeto:

bashCopy code

`cd seu_repositorio` 

### 3. Construa e execute a aplicação com Docker Compose

Na pasta do projeto, execute o seguinte comando para construir e iniciar a aplicação e o banco de dados usando Docker Compose:

cssCopy code

`docker-compose up --build` 

A aplicação FastAPI estará disponível em: [http://localhost:8000](http://localhost:8000/)

Para parar e remover os contêineres, execute o seguinte comando:

Copy code

`docker-compose down` 

## Endpoints

Os endpoints da API incluem:

-   `GET /taxis`: Recupera todos os registros de corridas de táxi
-   `POST /taxis`: Adiciona um novo registro de corrida de táxi
-   `GET /taxis/{taxi_id}`: Recupera um registro de corrida de táxi específico pelo ID
-   `PUT /taxis/{taxi_id}`: Atualiza um registro de corrida de táxi específico pelo ID
-   `DELETE /taxis/{taxi_id}`: Exclui um registro de corrida de táxi específico pelo ID
-   `POST /batch_process`: Processa dados em lote de corridas de táxi a partir de múltiplos arquivos Parquet

## Ingestão de dados em lote

A aplicação inclui uma funcionalidade para processar dados em lote a partir de múltiplos arquivos Parquet. Para utilizar esta funcionalidade, envie uma requisição `POST` para o endpoint `/batch_process` com um JSON contendo a lista de URLs dos arquivos Parquet:

jsonCopy code

`{
    "parquet_files": [
        "https://example.com/file1.parquet",
        "https://example.com/file2.parquet"
    ]
}` 

A aplicação baixará e processará os arquivos Parquet fornecidos, inserindo os registros de corridas de táxi no banco de dados.