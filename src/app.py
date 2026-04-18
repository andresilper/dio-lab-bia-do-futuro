import os
import json
import pandas as pd
import requests
import streamlit as st

# --- Configuração ---
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "llama2:7b"

# ------ Carregar dados -----
perfil = json.load(open("./data/perfil_investidor.json"))
historico = pd.read_csv(open("./data/historico_atendimento.csv"))
transacoes = pd.read_csv(open("./data/transacoes.csv"))
produtos = json.load(open("./data/produtos_financeiros.json"))

# ----- Montar Contexto ----
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES: 
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ------ System Prompt ------

SYSTEM_PROMPT = """Bom dia, chat! Comporte-se como um educador financeiro para explicar sobre diversos tipos de produtos de investimento disponíveis para o meu perfil.

OBJETIVO: Ensinar conceitos de finanças pessoais de forma a facilitar o entendimento.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Nunca recomende investimentos
5. Jamais responda a perguntas fora do tema de ensino de finanças pessoais
"""

# --- Chamar Ollama ---
def perguntar(msg):
    prompt = f"""
    {SYSTEM_PROMPT}

    CONTEXTO DO CLIENTE:
    {contexto}

    Pergunta: {msg} """
    r = requests.post(OLLAMA_URL, json={"model" : MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# ----- Interface ----
st.title("Dr. Marvin Educador Financeiro")

if pergunta:= st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message('assistant').write(perguntar(pergunta))
