import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv('healthcare.csv')

# Dropping Id as it is not of any use

df.drop('id',axis=1,inplace=True)

st.title('Tanishq', anchor=None)
str_text = ':Attribute Information:\n        - gender\n        - age\n        - hypertension\n        - heart_disease\n        - ever_married\n        - work_type\n        - Residence_type\n        - avg_glucose_level\n        - bmi\n        - smoking status\n      - stroke\n '
st.text(str_text)
st.write('**Healthcare Stroke dataset**')

test1= df.loc[(df["stroke"] == 1)]

col1,col2 = st.columns(2,gap='large')

with col1:
    column_name =  st.selectbox(
    'For which column would you like to see the distribution plot of Strokes (as the below plot displays the distribution of just having strokes)?',
    ("age","avg_glucose_level","bmi")
    )

    plt.figure(figsize=(15, 15))

    fig = sns.displot(test1,x=column_name,hue="stroke",element="step")

    st.header("Simple Distribution plot")
    st.pyplot(fig)

with col2:
    column_name_3 =  st.selectbox(
    'Choose the categorical column',
    ("gender","hypertension","heart_disease","ever_married","work_type","Residence_type","smoking_status")
    )
    column_name_4 = st.selectbox(
        'Choose the y axis',
        ("age","avg_glucose_level","bmi")
        )

    plt.figure(figsize=(15, 15))

    fig = sns.catplot(data=test1,x=column_name_3,y=column_name_4,hue="stroke")

    st.header("Simple Categorial plot")
    st.pyplot(fig)

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

col3,col4 = st.columns(2,gap='large')

with col3:
    options = st.multiselect(
        'Features',df.columns[:-1],default=['age','avg_glucose_level','bmi'],key=10
        )

    st.set_option('deprecation.showPyplotGlobalUse', False)
    # st.write('You selected:', options)

    fig3 = sns.pairplot(
    pd.concat([df[options],
               df['stroke']],
              axis=1),hue='stroke')    

    st.header("Simple Pair plot")
    st.pyplot(fig3)

with col4:
    
    column_name_2 =  st.selectbox(
        'For which column would you like to see the KDE plot',
        ("age","hypertension","heart_disease","avg_glucose_level","bmi"),
        key=2
        )

    # st.write('You selected:', column_name)


    plt.figure(figsize=(20, 15))
    fig4 = sns.displot(test1, x=column_name_2, hue="stroke", kind="kde", fill= True)

    st.header("KDE plot")
    st.pyplot(fig4)


st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text(' The below is a first 10 rows of the dataset')
st.dataframe(df.head(10))

