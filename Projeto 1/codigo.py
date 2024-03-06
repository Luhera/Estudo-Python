#Passo a passo do projeto  
#pyautogui.write -> esrever um texto
#pyautogui.press -> aperta 1 tecla
#pyautogui.click -> clicar em algum lugar da tela
#pyautogui.hotkey -> combinação de teclas

#Passo 1: Entrar no sistema da empresa
    #abrir o navegador (chrome)
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
    #entrar no link
#Passo 2: Fazer Login
    #selecionar o campo de email
    #escrever o seu email
#Passo 3: Importar a base de produtos pra cadastrar
#Passo 4: Cadastrar um produto
    #clicar no campo de código 
    #pegar da tabela o valor do campo que a gente quer preencher
    #preencher o campo
    #passar para o proximo campo
    #preencher o campo
    #cadastrar o produto(botao enviar)
    #dar scroll de tudo para cima
#Passo 5: Repeti esse processo 
import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3 # faz com que cada linha de codigo de um pause de 3s entre cada linha

#Passo 1:
#abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

#passo 2:
#selecionar o campo de email
pyautogui.click(x=987, y=508)
#escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("sua senha")
pyautogui.click(x=943, y=702)

#Passo 3:
#importar a tabela para base de produtos para cadastrar

tabela = pd.read_csv("produtos.csv")

#Passo 4:
#cadastrar varios produtos da tabela ate acabar

for linha in tabela.index:
    #clicar no campo de código
    pyautogui.click(x=927, y=353)
    #pega da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha,"codigo"]
    #preenche o campo
    pyautogui.write(str(codigo))
    #passa para o proximo campo
    pyautogui.press("tab")
     # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
