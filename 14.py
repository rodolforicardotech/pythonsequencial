# #14)Entrar com quatro números e imprimir a média ponderada, sabendo-se que os pesos
# são respectivamente: 1, 2, 3 e 4
nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))
nota03 = float(input('Digite a terceira nota: '))
nota04 = float(input('Digite a quarta nota: '))

print('A notas terão respectivamete: Peso 1, 2, 3, 4.')

mediaponderada = ((nota01*1) + (nota02*2) + (nota03*3) + (nota04*4))/(1+2+3+4)

print('\n''A média ponderada é:', mediaponderada)
