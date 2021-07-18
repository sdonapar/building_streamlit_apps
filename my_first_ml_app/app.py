from math import pi
from altair.vegalite.v4.schema.core import FontStyle
import numpy as np
import pandas as pd

import streamlit as st

from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split

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

st.sidebar.title("Input Parameters")
st.title("House Price Prediction")

overall_quality_values = sorted(list(df.OverallQual.unique()))

overall_quality = st.sidebar.slider(
    "Overall Quality",
    int(min(overall_quality_values)),
    int(max(overall_quality_values)),
    step=1,
    value=int(overall_quality_values[3])
)

living_area = st.sidebar.number_input(
    "Living Area",
    min_value=df.GrLivArea.min(),
    max_value=df.GrLivArea.max(),
    step=100
)

garage_cars_values = sorted(list(df.GarageCars.unique()))

garage_cars = st.sidebar.selectbox("Garage Cars Space",garage_cars_values,index=2)

submit_button = st.sidebar.button("Submit")

st.sidebar.write(f"Model Accuracy : {round(accuracy,2)}")

if submit_button:
    data = [[overall_quality,living_area,garage_cars]]
    y_pred = model.predict(data)
    my_data = list(data[0])
    my_data.append(round(y_pred[0],0))
    header = ['Overall Quality','Living Area','Garage Cars Space','Predicted Price']
    df_pred = pd.DataFrame([my_data],columns=header)
    df_pred_t = df_pred.T.copy()
    df_pred_t.columns = ['Value']
    st.table(df_pred_t)