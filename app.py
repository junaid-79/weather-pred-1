import streamlit as st
import pickle


st.title('Weather Prediction')
model=pickle.load(open('model.pkl','rb'))

col1,col2=st.columns(2)
humidity=col1.number_input('Enter humidity')
temperature=col2.number_input('Enter temperature')
precipitation=col1.number_input('Enter precipitation')



if st.button('Predict'):
    data=[[humidity,temperature,precipitation]]
    result=model.predict(data)[0]
    st.success(result)