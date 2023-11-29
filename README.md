# Simulador de Memória

## Marcio Lima e Bruno Froza

Este é um simulador de memória desenvolvido em Python que implementa duas abordagens de busca de palavras em um conjunto de dados. O simulador opera em dois modos: SAM (Sequential Access Memory) e RAM (Random Access Memory). O objetivo é buscar por uma palavra específica em um arquivo de palavras e medir o tempo de execução em cada modo.

## Funcionalidades

- **CARREGAR ARQUIVO DE TEXTO:** Permite carregar um arquivo de texto contendo um conjunto de palavras.
- **SAM (Sequential Access Memory):** Realiza uma busca sequencial pela palavra no arquivo.
- **RAM (Random Access Memory):** Realiza uma busca aleatória pela palavra no arquivo.
- **BUSCAR POR UMA INFORMAÇÃO:** Permite ao usuário digitar uma palavra para buscar no conjunto de palavras.
- **Armazenamento de Dados:** Armazena os resultados da busca, incluindo a palavra, o número de iterações e o tempo total de execução.
- **Criação de Gráficos:** Gera gráficos para visualizar o tempo total de execução para cada palavra em cada modo.

## Estrutura do Projeto

- **`codigo.py´:** Contém o código principal que implementa as funcionalidades do simulador.
- **`resultSAM.txt´:** Arquivo para armazenar os resultados da busca em modo SAM.
- **`resultRAM.txt´:** Arquivo para armazenar os resultados da busca em modo RAM.
- **`armazenadoRAM.txt´:** Arquivo para armazenar os resultados da busca em modo RAM com informações armazenadas.
- **`palavras.txt´:** Arquivo de texto que contém o conjunto de palavras.
- **`README.txt´:** Este arquivo, fornecendo informações sobre o simulador.

## Como Usar

1. Digite o nome do arquivo e sua extensão "palavras.txt" por exemplo.
2. Execute o programa e escolha entre as opções 1 (SAM) e 2 (RAM).
3. Digite a palavra desejada para buscar no conjunto de palavras.
4. Os resultados da busca serão exibidos no console e armazenados nos arquivos correspondentes.
5. Os gráficos podem ser gerados automaticamente a cada quinta execução.
OBS: Existem 3 arquivos Simulador Memória.py, Simulador Memória RAM.py e Simulador Memória - Gráfico.py. O primeiro é a versão mais básica, realiza apenas as funções das memórias e mostra no terminal. O segundo realiza as mesmas funções, mas mostra em formato de gráfico, comparando o número de iterações e o tempo de execução, conforme o tipo de memória escolhido e se já está salvo na memória Principal. O terceiro é a versão mais próxima da memória RAM utilizada em computadores. Inicialmente, o programa lê o arquivo, este servirá como um "HD", onde o programa irá procurar as palavras caso não estejam armazenadas na memória RAM. Logo após lê-las, ele salva na memória RAM, que possui apenas 5 espaços (podem ser mudados na linha de código). Esses têm uma fila de prioridade, o último que foi acessado é excluído da memória. Desta forma, caso eu procure alguma palavra que já tenha passado pela RAM e ainda esteja armazenada, o programa realizará uma pesquisa aleatória dentro do dicionário na qual foi armazenada, caso já tenha saído. Realizará a pesquisa novamente no arquivo que contém as palavras.

## Dependências

- Python 3.x
- Biblioteca matplotlib para a geração de gráficos. Instale usando `pip install matplotlib`.
- Recomendamos que utilize o Visual Studio Code.
- Um arquivo contendo palavras para realizar a busca

## Observações

- Evite alterar os nomes dos arquivos ou a estrutura do projeto para garantir o correto funcionamento do simulador.
- Certifique-se de que o arquivo palavras.txt contém o conjunto de palavras apropriado.
- Existem dois códigos: um possui apenas as bibliotecas padrões e funciona pelo uso do terminal. O outro precisa da instalação da biblioteca matplotlib para gerar o gráfico.
