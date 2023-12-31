import time
import random
import matplotlib.pyplot as plt

palavras_ram = {}
absolute = True
pedir = 0
repet = 0

#Bruno e Marcio 

def codigoSAM():
    global pedir
    sam = input("Digite uma palavra: ")
    inicio = time.time()

    with open(local,'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()

    cont = 1
    tempo_total = 0

    for palavra in palavras:
        if(cont > 20000000):
            print("Essa palavra não está no arquivo")
            break
        if sam == palavra:
            print(f'Foram realizadas {cont} iterações para achar a palavra {sam}')
            fim = time.time()
            tempo_total = fim - inicio
            print(f"Tempo total de execução: {tempo_total} segundos")
            salvar_resultadosSAM(sam, cont, tempo_total)
            pedir += 1
            break
        cont += 1

def salvar_resultadosSAM(sam, cont, tempo_total):
    with open('resultSAM.txt', 'a', encoding='utf-8') as result_file:
        result_file.write(f'Palavra: {sam}\n')
        result_file.write(f'Iterações: {cont}\n')
        result_file.write(f'Tempo total: {tempo_total} segundos\n\n')

def codigoRAM():
    global pedir
    ram = input("Digite uma palavra: ")
    inicio = time.time()
    
    if(ram not in palavras_ram):
        with open(local, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            #print(type(palavras))
        verdade = 1
    else:
        verdade = 0

    cont = 0
   
    tempo_total = 0
    posicao = 0

    while True:
        global repet
        if verdade:
            palavra_aleatoria = random.choice(palavras)
        else:
            palavra_aleatoria = ram
      
        cont += 1
       
        if(cont > 20000000):
            print("Essa palavra não está no arquivo")
            break
        if palavra_aleatoria == ram and palavra_aleatoria not in palavras_ram:
            indice = palavras.index(palavra_aleatoria)
            palavras_ram.update({palavra_aleatoria: indice})
            fim = time.time()
            tempo_total = fim - inicio
            print(f'Foram realizadas {cont+1} iterações para achar a palavra "{palavra_aleatoria}" no índice {indice} no arquivo original')
            print(f"Tempo total de execução: {tempo_total} segundos")
            salvar_resultadosRAM(cont, tempo_total, palavra_aleatoria)
            pedir += 1
            break
        
        elif palavra_aleatoria == ram and palavra_aleatoria in palavras_ram:
            inicio = time.time()
            print("Esse valor já passou pela memória")
            cont=0
            while True:
                chave = random.choice(list(palavras_ram.keys()))
                if chave == palavra_aleatoria:
                    print(f'Foram realizadas {cont} iterações para achar a palavra "{chave}" ')
                    fim = time.time()
                    tempo_total = fim - inicio
                    print(f"Tempo total de execução: {tempo_total} segundos")
                    break
                cont+=1
            #busca realizada por for, iterando palavra por palavra
            '''
            for posicao, (chave, valor) in enumerate(palavras_ram.items()):
                if chave == palavra_aleatoria:
                    indice = valor
                    repet +=1
                    print(f'Foram realizadas {repet} iterações para achar a palavra "{chave}" no índice {indice} do arquivo original e na posição {posicao} da memória RAM')

                    fim = time.time()
                    
                    tempo_total = fim - inicio
                    print(f"Tempo total de execução: {tempo_total} segundos")
            salvar_resultadosArmazenadosRAM(repet, tempo_total, chave, indice, posicao)
            '''
            salvar_resultadosArmazenadosRAM(cont, tempo_total, chave)
            pedir += 1
            break
        
#funções para salvar o resultado, quando a função realizava busca por for           
'''
def salvar_resultadosRAM(cont, tempo_total, ram, indice, posicao):
    with open('resultRAM.txt', 'a', encoding='utf-8') as result_file:
        result_file.write(f'Palavra: {ram}\n')
        result_file.write(f'Índice no arquivo original: {indice}\n')
        result_file.write(f'Posição na memória RAM: {posicao}\n')
        result_file.write(f'Iterações: {cont}\n')
        result_file.write(f'Tempo total: {tempo_total} segundos\n\n')

def salvar_resultadosArmazenadosRAM(repet, tempo_total, ram, indice, posicao):
    with open('armazenadoRAM.txt', 'a', encoding='utf-8') as result_file:
        result_file.write(f'Palavra: {ram}\n')
        result_file.write(f'Índice no arquivo original: {indice}\n')
        result_file.write(f'Posição na memória RAM: {posicao}\n')
        result_file.write(f'Iterações: {repet}\n')
        result_file.write(f'Tempo total: {tempo_total} segundos\n\n')
'''
def salvar_resultadosRAM(cont, tempo_total, palavra_aleatoria):
    with open('resultRAM.txt', 'a', encoding='utf-8') as result_file:
        result_file.write(f'Palavra: {palavra_aleatoria}\n')
        result_file.write(f'Iterações: {cont}\n')
        result_file.write(f'Tempo total: {tempo_total} segundos\n\n')

def salvar_resultadosArmazenadosRAM(cont, tempo_total, chave):
    with open('armazenadoRAM.txt', 'a', encoding='utf-8') as result_file:
       result_file.write(f'Palavra: {chave}\n')
       result_file.write(f'Iterações: {cont}\n')
       result_file.write(f'Tempo total: {tempo_total} segundos\n\n')

def calcular_medias(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        linhas = []
        linhas = arquivo.readlines()

        total_iteracoes = 0
        total_tempo = 0
        contagem = 0

        for linha in linhas:
            if linha.startswith('Iterações:'): #pesquisa as linhas no arquivo que começam com esse nome
                total_iteracoes += int(linha.split(":")[1].strip())
                contagem += 1
            elif linha.startswith('Tempo total:'): #pesquisa as linhas no arquivo que começam com esse nome
                total_tempo += float(linha.split(":")[1].strip().split()[0])

        if contagem == 0:
            return 0, 0  

        media_iteracoes = total_iteracoes / contagem
        media_tempo = total_tempo / contagem

    return media_iteracoes, media_tempo

local = input("Digite o nome do arquivo para carregar as palavras: ")
while True:
    try:
        escolha = int(input("Escolha o código (1 para SAM ou 2 RAM) ou 0 para sair: "))
        if escolha == 1:
            codigoSAM()
        elif escolha == 2:
            codigoRAM()
        elif escolha == 0:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
        if pedir %5 == 0:
            quer = input("Quer um gráfico para mostrar o comparativo de cada tipo de Memória? (s or n)").lower()
            lista = ["s","sim","1"]
            if(quer in lista):
                media_iteracoes_sam, media_tempo_sam = calcular_medias('resultSAM.txt')
                media_iteracoes_ram, media_tempo_ram = calcular_medias('resultRAM.txt')
                media_iteracoes_ram_armazenada, media_tempo_ram_armazenada = calcular_medias('armazenadoRAM.txt')

                plt.figure(figsize=(10, 5))
                plt.bar(['SAM', 'RAM', 'RAM Armazenada'], [media_iteracoes_sam, media_iteracoes_ram, media_iteracoes_ram_armazenada])
                plt.xlabel('Função')
                plt.ylabel('Média de Iterações')
                plt.title('Média de Iterações por Função')
                plt.show()

                plt.figure(figsize=(10, 5))
                plt.bar(['SAM', 'RAM', 'RAM Armazenada'], [media_tempo_sam, media_tempo_ram, media_tempo_ram_armazenada])
                plt.xlabel('Função')
                plt.ylabel('Média de Tempo Total (s)')
                plt.title('Média de Tempo Total por Função')
                plt.show()
            else:
                print("Ok, vamo seguir")

    except ValueError:
        print("Digite um número válido.")
