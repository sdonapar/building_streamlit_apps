from math import pi
from altair.vegalite.v4.schema.core import FontStyle
import numpy as np
import pandas as pd

import streamlit as st
from aggrid import interactive_datatable

import altair as alt

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

st.set_page_config(layout="wide")
#st.title("House Price Prediction")

RANDOM_SEED = 42
np.random.seed(RANDOM_SEED)

@st.cache
def train_model():
    df = pd.read_csv('./data/house_prices_train.csv')
    df_validation = pd.read_csv('./data/house_prices_test.csv')

    df_train,df_test = train_test_split(df,test_size=0.2)

    x_train = df_train[['OverallQual', 'GrLivArea', 'GarageCars']] #features
    y_train = df_train['SalePrice']

    x_test = df_test[['OverallQual', 'GrLivArea', 'GarageCars']]
    y_test = df_test['SalePrice']

    pipe_line = Pipeline([
        ('scaler',StandardScaler()),
        ('linear_regressor',linear_model.LinearRegression())
    ])

    pipe_line.fit(x_train,y_train)
    accuracy = pipe_line.score(x_test,y_test)
    return df,pipe_line, accuracy


df,model,accuracy = train_model()

st.sidebar.title("Model Input")
st.title("House Price Prediction")

overall_quality_values = sorted(list(df.OverallQual.unique()))

overall_quality = st.sidebar.slider(
    "Overall Quality",
    int(min(overall_quality_values)),
    int(max(overall_quality_values)),
    step=1,
    value=int(overall_quality_values[3])
)

garage_cars_values = sorted(list(df.GarageCars.unique()))
garage_cars = st.sidebar.selectbox("Garage Cars Space",garage_cars_values,index=2)

df_temp = df[
    (df['OverallQual'] == overall_quality) &
    (df['GarageCars']==garage_cars)
]
living_area = st.sidebar.number_input(
    "Living Area",
    min_value=df.GrLivArea.min(),
    max_value=df.GrLivArea.max(),
    step=100
)
if len(df_temp) > 0:
    min_liv_value = df_temp['GrLivArea'].min()
    max_liv_value = df_temp['GrLivArea'].max()
    st.sidebar.markdown(f"""
    <p style="font-family:Courier; color:Red; font-size: 16px;">Min Value : {min_liv_value}</p>
    <p style="font-family:Courier; color:Red; font-size: 16px;">Max Value : {max_liv_value}</p>
    """,unsafe_allow_html=True)
else:
    min_liv_value = 0
    max_liv_value = 0
    st.sidebar.markdown(f"""
    <p style="font-family:Courier; color:Red; font-size: 16px;">No Training Data</p>
    """,unsafe_allow_html=True)




#submit_button = st.sidebar.button("Submit")
st.sidebar.write("_________")
st.sidebar.write(f"#### Model Accuracy : {round(accuracy,2)}")
st.sidebar.write("_________")

living_area_th = st.sidebar.number_input(
    label="± Living Area Threshold for searching samples",
    min_value = 10,
    max_value=100,
    value=50,
    step=5
)
col1, col2 = st.columns(2)
#if submit_button:
data = [[overall_quality,living_area,garage_cars]]
y_pred = model.predict(data)
my_data = list(data[0])
my_data.append(round(y_pred[0],0))
header = ['Overall Quality','Living Area','Garage Cars Space','Predicted Price']
df_pred = pd.DataFrame([my_data],columns=header)
df_pred_t = df_pred.T.copy()
df_pred_t.columns = ['Value']
df_filtered = df[
    (df['OverallQual'] == overall_quality) &
    ((df['GrLivArea'] >= living_area-living_area_th) & (df['GrLivArea'] <= living_area+living_area_th)) &
    (df['GarageCars']==garage_cars)
]

with col1:
    st.table(df_pred_t)
    st.metric(label="",value="")
    st.metric(label="Samples",value=len(df_filtered))
print(df.columns)

if len(df_filtered) > 0:
    avegage_price = round(df_filtered['SalePrice'].mean(),2)
    with col2:
        st.bar_chart(df_filtered['SalePrice'])
        delta_value = round(y_pred[0]-avegage_price,0)
        st.metric(label="Avegage Price", value=avegage_price,delta=delta_value)

with st.expander("Train Data"):
    
    grid_response,df_grid = interactive_datatable(df_filtered)
    
with st.expander("Scatter Plot"):
    df_temp_plot = df[['SalePrice','GrLivArea','OverallQual','GarageCars','YrSold']].dropna(how='any').copy()
    fig = alt.Chart(df_temp_plot).mark_circle().encode(
        x = 'SalePrice', y='GrLivArea', color='YrSold',size='GarageCars',
        tooltip=['OverallQual','GrLivArea','SalePrice', 'GarageCars']
    )
    st.altair_chart(fig,use_container_width=True)