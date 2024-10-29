import sys

with open("arquivo.txt", "w") as file:
    linha = input('digite algo: ')
    while linha:
        file.write(linha + '\n')
        linha = input('digite algo: ')
