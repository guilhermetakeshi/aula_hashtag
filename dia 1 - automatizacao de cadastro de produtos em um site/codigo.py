# passo a passo do projeto

# Passo 1 - entrar no sistema da empresa
#   https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> aperta um atalho (combinação de teclas) ex: alt+f4 ou alt+tab

pyautogui.PAUSE = 0.6
# isso cria uma pausa após cada comando dado

# 1 - abrir o opera
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# 2 - entrar no link
time.sleep(1)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
time.sleep(1)
pyautogui.write(link)
pyautogui.press("enter")

# 3 - esperar o site carregar
time.sleep(2)

# Passo 2 - Fazer login

# login = Point(x=1007, y=489)
# senha = Point(x=947, y=604)
# click logar = Point(x=980, y=693)
# pegamos essas posições usando o pegar_posição.py

pyautogui.click(x=1007, y=489)
pyautogui.write("guioshiro.jp@gmail.com")

pyautogui.click(x=947, y=604)
# podemos fazer usando o tab com: 
# pyautogui.press("tab")
pyautogui.write("senhaTESTE")

pyautogui.click(x=980, y=693)
# podemos fazer usando o tab e enter com: 
# pyautogui.press("tab")
# pyautogui.click("enter")

time.sleep(2)

# Passo 3 - importar a base de dados "produtos.csv"

import pandas as pd
tabela = pd.read_csv("produtos.csv")

# Passo 4 - Cadastrar o produto no formulario
for linha in tabela.index:
    # Passo 5 - Repetir o cadastro para todos os produtos
    pyautogui.click(x=885, y=342)
    
    codigo = tabela.loc[linha, "codigo"]
    # o tabela.loc localiza o que esta lá, a linha significa o indice em que estamos e o "codigo" é sobre qual coluna
    # e assim por diante
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]

    # preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    if not pd.isna(obs):
    
        pyautogui.write(str(obs))
        pyautogui.press("tab")
    else:
        pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000)



