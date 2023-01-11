arquivo = open("palavras.txt", "w")
print(arquivo) # Mostra nome do arquivo, modo (w, a ou r) e UTF-8

arquivo.write("banana")
arquivo.write("melancia")
arquivo.write("abacate")

arquivo.close()

arquivo = open("palavras.txt", "w")
arquivo.write("banana")

arquivo.close()

arquivo = open("palavras.txt", "w")

arquivo.write("banana\n")
arquivo.write("melancia\n")
arquivo.write("abacate\n")
arquivo.write("morango\n")
arquivo.write("abacaxi\n")
arquivo.write("amora\n")

arquivo.close()

# Trabalhando em modo leitura
arquivo = open("palavras.txt", "r") # r -> modo leitura

print(arquivo.read())
print(arquivo.read())

arquivo.close()
