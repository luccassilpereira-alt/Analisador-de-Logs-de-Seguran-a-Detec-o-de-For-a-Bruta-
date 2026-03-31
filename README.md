# 🛡️ Analisador de Logs de Segurança (Detecção de Força Bruta)

Este é um projeto prático desenvolvido em Python com o objetivo de automatizar a análise de logs de servidores e identificar possíveis ataques de força bruta. O script processa um arquivo de texto contendo registros de login, analisa as tentativas falhas por IP e gera um relatório automatizado isolando os endereços suspeitos.

---

## 🚀 Tecnologias e Conceitos Aplicados

* **Linguagem:** Python 🐍
* **Estruturas de Dados:** Uso de Dicionários (para contagem dinâmica) e Tuplas (para armazenamento imutável dos registros lidos).
* **Manipulação de Arquivos (I/O):** Leitura segura de logs e escrita automatizada de relatórios.
* **Lógica de Programação:** Controle de fluxo, laços de repetição e funções modulares.

---

## ⚙️ Como executar

Segue os passos abaixo para testar o projeto na tua máquina:

1. **Clona este repositório:**
   ```bash
   git clone https://github.com/luccassilpereira-alt/Analisador-de-Logs-de-Seguran-a-Detec-o-de-For-a-Bruta-.git

3. **Certifique-se de que o arquivo logs.txt (com os dados de exemplo) está na mesma pasta do script principal.**

4. **Execute o script:**

python nome_do_script.py

4. **O resultado da análise será salvo automaticamente no arquivo relatorio_alerta.txt dentro do mesmo diretório.**
