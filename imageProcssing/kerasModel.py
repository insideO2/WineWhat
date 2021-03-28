from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
from keras.utils import np_utils
import os
import numpy as np

# 분류 대상 카테고리
root_dir = "./image/101_ObjectCategories"
categories = ["accordion", "airplanes", "anchor", "ant", "BACKGROUND_Google"]
nb_classes = len(categories)
image_size = 50

def main():
    # 데이터 다운로드
    X_train, X_test, y_train, y_test = np.load("./image/5obj.npy",  allow_pickle=True)

    # 데이터 정규화
    X_train = X_train.astype("float") / 256
    X_test  = X_test.astype("float") / 256
    y_train = np_utils.to_categorical(y_train, nb_classes)
    y_test  = np_utils.to_categorical(y_test, nb_classes)

    # 모델을 훈련하고 평가
    model = model_train(X_train, y_train)
    model_eval(model, X_test, y_test)

# 모델 구축
def build_model(in_shape):
    model = Sequential()
    model.add(Convolution2D(32, 3, 3, padding='same', input_shape=in_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(Dropout(0.25))
    model.add(Convolution2D(64, 3, 3, padding='same'))
    model.add(Activation('relu'))
    model.add(Convolution2D(64, 3, 3))
    model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(nb_classes))
    model.add(Activation('softmax'))
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    return model

# 모델 훈련
def model_train(X, y):
    model = build_model(X.shape[1:])
    model.fit(X, y, batch_size=64, epochs=100)

    # 모델 저장
    hdf5_file = "./image/5obj-model.hdf5"
    model.save_weights(hdf5_file)
    return model

# 모델 평가
def model_eval(model, X, y):

    score = model.evaluate(X, y)
    print('loss=', score[0])
    print('accuracy=', score[1])

if __name__ == "__main__":
    main()