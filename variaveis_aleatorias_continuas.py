#Distribuição Uniforme
'''
import numpy as np

#Gerar uma distribuição uniforme entre 0 e 1 com numpy
uniform_dist = np.random.uniform(0, 1, size=1000)

#Exibir os primeiros 10 valores da distribuição
print("\n")
print(uniform_dist[:10])
print("\n")

#Gerar 1000 resultados de um dado 
uniform_dist = np.random.randint(1,7, size=1000)

#Exibir os primeiros 10 valore da distribuição
print("\n")
print(uniform_dist[:10])
print("\n")
'''

#Distribuição Exponencial
'''
from scipy.stats import expon

#Definir a média lambda
x = float(input("Digite o numero de ocorrencias que desejar: "))
y = float(input("Digite a média (lambda): "))

lambda_ = 1/y

#Calcular a probabilidade com scipy.stats
prob = expon.cdf(x, scale=1/lambda_)

#Exibir o resultado
print(f"O resultado é {prob:.3f}")
print(f"Em porcentagem: {100* prob:.1f}%")
'''

#Distribuição Normal
'''
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
'''
'''
#Definir média e desvio padrão
mu = float(input("Digite a Média: "))
sigma = float(input("Digite o Desvio Padrão: "))

#Definir o valor minimo de retorno desejado
x = float(input("Digite o valor X: "))

#Calcular a probabilidade com scipy.stats
prob = 1 - norm.cdf(x, loc=mu, scale=sigma)

#Exibir a probabilidade 
print(f"A Probabilidade desse evento {x:.0f} ocorrer é de {prob:.2f}")
'''
'''
#Parâmetros da distribuição normal
mu = float(input("Digite a Média: "))
sigma = float(input("Digite o Desvio Padrão: "))

#Intervalo de alturas para o cálculo da densidade de probabilidade
alturas = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 1000)

#Calculo da densidade de probabilidade usando a função norm.pdf
densidade_probabilidade = norm.pdf(alturas, loc=mu, scale=sigma)

#Criação do gráfico
plt.plot(alturas, densidade_probabilidade)
plt.xlabel('Alturas (cm)')
plt.ylabel('Densidade de probabilidade')
plt.title('Distribuição normal para a altura de pessoas adultas')
plt.grid(True)
plt.show()
'''