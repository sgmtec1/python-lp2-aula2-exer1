''' Preencha uma lista com 10 números digitados pelo usuário e exiba:
a) o maior número da lista
b) o menor número da lista
c) a média dos números contidos na lista
d) todos os números menores do que a média calculada no item anterior
'''

lista = []
for i in range(10):
    n = int(input('Número: '))
    lista.append(n) #inclusao de dados

maior = max(lista)
print('O maior numero ', maior)
menor = min(lista)
print('O menor numero ', menor)
media = sum(lista) / len(lista)
print('A media do numero ', media)

print('Numeros menores que a media calculada:')
for i in lista:
    if i < media:
        print(i)
