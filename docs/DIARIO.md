# Diário de Bordo

## 2026-09-23

**O que tentei:**
Construir a versão 0.1 do agente de mentoria.

**O que funcionou:**
- Módulos ia_helper, git_helper, diario e agente funcionando
- Chamada real ao Groq retornando respostas em português
- Sugestão de commit com IA no padrão Conventional Commits
- Validação de entradas vazias no diário
- Cores ANSI no terminal

**O que quebrou:**
- Conflito de versão (proxies) — resolvido atualizando openai
- Chave duplicada no .env — resolvido reescrevendo
- Modelo llama-3.3-70b virou Enterprise — trocado por gpt-oss-120b
- Import de módulo src — resolvido rodando com python3 -m

**Próximo passo:**
- Atualizar README
- Adicionar testes automatizados
- Fazer commit da versão 0.1