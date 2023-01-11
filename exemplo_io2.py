# Trabalhado em modo de leitura
arquivo = open("palavras.txt", "r") # r -> modo de leitura

# Usando uma estrutura de repetição para ler todas as linhas:
for linha in arquivo:
    print("Linha capturada:", linha)

arquivo.close()

# Trabalhado em modo de leitura
arquivo = open("palavras.txt", "r") # r -> modo de leitura

# Lendo apenas uma linha do arquivo:
linha = arquivo.readline()
print("Única linha capturada: ", linha)

linha = arquivo.readline()
print("Única linha capturada: ", linha)
print("Única linha capturada: ", linha)

# Para remover o \n após a palavra capturada:
linha = linha.strip()

print("Única linha capturada: ", linha)
print("Única linha capturada: ", linha)

arquivo.close()