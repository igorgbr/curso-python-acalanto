from sys import argv

script, arg1, arg2 = argv


def print_script(arg):
    print(f"Es sou o script {arg}")


def print_primeiro(arg):
    print(f"O primeiro argumento foi {arg}")


def print_segundo(arg):
    print(f"O segundo argumento foi {arg}")


print_script(script)
print_primeiro(arg1)
print_segundo(arg2)
