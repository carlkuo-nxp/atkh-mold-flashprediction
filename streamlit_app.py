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

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='Area', y='Unit per strip', color='cat_ppm')


##Data preparation##
with st.sidebar:
  st.header('Input features')
  Leadframe supplier = st.selectbox('Leadframe supplier',('0','1'))
  AssemblyCG = st.slider('Assembly CG', 0, 55, 25 )
  Outline = st.slider('Outline', 0, 55, 25 )
  Subpackage = st.slider('Subpackage', 0, 93, 25)
  Leadframe12NC = st.slider('Leadframe 12NC', 0, 85, 25)
