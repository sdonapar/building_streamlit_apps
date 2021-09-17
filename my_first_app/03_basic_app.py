#!/usr/bin/env python
"""
Following are demonstrated in this app
1. displyaing text, markdown and pandas dataframe
2. Metric widget
"""

import streamlit as st
import pandas as pd

@st.cache
def get_data(url):
    df_list = pd.read_html(url)
    return df_list



st.write("# My First App")

st.write("## Hello World!!")

df = pd.DataFrame(
    data = {
        'Id': [1,2,3],
        'Library Name' : ['Streamlit','Dash','Panel'],
        'Rating' : ['****','***','**'] 
    }
)
url = "https://www.geonames.org/countries/"
my_text = f'<p style="font-family:Courier; color:Blue; font-size: 8px;">{url}</p>'
df_list = pd.read_html(url)
st.metric(label="No of Tables",value=len(df_list),delta=1)
st.write(df_list[1])

st.markdown(my_text, unsafe_allow_html=True)

st.success("I have built my first app successfully")
