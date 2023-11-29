import time
import random


#Bruno e Marcio 

palavras_ram = {}
absolute = True

def codigoSAM(local):
    sam = input("Digite uma palavra: ")
    inicio = time.time()

    try:
        with open(local, 'r', encoding='utf-8') as arquivo:
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

    except FileNotFoundError:
        print("Arquivo não encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def codigoRAM(local):
    ram = input("Digite uma palavra: ")
    inicio = time.time()

    if ram not in palavras_ram:
        try:
            with open(local, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                palavras = conteudo.split()
        except FileNotFoundError:
            print("Arquivo não encontrado.")
            return
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return
        verdade = 1
    else:
        verdade = 0

    cont=0

    while True:
        
        if verdade:
            palavra_aleatoria = random.choice(palavras)
        else:
            palavra_aleatoria = ram
        cont += 1
        if cont > 20000000:
            print("Essa palavra não está no arquivo")
            break
        if palavra_aleatoria == ram and palavra_aleatoria not in palavras_ram.keys():
            indice = palavras.index(palavra_aleatoria)
            palavras_ram.update({palavra_aleatoria: indice})
            fim = time.time()
            tempo_total = fim - inicio
            print(f'Foram realizadas {cont} iterações para achar a palavra {ram} no índice {indice}')
            print(f"Tempo total de execução: {tempo_total} segundos")
            cont = 0
            break
        elif palavra_aleatoria == ram and palavra_aleatoria in palavras_ram.keys():
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
            break
local = input("Digite o nome do arquivo para carregar as palavras: ")
while True:
    try:
        escolha = int(input("Escolha o código (1 SAM ou 2 RAM) ou 0 para sair: "))
        if escolha == 1:
            codigoSAM(local)
        elif escolha == 2:
            codigoRAM(local)
        elif escolha == 0:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Digite um número válido.")
