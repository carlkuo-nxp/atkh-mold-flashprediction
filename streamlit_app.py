import streamlit as st
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix

st.title('Machine Learning App')

st.write('This is a machine learning app and builds a machine learning model!')

with st.expander('Data'):
  st.write('**Raw data**')
  df = pd.read_csv('label_encoding_std-Original_V01.csv')
  df

  st.write('**Input Variable**')
  X_raw = df.drop('cat_ppm', axis=1)
  X_raw

  st.write('**Output Variable**')
  Y_raw = df.cat_ppm
  Y_raw

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='Area', y='Unitperstrip', color='cat_ppm')


##Input features##
with st.sidebar:
  st.header('Input features')
  Leadframesupplier = st.selectbox('Leadframe supplier; MHT=1 / HDS=0',('0','1'))
  Rough = st.selectbox('Rough design? ; Yes=1 / No=0' ,('0','1'))
  Leaddesign = st.selectbox('Lead design; long-half etching=0 / long-inner lead=1 / normal=2',('0','1','2'))
  Square = st.selectbox('IC is a square? no=0 / yes=1',('0','1'))
  Dimple = st.selectbox('Dimple design? ; Deep=0 / No=1 / Normal=2',('0','1','2'))
  Wiretype = st.selectbox('Wire type ; Au=0 / Cu=1',('0','1'))
  Compound = st.selectbox('Compound',('0','1','2','3','4','5'))
  Taping = st.selectbox('Taping; post-taping=0 / pre-taping=1',('0','1'))
  Area = st.slider('Area', 2.295, 100.000, 10.000 )
  Unitperstrip = st.slider('Unit per strip', 110, 3990, 500)
  AssemblyCG = st.slider('Assembly CG', 0, 55, 25 )
  Outline = st.slider('Outline', 0, 55, 25 )
  Subpackage = st.slider('Subpackage', 0, 93, 25)
  Leadframe12NC = st.slider('Leadframe 12NC', 0, 85, 25)

##Create a dataframe for the input features##
data = { 'Leadframesupplier' : Leadframesupplier,
        'Rough' : Rough,
        'Leaddesign' : Leaddesign,
        'Square' : Square,
        'Dimple' : Dimple,
        'Wiretype' : Wiretype,
        'Compound' : Compound,
        'Taping' : Taping,
        'Area' : Area,
        'Unitperstrip' : Unitperstrip,
        'AssemblyCG' : AssemblyCG,
        'Outline' : Outline,
        'Subpackage' : Subpackage,
        'Leadframe12NC' :  Leadframe12NC}
input_df = pd.DataFrame(data, index=[0])
input_label_encoding = pd.concat([input_df, X_raw], axis=0) ##axis=0 append by row, o.w. axis=1 append by column##

with st.expander('Input  features'):
 st.write('**Input data**')
 input_df
 st.write('**Combined all input data**')
 input_label_encoding

##Data preparation##
##Encode X ## (testing)
#encode = ['Leadframesupplier','Rough','Leaddesign','Square','Dimple','Wiretype','Compound','Tape']
#df_input = pd.get_dummies(input_label_encoding, prefix=encode)
#input_row = df_input[:1]

##Encode Y ## (testing)
target_mapper = {'A':0,
                'B':1,
                'C':2}
def target_encode(val):
  return target_mapper[val]

Y=Y_raw.apply(target_encode)
Y
Y_raw









