#!/usr/bin/env python

"""
Following are demonstrated in the following app

1. call back on_change on the streamlit widget
2. container concept
3. sidebar for some of the inputs
4. slider and text_input widgets

"""
import streamlit as st

my_age_default_value = 21
my_age_min_value = 18
my_age_max_value = 100
my_name_default_value = "Your Name Please"

my_container = st.container()

st.write("This is some test")

st.sidebar.title = "My First Working App"

with my_container:
    st.write("""
    # My First Beautiful App
    """)

def test_func(*args,**kwargs):
    with my_container:
        if len(args) > 0 and args[0]:
            if args[0] <= 21 :
                st.warning("## Welcome to our Young Customer")
            elif args[0] <= 50:
                st.success("## Welcome to our Invested Customer")
            elif args[0] <= 100:
                st.error("## Welcome to our Senior Customer")
            else:
                st.write("## Welcome to our Customer")

age = st.sidebar.slider(
    label = "Select Age",
    min_value = my_age_min_value,
    max_value = my_age_max_value,
    step = 1,
    value = my_age_default_value
)

name = st.sidebar.text_input(
    label= "Enter your name",
    value = my_name_default_value,
    on_change=test_func,
    args=(age,)
)

if name != "Your Name Please":
    st.markdown(f"## Hello -  {name}")