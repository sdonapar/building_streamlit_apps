import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

st.title("Country Demographics")

col1, col2 = st.columns(2)

@st.cache(show_spinner=False)
def get_data(url):
    df_list = pd.read_html(url)
    if len(df_list) > 1:
        return df_list[1]
    else:
        return pd.DataFrame()

url = "https://www.geonames.org/countries/"

with st.spinner("Loading Data...."):
    df_countries = get_data(url)

selected_country = st.sidebar.selectbox("Select Country",list(df_countries.Country),index=104)

columns = ['ISO-3166alpha3','Country','Capital','Area in km²','Population','Continent']




with col2:
    df_filtered = df_countries[df_countries.Country==selected_country][columns].copy()
    st.table(df_filtered)

with col1:   
    df_countries_l = df_countries[df_countries.Country.str.startswith(selected_country[0])].reset_index(drop=True).copy()
    st.metric(label="Number of Countries",value=len(df_countries_l))
    df_countries_l['Mean'] = df_countries_l['Area in km²'].mean()
    st.bar_chart(df_countries_l.set_index(['Country'])[['Area in km²','Mean']])

with st.expander("All Countries"):
    st.dataframe(df_countries)