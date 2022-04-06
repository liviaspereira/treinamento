"""Construa um programa que recebe um valor, integer , e retorna uma lista de seus múltiplos até outro valor, limit . Se limite for um múltiplo de inteiro, ele também deve 

ser incluído. Só haverá inteiros positivos passados para a função, não consistindo em 0. O limite será sempre maior que a base. Por exemplo, se os parâmetros passados

forem (2, 6), a função deve retornar [2, 4, 6] pois 2, 4 e 6 são os múltiplos de 2 até 6. Se puder, tente escrevê-lo em apenas uma linha de código."""


def retorna_multiplos():
    base = int(input("Digite um número: "))
    limite = int(input("Digite um número: "))
    multiplos = []
    for i in range(0, limite + 1):
        if i % base == 0:
            multiplos.append(i)
    return multiplos

print(retorna_multiplos()) 