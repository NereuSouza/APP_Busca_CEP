import json
import requests
from tkinter import *


def busca(CEP):

    efetuada = requests.get("https://ws.apicep.com/cep/"+CEP+".json")
    endereco = json.loads(efetuada.text)
    nome = Label(janela, text="Nome: " + endereco['address']+"\n Bairro: "+ endereco['district']+"\nCidade: "+endereco['city']+"\n Estado: "+endereco['state'])
    nome.grid(column=1, row=3, padx=10, pady=10)


janela = Tk()
janela.title("Busca CEP")
janela.geometry('230x250')
Texto = Label(janela, text="                     DIGITE UM CEP                    ")
Texto.grid(column=1, row=0, padx=10, pady=10)

entrada = Entry(janela)
entrada.grid(column=1, row=1, padx=10, pady=10)

botao1 = Button(janela, text="Buscar", command=lambda: busca(entrada.get()))
botao1.grid(column=1, row=2, padx=10, pady=10)

janela.mainloop()

