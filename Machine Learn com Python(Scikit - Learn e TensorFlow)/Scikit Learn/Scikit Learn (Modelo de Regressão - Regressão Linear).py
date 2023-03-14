from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split

# Carregando o conjunto de dados da habitação da Califórnia
california = fetch_california_housing()

# Separando os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(california.data, california.target, test_size=0.2, random_state=42)

# Criando um modelo de regressão linear
model = LinearRegression()

# Treinando o modelo nos dados de treinamento
model.fit(X_train, y_train)

# Avaliando o modelo nos dados de teste
score = model.score(X_test, y_test)

print("Score do modelo: {:.2f}".format(score))
