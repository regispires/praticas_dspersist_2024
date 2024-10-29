import sys

linha = sys.stdin.readline().strip()

while linha:
	# .strip() remove espaços em branco e quebras de linha extras
    print(linha)  
    linha = sys.stdin.readline().strip()