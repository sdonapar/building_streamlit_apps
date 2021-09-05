import streamlit as st
from streamlit_plotly_events import plotly_events
import plotly.express as px
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode
from table_configuration import get_table_configuration

import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout='wide')

@st.cache
def get_data():
    df = px.data.iris()
    return df

df = get_data()

if 'selected_points' not in st.session_state:
    st.session_state['selected_points'] = []

st.title("Iris Data")
col1, col2 = st.columns((4,2))
colors = list(df['species'].drop_duplicates())
#st.write(colors)

#
color_discrete_map={
                "versicolor": "red",
                "setosa": "green",
                "virginica": "magenta",}

fig = px.scatter(
    df, x="sepal_width", y="sepal_length",color="species", symbol="species",
    color_discrete_map=color_discrete_map,
)
with col1:
    selected_points = plotly_events(fig, click_event=True,select_event=False, hover_event=False,override_height=800)
if selected_points:
    for selected_point in selected_points:
        if selected_point not in st.session_state['selected_points']:
            st.session_state['selected_points'].append(selected_point)
            print(selected_point)
            #print(df_temp.iloc[selected_point['pointIndex']])

with col2:
    data = []
    for point in st.session_state['selected_points']:
        color = colors[int(point['curveNumber'])]
        records = df[df.species==color].iloc[[point['pointIndex']]].to_dict("records")
        data.extend(records)
    if data:
        df_selected = pd.DataFrame(data)
    else:
        df_selected = pd.DataFrame(data=[],columns=df.columns)
    grid_options = get_table_configuration(df_selected)
    st.subheader("Selected Data")
    grid_response = AgGrid(
        df_selected,
        gridOptions = grid_options,
        height = 500,
        width = "100%",
        data_return_mode = list(DataReturnMode.__members__)[0],
        update_mode = list(GridUpdateMode.__members__)[6],
        fit_columns_on_grid_load = False,
        allow_unsafe_jscode= False,
        enable_enterprise_modules = False
    )
print(list(DataReturnMode.__members__))
print(list(GridUpdateMode.__members__))
print(grid_response['selected_rows'])
if grid_response['selected_rows']:
    with col2:
        st.write(grid_response['selected_rows'])

