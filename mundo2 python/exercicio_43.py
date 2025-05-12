"""Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)

 e mostre seu status, de acordo com a tabela abaixo:


– IMC abaixo de 18,5: Abaixo do Peso


– Entre 18,5 e 25: Peso Ideal


– 25 até 30: Sobrepeso


– 30 até 40: Obesidade


– Acima de 40: Obesidade Mórbida
"""


def get_message(message):

    return float(input(message))


def validate_message(message):

    while True:

        try:
            return get_message(message)

        except ValueError:

            print("Please enter a valid value.")


def calculate_BMI(height,weight):

    return  weight / (height * height)
    

def check_BMI(height, weight):
    
    if (calculate_BMI(height, weight)) < 18.5:

        print("underweight ")
    

    elif (calculate_BMI(height, weight)) >= 18.5 and (calculate_BMI(height, weight)) <= 25:
        print("ideal weight")
    
    elif (calculate_BMI(height, weight)) >= 25 and (calculate_BMI(height, weight)) <= 30:
        print("overweight ")
    
    elif (calculate_BMI(height, weight)) >= 30 and (calculate_BMI(height, weight)) <= 40:
        print("obesity ")
    
    else:
        print("Morbid Obesity")

def main():
    height = validate_message('enter your height: ')
    weight = validate_message('enter your weight: ')
    check_BMI(height, weight)


if __name__ == "__main__":
    main()