from math import hypot

oposto = float(input("digitie o cateto oposto: "))
adjacente = float(input("digitie o cateto adjacente: "))
hipotenusa = hypot(oposto, adjacente)
print(f"A hipotenusa vai medir {hipotenusa:.2f} cm")