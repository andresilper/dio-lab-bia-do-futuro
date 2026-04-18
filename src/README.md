# Passo a Passo de Execução

## Setup do Ollama 

```bash
# 1. Instalar Ollama (ollama.com)
# 2. Baixar um modelo leve (llama2:7b)

#. Testar se funciona
ollama run llama2:7b "Olá!"
```
## Código Completo

Todo o código-fonte está no arquivo "app.py"


---
## Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas requests

# 2. Garantir que o Ollama está rodando
ollama serve

# 3. Rodar a aplicação
streamlit run app.py

<img width="1366" height="728" alt="image" src="https://github.com/user-attachments/assets/46ca22fc-c044-4897-bf27-c63fd7c47eb8" />
