#6) Leia e apresente dois números inteiros.
n1 = input('Digite o primeiro número inteiro: ')
n2 = input('Digite o segundo número inteiro: ')
print('Os número inteiros digitados foram: ', n1, 'e', n2)


#>>>>>>>Caso queira utilizar TRY e EXCEPT para sinalizar que os números dever ser INTEIROS: <<<<<<<<<
# try:
#     inteiro1 = int(n1)
#     inteiro2 = int(n2)
#     print('Os dois números inteiros digitados foram:', n1, 'e', n2)

# except ValueError:
#     print('Número inteiro não encontrado em um dos números')