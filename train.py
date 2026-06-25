import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

from load_data import X, y

print("TRAINING STARTED 🚀")

# =========================
# NORMALIZE SAFETY CHECK
# =========================
X = X.astype("float32")

# =========================
# SPLIT DATA (IMPORTANT)
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    shuffle=True
)

print("Data split done ✔")

# =========================
# ONE HOT ENCODING
# =========================
y_train = to_categorical(y_train, 43)
y_test = to_categorical(y_test, 43)

print("Labels encoded ✔")

# =========================
# MODEL
# =========================
model = Sequential()

model.add(Conv2D(32, (3,3), activation='relu', input_shape=(30,30,3)))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Conv2D(128, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))

model.add(Flatten())

model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(43, activation='softmax'))

print("Model built ✔")

# =========================
# COMPILE
# =========================
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("Model compiled ✔")

# =========================
# TRAIN
# =========================
history = model.fit(
    X_train,
    y_train,
    epochs=10,
    batch_size=64,
    validation_data=(X_test, y_test)
)

print("Training finished ✔")

# =========================
# SAVE MODEL
# =========================
model.save("traffic_sign_model.keras")

print("Model saved 🚀")