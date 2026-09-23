"""
git_helper.py — Funções para obter informações do Git.
"""

import subprocess


def _executar_comando(comando: list) -> str:
    """Executa um comando no sistema e retorna a saída como texto."""
    try:
        resultado = subprocess.run(
            comando,
            capture_output=True,
            text=True,
            check=True
        )
        return resultado.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"ERRO: {e.stderr.strip()}"


def status_resumido() -> str:
    """Retorna o 'git status' em formato curto."""
    return _executar_comando(["git", "status", "--short"])


def branch_atual() -> str:
    """Retorna o nome da branch atual."""
    return _executar_comando(["git", "branch", "--show-current"])


def ultimo_commit() -> str:
    """Retorna o último commit em formato de uma linha."""
    return _executar_comando(["git", "log", "-1", "--oneline"])


def diff_staged() -> str:
    """Retorna o diff do que está em staging."""
    return _executar_comando(["git", "diff", "--staged"])


def resumo_do_repo() -> dict:
    """Retorna um dicionário com o estado atual do repositório."""
    return {
        "branch": branch_atual(),
        "ultimo_commit": ultimo_commit(),
        "status": status_resumido(),
        "tem_mudancas": bool(status_resumido()),
    }

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