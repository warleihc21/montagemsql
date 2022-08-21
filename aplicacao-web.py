from re import S
import streamlit as st
import sys

from PIL import Image

import threading
import time

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
import pandas as pd
import numpy as np
import tkinter as Tk
import os
from tkinter import PhotoImage, filedialog
from tkinter.filedialog import askopenfile, asksaveasfilename
from tkinter import Tk
from csv import reader
import csv
import pickle
import pyautogui
import click


with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

image = Image.open('logo.png')

st.image(image, caption='A Melhor Promotora de Crédito Consignado do Brasil')


st.title('Montagem SQL')

#Safra
def safra():
    Tk().withdraw()
    filenames = askopenfile()

            #ler = open(filenames, 'r')
    tabela = pd.read_csv(filenames, sep=';')


    tabela.insert(loc=31, column='Natureza', value=0)
    tabela.insert(loc=32, column='Tipo', value=0)
    celulas_vazias = tabela.isnull()
    somente_vazias = tabela[tabela['Nome Subcorban'].isnull()]

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Natureza'] = 'CREDITO DIFERIDO'

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Tipo'] = 'DIFERIDO'


            #somente_vazias.to_csv(r"C:\Users\warlei.junio\Downloads\retestesql\SAFRA04042022SQLTESTE-V2.csv", index=False)
    filenamessave = filedialog.asksaveasfilename(
                    filetypes=(
                        ("Arquivos csv", "*.csv"),
                        ("Todos os arquivos", "*.*"),
                    )
                )

            #ler = open(filenames, 'r')
    
    somente_vazias.to_csv(filenamessave, index=False)

#Facta
def facta():
    Tk().withdraw()
    filenames = askopenfile()

            #ler = open(filenames, 'r')
    tabela = pd.read_csv(filenames, sep=';')


    tabela.insert(loc=31, column='Natureza', value=0)
    tabela.insert(loc=32, column='Tipo', value=0)
    celulas_vazias = tabela.isnull()
    somente_vazias = tabela[tabela['Nome Subcorban'].isnull()]

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Natureza'] = 'CREDITO DIFERIDO'

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Tipo'] = 'DIFERIDO'


            #somente_vazias.to_csv(r"C:\Users\warlei.junio\Downloads\retestesql\SAFRA04042022SQLTESTE-V2.csv", index=False)
    filenamessave = filedialog.asksaveasfilename(
                    filetypes=(
                        ("Arquivos csv", "*.csv"),
                        ("Todos os arquivos", "*.*"),
                    )
                )

            #ler = open(filenames, 'r')
    
    somente_vazias.to_csv(filenamessave, index=False)

#Banrisul
def banrisul():
    Tk().withdraw()
    filenames = askopenfile()

            #ler = open(filenames, 'r')
    tabela = pd.read_csv(filenames, sep=';')


    tabela.insert(loc=31, column='Natureza', value=0)
    tabela.insert(loc=32, column='Tipo', value=0)
    celulas_vazias = tabela.isnull()
    somente_vazias = tabela[tabela['Nome Subcorban'].isnull()]

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Natureza'] = 'CREDITO DIFERIDO'

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Tipo'] = 'DIFERIDO'


            #somente_vazias.to_csv(r"C:\Users\warlei.junio\Downloads\retestesql\SAFRA04042022SQLTESTE-V2.csv", index=False)
    filenamessave = filedialog.asksaveasfilename(
                    filetypes=(
                        ("Arquivos csv", "*.csv"),
                        ("Todos os arquivos", "*.*"),
                    )
                )

            #ler = open(filenames, 'r')
    
    somente_vazias.to_csv(filenamessave, index=False)
  
