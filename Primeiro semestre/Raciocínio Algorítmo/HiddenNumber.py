import random
numeroculto=random.randint(0,100)
print('O JOGO DO NÚMERO OCULTO')
tentativas=0
numeros=0
numeros_repetidos=[]
maior_numero = 0
menor_numero = 0

while tentativas <10:
    print('Número da sua tentativa:',tentativas+1,'.Você tem 10 tentativas ao total nesse jogo!!')
    numeros=int(input('Digite um número de 0 a 100:  '))
    if numeros in numeros_repetidos:
        print('Você já digitou esse número antes! Escolha outro')
        continue
    else:
        numeros_repetidos.append(numeros)
        if tentativas == 0:
            maior_numero = numeros
            menor_numero = numeros
        else:
            if numeros > maior_numero:
                maior_numero = numeros
            elif numeros < menor_numero:
                menor_numero = numeros
    tentativas+=1
    if numeros > numeroculto:
        print('Esse número é maior que o número oculto!!')
    elif numeros < numeroculto:
        print('Esse número é menor que o número oculto!!')
    else:
        print('Parabéns!! Você conseguiu acertar o número oculto :)')
        break
else:
    print('Que pena! Você não conseguiu acertar o número oculto :(')
print('O número oculto era:',numeroculto,'!')
print(maior_numero,'Foi o maior número digitado!')
print(menor_numero,'Foi o menor número digitado!')