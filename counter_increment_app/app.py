import streamlit as st
from datetime import datetime

if 'count' not in st.session_state:
    st.session_state['count'] = 0

@st.cache
def get_time():
    return datetime.now()

start_time = get_time()
#start_time = datetime.now()
st.write(start_time)

#count = 0

if st.button('Increment'):
    st.session_state['count'] += 1
    count = st.session_state['count']
    st.write(f'Clicked! Start Time {start_time}; Count {count}')