#Bradesco
def bradesco():
    Tk().withdraw()
    filenames = askopenfile()

            #ler = open(filenames, 'r')
    tabela = pd.read_csv(filenames, sep=';')


    tabela.insert(loc=31, column='Natureza', value=0)
    tabela.insert(loc=32, column='Tipo', value=0)
    celulas_vazias = tabela.isnull()
    somente_vazias = tabela[tabela['Nome Subcorban'].isnull()]

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Natureza'] = 'CREDITO DIFERIDO'

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Tipo'] = 'DIFERIDO'


            #somente_vazias.to_csv(r"C:\Users\warlei.junio\Downloads\retestesql\SAFRA04042022SQLTESTE-V2.csv", index=False)
    filenamessave = filedialog.asksaveasfilename(
                    filetypes=(
                        ("Arquivos csv", "*.csv"),
                        ("Todos os arquivos", "*.*"),
                    )
                )

            #ler = open(filenames, 'r')
    
    somente_vazias.to_csv(filenamessave, index=False)


#C6BANK
def c6bank():
    Tk().withdraw()
    filenames = askopenfile()

            #ler = open(filenames, 'r')
    tabela = pd.read_csv(filenames, sep=';')


    tabela.insert(loc=31, column='Natureza', value=0)
    tabela.insert(loc=32, column='Tipo', value=0)
    celulas_vazias = tabela.isnull()
    somente_vazias = tabela[tabela['Nome Subcorban'].isnull()]

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Natureza'] = 'CREDITO DIFERIDO'

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Tipo'] = 'DIFERIDO'


            #somente_vazias.to_csv(r"C:\Users\warlei.junio\Downloads\retestesql\SAFRA04042022SQLTESTE-V2.csv", index=False)
    filenamessave = filedialog.asksaveasfilename(
                    filetypes=(
                        ("Arquivos csv", "*.csv"),
                        ("Todos os arquivos", "*.*"),
                    )
                )

            #ler = open(filenames, 'r')
    
    somente_vazias.to_csv(filenamessave, index=False)



#Cetelem
def cetelem():
    Tk().withdraw()
    filenames = askopenfile()

            #ler = open(filenames, 'r')
    tabela = pd.read_csv(filenames, sep=';')


    tabela.insert(loc=31, column='Natureza', value=0)
    tabela.insert(loc=32, column='Tipo', value=0)
    celulas_vazias = tabela.isnull()
    somente_vazias = tabela[tabela['Nome Subcorban'].isnull()]

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Natureza'] = 'CREDITO A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Natureza'] = 'CREDITO DIFERIDO'

    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'A VISTA FGTS', 'Tipo'] = 'A VISTA'
    somente_vazias.loc[tabela['Tp Pagamento Bruto Comissao'] == 'SERVICO', 'Tipo'] = 'DIFERIDO'


            #somente_vazias.to_csv(r"C:\Users\warlei.junio\Downloads\retestesql\SAFRA04042022SQLTESTE-V2.csv", index=False)
    filenamessave = filedialog.asksaveasfilename(
                    filetypes=(
                        ("Arquivos csv", "*.csv"),
                        ("Todos os arquivos", "*.*"),
                    )
                )

            #ler = open(filenames, 'r')
    
    somente_vazias.to_csv(filenamessave, index=False)



button_safra = st.button("Importar Safra", on_click=safra)
if button_safra:
    st.write("Arquivo Montado com Sucesso!")


button_facta = st.button("Importar Facta", on_click=facta)
if button_facta:
    st.write("Arquivo Montado com Sucesso!")


button_banrisul = st.button("Importar Banrisul", on_click=banrisul)
if button_banrisul:
    st.write("Arquivo Montado com Sucesso!")


button_bradesco = st.button("Importar Bradesco", on_click=bradesco)
if button_bradesco:
    st.write("Arquivo Montado com Sucesso!")


button_c6bank = st.button("Importar C6Bank", on_click=c6bank)
if button_c6bank:
    st.write("Arquivo Montado com Sucesso!")


button_cetelem = st.button("Importar Cetelem", on_click=cetelem)
if button_cetelem:
    st.write("Arquivo Montado com Sucesso!")




   

    



