resp = "s"
contador = 0
soma = 0
while resp == "s" or resp == "s": 
    num = float(input("digite um numero: "))
    soma += num
    resp = str(input("deseja continuar? (S/N)"))
    contador+= 1
    media = soma / contador
print("a media dos numeros digitados é %.2f" %media)    