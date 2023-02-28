import streamlit as st
from PIL import Image

st.title("Data Science Internship :bar_chart:")

btn_click = st.button("Enter!")

if btn_click == True:
    st.subheader("Welcome!!")
    st.balloons()
    st.write('Here is my first task as an Intern in :red[innomatics] :sunglasses:')      