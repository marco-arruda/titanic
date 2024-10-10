import streamlit as st

st.title('Marco')

input = st.text_input('Nome:')

st.write('Olá,', input)