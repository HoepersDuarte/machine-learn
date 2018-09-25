#!-*- coding: utf8 -*-

import pandas as pd
from collections import Counter
import numpy as np
from sklearn.model_selection import cross_val_score

classificacoes = pd.read_csv('emails.csv')
textosPuros = classificacoes['email']
textosQuebrados = textosPuros.str.lower().str.split(' ')
dicionario = set()

for lista in textosQuebrados:
    dicionario.update(lista)

totalDePalavras = len(dicionario)
tuplas = zip(dicionario, range(totalDePalavras))
tradutor = {palavra:indice for palavra,indice in tuplas}


def vetorizar_texto(texto, tradutor):
    vetor = [0] * len(tradutor)

    for palavra in texto:
        if palavra in tradutor:
            posicao = tradutor[palavra]
            vetor[posicao] += 1
    
    return vetor

vetoresDeTexto = [vetorizar_texto(texto, tradutor) for texto in textosQuebrados]
print(vetoresDeTexto)    