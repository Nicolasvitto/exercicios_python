"""Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você."""
import random
import time
from operator import itemgetter
from colorama import Fore, Style
from colorama import init
init()
def get_message(message):
    return input(message)
def validate_message(message):
    while True:
        try:
            return get_message(message)
        except ValueError:
            print("Por favor, insira um valor válido.")
def get_computer_choice():
    choices = ['Pedra', 'Papel', 'Tesoura']
    return random.choice(choices)
def get_user_choice():
    print("Escolha entre Pedra, Papel ou Tesoura:")
    return validate_message('')
def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate"
    elif (user_choice == "Pedra" and computer_choice == "Tesoura") or \
         (user_choice == "Papel" and computer_choice == "Pedra") or \
         (user_choice == "Tesoura" and computer_choice == "Papel"):
        return "Você venceu!"
    else:
        return "Você perdeu!"
def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Você escolheu: {user_choice}")
    print(f"O computador escolheu: {computer_choice}")
    winner = get_winner(user_choice, computer_choice)
    print(winner)
if __name__ == "__main__":
    main()