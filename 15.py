#15)Entrar com um ângulo em graus e apresentar: seno, co-seno, tangente, secante, cosecante e co-tangente deste ângulo.

#Precise importar uma biblioteca para encontrar os valores. Para os cálculos trigonométricos é preciso que o ângulo esteja em RADIANO. Para isso, utiliza-se uma função para converter de graus para radiano.
import math 

#poderia colocar também: from math import sin, cos, tan, radians. Para não precisar ficar digitando math.

angulo = float(input('Informe o ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
secante = 1/seno
cosecante = 1/cosseno


print('\n''Seno: {:.2f}'.format(seno),'\n''Cosseno: {:.2f}'.format(cosseno),'\n''Tangete: {:.2f}'.format(tangente),'\n''Secante: {:.2f}'.format(secante),'\n''Cosecante: {:.2f}'.format(cosecante))

#Adicionei ao print o comando {:.2f} para limitar a duas casas decimais
#Adicionei o .format para fixar a solicitação das {:.2f}