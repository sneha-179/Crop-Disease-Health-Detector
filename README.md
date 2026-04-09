# Crop Disease Health Detector 🌿

A Deep Learning project that detects crop diseases from leaf images 
using CNN (Convolutional Neural Network).

## Project Structure
Crop_Health_Disease/
├── dataset/          # PlantVillage dataset (not included - see below)
├── model/            # Saved trained model
├── notebooks/        # EDA and experimentation
├── split_dataset.py  # Splits dataset into train/val
├── train.py          # Model training script
└── requirements.txt  # Required libraries

## Dataset
Download PlantVillage dataset from Kaggle:
https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset

Place it in the dataset/ folder and run:
    python split_dataset.py

## Setup & Run

### 1. Create virtual environment
    python -m venv venv
    venv\Scripts\activate      # Windows
    source venv/bin/activate   # Mac/Linux

### 2. Install libraries
    pip install -r requirements.txt

### 3. Split dataset
    python split_dataset.py

### 4. Train model
    python train.py

## Tech Stack
- Python
- TensorFlow / Keras
- FastAPI
- OpenCV
- NumPy, Pandas, Matplotlib