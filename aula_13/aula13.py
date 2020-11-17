from sys import argv

script, idade, peso = argv

if idade == '--help':
    print("menu de ajuda")
    print("you need 2 params, [age = 'int'] and [weight = 'float']")
    print(f"exeample: python3 {script} [age] [weight]")

print(f"{idade} anos e {peso} kilos")
