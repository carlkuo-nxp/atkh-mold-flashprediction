import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.write('This is a machine learning app and builds a machine learning model!')

df = pd.read_csv('label_encoding_std-Original_V01.csv')
df
