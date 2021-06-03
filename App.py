import numpy as np
import joblib
import sklearn
import pandas
import streamlit as st
lr = joblib.load('linearregression.joblib')

def welcome():
    return "Welcome All"

def pred_yield(row, clonesize, honeybee, bumbles, andrena, osmia,maxutrange, minutrange,avgutrange,maxltrange,minltrange,avgltrange,rainingdays,avgrainingdays,fruitset,fruitmass,seeds):

    prediction = lr.predict([[row, clonesize, honeybee, bumbles, andrena, osmia,maxutrange, minutrange,avgutrange,maxltrange,minltrange,avgltrange,rainingdays,avgrainingdays,fruitset,fruitmass,seeds]])
    print('prediction')
    return prediction


def main():

    st.title('Blueberry Yield Predictor')

    clonesize = st.text_input('clonesize','Type Here')
    honeybee = st.text_input('honeybee','Type Here')
    bumbles = st.text_input('bumbles','Type Here')
    andrena = st.text_input('andrena','Type Here')
    osmia = st.text_input('osmia','Type Here')
    maxutrange = st.text_input('maxutrange','Type Here')
    minutrange = st.text_input('minutrange','Type Here')
    avgutrange = st.text_input('avgutrange','Type Here')
    maxltrange = st.text_input('maxltrange','Type Here')
    minltrange = st.text_input('minltrange','Type Here')
    avgltrange = st.text_input('avgltrange','Type Here')
    rainingdays = st.text_input('rainingdays','Type Here')
    avgrainingdays= st.text_input('avgrainingdays','Type Here')
    fruitset = st.text_input('fruitset','Type Here')
    fruitmass = st.text_input('fruitmass','Type Here')
    seeds = st.text_input('seeds','Type Here')
    pred=""
    result=0
    row=1
    if st.button("Predict"):
        result=pred_yield(row, clonesize, honeybee, bumbles, andrena, osmia,maxutrange, minutrange,avgutrange,maxltrange,minltrange,avgltrange,rainingdays,avgrainingdays,fruitset,fruitmass,seeds)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Built with Streamlit")


if __name__ == '__main__':

    main()
