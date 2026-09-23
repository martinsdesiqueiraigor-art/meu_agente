"""
agente.py — Programa principal do agente de mentoria.
"""

from src import git_helper
from src import diario
from src.ia_helper import perguntar_ia, sugerir_commit


# Códigos ANSI para cores no terminal
COR_TITULO = "\033[1;36m"    # ciano negrito
COR_OK = "\033[1;32m"        # verde negrito
COR_AVISO = "\033[1;33m"     # amarelo negrito
COR_ERRO = "\033[1;31m"      # vermelho negrito
COR_IA = "\033[1;35m"        # magenta negrito
COR_RESET = "\033[0m"        # volta ao normal


def _mostrar_menu() -> None:
    """Imprime o menu principal na tela."""
    print()
    print(f"{COR_TITULO}=== Agente de Mentoria ==={COR_RESET}")
    print("1) Ver status do repositório")
    print("2) Sugerir mensagem de commit")
    print("3) Registrar no diário")
    print("4) Conversar com a IA")
    print("5) Sair")
    print()


def _perguntar_obrigatorio(texto: str) -> str:
    """Pergunta algo e insiste até receber uma resposta não vazia."""
    while True:
        resposta = input(texto).strip()
        if resposta:
            return resposta
        print(f"{COR_AVISO}⚠  Por favor, digite algo.{COR_RESET}")


def _opcao_status() -> None:
    """Mostra o status do repositório Git."""
    info = git_helper.resumo_do_repo()

    print()
    print(f"{COR_TITULO}Branch:{COR_RESET} {info['branch']}")
    print(f"{COR_TITULO}Último commit:{COR_RESET} {info['ultimo_commit']}")

    if info["tem_mudancas"]:
        print(f"{COR_TITULO}Arquivos com mudanças:{COR_RESET}")
        for linha in info["status"].split("\n"):
            print(f"  {COR_AVISO}{linha}{COR_RESET}")
    else:
        print(f"{COR_OK}Status: tudo limpo ✨{COR_RESET}")
    print()


def _opcao_sugerir_commit() -> None:
    """Lê o estado do Git e pede sugestões de commit para a IA."""
    info = git_helper.resumo_do_repo()

    if not info["tem_mudancas"]:
        print(f"\n{COR_OK}✨ Nada para commitar. Working tree limpo.{COR_RESET}")
        return

    diff = git_helper.diff_staged()
    status = info["status"]

    contexto = (
        f"Status:\n{status}\n\n"
        f"Diff staged:\n{diff if diff else '(nada staged ainda)'}"
    )

    print(f"\n{COR_AVISO}🤔 Analisando e gerando sugestões...{COR_RESET}\n")
    sugestoes = sugerir_commit(contexto)
    print(f"{COR_IA}Sugestões de mensagem de commit:{COR_RESET}\n")
    print(sugestoes)
    print()


def _opcao_diario() -> None:
    """Pergunta ao usuário e adiciona uma entrada no diário."""
    print()
    tentei = _perguntar_obrigatorio("O que você tentou fazer? ")
    funcionou = _perguntar_obrigatorio("O que funcionou? ")
    quebrou = _perguntar_obrigatorio("O que quebrou? ")
    proximo = _perguntar_obrigatorio("Próximo passo? ")

    diario.adicionar_entrada(tentei, funcionou, quebrou, proximo)
    print(f"\n{COR_OK}✅ Entrada adicionada em docs/DIARIO.md{COR_RESET}")


def _opcao_conversar() -> None:
    """Conversa livre com a IA."""
    print()
    pergunta = input("Pergunte algo para a IA: ").strip()
    if not pergunta:
        print(f"{COR_AVISO}⚠  Pergunta vazia. Voltando ao menu.{COR_RESET}")
        return

    print(f"\n{COR_AVISO}🤔 Pensando...{COR_RESET}\n")
    resposta = perguntar_ia(pergunta)
    print(f"{COR_IA}🤖 {resposta}{COR_RESET}")


def main() -> None:
    """Loop principal do agente."""
    while True:
        _mostrar_menu()
        escolha = input("> ").strip()

        if escolha == "1":
            _opcao_status()
        elif escolha == "2":
            _opcao_sugerir_commit()
        elif escolha == "3":
            _opcao_diario()
        elif escolha == "4":
            _opcao_conversar()
        elif escolha == "5":
            print(f"\n{COR_OK}Até logo! 👋{COR_RESET}")
            break
        else:
            print(f"\n{COR_ERRO}❌ Opção inválida. Digite 1, 2, 3, 4 ou 5.{COR_RESET}")


if __name__ == "__main__":
    main()