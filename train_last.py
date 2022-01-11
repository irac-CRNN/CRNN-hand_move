from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Bidirectional
from tensorflow.keras.layers import LSTM, BatchNormalization
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.wrappers import TimeDistributed
from tensorflow.keras.preprocessing import image
from keras.applications.resnet import ResNet50
from tensorflow.keras.utils import to_categorical
import numpy as np
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt

train = pd.read_csv('train_list.csv')
test = pd.read_csv('test_list.csv')

train_image = []
test_image = []

frame = []
k = 0

# for loop to read and store frames
for i in tqdm(range(train.shape[0])):
    train_img = image.load_img('train/'+train['image'][i], target_size=(64,36,3))
    train_img = image.img_to_array(train_img)
    train_img = train_img/255
    frame.append(train_img)
    k += 1
    if k > 25:
        train_image.append(frame)
        frame = []
        k = 0
    
for i in tqdm(range(test.shape[0])):
    test_img = image.load_img('test/'+test['image'][i], target_size=(64,36,3))
    test_img = image.img_to_array(test_img)
    test_img = test_img/255
    frame.append(test_img)
    k += 1
    if k > 25:
        test_image.append(frame)
        frame = []
        k = 0

X_train = np.array(train_image)
X_test = np.array(test_image)

Y_train = np.zeros((len(X_train),))
Y_train[0:10] = 0
Y_train[10:20] = 1
Y_train[20:30] = 2
Y_train[30:40] = 3
Y_train[40:50] = 4
Y_train = to_categorical(Y_train)

Y_test = np.zeros((len(X_test),))
Y_test[0:2] = 0
Y_test[2:4] = 1
Y_test[4:6] = 2
Y_test[6:8] = 3
Y_test[8:10] = 4
Y_test = to_categorical(Y_test)

#Y_train = train['class']
#Y_test = test['class']

#Y_train = pd.get_dummies(Y_train)
#Y_test = pd.get_dummies(Y_test)

#train_dataset = timeseries_dataset_from_array(X_train, Y_train, sequence_length=26, sequence_stride=26, batch_size=10)
#test_dataset = timeseries_dataset_from_array(X_test, Y_test, sequence_length=26, sequence_stride=26, batch_size=10)

base_model = ResNet50(include_top=False, weights='imagenet', input_shape=(64,36,3), pooling='max')

model = Sequential()
#model.add(TimeDistributed(base_model, input_shape=(None,64,36,3)))
model.add(TimeDistributed(Conv2D(32, (3,3), activation='relu', padding='same'), input_shape=(26,64,36,3)))
model.add(BatchNormalization())
model.add(TimeDistributed(MaxPooling2D(pool_size=(2,2), strides=(2,2))))
model.add(TimeDistributed(Conv2D(64, (3,3), activation='relu', padding='same')))
model.add(BatchNormalization())
model.add(TimeDistributed(MaxPooling2D(pool_size=(2,2), strides=(2,2))))
model.add(TimeDistributed(Conv2D(128, (3,3), activation='relu', padding='same')))
model.add(BatchNormalization())
model.add(TimeDistributed(MaxPooling2D(pool_size=(2,2), strides=(2,2))))
model.add(TimeDistributed(Conv2D(256, (3,3), activation='relu', padding='same')))
model.add(BatchNormalization())
model.add(TimeDistributed(MaxPooling2D(pool_size=(2,2), strides=(2,2))))
model.add(TimeDistributed(Flatten()))
model.add(Bidirectional(LSTM(256, activation='tanh', return_sequences=True)))
model.add(Bidirectional(LSTM(256, activation='tanh')))
model.add(Dense(1024, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(5, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()

hist = model.fit(X_train, Y_train, batch_size=1, epochs=100, shuffle=True, validation_data=(X_test, Y_test))

model.save('model/crnn_model.h5')
print('Saved model successfully')

output = model.predict(X_test)
classes_x = np.argmax(output, axis=1)
print(classes_x)

train_loss=hist.history['loss']
val_loss=hist.history['val_loss']
train_acc=hist.history['accuracy']
val_acc=hist.history['val_accuracy']
xc=range(100)

timedisloss=plt.figure(1,figsize=(7,5))
plt.plot(xc,train_acc)
plt.plot(xc,train_loss)
plt.xlabel('num of Epochs')
plt.ylabel('acc & loss')
plt.title('train')
plt.grid(True)
plt.legend(['acc','loss'])
print("plotting")

timedisacc=plt.figure(2,figsize=(7,5))
plt.plot(xc,val_acc)
plt.plot(xc,val_loss)
plt.xlabel('num of Epochs')
plt.ylabel('acc & loss')
plt.title('validation')
plt.grid(True)
plt.legend(['acc','loss'])

plt.show()