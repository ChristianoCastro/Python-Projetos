import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Criando um DataFrame com informações de funcionários
dados = pd.DataFrame({
    'Nome': ['João', 'Maria', 'José', 'Pedro', 'Ana'],
    'Idade': [23, 35, 42, 18, 27],
    'Salário': [2000, 3500, 5000, 1800, 2700],
    'Cargo': ['Analista', 'Gerente', 'Coordenador', 'Estagiário', 'Analista']
})

# Obtendo estatísticas descritivas dos dados
print(dados.describe())

# Criando um histograma dos salários dos funcionários
plt.hist(dados['Salário'])
plt.show()

# Calculando a média dos salários dos funcionários
media_salarios = np.mean(dados['Salário'])
print(f'Média dos salários: R${media_salarios:.2f}')
