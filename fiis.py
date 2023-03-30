import pandas as pd
import urllib.request
import matplotlib.pyplot as plt
import PySimpleGUI as sg

def fiis_atualizar():

    tabela = pd.read_excel("fiis.xlsx")

    # Pega as cotações atuais de cada ativo

    for i in range(len(tabela)): 
        ativo = tabela["ATIVO"][i]
        #open_adress = urllib.request.urlopen('https://www.google.com/finance/quote/'+str(ativo)+':BVMF?sa=X&ved=2ahUKEwjN3bPOg9D8AhWgF7kGHR6TCpYQ3ecFegQIMhAg')
        open_adress = urllib.request.urlopen('https://www.google.com/finance/quote/'+str(ativo)+':BVMF?sa=X&ved=2ahUKEwizjc384oz9AhXRFbkGHZLfCCUQ3ecFegQIMBAg')
        codigo_html = str(open_adress.read())
        index_cotacao=(codigo_html.index("data-last-price="))
        cte0=0
        while True:
            try:
                0+int(codigo_html[index_cotacao+17+cte0])
            except:
                if codigo_html[index_cotacao+17+cte0] != ".":
                    break
                cte0=cte0+2
                break
            else:
                cte0=cte0+1 
        cotacao=(codigo_html[index_cotacao+17:index_cotacao+17+cte0])
        tabela["COTAÇÃO"][i] = float(cotacao)
        tabela.to_excel("fiis.xlsx")

    # Calcula o valor bruto

    tabela["BRUTO"] = (tabela["QUANTIDADE"]*tabela["COTAÇÃO"])
    tabela.to_excel("fiis.xlsx")

def fiis_total():

    tabela = pd.read_excel("fiis.xlsx")

    # Tipos

    bruto_agro, bruto_tijolo, bruto_shoppings, bruto_logistico, bruto_papel = 0, 0, 0, 0, 0
    for i in range(len(tabela)):
        if tabela["TIPO"][i] == "AGRO":
            bruto_agro = bruto_agro + tabela["BRUTO"][i]
        if tabela["TIPO"][i] == "TIJOLO":
            bruto_tijolo = bruto_tijolo + tabela["BRUTO"][i]
        if tabela["TIPO"][i] == "SHOPPINGS":
            bruto_shoppings = bruto_shoppings + tabela["BRUTO"][i]
        if tabela["TIPO"][i] == "LOGÍSTICO":
            bruto_logistico = bruto_logistico + tabela["BRUTO"][i]
        if tabela["TIPO"][i] == "PAPEL":
            bruto_papel = bruto_papel + tabela["BRUTO"][i]

    # Gráficos
    total = bruto_agro + bruto_tijolo + bruto_shoppings + bruto_logistico + bruto_papel
    porcentagem_agro = round(bruto_agro*100/total, 2)
    porcentagem_tijolo = round(bruto_tijolo*100/total, 2)
    porcentagem_shoppings = round(bruto_shoppings*100/total, 2)
    porcentagem_logistico = round(bruto_logistico*100/total, 2)
    porcentagem_papel = round(bruto_papel*100/total, 2)
    lista_brutos = [bruto_agro, bruto_tijolo, bruto_shoppings, bruto_logistico, bruto_papel]
    lista_tipos = ["AGRO "+str(porcentagem_agro)+"%", "TIJOLO "+str(porcentagem_tijolo)+"%", "SHOPPINGS "+str(porcentagem_shoppings)+"%", "LOGÍSTICA "+str(porcentagem_logistico)+"%", "PAPEL "+str(porcentagem_papel)+"%"]

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.pie(lista_brutos, labels = lista_tipos)
    return plt.show()

def fiis_agro():

    tabela = pd.read_excel("fiis.xlsx")

    fiis_agro = []
    brutos_agro = []
    total = 0
    for i in range(len(tabela)):
        if tabela["TIPO"][i] == "AGRO":
            fiis_agro.append(tabela["ATIVO"][i])
            brutos_agro.append(tabela["BRUTO"][i])
            total = total + tabela["BRUTO"][i]

    fiis_porcentagem = []
    for i in range(len(fiis_agro)):
        fiis_porcentagem.append(str(fiis_agro[i])+" "+str(round(brutos_agro[i]*100/total, 2))+"%")
    
    fig, ax = plt.subplots(figsize=(12,5))
    ax.pie(brutos_agro, labels = fiis_porcentagem)
    plt.show()

def fiis_tijolo():

    tabela = pd.read_excel("fiis.xlsx")

    fiis_tijolo = []
    brutos_tijolo = []
    total = 0
    for i in range(len(tabela)):
        if tabela["TIPO"][i] == "TIJOLO":
            fiis_tijolo.append(tabela["ATIVO"][i])
            brutos_tijolo.append(tabela["BRUTO"][i])
            total = total + tabela["BRUTO"][i]

    fiis_porcentagem = []
    for i in range(len(fiis_tijolo)):
        fiis_porcentagem.append(str(fiis_tijolo[i])+" "+str(round(brutos_tijolo[i]*100/total, 2))+"%")
    
    fig, ax = plt.subplots(figsize=(12,5))
    ax.pie(brutos_tijolo, labels = fiis_porcentagem)
    plt.show()

