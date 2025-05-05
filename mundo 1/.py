import pyautogui
import time
import webbrowser
import pyperclip


destino = str(input("escreva o email: "))
assunto = str(input("escreva o assunto: "))
mensagens = str(input("escreva a mensagem: "))

pyautogui.PAUSE = 1

webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
time.sleep(7)
pyautogui.click(x=86, y=276)
time.sleep(7)
pyperclip.copy(destino)
pyautogui.hotkey('ctrl' , 'v')
time.sleep(3)
pyautogui.hotkey('tab')
time.sleep(3)
pyperclip.copy(assunto)
pyautogui.hotkey('ctrl' , 'v')
time.sleep(3)
pyautogui.hotkey('tab')
time.sleep(3)
pyperclip.copy(mensagens)
time.sleep(3)
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)
pyautogui.click(x=1231, y=980)
    
pyautogui.alert(text='a mensagem foi enviada com sucesso', title='aviso', button='ok' )
