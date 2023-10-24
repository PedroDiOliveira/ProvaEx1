############################################################
##Programa que para auxiliar o funcionamento de um armazem##
############################################################

#ALUNOS: Pedro Henrique Santana Di Oliveira      RA:22302668
#        Pedro Cesar

######################
##Caminhos e imports##
######################

import os
import time
import re

caminhoLogs = 'C:\\Users\\pedro\\exercicio1\\logs.txt'

#######################################
##Funcao que cria a interdace do menu##
#######################################

def interface_menu():
    print(''' 
_________________________________________________
|                                                |
|               Menu principal                   |
|                                                |
|    1- Entrada de dados(preços e quantidade)    |
|    2- Mostrar produtos                         |
|    3- Calculo do faturamento                   |
|    4- Percentual de vendas                     |
|________________________________________________|
    
Escolha uma opcao para prosseguir:
    ''')

###################################################################
##Funcao que recebe os dados dos produtos e bota em um dicionario##  -> Elemento 1 do menu
###################################################################

def get_dados_produtos():
    produtos = {}
    j = 0
    for i in range(3):
        quantidade = int(input(f"Digite a quantidade de produtos vendidos {i}: "))
        preco = int(input(f"Digite o valor referente ao produto {i}: "))
        produtos[quantidade] = preco
    return produtos

##################################################
##Funcao que printa na tela o resultado do input##  -> Elemento 2 do menu
##################################################

def mostra_produtos(produtos):
    for quantidade, preco in produtos.items():
        print(f"O produto {j} tem {quantidade} unidades e custa R${preco:.2f}\n")
        j += 1

################################################
##Funcao que verifica se um arquivo esta vazio##
################################################

def verificaArquivoVazio(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        return not conteudo

###########################################
##Funcao que cria uma animacao de loading##
###########################################

def animacao():
    os.system("cls")
    for i in range(1, 11):  
        print("Loading [" + "=" * i + " " * (10 - i) + "] " + str(i * 10) + "%")
        time.sleep(0.3)
        os.system('cls')

###################################################
##Funcao que salva os produtos em um arquivo .txt##
###################################################

def salva_Arquivo(produtos, caminhoLogs):
    i = 0
    if not verificaArquivoVazio(caminhoLogs):
        sobrepor = int(input("Parece que já existe um save anterior! Deseja sobrepor o antigo save? (1-sim / 2-não)"))
        if sobrepor == 1:
            animacao()
            with open(caminhoLogs, 'w') as arquivo:
                arquivo.write('')
            with open(caminhoLogs, 'a') as arquivo:  
                for quantidade, preco in produtos.items():
                    arquivo.write(f"Produto {i}: Quantidade vendida: {quantidade}   Valor: R${preco:.2f}\n")
                    i += 1 
            print("")
            print("Valores atualizados com sucesso! ")
        else:
            print("")

###############################################
##Funcao que calcula o faturamento da empresa##
###############################################

def calcula_Faturamento():
    vendas = []
    produtos = leituraArquivo(caminhoLogs)

    for quantidade, preco in produtos.items():
        faturamento_produto = quantidade * preco
        vendas.append(faturamento_produto)

    faturamento_total = sum(vendas)

    return faturamento_total


####################################################################
##Funcao que le o arquivo e recebe quatidade e preco em dicionario##
####################################################################

def leituraArquivo(nome_arquivo):
    # Inicializa um dicionário vazio para armazenar as informações
    produtos = {}

    # Expressão regular para corresponder à quantidade e ao preço
    padrao = r"Quantidade: (\d+)   Valor: R\$(\d+\.\d{2})"

    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                match = re.search(padrao, linha)
                if match:
                    quantidade = int(match.group(1))
                    preco = float(match.group(2))
                    produtos[quantidade] = preco

        return produtos

    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        return {}


        
###############################################
##Funcao menu que gerencia as funcoes criadas##
###############################################

def menu():
    sair = False
    while not sair:
        interface_menu()
        opcao = int(input("Digite uma opcao: "))
        if opcao == 1:
            produtos = get_dados_produtos()
            salva_Arquivo(produtos, caminhoLogs)
        elif opcao == 2:
            mostra_produtos(produtos)
        elif opcao == 3:
            animacao()
            x = calcula_Faturamento()
            print(f"O faturamento total e de R${x:.2f}!")
            time.sleep(2)
            
        #elif opcao == 4:

menu()
