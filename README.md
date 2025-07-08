# Brain Tumor Prediction Using CNN

Real-time brain tumor detection from MRI images using Convolutional Neural Networks integrated with a responsive web interface.

---
## Description

This project detects the presence of a brain tumor in MRI images using a **Convolutional Neural Network (CNN)**. The model is trained on a medical image dataset and can classify MRI scans as **Tumor** or **No Tumor**. The application is powered by **Python**, **Django**, and **CNN**, and features a web interface using **HTML/CSS/JavaScript** for user interaction and image uploads.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Applications](#applications)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Folder Structure](#folder-structure)
- [License](#license)
- [Author](#author)

---

## Installation

1. **Clone the repository:**

```
git clone https://github.com/YourUsername/Brain-Tumor-Prediction.git
cd Brain-Tumor-Prediction
```

#### 2. Install Dependencies :
```
pip install -r requirements.txt
```

#### 3. Run the Project :
```
python manage.py runserver
```

## Usage

 ## 1: Typing a Few Letters to Save Time
User Input: rec
#### Suggestions:
- recipe
- record
- recovery

### Usage Purpose:
#### 1: Upload an MRI Image
Upload an image from your local system using the file input form.

Example Input:
A brain MRI image file in .jpg, .png, or .jpeg format.

#### 2: Model Predicts Tumor or No Tumor
Upon submission, the system processes the image and displays the prediction result on the screen.

##### Example Output:

 - Tumor Detected

 -  No Tumor Detected
#### 3: View Classification Result with Confidence Score
Displays model confidence (e.g., 98.3%) along with the prediction label.

## Applications

### 1. Medical Diagnostics
Hospitals and clinics can integrate this system to support radiologists in identifying tumor presence in MRI scans.

### 2. Educational Platforms
Used in medical AI labs and courses to demonstrate deep learning applications in healthcare.

### 3. Telemedicine & Remote Screening
Can be used in remote healthcare platforms to screen MRI scans quickly before involving specialists.


## Features
### Accurate Brain Tumor Detection Using CNN
- Built with a deep CNN model trained on labeled MRI scan images

- High accuracy in classifying Tumor vs Non-Tumor categories

- Includes image preprocessing like resizing, normalization, and augmentation

### Simple and Intuitive Web Interface
- Upload MRI images through an easy-to-use HTML form

- Real-time prediction updates directly on the frontend

- Clean UI designed using HTML, CSS, and JavaScript

### Django Backend for Prediction Handling
- Django serves as the backend framework handling image upload, prediction, and response

- RESTful approach ensures scalability and modularity

### Pretrained Model Integration
- Loads pre-trained model weights on startup

- No need to re-train on every run — instant predictions with loaded CNN model


## Tech Stack
### Core Technologies
#### Python
- Image processing and prediction logic
- Model loading, preprocessing, and classification

#### CNN (Convolutional Neural Network)
- Deep learning model built using TensorFlow/Keras
- Trained to distinguish MRI images of tumor vs non-tumor

#### Django
- Backend server for handling image uploads and making predictions
- URL routing, views, and template rendering

#### HTML / CSS / JavaScript
- Frontend interface for user interactions
- Form input for file uploads and dynamic result rendering
## Folder Structure

```
BrainTumorPrediction/
├── MyApp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── Templates/
│   │   └── index.html
│   ├── Backend/
│   │   ├──dataset/
│   │   │   ├── no/
│   │   │   └── yes/
│   │   ├── model.h5
│   │   ├── predictor.py
│   │   ├── main.py
│   │   └── tumor_detecor.ipynb
├── BrainTumorPrediction/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── README.md
└── LICENSE
          

```

## License
This project is open-source and available under the [MIT License](LICENSE).  
© 2025 Sruthi Pulipati

## Author
**Sruthi Pulipati**

This project was created to explore real-world applications of deep learning in healthcare and demonstrate how CNN models can be integrated with web-based platforms for impactful results.

