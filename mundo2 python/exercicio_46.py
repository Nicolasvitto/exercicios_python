from time import sleep

def contagem_regressiva():
    for cont in range (10, -1, -1):
        print(cont)
        sleep(0.5)
  
def main():
    
    contagem_regressiva()
    print("bummmmmm!")

if __name__ == "__main__":
    main()