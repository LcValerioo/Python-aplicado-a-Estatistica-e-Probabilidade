#Fazendo calculos probabilisticos usando a distribuição de Bernoulli
'''
from scipy.stats import bernoulli

# Define a probabilidade de sucesso como p
print("A probabilidade do evento ocorrer vai ser dada por p")

p = float(input("Digite o valor de p: "))

# Criando a distribuição de Bernoulli
distribuicao = bernoulli(p)

# Calculando a probabilidade para o valor p (sucesso)
probabilidade_sucesso = distribuicao.pmf(1)

#Calcular a média e a variância da distribuição
media = distribuicao.mean()
variancia = distribuicao.var()
print(media)
print(variancia)

print(f"A probabilidade de obter sucesso é: {probabilidade_sucesso:.2f}")
'''

#Distribuição Binomail
'''
import scipy.stats as stats

#Criando variaveis para armazenar valores n e p

print("Para fazer o Calculo da Função de distribuição Binomial, precisaremos do paramentros n (número total de observações e/ou elementos) e p(probabilidade de sucesso)")
n = float(input("Digite o valor de n: "))
p = float(input("Digite o valor de p: "))

#Criando uma distribuição binomial com n e p
distribuicao = stats.binom(n,p)

#Calcular a probabilidade de obter exatamente x sucessos
x = float(input("Digite o valor de x sucessos: "))
probabilidade_x_sucessos = distribuicao.pmf(x)

#Calcular a probabilidade de obter x ou menos sucessos
y = float(input("Digite o valor de x ou menos sucessos: "))
probabilidade_x_ou_menos_sucessos = distribuicao.cdf(y)

#Calcular a média e a variância da distruibuição
media = distribuicao.mean()
variancia = distribuicao.var()

#Exibir resultados
print(f"Probabilidade de obter exatamente {x:.0f} sucessos: {probabilidade_x_sucessos:.2f}.")
print(f"Probabilidade de obter exatamente {y:.0f} ou menos sucessos: {probabilidade_x_ou_menos_sucessos:.2f}.")
print(f"Média: {media:.2f}")
print(f"Variância: {variancia:.2f}")
'''