ler = "ler.txt"
escrever = "escrever.txt"

fler = open(ler, "r")
data = fler.read()
fler.close()

fescrever = open(escrever, 'a')
fescrever.write(data + '\n')
fescrever.close()