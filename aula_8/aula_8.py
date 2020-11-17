formatter = "{}, {}, {} e {}"

print(formatter.format("a", "b", "c", "d"))
print(formatter.format(1, 2, 3, 4))

nome = "Sara"
idade = "31"
peso = "55"

format2 = "Eu me chamo {}, tenho {} anos e peso {} kilos"

texto = format2.format(nome, idade, peso)
print(texto)


dia = "05"
mes = 11
ano = 1988

date = "{} / {} / {}"
date_br = date.format(dia, mes, ano)
date_us = date.format(mes, dia, ano)

print("BR: " + date_br)
print("US: " + date_us)