# passo a passo do projeto 
# 1 passo: entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
         
import pyautogui
import time 
import pandas as pd

#pyautogui.write-> VAI ESCREVER UM TEXTO 
#pyautogui.press-> APERTAR 1 TECLA 
#pyautogui.click-> CLICAR EM ALGUM LUGAR DA TELA 
pyautogui.PAUSE = 0.3
#Abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

#2 passo: entrar com login e senha
    #SELECIONAR o campo de email 
pyautogui.click(x=699, y=376)
    #Escrever seu email 
pyautogui.write("migueldev@gmail.com")
pyautogui.press("tab")#passando pro proximo produto 
pyautogui.write("password")
pyautogui.click(x=693, y=536)
time.sleep(3)

#3 passo: importar a base de produtor para cadastrar
# importando pandas 
tabela = pd.read_csv("produtos.csv")
print(tabela)

#4 passo: cadastrar  um produto 
for linha in tabela.index:
    
    #clicar no campo de código
    pyautogui.click(x=456, y=253)
    #pegar  da tabela  o valor  do campo que a gente  quer preencher 
    codigo = tabela.loc[linha, "codigo"]
    #preencher o campo
    pyautogui.write(str(codigo))
    #passar para o proximo campo 
    pyautogui.press("tab")

    #preencher o campo
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
    pyautogui.press("enter")
    #dar um scroll de tudo pra cima
    pyautogui.scroll(5000)

    #5 passo: repetir o processo dps://dlp.hashtagtreinamentos.com/python/intensivao/login
    # e cadastro  até o fim 


