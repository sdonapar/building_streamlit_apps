import streamlit as st
import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

st.title("NER Demo")

my_sentence = None

my_sentence = st.text_input("Enter your sentence")

if my_sentence:
    data = []
    doc = nlp(my_sentence)
    for ent in doc.ents:
        data.append((ent.text,ent.label_))
    df = pd.DataFrame(data,columns=['Text','Entity']).set_index(['Text'])
    st.write(df)