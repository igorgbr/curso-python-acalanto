def exibe_linha(n, f):
    n = int(n)-1
    lines = f.readlines()
    print(lines[n])


file = open('texto.txt')
exibe_linha(input('qual linha vc quer ler? > '), file)
