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
