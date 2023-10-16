# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(2)
pyautogui.press("enter")

# entrar no link 
pyautogui.write("http://localhost/fazenda/")
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=652, y=418)
# escrever o seu email
pyautogui.press("enter") # enter no botao de login
time.sleep(3)
pyautogui.click(x=1137, y=339)
time.sleep(2)
pyautogui.click(x=276, y=114)
time.sleep(3)
pyautogui.click(x=450, y=252)


import pandas as pd

tabela = pd.read_csv("tabela_empresas_taboao3.csv")

# clicar no campo de nome da empresa

# pegar da tabela o valor do campo que a gente quer preencher
nome = tabela.loc[74, "nome"]
ccm = tabela.loc[74, "codigo"]
cnpj = tabela.loc[74, "numero_documento"]
email = tabela.loc[74, "email"]
telefone = tabela.loc[74, "telefone"]
cep = tabela.loc[74, "cep"]
numero = tabela.loc[74, "numero"]
telefone = tabela.loc[74, "telefone"]
atividade_principal = tabela.loc[74, "atividade_principal"]

pyautogui.write(str(nome))
pyautogui.press("tab")
pyautogui.write(str(cnpj))
pyautogui.press("tab")
pyautogui.write(str(ccm))
pyautogui.press("tab")
pyautogui.write(str(cep))
time.sleep(2)
pyautogui.click(x=1418, y=412)
time.sleep(2)
pyautogui.click(x=838, y=573)
pyautogui.write(str(email))
pyautogui.press("tab")
pyautogui.write(str(telefone))
pyautogui.press("tab")
pyautogui.click(x=645, y=926)
pyautogui.write(str(atividade_principal))
pyautogui.press("tab")



    