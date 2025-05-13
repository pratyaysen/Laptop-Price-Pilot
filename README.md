# Laptop-Price-Pilot
💻 Laptop Price Predictor
A machine learning-powered web application built with Streamlit that predicts laptop prices based on user-selected configurations. This project uses a dataset of laptop specifications and prices to train a regression model that outputs price predictions in real time.

📁 Dataset
The dataset used is laptop_data.csv, which includes various laptop attributes such as:

Brand

Type

RAM

Weight

Touchscreen / IPS Display

Screen Size / Resolution

CPU / GPU / Storage

Operating System

Price (Target variable)

⚙️ Features
Intuitive Streamlit UI for easy interaction.

User input for hardware specs and features.

Real-time price prediction with a trained machine learning pipeline.

Feature engineering, including PPI (Pixels Per Inch) calculation.

🧪 How it Works
1. Data Preprocessing
Removed irrelevant or duplicate columns.

Cleaned and converted data types (e.g., stripped GB, converted RAM to int, etc.).

Derived new features like PPI to enhance model performance.

2. Model Training
Used scikit-learn pipelines for preprocessing and regression modeling.

Handled categorical variables and scaling within the pipeline.

Applied log transformation on the target variable (price) for better regression performance.

Saved the trained model and processed dataframe as pipe.pkl and df.pkl.

3. Web Application
User selects specs (e.g., brand, RAM, GPU) through dropdowns and sliders.

The app computes derived features (like PPI).

The trained model predicts the log(price), which is then converted back to actual price using np.exp().

The result is displayed in a user-friendly format.

🚀 Getting Started
Clone the repository:

git clone https://github.com/yourusername/laptop-price-predictor.git
cd laptop-price-predictor
Install dependencies:

pip install -r requirements.txt
Run the app:

streamlit run app.py
📦 Requirements
python 3.11.9

pandas

numpy

scikit-learn

matplotlib

seaborn

streamlit

pickle

📊 Screenshot:
upload soon


📌 Conclusion
This project successfully demonstrates how machine learning can be used to predict product prices based on multiple categorical and numerical inputs. The model integrates:

Robust preprocessing with custom feature engineering (like screen PPI),

Efficient use of scikit-learn pipelines for streamlined prediction,

A clean and interactive frontend built with Streamlit.

The result is an intuitive and practical app that helps users estimate the price of a laptop based on their desired configuration. This serves not only as a useful tool for consumers but also as a strong template for deploying regression models in production.
