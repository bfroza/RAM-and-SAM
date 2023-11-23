import time
import random

#Bruno e Marcio 

palavras_ram = {}
acesso = 0
maior_valor = 0

menor_valor = 0
chave_menor_valor = 0

def mem_ram_sam():
    global acesso, maior_valor  
    var = input("Digite uma palavra: ")
    inicio = time.time()
    acesso += 1
    
    if var not in palavras_ram:
        cont = 1
        try:
            with open(local, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.read()
                palavras = conteudo.split()

            for palavra in palavras:
                if var == palavra:
                    print(f"Foram realizadas {cont} iterações para achar a palavra '{var}'")
                    if var in palavras_ram:
                        palavras_ram[var][0] += 1
                    else:
                        palavras_ram.update({var: [acesso, cont]})
                    fim = time.time()
                    tempo_total = fim - inicio
                    print(f"Tempo total de execução: {tempo_total} segundos")
                    print("Palavra salva na Memória RAM")
                    break

                cont += 1

        except FileNotFoundError:
            print("Arquivo não encontrado.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    else:
        while True:
            global menor_valor
            global chave_menor_valor
            sorteio = random.choice(list(palavras_ram.keys()))
            chave = sorteio
            if chave == var:
                inicio = time.time()
                print("O valor está na memória RAM")
                print()
                for chave, valor_lista in palavras_ram.items():
                    if valor_lista[0] > maior_valor:
                        maior_valor = valor_lista[0]
                palavras_ram[sorteio][0] = int(maior_valor) + 1
                fim = time.time()
                tempo_total = fim - inicio
                print(f"Tempo total de execução: {tempo_total} segundos até encontrar a palavra '{var}'")
                print()
                # print(maior_valor)
                break

    if len(palavras_ram) >= 5:
        menor_valor = 10000000000
        for chave, valor_lista in palavras_ram.items():
            if valor_lista[0] < menor_valor:
                menor_valor = valor_lista[0]
                chave_menor_valor = chave
        print(f'A palavra "{chave_menor_valor}" foi excluida da RAM')
        print(f'A palavra "{var}" foi adicionada a RAM')
        palavras_ram.pop(chave_menor_valor)

local = input("Digite o nome do arquivo para carregar as palavras: ")
while True:
    try:
        escolha = input("Escolha 1 para começar e 0 para parar: ")
        if int(escolha) == 1:
            mem_ram_sam()
            print(palavras_ram)
            print()
            # print(len(palavras_ram))
        elif int(escolha) == 0:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Digite um número válido.")
