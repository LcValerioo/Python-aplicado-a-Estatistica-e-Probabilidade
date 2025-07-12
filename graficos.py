import matplotlib.pyplot as plt
import pandas as pd

'''
Aqui vamos escrever algumas das funções de criação de graficos da biblioteca MatPlotLib.

# plt.plot(x,y): cria grafico de linha simples
# plt.scatter(x,y): cria grafico de dispersão.
# plt.bar(x,height): cria um grafico de barras verticais.
# plt.hist(x,bins): cria um histograma para visualizar a distribuição de uma variavel aleatoria continua.
# plt.pie(sizes,labels): cria um grafico de pizza para vizualizar a proporção de diferentes categorias em relação ao todo.
# plt.boxplot(x): cria um grafico de caixa para vizualizar a distribuição de uma variável contínua.

'''
'''
#Criando uma tabela utilizando a Biblioteca Pandas

dados = [[1186,1751],[21328,25280],[947,18432],[29,280]]
linhas = ["Estadual", "Privada", "Municipal", "Federal"]
colunas = ["Número de Alunos", "Número de Professores"]
df = pd.DataFrame(dados, index=linhas, columns=colunas)
print(df)

df["Tipo de Escola"] = linhas #adiciona a coluna "Tipo de Escola"
print(df)
'''

#Criando grafico de barras da variavel "Numero de Alunos", por tipo de escola:
'''
df = pd.DataFrame({
    "Tipo de Escola": ["Pública", "Privada", "Federal"],
    "Número de Alunos": [500, 300, 200]
})

df.plot.bar(x="Tipo de Escola", y="Número de Alunos")
plt.title("Número de Alunos por Tipo de Escola")
plt.xlabel("Tipo de Escola")
plt.ylabel("Número de Alunos")
plt.show()


'''
#Invertendo o Grafico de Barras
'''
# Aqui você define o df (dataframe) com seus dados
df = pd.DataFrame({
    "Tipo de Escola": ["Pública", "Privada", "Federal"],
    "Número de Alunos": [500, 300, 200]
})


df.plot.barh(x="Tipo de Escola", y="Número de Alunos", orientation="horizontal", color="red") 

plt.title("Número de Alunos por Tipo de Escola")
plt.xlabel("Número de Alunos")  # Aqui inverti, porque o eixo x é o valor numérico
plt.ylabel("Tipo de Escola")
plt.show()
'''
#Grafico de Barra Empilhadas
'''
df = pd.DataFrame({
    "Tipo de Escola": ["Pública", "Privada", "Federal", "Estadual"],
    "Número de Alunos": [500, 300, 200, 955], "Número de Professores": [100, 200, 150, 439]
})

ax = df.plot.bar(stacked=True)
plt.title("Distribuição de Número de Alunos e Professores por Tipo de Escola")
plt.xlabel("Tipo de Escola")
plt.ylabel("Número de Individuos")
plt.legend(loc='upper left')
plt.show()
'''
#Grafico de Dispersão
'''
df = pd.DataFrame({
    "Tipo de Escola": ["Pública", "Privada", "Federal", "Estadual"],
    "Número de Alunos": [500, 300, 200, 955], "Número de Professores": [100, 200, 150, 439]
})

x = df["Número de Professores"]
y = df["Número de Alunos"]

plt.scatter(x, y)
plt.title("Relação entre Número de Professores e Número de Alunos")
plt.xlabel("Número de Professores")
plt.ylabel("Número de Alunos")
plt.show()
'''

#Implementando Graficos de Setor
'''
df = pd.DataFrame({
    "Tipo de Escola": ["Pública", "Privada", "Federal", "Estadual"],
    "Número de Alunos": [500, 300, 200, 955], "Número de Professores": [100, 200, 150, 439]
})

cores = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray']
dados_alunos = df["Número de Alunos"]
dados_instituicao = df["Tipo de Escola"]
plt.pie(dados_alunos, labels=dados_alunos.index, autopct='%1.1f%%')
plt.title("Distribuição de Número de Alunos por Tipo de Escola")
plt.show()
'''
#Implentando mais de um grafico de setor
'''
df = pd.DataFrame({"Tipo de Escola": ["Pública", "Privada", "Federal", "Estadual"],
    "Número de Alunos": [500, 300, 200, 955], "Número de Professores": [100, 200, 150, 439]
})

x = df["Tipo de Escola"]
fig, axs = plt.subplots(1, 2, figsize=(8, 4))
df.plot.pie(y="Número de Alunos", ax=axs[0], autopct="%1.1f%%", colors=["blue", "orange", "green", "red"], labels=x)
axs[0].set_title("Número de Alunos por Tipo de Escola")
df.plot.pie(y="Número de Professores", ax=axs[1], autopct="%1.1f%%", colors=["blue", "orange", "green", "red"], labels=x)
axs[1].set_title("Número de Professores por Tipo de Escola")
plt.tight_layout()
plt.show()
'''