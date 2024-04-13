from random import *
num = randint(0,100)
numUsuario = 101

while num != numUsuario:
    numUsuario = int(input("Digite um numero entre 0 e 100:\n"))
    if num > numUsuario:
        print(num)
        print(f"O numero é maior que {numUsuario}")
    elif num < numUsuario:
        print(f"O numero é menor que {numUsuario}")
    else:
        print("-------------------------------")
        print("Parabens voce ganhou!!!")
        print(f"O numero era {numUsuario}")

              