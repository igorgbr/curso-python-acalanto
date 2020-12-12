def pega_linha(n, f):
    n = int(n)-1
    f.seek(0)
    lines = f.readlines()
    return lines[n]


file = open('texto.txt')

linha1 = pega_linha(input('qual linha vc quer ler? > '), file)
print(linha1)

linha2 = pega_linha(input('qual linha vc quer ler? > '), file)
print(linha2)

print(linha1 + linha2)
