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