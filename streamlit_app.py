import streamlit as st
import pandas as pd

st.title('Machine Learning App')

st.write('This is a machine learning app and builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('label_encoding_std-Original_V01.csv')
  df

  st.write('**Input Variable**')
  X = df.drop('cat_ppm', axis=1)
  X

  st.write('**Output Variable**')
  Y = df.cat_ppm
  Y

with st.expander('Data visualization')
  st.scatter_chart(data=df, x='Area', y='Unit per strip', color='cat_ppm')
