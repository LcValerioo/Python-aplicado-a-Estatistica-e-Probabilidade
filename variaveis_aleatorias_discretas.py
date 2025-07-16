#Fazendo calculos probabilisticos usando a distribuição de Bernoulli
'''
from scipy.stats import bernoulli

# Define a probabilidade de sucesso como 0.7
p = 0.7

# Criando a distribuição de Bernoulli
distribuicao = bernoulli(p)

# Calculando a probabilidade para o valor 1 (sucesso)
probabilidade_sucesso = distribuicao.pmf(1)

#Calcular a média e a variância da distribuição
media = distribuicao.mean()
variancia = distribuicao.var()
print(media)
print(variancia)

print(f"A probabilidade de obter sucesso (valor 1) é: {probabilidade_sucesso:.2f}")
'''

