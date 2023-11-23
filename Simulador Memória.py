import time
import random
palavras_ram = {}
absolute = True
def codigoSAM():
    sam = input("Digite uma palavra: ")
    inicio = time.time()

    with open(local, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()

    cont = 1  
    try:
        for palavra in palavras:
            if sam == palavra:
                print(f'Foram realizadas {cont} iterações para achar a palavra {sam}')
                fim = time.time()
                tempo_total = fim - inicio
                print(f"Tempo total de execução: {tempo_total} segundos")
                break  

            cont += 1

    except:
        print("Essa palavra não está no arquivo")

def codigoRAM():
    ram = input("Digite uma palavra: ")
    inicio = time.time()  
    
    if(ram not in palavras_ram):
        with open(local, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            print(type(palavras))
        verdade = 1
    else:
        verdade = 0
            
   
    cont = 0

    while True:
        repet = 0
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
            palavras_ram.update({palavra_aleatoria:indice})
            fim = time.time()
            tempo_total = fim - inicio
            print(f'Foram realizadas {cont} iterações para achar a palavra {ram} no índice {indice}')
            print(f"Tempo total de execução: {tempo_total} segundos")
            cont = 0
            break  
       
        elif palavra_aleatoria == ram and palavra_aleatoria in palavras_ram:
            inicio = time.time()  
            print("Esse valor já passou pela memória")
            for posicao, (chave, valor) in enumerate(palavras_ram.items()):
                if chave == palavra_aleatoria:
                    indice = valor
                    repet+=1
                    print(f'Foram realizadas {repet} iterações para achar a palavra {chave} no índice {indice} do arquivo original na posição {posicao} da memória RAM')

                    fim = time.time()
                    tempo_total = fim - inicio
                    print(f"Tempo total de execução: {tempo_total} segundos")
                

            break  

local = input("Digite o nome do arquivo para carregar as palavras: ")  
while True:
    try:
        escolha = int(input("Escolha o código (1 SAM ou 2 RAM) ou 0 para sair: "))
        if escolha == 1:
            codigoSAM()
        elif escolha == 2:
            codigoRAM()
        elif escolha == 0:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Digite um número válido.")
