import streamlit as st
import pandas as pd
import numpy as np
import math
import random

st.write('Hi!')
st.title("Make Your Own Chat Bot")

st.header("This is a Header")

st.subheader("subheader")

st.text("text")

st.write("default font")

st.markdown("This is markdown")
st.markdown("# This is markdown heading")
st.markdown("## This is markdown subheading")

name = st.text_area("Enter your name")

button = st.button("Click Me")
if button:
    st.write("Clicked Btn")

