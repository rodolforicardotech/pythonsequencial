#5) Leia e apresente um número inteiro.
# x = input('Digite um número inteiro: ')
# print(x)

numero = input('Digite um número inteiro: ')

try:
    inteiro = int(numero)
    print("O número INTEIRO digitado foi:", inteiro, '\n')

except ValueError:
    print("Este não é um número inteiro!")