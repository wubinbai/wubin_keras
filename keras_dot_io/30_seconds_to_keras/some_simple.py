# core data structure of keras is a MODEL, a way to organize layers.
# The simplest type of model is the SEQUENTIAL model, a linear stack of layers.
# For more complex structures, you should use keras functional API, which allow you to build arbitrary graphs of layers

# Here is the Sequential model:

from keras.models import Sequential
model = Sequential()

# Stacking layers is as easy as .add():

from keras.layers import Dense

model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))

# Once your model looks good, configure its learning process with .compile():

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
#If you need to, you can further configure your optimizer. A core principle of Keras is to make things reasonably simple

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))

# You can now iterate on your training data in batches:

# x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.
model.fit(x_train, y_train, epochs=5, batch_size=32)

# Alternatively, you can feed batches to your model manually:

model.train_on_batch(x_batch, y_batch)


#Evaluate your performance in one line:

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

#Or generate predictions on new data:

classes = model.predict(x_test, batch_size=128)


