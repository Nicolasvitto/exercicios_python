""""
m = int(input("coloque quantos metros: "))

c = m * 100
mi = m * 1000
print(f"{m} metros equivalem a {c} centimetros e {mi} milímetros")"""


from util import receber_entrada

#conversão de metros para centimetros
def converte_para_centimetros(metros):
    return metros * 100

#converte de metros para milímetros
def converte_para_milímetros(metros):
    return metros * 1000

# função principal
def main():
    
    metros = receber_entrada("digite os Metros: ")
    
    print(f"Metros para Centimetros: {converte_para_centimetros(metros)}")
    print(f"Metros para Milímetros: {converte_para_milímetros(metros)}")
    
if __name__ =="__main__":
    main()