import streamlit as st
import spacy
import pandas as pd

@st.cache(allow_output_mutation=True)
def load_model(name):
    return spacy.load(name)

@st.cache(allow_output_mutation=True)
def process_text(spacy_model,text):
    return spacy_model(text)

#nlp = load_model("en_core_web_sm")
nlp = spacy.load("en_core_web_md")

st.title("NER Demo")

my_sentence = None

my_sentence = st.text_input("Enter your sentence")

if my_sentence:
    data = []
    doc = nlp(my_sentence)
    for ent in doc.ents:
        data.append((ent.text,ent.label_))
    df = pd.DataFrame(data,columns=['Text','Entity']).set_index(['Text'])
    if len(df) > 0:
        st.write(df)
    else:
        st.write("No Entities found!")