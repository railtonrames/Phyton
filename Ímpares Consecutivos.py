n = int(input('Entre com o valor de N:'))
maior = 0
menor = 0

while n > 0:
    xy = input('Entre com o valor X/Y:').split()

    while int(xy[1]) < 1:
        xy = input('Valor de Y inválido, insira outro X/Y:').split()

    n1 = int(xy[0])
    n2 = int(xy[1])

    resto = n1 % 2


    if resto == 0:
        n1 += 1

    stop = n1+(n2*2)
    conta = range(n1, stop, 2)
    soma = 0

    for x in conta:
        soma += x

    print(soma)
    n -= 1

    if menor == 0:
        menor = soma
    if maior == 0:
        maior = soma
    elif soma > maior:
        maior = soma
    elif soma < menor:
        menor = soma

print('Maior:', maior)
print('Menor:', menor)
print('Média:', "%.2f" % ((maior+menor)/2))