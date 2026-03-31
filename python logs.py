# 1. Função para ler o arquivo e guardar os dados
def ler_logs(nome_arquivo):  # <- Adicionei o parâmetro aqui
    lista_logs = []

    with open(nome_arquivo, 'r') as arquivo:  # <- Usa a variável em vez de fixar o nome
        for linha in arquivo:
            linha_limpa = linha.strip()
            ip, status = linha_limpa.split(',')
            lista_logs.append((ip, status))

    return lista_logs

# 2. Função para contar as falhas


def analisar_falhas(lista_logs):  # <- Agora ela RECEBE a lista da função 1
    contagem_falhas = {}

    for ip, status in lista_logs:
        if status == "falha":
            if ip in contagem_falhas:
                contagem_falhas[ip] += 1
            else:
                contagem_falhas[ip] = 1

    return contagem_falhas

# 3. Função para gerar o arquivo de alerta


def gerar_relatorio(contagem_falhas, nome_arquivo_saida):

    # Usa a variável de saída e não esquece das aspas quando for chamar lá embaixo!
    with open(nome_arquivo_saida, 'w') as arquivo_saida:
        for ip, falhas in contagem_falhas.items():
            if falhas >= 3:
                arquivo_saida.write(f"{ip} - {falhas} falhas\n")


# --- Execução principal do script ---
# Aqui a mágica acontece na ordem certa:

# Passo 1: Lê o txt e guarda a lista na variável 'dados'
dados = ler_logs('logs.txt')

# Passo 2: Pega os 'dados', analisa e guarda o dicionário na variável 'falhas_encontradas'
falhas_encontradas = analisar_falhas(dados)

# Passo 3: Pega o dicionário e gera o arquivo final
gerar_relatorio(falhas_encontradas, 'relatorio_alerta.txt')

print("Análise concluída! Verifique o arquivo relatorio_alerta.txt")
