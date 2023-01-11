# Trabalhado em modo de leitura
arquivo = open("palavras.txt", "r") # r -> modo de leitura

palavras = [] # lista dinâmica!

for linha in arquivo:
    palavras.append(linha.strip())

arquivo.close()

print(palavras)
