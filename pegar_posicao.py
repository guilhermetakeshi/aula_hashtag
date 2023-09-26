import time
import pyautogui

# usamos essa parte pra gente colocar o mouse naonde a gente quer 
# e o python printar a posição em X e Y pra gente usar no codigo.py
# pra ele saber exatamente onde clicar na tela pra digitar as coisas

time.sleep(5)
print(pyautogui.position())
# mostra a posição do mouse em X e Y

pyautogui.scroll(200)