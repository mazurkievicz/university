'''
AAP2:
A atividade consiste em trabalhar os algoritmos em 5 funções:

1. Colocar todos os algoritmos dentro de funções.
2. Adicionar os parâmetros corretos nas funções.
3. Adicionar os retornos corretos das funções.
4. Adicionar os argumentos corretos nas chamadas das funções.
5. Adicionar os comentários dos comportamentos das funções usando aspas triplas (PEP-0257).
6. Adicionar os comentários dos parâmetros das funções (PEP-0257).
7. Adicionar os comentários dos retornos das funções: (PEP-0257).
8. Corrigir todos os 60 problemas na formatação de código seguindo o estilo PEP-0008.
Em breve disponibilizo os códigos
'''


def nums_primes(upper=5):
    """
    Retorna o número primo abaixo do upper

    :param upper: Máximo valor que vai determinar números primos, default = 5
    :return: Vai retornar uma lista com valores primos
    """
    # Declaração de lista
    r = []
    #  Incrementa n de 2 até o valor de upper + 1
    for n in range(2, upper + 1):
        # Incrementa i de 2 até o valor n (que é um intervalo aberto)
        for i in range(2, n):
            # Verifica se resto é 0, se sim, para, se não,
            # verifica se chegou ao final da contagem, e inclui n na lista
            if n % i == 0:
                break
            elif (n - 1) == i:
                r.append(n)
    return r


def factors_nums(x=6):
    """
    Calcula os fatores de um número inteiro

    :param x: Inteiro com default 6
    :return: Lista de fatores
    """
    # Declaração de lista
    r = []
    # Incrementa i de 1 até x + 1
    for i in range(1, x + 1):
        # Se o resto de x for zero, ele adiciona i à lista
        if x % i == 0:
            r.append(i)
    return r


def mmc_calculator(x=2, y=7):
    """
    Retorna o mínimo múltiplo comum entre dois valores

    :param x: Valor default 2
    :param y: Valor default 7
    :return: Retorna um valor inteiro que é o MMC
    """
    # Atribui o maior valor entre x e y à g
    if x > y:
        g = x
    else:
        g = y
    # Enquanto não houver um break, o while vai rodar
    while True:
        # Se o resto de x e de y for 0, ele registra g como common,
        #  e quebra o laço
        if g % x == 0 and g % y == 0:
            common = g
            break
        # É um contador, que a cada repetição do laço, adiciona 1 à g
        g += 1
    return common


def mdc_calculator(x=6, y=18):
    """
    Calcula o máximo divisor comum entre dois números

    :param x: Inteiro default 6
    :param y: Inteiro default 18
    :return: O máximo divisor comum
    """
    # Inicializa a variável common com valor 0
    common = 0
    # Verifica qual dos valores x ou y é maior, e atribui à s
    if x > y:
        s = y
    else:
        s = x
    # Incrementa i de 1 à s + 1
    for i in range(1, s + 1):
        # Se o módulo for 0, atribui i à common
        if x % i == 0 and y % i == 0:
            common = i
    return common


def upward_list(lst):
    """
    Ordena a lista de forma ascendente

    :param lst: É uma lista de valores
    :return: Lista ordenada ascendente
    """
    # Incrementa i de 0 até o tamanho de lst
    for i in range(len(lst)):
        # Incrementa j de i + 1, até o tamanho de lst
        for j in range(i + 1, len(lst)):
            # Se lst na posição i, for maior que na posição j,
            # troca os valores de posição
            if lst[i] > lst[j]:
                tmp = lst[i]
                lst[i] = lst[j]
                lst[j] = tmp
    return lst

# Verifica se foi usado como programa principal ou biblioteca
# Caso seja o programa principal (main), imprime todos os retornos das funções


if _name_ == '_main_':
    prime = nums_primes()
    print(prime)
    factors = factors_nums()
    print(factors)
    mmc = mmc_calculator()
    print(mmc)
    mdc = mdc_calculator()
    print(mdc)
    upward = upward_list([2, 3, 1])
    print(upward)