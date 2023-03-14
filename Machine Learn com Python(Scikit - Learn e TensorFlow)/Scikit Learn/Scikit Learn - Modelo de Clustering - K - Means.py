from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Gerando dados aleatórios em formato de blobs
X, y = make_blobs(n_samples=1000, centers=4, random_state=42)

# Criando modelo de K-Means com 4 clusters
model = KMeans(n_clusters=4)

# Treinando o modelo
model.fit(X)

# Visualizando os clusters
plt.scatter(X[:, 0], X[:, 1], c=model.labels_)
plt.show()