def fiis_shoppings():

    tabela = pd.read_excel("fiis.xlsx")

    fiis_shoppings = []
    brutos_shoppings = []
    total = 0
    for i in range(len(tabela)):
        if tabela["TIPO"][i] == "SHOPPINGS":
            fiis_shoppings.append(tabela["ATIVO"][i])
            brutos_shoppings.append(tabela["BRUTO"][i])
            total = total + tabela["BRUTO"][i]

    fiis_porcentagem = []
    for i in range(len(fiis_shoppings)):
        fiis_porcentagem.append(str(fiis_shoppings[i])+" "+str(round(brutos_shoppings[i]*100/total, 2))+"%")
    
    fig, ax = plt.subplots(figsize=(12,5))
    ax.pie(brutos_shoppings, labels = fiis_porcentagem)
    plt.show()

def fiis_logistico():

    tabela = pd.read_excel("fiis.xlsx")

    fiis_logistico = []
    brutos_logistico = []
    total = 0
    for i in range(len(tabela)):
        if tabela["TIPO"][i] == "LOGÍSTICO":
            fiis_logistico.append(tabela["ATIVO"][i])
            brutos_logistico.append(tabela["BRUTO"][i])
            total = total + tabela["BRUTO"][i]

    fiis_porcentagem = []
    for i in range(len(fiis_logistico)):
        fiis_porcentagem.append(str(fiis_logistico[i])+" "+str(round(brutos_logistico[i]*100/total, 2))+"%")
    
    fig, ax = plt.subplots(figsize=(12,5))
    ax.pie(brutos_logistico, labels = fiis_porcentagem)
    plt.show()

def fiis_papel():

    tabela = pd.read_excel("fiis.xlsx")

    fiis_papel = []
    brutos_papel = []
    total = 0
    for i in range(len(tabela)):
        if tabela["TIPO"][i] == "PAPEL":
            fiis_papel.append(tabela["ATIVO"][i])
            brutos_papel.append(tabela["BRUTO"][i])
            total = total + tabela["BRUTO"][i]

    fiis_porcentagem = []
    for i in range(len(fiis_papel)):
        fiis_porcentagem.append(str(fiis_papel[i])+" "+str(round(brutos_papel[i]*100/total, 2))+"%")
    
    fig, ax = plt.subplots(figsize=(12,5))
    ax.pie(brutos_papel, labels = fiis_porcentagem)
    plt.show()

def fiis_add(x,y,z):

    tabela = pd.read_excel("fiis.xlsx")

    tamanho=len(tabela)
    cte=0
    for i in range(tamanho):
        if str(y) in tabela["ATIVO"][i]:
            posicao=i
            print(posicao)
            tabela["QUANTIDADE"][posicao] = tabela["QUANTIDADE"][posicao] + int(z)
            break
        else:
            cte = cte + 1
            if cte == tamanho:
                dados = [{"TIPO": str(x), "ATIVO": str(y), "QUANTIDADE": int(z)}]
                tabela = tabela.append(dados, ignore_index = True)
                tabela.to_excel("fiis.xlsx")      

    tabela.to_excel("fiis.xlsx")

sg.theme("Dark2")
layout = [
    [sg.Button("Atualizar")],
    [sg.Text("Adicionar FIIs:")],
    [sg.Text("Código do FII"), sg.Input(key="cod_fii")],
    [sg.Text("Quantidade"), sg.Input(key="qnt_fii")],
    [sg.Text("Tipo do FII:"), sg.Checkbox("Agro", key="agro"), sg.Check("Tijolo", key="tijolo"), sg.Check("Shoppings", key="shoppings"), sg.Check("Logístico", key="logístico"), sg.Check("Papel", key="papel"), sg.Button("Confirmar")],
    [sg.Text("Carregar gráfico de:")],
    [sg.Button("FIIs Total"),sg.Button("FIIs Agro"), sg.Button("FIIs Tijolo"), sg.Button("FIIs Shoppings"), sg.Button("FIIs Logístico"), sg.Button("FIIs Papel")],
    ]

window = sg.Window("Gerenciador de FIIs", layout=layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    if event == "FIIs Total":
        fiis_total()
    if event == "FIIs Agro":
        fiis_agro()
    if event == "FIIs Tijolo":
        fiis_tijolo()
    if event == "FIIs Shoppings":
        fiis_shoppings()
    if event == "FIIs Logístico":
        fiis_logistico()
    if event == "FIIs Papel":
        fiis_papel()
    if event == "Confirmar":
        if values["agro"]:
            fiis_add("AGRO", str(values["cod_fii"]), int(values["qnt_fii"]))
        if values["tijolo"]:
            fiis_add("TIJOLO", str(values["cod_fii"]), int(values["qnt_fii"]))
        if values["shoppings"]:
            fiis_add("SHOPPINGS", str(values["cod_fii"]), int(values["qnt_fii"]))
        if values["logístico"]:
            fiis_add("LOGÍSTICO", str(values["cod_fii"]), int(values["qnt_fii"]))
        if values["papel"]:
            fiis_add("PAPEL", str(values["cod_fii"]), int(values["qnt_fii"]))
    if event == "Atualizar":
        fiis_atualizar()