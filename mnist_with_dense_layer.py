# -*- coding: utf-8 -*-
"""MNIST_Dense_example.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qs8kCUjObrDyVqSkpR2985poaaZkVHPr
"""

import keras
keras.__version__

from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print train_images.shape, train_labels

print len(train_labels), train_images.shape[0]
a, b, c =  train_images.shape
print a, b, c

import matplotlib.pyplot as plt
digit = train_images[0]
print train_labels[0]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()

from keras import models
from keras import layers

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
network.add(layers.Dense(10, activation='softmax'))

network.compile(optimizer='rmsprop',
               loss='categorical_crossentropy',
               metrics=['accuracy'])

train_images = train_images.reshape((60000, 28*28))
train_images = train_images.astype('float32') / 255
# 정규화 시켜줘서(0~1 값으로 바꿔서) softmax에 넣기 좋은 input값으로 바꿔준다
# 왜냐면 한 픽셀당 0~255까지 RGB값을 갖고 있으니까

# train과 같은 값으로 바꾸어 준다. 우리가 이미 255란 걸 알고 있는 상황에서 하는게 한계.
test_images = test_images.reshape((10000, 28*28))
test_images = test_images.astype('float32') / 255

from keras.utils import to_categorical

# input : 5 면 to_categorical output : [ 0 0 0 0 0 1 0 0 0 0 ]
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

network.fit(train_images, train_labels, epochs=5, batch_size=128)
#batch_size = 60000장 중에 128씩 끊어서 넣는다, 60000 다 도는게 1번의 epoch임
#batch_size는 클 수록 정확도가 높아질 것이다. 한 번에 많이 넣으니까. batch size가 너무 작으면 local minima에 빠진다

test_loss, test_acc = network.evaluate(test_images, test_labels)

print('test_acc:', test_acc)
