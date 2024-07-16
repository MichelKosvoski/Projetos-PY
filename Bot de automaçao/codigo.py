#Passo 1 - entrar no sistema da empresa
#   link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
# 2 - fazer login
# 3 - pegar /Importar a base de dados
# 4 - Cadastrar um produto
# 5 - Repetir o passo 4 até cadastrar todos os produtos

import pyautogui
import time
# Ele automatiza seu mouse e teclado

# pyautogui.click -clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas (ctrl C)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5

# Passo 1 - Entrar no sistema
# Abrir o navegar
pyautogui.press("Win")
pyautogui.write("Opera")
pyautogui.press("enter")

#https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("Enter")

time.sleep(3)

# Passo 2 Fazer login
pyautogui.click(x=763, y=361)
pyautogui.hotkey("ctrol", "a")
pyautogui.write("sharksoareskosvoski@gmail.com")

#passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("minhasenha")

pyautogui.click(x=985, y=518)

time.sleep(3)

#passo 3 - Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

#passo 4 - Cadastrar produto
for linha in tabela.index:
    # codigo
    pyautogui.click(x=826, y=241)

    tabela.loc[linha, "codigo"]

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.press("tab")
    pyautogui.write(codigo)
  
    # marca
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    # marca   tipo    categoria   
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    # categoria
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    # preço
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    # custo
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)
    
    # obs
    obs = str(tabela.loc[linha, "obs"])
    pyautogui.press("tab")
    pyautogui.write(obs)

    # Clicar no botao de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5 - Repetir