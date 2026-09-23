"""
diario.py — Gerencia o diário de bordo em docs/DIARIO.md.
"""

from datetime import date
from pathlib import Path

# Caminho do arquivo de diário (a partir da raiz do projeto)
CAMINHO_DIARIO = Path("docs/DIARIO.md")

# Cabeçalho que fica no topo do diário, uma vez só
CABECALHO = "# Diário de Bordo\n"


def _garantir_arquivo() -> None:
    """Cria o arquivo e o cabeçalho, se ainda não existirem."""
    CAMINHO_DIARIO.parent.mkdir(parents=True, exist_ok=True)
    if not CAMINHO_DIARIO.exists():
        CAMINHO_DIARIO.write_text(CABECALHO, encoding="utf-8")


def ler_diario() -> str:
    """Retorna o conteúdo completo do diário."""
    _garantir_arquivo()
    return CAMINHO_DIARIO.read_text(encoding="utf-8")


def adicionar_entrada(tentei: str, funcionou: str, quebrou: str, proximo: str) -> None:
    """Adiciona uma nova entrada no topo do diário."""
    _garantir_arquivo()

    hoje = date.today().isoformat()  # ex: "2026-09-22"

    nova_entrada = (
        f"\n## {hoje}\n\n"
        f"**O que tentei:**\n{tentei}\n\n"
        f"**O que funcionou:**\n{funcionou}\n\n"
        f"**O que quebrou:**\n{quebrou}\n\n"
        f"**Próximo passo:**\n{proximo}\n"
    )

    conteudo_atual = CAMINHO_DIARIO.read_text(encoding="utf-8")

    # Se o arquivo tem só o cabeçalho, adiciona a entrada logo abaixo
    if conteudo_atual.strip() == CABECALHO.strip():
        novo_conteudo = f"{CABECALHO}{nova_entrada}"
    else:
        # Insere a nova entrada DEPOIS do cabeçalho, antes das entradas antigas
        corpo = conteudo_atual[len(CABECALHO):].lstrip("\n")
        novo_conteudo = f"{CABECALHO}{nova_entrada}\n{corpo}"

    CAMINHO_DIARIO.write_text(novo_conteudo, encoding="utf-8")