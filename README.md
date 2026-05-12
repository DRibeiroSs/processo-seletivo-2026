# Sistema Agêntico de IA — LAPES 2026

Projeto desenvolvido para o Processo Seletivo LAPES 2026.

## Sobre o projeto

Sistema multiagente capaz de responder perguntas sobre fundamentos de Ciência da Computação, combinando recuperação vetorial (RAG) com busca na web como fallback.

## Corpus

25 artigos da Wikipedia sobre tópicos fundamentais de Ciência da Computação, incluindo algoritmos, estruturas de dados, paradigmas de programação e conceitos de sistemas.

## Como rodar

### Pré-requisitos
- Python 3.9+
- Git

### Instalação

```bash
# Clone o repositório
git clone https://github.com/DRibeiroSs/processo-seletivo-2026.git
cd processo-seletivo-2026

# Crie o ambiente virtual
python -m venv .venv
.venv\Scripts\Activate.ps1  # Windows

# Instale as dependências
pip install -r requirements.txt
```

## Estrutura do projeto
├── agentes/        # Agentes do sistema
├── avaliacao/      # Benchmark e métricas
├── corpus/         # Pipeline de ingestão e documentos
├── traces/         # Logs de execução em JSON
├── app.py          # Interface Streamlit
└── requirements.txt

## Autor

Davi de Lemos Soares Ribeiro  
davi26070009@aluno.cesupa.br  
Processo Seletivo LAPES 2026