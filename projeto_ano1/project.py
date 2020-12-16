from datetime import datetime

escrever = "projeto.txt"

def celToFar(cValue):
    farenheit = (float(cValue) * (9 / 5)) + 32
    return farenheit


def farToCel(fValue):
    celcius = ((float(fValue) - 32) * (5 / 9))
    return celcius

def writeData(respUser, result):
    
    now = datetime.now()

    fescrever = open(escrever, 'a')
    fescrever.write(f"Data da consulta: {str(now)} // Graus: {result}\n")
    fescrever.close()


respUserRelatorio = input(f'O relatório esta no arquivo {escrever}, deseja abrir? [S/n]')

if(respUserRelatorio.upper() == 'S'):
    target = open(escrever, "r")
    print(target.read())


respUserGrau = input('\n[F]arenheit para Celcius / [C]elcius para Farenheit, >')

if (respUserGrau.upper() == 'C'):
    farenheitRes = celToFar(input('Valor em Celcius: '))
    farData = (f"{farenheitRes}º farenheit")
    writeData(respUserGrau, farData)

if (respUserGrau.upper() == 'F'):
    celciusRes = farToCel(input('Valor em Farenheit: '))
    celcData = (f"{celciusRes}º celcius")
    writeData(respUserGrau, celcData)
