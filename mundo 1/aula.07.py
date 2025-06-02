n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))
media = (n1 + n2) /2
print("=-"*30)
print("media = {:.1f}".format(media))


if  4.5 <= media  <= 4.9:
    
    print("arendodamos sua media para: 5")
    print("APROVADO!")
    print("=-"*30)
else:
    
    print("reprovado!")
    print("=-"*30)