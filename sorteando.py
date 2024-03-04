from random import shuffle

lista = []
contador = 1

while True:
    nome = input(f'Digite o {contador}º nome (Digite "sair" para encerrar): ')
    contador += 1
    if nome.lower() == 'sair':
        break
    lista.append(nome)

shuffle(lista)

print(f'A ordem de apresentação é: {lista}')