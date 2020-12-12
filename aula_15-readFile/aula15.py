from sys import argv


reais = float(input(f"Valor em reais: "))


txt = open('1.txt')

dolar = float(txt.read())

print(f'Valor em dolar: {reais * dolar}')
