import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout

def load_data(data_dir):
    categories = ["yes", "no"]
    data = []
    for category in categories:
        path = os.path.join(data_dir, category)
        label = 1 if category == "yes" else 0

        for img_file in os.listdir(path):
            try:
                img_path = os.path.join(path, img_file)
                img = cv2.imread(img_path)
                img = cv2.resize(img, (150, 150))
                data.append([img, label])
            except Exception as e:
                print(f"Skipping file {img_file} due to error: {e}")
    return data

def preprocess_data(data):
    X = []
    y = []
    for features, label in data:
        X.append(features)
        y.append(label)
    X = np.array(X) / 255.0
    y = np.array(y)
    return X, y

def build_model():
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(150,150,3)),
        MaxPooling2D(2,2),
        Conv2D(64, (3,3), activation='relu'),
        MaxPooling2D(2,2),
        Flatten(),
        Dense(128, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def main():
    data_dir = "dataset"
    model_dir = "model"
    os.makedirs(model_dir, exist_ok=True)

    print("Loading data...")
    data = load_data(data_dir)
    print(f"Total images loaded: {len(data)}")

    print("Preprocessing data...")
    X, y = preprocess_data(data)

    print("Splitting data...")
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Building model...")
    model = build_model()

    print("Training model...")
    model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))

    print("Saving model...")
    model.save(os.path.join(model_dir, "brain_tumor_cnn.h5"))
    print("Model saved successfully!")

if __name__ == "__main__":
    main()
