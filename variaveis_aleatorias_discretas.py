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

#Distribuição Geometrica

#Frequencia absoluta 
'''
import scipy.stats as stats

print("Nosso interesse é calcular a probabilidade de se obter um sucesso, após n fracassos ocorrerem.")
#Definir a probabilidade de sucesso (p)
p = float(input("Insira o valor da probabilidade de sucesso (p): "))

#Definir o número de tentativas até o primeiro sucesso (k)
k = float(input("Insira o número de tentativas até o primeiro sucesso (k): "))

#Calcular a probabilidade de X = k usando a função pmf da distribuição geométrica
probabilidade = stats.geom.pmf(k, p)

print(f"A probabilidade de precisar de exatamente {k:.0f} é de {probabilidade:.5f}")
'''
#Frequencia acumulada
'''
import scipy.stats as stats
# Definir a probabilidade de sucesso (p)
p = float(input("Insira o valor da probabilidade de sucesso (p): "))

#Definir o número de tentativas até o primeiro sucesso (k)
k = float(input("Insira o número de tentativas até o primeiro sucesso (k): "))

# Calcular a probabilidade de X=k usando a função pmf da distribuição geométrica
probabilidade = stats.geom.pmf(k, p)+stats.geom.pmf(k+1, p)

print(f"A probabilidade de que precise de no máximo {k+1 :.0f} é de {probabilidade:.5f}")
'''

#Distribuição Hipergeometrica
'''
import scipy.stats as stats

#Inicialização das variaveis
print("Para fazer esse calculo, precisaremos dos seguintes dados:")
m = float(input("O tamanho total da Populção (m): "))
n = float(input("número total de sucessos na população (n): "))
k = float(input("O tamanho da amostra retirada (k): "))
x = float(input("número de sucessos desejados na amostra (x): "))

#Criar uma distribuição hipergeométrica com x, m e n
distribuicao = stats.hypergeom(m,n,k)

#Calcular a probabilidade de obter exatamente k sucessos na amostra
probabilidade_k_sucessos = distribuicao.pmf(x)

#Calcular a probabilidade de obter k ou menos sucessos na amostra
probabilidade_k_ou_menos_sucessos = distribuicao.cdf(x)

#Calcular média e variância da distribuição
media = distribuicao.mean()
variancia = distribuicao.var()

#Exibir Resultados
print(f"Probabilidade de obter exatamente {x:.0f} sucessos na amostra: {probabilidade_k_sucessos:.3f}")
print(f"Probabilidade de obter {x:.0f} ou menos sucessos na amostra: {probabilidade_k_ou_menos_sucessos:.3f}")
print(f"Média: {media:.1f}")
print(f"Variância: {variancia:.2f}")
'''
#Distribuição de Poisson
'''
from scipy.stats import poisson

x = float(input("Digite o numero de eventos a ser calculada: "))
y = float(input("Digite a media dos dados desse evento: "))

prob = poisson.pmf(x, y)

print(f"A probabilidade de acontencer {x:.0f} eventos é de: {prob:.3f}")
print(f"Ou {100* prob:.1f}%")
'''
#Ainda no Poisson
'''
import numpy as np
# definir a média lambda
lambda_ = 2
# gerar a distribuição de Poisson com numpy
poisson_dist = np.random.poisson(lambda_, size=1000)
# exibir os primeiros 20 valores da distribuição
print(poisson_dist[:20])
'''