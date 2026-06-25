# 🚦 Traffic Sign Recognition using CNN

A machine learning-based Traffic Sign Recognition System built using Python, TensorFlow, and Streamlit.  
The model classifies traffic signs into 43 categories using a Convolutional Neural Network (CNN) trained on the GTSRB dataset.

---

## 📌 Project Overview

This project takes an image of a traffic sign and predicts what sign it is (e.g., Stop, Speed Limit, No Entry, etc.).  
It includes a trained CNN model and a simple web interface built with Streamlit for real-time predictions.

---

## 🎯 Features

- CNN-based image classification model
- 43 traffic sign categories (GTSRB dataset)
- Image upload and real-time prediction
- Confidence score display
- Interactive Streamlit web app
- Fast inference using trained model

---

## 🧠 Tech Stack

- Python
- TensorFlow / Keras
- NumPy
- Pillow (PIL)
- Streamlit
- Scikit-learn

---

## 📁 Project Structure

traffic-sign-recognition/
│
├── app.py                      # Streamlit web app
├── train.py                    # Model training script
├── load_data.py                # Dataset loading & preprocessing
├── labels.py                  # Class label mapping (43 classes)
├── traffic_sign_model.keras   # Trained CNN model
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation

---

## 📊 Dataset

This project uses the German Traffic Sign Recognition Benchmark (GTSRB) dataset.

- 43 traffic sign classes
- Thousands of labeled images
- Real-world traffic sign variations

---

## 🚀 How to Run the Project

### 1. Clone the repository

git clone https://github.com/your-username/traffic-sign-recognition.git
cd traffic-sign-recognition

---

### 2. Install dependencies

pip install -r requirements.txt

---

### 3. Run Streamlit app

streamlit run app.py

---

## 🧪 Model Training (Optional)

To retrain the model:

python train.py

---

## 📸 Example Output

Input: Traffic sign image  
Output: Predicted label + confidence score  

Example:

Prediction: Stop Sign 🚦  
Confidence: 0.98

---

## 🧠 Model Architecture

- Conv2D → MaxPooling
- Conv2D → MaxPooling
- Conv2D → MaxPooling
- Flatten
- Dense (128 units)
- Dropout (0.5)
- Dense (Softmax output layer - 43 classes)

---

## 📈 Results

- High training accuracy
- Good validation performance
- Real-time prediction using Streamlit

---

## 👩‍💻 Author

Sadaf  
Computer Science Student  
Focus: Data Science, Machine Learning, Data analysis

---

## ⭐ Future Improvements

- Deploy on Streamlit Cloud
- Improve accuracy with data augmentation
- Add top-3 predictions
- Enhance UI design

---

## 📌 Note

This project demonstrates:
- CNN-based image classification
- End-to-end machine learning pipeline
- Real-time deployment using Streamlit
