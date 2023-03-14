from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Carregando dataset de íris
iris = load_iris()
X = iris.data
y = iris.target

# Dividindo dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando modelo de árvore de decisão
model = DecisionTreeClassifier()

# Treinando o modelo
model.fit(X_train, y_train)

# Avaliando o modelo
score = model.score(X_test, y_test)
print(f"Acurácia: {score:.2f}")
