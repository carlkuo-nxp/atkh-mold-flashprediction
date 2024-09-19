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
  Leadframesupplier = st.selectbox('Leadframe supplier; MHT=1 / HDS=0',('0','1'))
  Rough = st.selectbox('Rough design? ; Yes=1 / No=0' ,('0','1'))
  Leaddesign = st.selectbox('Lead design; long-half etching=0 / long-inner lead=1 / normal=2',('0','1','2'))
  Square = st.selectbox('IC is a square? not a square=0 / a square=1',('0','1'))
  Area = st.slider('Area',2.295, 100, 10)
  AssemblyCG = st.slider('Assembly CG', 0, 55, 25 )
  Outline = st.slider('Outline', 0, 55, 25 )
  Subpackage = st.slider('Subpackage', 0, 93, 25)
  Leadframe12NC = st.slider('Leadframe 12NC', 0, 85, 25)
