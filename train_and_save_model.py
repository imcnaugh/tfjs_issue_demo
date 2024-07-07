import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras

train_data = tf.constant([[0], [0], [0], [1], [1], [1]], dtype=tf.float32)
train_label = tf.constant([0, 0, 1, 1, 1, 1], dtype=tf.float32)

validation_data = tf.constant([[0], [0], [0], [1], [1], [1]], dtype=tf.float32)
validation_label = tf.constant([0, 0, 1, 1, 1, 1], dtype=tf.float32)

inputLayer = layers.Input(shape=(1,), dtype='float32')
features = layers.Dense(16, activation='relu')(inputLayer)
outputLayer = layers.Dense(1, activation='sigmoid')(features)

model = keras.Model(inputs=inputLayer, outputs=outputLayer)

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

history = model.fit(train_data, train_label, epochs=10, validation_data=(validation_data, validation_label))

import tensorflowjs as tfjs
tfjs.converters.save_keras_model(model, 'tfjs-model')