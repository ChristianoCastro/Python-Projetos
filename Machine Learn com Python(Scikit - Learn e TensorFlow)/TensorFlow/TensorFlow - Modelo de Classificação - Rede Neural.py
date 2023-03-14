import tensorflow as tf
from tensorflow import keras

# Carregando o conjunto de dados de classificação MNIST
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalizando os dados
x_train = x_train / 255.0
x_test = x_test / 255.0

# Definindo a arquitetura da rede neural
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])

# Compilando o modelo com a função de perda e otimizador
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# Treinando o modelo com os dados de treinamento
model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Avaliando o modelo nos dados de teste
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print('\nAcurácia no conjunto de testes:', test_acc)
