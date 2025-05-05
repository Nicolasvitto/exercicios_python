d = int(input("quantos dias ficou com o carro: "))
km = float(input("digita quantos km você percorreu com o carro KM: "))
P1= d * 60
P2 = km * 0.15
valor_total = P1 + P2
print(f"o valor total a ser pago é de R${valor_total:.2f}")