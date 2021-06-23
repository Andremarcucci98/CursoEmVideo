def maior_primo(n):
    j = n
    while j > 1 and e_primo(j) == False:
        j = j - 1
    return j


def e_primo(j):
    primo = True
    div = 2
    while j > div:
        if j % div == 0:
            primo = False
        div = div + 1
    return primo


num = int(input('Digite um numero para saber seu maior primo: '))
print(maior_primo(num))