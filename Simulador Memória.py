import time
import random
palavras_ram = {}
absolute = True
def codigoSAM():
    sam = input("Digite uma palavra: ")
    inicio = time.time()

    with open(r'palavras.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()

    cont = 1  
    for palavra in palavras:
        if sam == palavra:
            print(f'Foram realizadas {cont} iterações para achar a palavra {sam}')
            fim = time.time()
            tempo_total = fim - inicio
            print(f"Tempo total de execução: {tempo_total} segundos")
            break  
        cont += 1

def codigoRAM():
    ram = input("Digite uma palavra: ")
    inicio = time.time()  
    with open(r'palavras.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        palavras = conteudo.split()
        print(type(palavras))
   
    cont = 0

    while True:
        palavra_aleatoria = random.choice(palavras)
        cont += 1

        if palavra_aleatoria == ram and palavra_aleatoria not in palavras_ram:
            indice = palavras.index(palavra_aleatoria)
            palavras_ram.update({palavra_aleatoria:indice})
            fim = time.time()
            tempo_total = fim - inicio
            print(f'Foram realizadas {cont} iterações para achar a palavra {ram} no indice {indice}')
            print(f"Tempo total de execução: {tempo_total} segundos")
            cont = 0
            break
       
        elif palavra_aleatoria == ram and palavra_aleatoria in palavras_ram:
            repet = 0
            inicio = time.time()  
            print("Esse valor já passou pela memória")
            for posicao, (chave, valor) in enumerate(palavras_ram.items()):
                if chave == palavra_aleatoria:
                    indice = valor
                    print(f'Foram realizadas {repet} iterações para achar a palavra {chave} no índice {indice} do arquivo original na posição {posicao} da memória RAM')

                    fim = time.time()
                    tempo_total = fim - inicio
                    print(f"Tempo total de execução: {tempo_total} segundos")
                repet =+1

            break
   
while True:
    try:
        escolha = int(input("Escolha o código (1 ou 2) ou 0 para sair: "))
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