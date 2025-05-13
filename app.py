import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load trained pipeline and dataframe
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title("💻 Laptop Price Predictor")

# 1. Brand
company = st.selectbox('Brand', df['Company'].unique())

# 2. Type of Laptop
type = st.selectbox('Type', df['TypeName'].unique())

# 3. RAM
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# 4. Weight
weight = st.number_input('Weight of the Laptop (kg)', min_value=0.5, max_value=5.0, value=2.0, step=0.1)

# 5. Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# 6. IPS Panel
ips = st.selectbox('IPS Display', ['No', 'Yes'])

# 7. Screen Size
screen_size = st.slider('Screen Size (in inches)', 10.0, 18.0, 13.3)

# 8. Resolution
resolution = st.selectbox(
    'Screen Resolution',
    ['1920x1080', '1366x768', '1600x900', '3840x2160',
     '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440']
)

# 9. CPU Brand
cpu = st.selectbox('CPU', df['Cpu brand'].unique())

# 10. HDD
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

# 11. SSD
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

# 12. GPU
gpu = st.selectbox('GPU Brand', df['Gpu brand'].unique())

# 13. OS
os = st.selectbox('Operating System', df['os'].unique())

# Predict Button
if st.button('Predict Price'):

    # Convert categorical values to numerical
    touchscreen_val = 1 if touchscreen == 'Yes' else 0
    ips_val = 1 if ips == 'Yes' else 0

    # Calculate PPI (Pixels Per Inch)
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5 / screen_size

    # Prepare query
    query = np.array([company, type, ram, weight, touchscreen_val, ips_val, ppi, cpu, hdd, ssd, gpu, os])

    # Ensure column order matches training data
    input_df = pd.DataFrame([query], columns=df.drop('Price', axis=1).columns)

    # Predict and convert from log price
    log_price = pipe.predict(input_df)[0]
    predicted_price = int(np.exp(log_price))

    st.success(f"💰 The predicted price of this laptop configuration is: ₹ {predicted_price}")
