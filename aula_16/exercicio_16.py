# Atribui a vriavel chamada file com o nome do arquivos
file = "base"
# Abre o arquivo
target = open(file, "r")
# le e transforma o conteudo em inteiro
data = int(target.read())

# exibe o conteudo do Arquivos
print(f"Li {data}")

qtd = int(input("quanto ver quer adicionar?"))

# adicion 1 no conteudo do arquivo
data = str(data + qtd)

# abre o arquivo para escrita
target = open(file, "w")

# escreve o num no arquivo
target.write(data)

# mostra na tela o novo numero
print(f"Escrevi {data}")

# fecha o arquivo
target.close()
