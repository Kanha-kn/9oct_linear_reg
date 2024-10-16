import streamlit as st
import joblib
import sklearn as sk
import numpy as np

st.title("Price Prediction")
st.image("_img.jpeg")

house_size=st.number_input("please enter size of the house")
bedrooms=st.number_input("please enter no of bedrooms")

l_model=joblib.load('predict.pkl')

if st.button("predict"):
    features = np.array([[house_size,bedrooms]])
    output= l_model.predict(features)
    st.write(f"the price of the house is {output[0]}")