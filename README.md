# Sistema‑Triagem AI‑RAG
> **RAG** (Retrieval‑Augmented Generation) para o projeto **Sistema‑Triagem**.  
> Este módulo fornece a camada de recuperação de documentos e geração de respostas baseada em grandes modelos de linguagem, integrando‑se ao backend existente.
---  
## 📚 Visão geral  
- **Objetivo**: melhorar a triagem automática usando informações contextuais armazenadas em um vetor de embeddings.  
- **Tecnologias**:  
  - Python 3.11  
  - `torch` / `transformers` (modelo LLM)  
  - `faiss` ou `chromadb` (vetor store)  
  - `sentence‑transformers` (embeddings)  
- **Integração**: expõe uma API FastAPI (`/rag/query`) que o backend (`sistema‑triagem/back`) consome.
---  
## 🚀 Começando  
### Requisitos
| Ferramenta | Versão mínima |
|------------|----------------|
| Python     | 3.11          |
| pip        | 24.x          |
| Git LFS    | (opcional, para modelos >100 MB) |
### Instalação rápida
```bash
# 1️⃣ Clone o repositório
git clone https://github.com/<SEU_USUARIO>/sistema-triagem-ai-rag.git
cd sistema-triagem-ai-rag
# 2️⃣ (Opcional) Pull de arquivos LFS – necessário se usar modelos pesados
git lfs pull   # se houver arquivos *.bin ou *.pt rastreados por LFS
# 3️⃣ Crie e ative o venv
python -m venv .venv
.\.venv\Scripts\activate   # PowerShell no Windows
# ou: source .venv/bin/activate   # Bash/Linux
# 4️⃣ Instale as dependências
pip install -r requirements.txt
⚠️ Atenção: Se o repositório contiver arquivos de modelo > 100 MB, habilite o Git LFS antes de fazer o clone (ex.: git lfs install).

Configuração
Copie o template de configuração:

bash


cp .env.example .env
Edite o .env com as credenciais e caminhos corretos:

dotenv


# Modelo LLM (exemplo)
LLM_MODEL=meta-llama/Meta-Llama-3-8B-Instruct
# Banco de vetores (FAISS)
VECTOR_DB_PATH=./data/faiss_index
# Porta da API RAG
RAG_PORT=8001
(Opcional) Se quiser usar Chromadb ao invés de FAISS, altere VECTOR_DB_BACKEND=chromadb no .env.

📦 Estrutura de diretórios


ai-rag/
│
├─ src/                     # Código-fonte Python
│   ├─ __init__.py
│   ├─ app.py               # FastAPI entrypoint
│   ├─ rag/
│   │   ├─ __init__.py
│   │   ├─ retriever.py     # Busca de embeddings
│   │   ├─ generator.py     # Interface com o LLM
│   │   └─ pipelines.py     # Orquestração RAG
│   └─ utils/
│       ├─ logger.py
│       └─ config.py
│
├─ data/                    # Dados de exemplo / índices FAISS (não versionado)
│   └─ .gitkeep
│
├─ tests/                   # Testes unitários e de integração
│   └─ test_rag.py
│
├─ requirements.txt         # Dependências pip
├─ pyproject.toml           # (se usar Poetry)
├─ .gitignore
├─ .gitattributes          # Configura LFS (ex.: *.bin filter=lfs)
└─ README.md                # <‑‑ este arquivo
🧪 Testes
bash


# Executa todos os testes
pytest -vv
Os testes cobrem:

Inicialização do vetor de embeddings
Consulta RAG básica
Tratamento de erros (sem resultados, modelo indisponível)
📊 Como usar (exemplo rápido)
python


import requests
resp = requests.post(
    "http://localhost:8001/rag/query",
    json={"question": "Qual a prioridade de atendimento para paciente com dor no peito?"}
)
print(resp.json())
📦 Publicação como pacote (opcional)
Se quiser distribuir o módulo via PyPI ou um índice interno:

bash


# Build
python -m build
# Upload (test.pypi.org)
twine upload --repository testpypi dist/*
# Install
pip install sistema-triagem-ai-rag
🤝 Contribuindo
Fork o repositório
Crie uma branch feature/<nome‑da‑feature>
Rode os testes (pytest) e garanta que o CI passe
Abra um Pull Request
Veja o arquivo CONTRIBUTING.md (a ser criado) para detalhes sobre estilo de código, linting e revisão.

📜 Licença
Este projeto está licenciado sob a MIT License – veja o arquivo LICENSE para mais informações.

🙋‍♀️ Contato
Autor: Seu Nome – 
seu.email@example.com
Organização: Nome da empresa / time
Issues: abra uma issue no GitHub para dúvidas, bugs ou sugestões.


### Próximos passos
1. Crie o novo repositório no GitHub com o nome **`sistema-triagem-ai-rag`**.  
2. Inicialize‑o localmente (`git init`) ou faça o fork do diretório existente.  
3. Adicione o `README.md` acima (substitua os blocos `TODO:` pelos seus valores).  
4. Commit e push:
   ```bash
   git add .
   git commit -m "Initial commit – AI‑RAG module + README"
   git branch -M main
   git remote add origin https://github.com/<SEU_USUARIO>/sistema-triagem-ai-rag.git
   git push -u origin main
