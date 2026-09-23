"""
ia_helper.py — Funções para conversar com a IA (Groq).
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis do arquivo .env
load_dotenv()

# Cria o cliente apontando para o Groq
cliente = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

# Instrução fixa: sempre responder em português brasileiro
INSTRUCAO_IDIOMA = (
    "Responda sempre em português brasileiro, de forma clara e direta. "
    "Use linguagem informal mas profissional. Evite jargões sem explicar."
)


def perguntar_ia(pergunta: str) -> str:
    """Envia uma pergunta para a IA e retorna a resposta em texto."""
    resposta = cliente.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": INSTRUCAO_IDIOMA},
            {"role": "user", "content": pergunta}
        ]
    )
    return resposta.choices[0].message.content


def sugerir_commit(contexto_git: str) -> str:
    """Recebe o estado do Git e pede à IA sugestões de mensagem de commit."""
    instrucoes = (
        "Você é um assistente que ajuda a escrever mensagens de commit no padrão "
        "Conventional Commits (feat, fix, docs, refactor, chore, test, style). "
        "Responda APENAS com 3 sugestões de mensagem, uma por linha, em português, "
        "no formato: 'tipo: descrição curta no imperativo'. "
        "Não use markdown, não numere, não explique. Apenas as 3 linhas."
    )

    mensagem_usuario = (
        f"Aqui está o estado atual do repositório Git:\n\n"
        f"{contexto_git}\n\n"
        f"Sugira 3 mensagens de commit apropriadas."
    )

    resposta = cliente.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": instrucoes},
            {"role": "user", "content": mensagem_usuario}
        ]
    )
    return resposta.choices[0].message.content