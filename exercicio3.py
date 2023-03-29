import json;

f = open('dados.json')

valor = []

data = json.load(f)

for i in data:
    if(i['valor'] != 0):
        valor.append(i['valor'])

menor = valor[0]
maior = valor[0]
soma = 0

for i in valor:
    soma = soma + i
    if(menor > i):
        menor = i
    if(maior < i):
        maior = i

soma /= len(valor)
contador = 0

for i in valor:
    if(i > soma):
        contador = contador + 1

print('Menor valor: ', menor )
print('Maior valor: ', maior)
print('Média mensal: ', soma)
print('Dias acima da média mensal: ', contador)