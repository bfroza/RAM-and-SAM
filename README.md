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

1. Execute o programa e escolha entre as opções 1 (SAM) e 2 (RAM).
2. Digite a palavra desejada para buscar no conjunto de palavras.
3. Os resultados da busca serão exibidos no console e armazenados nos arquivos correspondentes.
4. Os gráficos podem ser gerados automaticamente a cada quinta execução.

## Dependências

- Python 3.x
- Biblioteca matplotlib para a geração de gráficos. Instale usando `pip install matplotlib`.
- Recomendamos que utilize o Visual Studio Code.
- Um arquivo chamado `palavras.txt` para realizar a busca

## Observações

- Evite alterar os nomes dos arquivos ou a estrutura do projeto para garantir o correto funcionamento do simulador.
- Certifique-se de que o arquivo palavras.txt contém o conjunto de palavras apropriado.
- Existem dois códigos: um possui apenas as bibliotecas padrões e funciona pelo uso do terminal. O outro precisa da instalação da biblioteca matplotlib para gerar o gráfico.
