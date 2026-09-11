"""
Script de ingestão da base de conhecimento no ChromaDB (etapa 1 da arquitetura RAG,
item 2.7 do TCC).

Uso:
    pip install -r requirements.txt
    python ingest_chromadb.py

Pré-requisito: um servidor ChromaDB em execução (`chroma run --path ./chroma_data`)
acessível em http://localhost:8000 (ou conforme configurado em appsettings.json).

O script:
1. Lê os arquivos .md da pasta knowledge_base/
2. Divide cada documento em trechos (chunks) menores
3. Envia os trechos ao ChromaDB, que gera os embeddings automaticamente
   (usando o modelo default do Chroma) e os armazena na coleção configurada.
"""

import os
import chromadb

KNOWLEDGE_DIR = os.path.join(os.path.dirname(__file__), "knowledge_base")
CHROMA_HOST = os.environ.get("CHROMA_HOST", "localhost")
CHROMA_PORT = int(os.environ.get("CHROMA_PORT", "8000"))
COLLECTION_NAME = os.environ.get("CHROMA_COLLECTION", "triagem_conhecimento")

CHUNK_SIZE = 500  # caracteres por trecho (aproximação simples, sem dependências extras)


def dividir_em_chunks(texto: str, tamanho: int = CHUNK_SIZE):
    paragrafos = [p.strip() for p in texto.split("\n\n") if p.strip()]
    chunks, atual = [], ""
    for p in paragrafos:
        if len(atual) + len(p) > tamanho and atual:
            chunks.append(atual.strip())
            atual = ""
        atual += p + "\n\n"
    if atual.strip():
        chunks.append(atual.strip())
    return chunks


def main():
    client = chromadb.HttpClient(host=CHROMA_HOST, port=CHROMA_PORT)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    documentos, metadados, ids = [], [], []
    contador = 0

    for nome_arquivo in sorted(os.listdir(KNOWLEDGE_DIR)):
        if not nome_arquivo.endswith(".md"):
            continue

        caminho = os.path.join(KNOWLEDGE_DIR, nome_arquivo)
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()

        for chunk in dividir_em_chunks(conteudo):
            documentos.append(chunk)
            metadados.append({"fonte": nome_arquivo})
            ids.append(f"{nome_arquivo}-{contador}")
            contador += 1

    if not documentos:
        print("Nenhum documento encontrado em knowledge_base/.")
        return

    collection.upsert(documents=documentos, metadatas=metadados, ids=ids)
    print(f"{len(documentos)} trechos indexados na coleção '{COLLECTION_NAME}'.")


if __name__ == "__main__":
    main()
