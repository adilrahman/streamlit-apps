import streamlit as st
import nltk
from nltk.corpus import words




st.title("wordLE")


@st.cache
def download():
    nltk.download("words")


download()

five_letter_words = [word for word in words.words() if len(word) == 5]

[a, b, c, d, e] = st.beta_columns(5)

with a:
    first_letter = st.text_input(label="1st", value="a")
with a:
    second_letter = st.text_input(label="2nd", value="b")
with a:
    third_letter = st.text_input(label="3rd", value="e")
with a:
    fourth_letter = st.text_input(label="4th", value="")
with a:
    fifith_letter = st.text_input(label="5th", value="t")

clue = first_letter + second_letter + third_letter + fourth_letter + fifith_letter

st.markdown("## CLUE")

st.write(clue)

st.markdown("# Exclusion letters")

exclutions = st.text_input(label="exclusions")

st.markdown("# WordLE CLUE")

clue_result = []

for word in five_letter_words:
    if all(c in word for c in clue) and not any(c in word for c in exclutions):
        clue_result.append(word)

st.write(clue_result)