# 🤖 Meu Agente

Um agente de terminal que ajuda desenvolvedores iniciantes a gerenciar Git, manter um diário de bordo e aprender com o apoio de Inteligência Artificial.

---

## ✨ O Que Ele Faz

- **📊 Status do repositório** — Mostra o estado atual do Git formatado de forma legível
- **💡 Sugestão de commit com IA** — Analisa as mudanças e sugere mensagens no padrão Conventional Commits
- **📔 Diário de bordo** — Registra o que você tentou, o que funcionou e o que quebrou
- **💬 Conversa com IA** — Faz perguntas ao modelo Llama (via Groq) e recebe respostas didáticas em português
- **🎨 Interface colorida** — Menu interativo no terminal com cores ANSI
- **✅ Validação de entrada** — Não aceita respostas vazias, garantindo dados úteis no diário

---

## 🛠️ Tecnologias Usadas

| Tecnologia | Para que serve |
|------------|----------------|
| **Python 3.14** | Linguagem principal |
| **Groq API** | Inferência rápida e gratuita de modelos Llama |
| **openai (SDK)** | Cliente compatível com a API do Groq |
| **python-dotenv** | Carregamento seguro de variáveis de ambiente |
| **Git** | Controle de versão do próprio projeto |
| **GitHub Codespaces** | Ambiente de desenvolvimento na nuvem |

---

## 🚀 Como Instalar e Rodar

### Pré-requisitos

- Python 3.11 ou superior
- Uma chave de API do [Groq](https://console.groq.com/keys) (gratuita)
- Git instalado

### Passo a passo

**1. Clone o repositório:**

```bash
git clone https://github.com/martinsdesiqueiraigor-art/meu_agente.git
cd meu_agente