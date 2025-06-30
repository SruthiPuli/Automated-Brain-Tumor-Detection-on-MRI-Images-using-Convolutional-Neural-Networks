import tensorflow as tf
import numpy as np
import cv2
import os

# Load the saved model (only once)
model_path = os.path.join(os.path.dirname(__file__), 'model', 'brain_tumor_cnn.h5')
model = tf.keras.models.load_model(model_path)

def predict_tumor(image_path):
    try:
        img = cv2.imread(image_path)
        img = cv2.resize(img, (150, 150))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)
        prediction = model.predict(img)[0][0]
        return "Tumor" if prediction > 0.5 else "No Tumor"
    except Exception as e:
        return f"Prediction error: {e}"
