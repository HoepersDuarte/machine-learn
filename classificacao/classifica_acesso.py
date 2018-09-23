import csv
from sklearn.naive_bayes import MultinomialNB

X = []
Y = []

arquivo = open('acesso.csv', 'r')
leitor = csv.reader(arquivo)
next(leitor)
for home,funciona,contato,comprou in leitor:
    dado = [int(home), int(funciona), int(contato)]
    X.append(dado)
    Y.append(int(comprou))


treino_dados = X[:90]
treino_marcacoes = Y[:90]

teste_dados = X[-9:]
teste_marcacoes = Y[-9:]

modelo = MultinomialNB()
modelo.fit(treino_dados, treino_marcacoes)

resultado = modelo.predict(teste_dados)
diferenca = resultado - teste_marcacoes

acertos = [d for d in diferenca if d == 0]

total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)

taxa_de_acerto = 100.0 * (total_de_acertos/total_de_elementos)
print(taxa_de_acerto)
print(total_de_elementos)
