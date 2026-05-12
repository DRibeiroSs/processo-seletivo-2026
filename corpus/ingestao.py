import os
import json
import wikipedia

wikipedia.set_lang("en")

ARTIGOS = [
    "Algorithm",
    "Data structure",
    "Array data structure",
    "Linked list",
    "Stack (abstract data type)",
    "Queue (abstract data type)",
    "Binary tree",
    "Hash table",
    "Graph (discrete mathematics)",
    "Sorting algorithm",
    "Binary search algorithm",
    "Big O notation",
    "Recursion",
    "Object-oriented programming",
    "Functional programming",
    "Operating system",
    "Computer network",
    "Internet protocol suite",
    "Database",
    "SQL",
    "Compiler",
    "Interpreter (computing)",
    "Boolean algebra",
    "Logic gate",
    "Turing machine",
]

os.makedirs("corpus/documentos", exist_ok=True)

for titulo in ARTIGOS:
    try:
        pagina = wikipedia.page(titulo, auto_suggest=False)
        dados = {
            "titulo": pagina.title,
            "url": pagina.url,
            "conteudo": pagina.content
        }
        nome_arquivo = titulo.replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "") + ".json"
        caminho = f"corpus/documentos/{nome_arquivo}"
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print(f"✓ {titulo}")
    except Exception as e:
        print(f"✗ {titulo} — erro: {e}")

print("\nDownload concluído!")