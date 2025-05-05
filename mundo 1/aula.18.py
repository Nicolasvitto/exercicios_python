from math import radians, cos, sin, tan
converter = float(input("digite um valor: "))
num1 = radians(converter)
seno = sin(num1)
cosseno = cos(num1)
tangente = tan(num1)
print("o seno de {} é {:.2f}".format(converter, seno))
print("o cosseno de {} é {:.2f}".format(converter, cosseno))
print("a tangente de {} é {:.2f}".format(converter, tangente))

