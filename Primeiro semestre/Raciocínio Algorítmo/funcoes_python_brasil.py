'''
Faça um programa para imprimir:

    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
https://learn-us-east-1-prod-fleet02-xythos.learn.cloudflare.blackboardcdn.com/5df7dfcfaf23d/140267?X-Blackboard-Expiration=1618801200000&X-Blackboard-Signature=F080t2GkV34hhPZBye%2B1w%2F2lxNSZin%2F38dQVUlJhlD8%3D&X-Blackboard-Client-Id=528696&response-cache-control=private%2C%20max-age%3D21600&response-content-disposition=inline%3B%20filename%2A%3DUTF-8%27%2705.%2520Func%25CC%25A7o%25CC%2583es.pdf&response-content-type=application%2Fpdf&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20210418T210000Z&X-Amz-SignedHeaders=host&X-Amz-Expires=21600&X-Amz-Credential=AKIAZH6WM4PL5SJBSTP6%2F20210418%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=ca4aa82980b44993b1c1c141410c55d892292b5ab858985a712230389606ae97

'''

def values():
    n = int(input('Digite um num:'))
    i = 0
    valor = ''
    while i < n:
        i += 1
        valor += str(i)
        print(valor)


values()







