import codecs
from gzip import READ
from matplotlib import interactive
from pydantic import ListMinLengthError
import streamlit as st
#from streamlit.hashing import _CodeHasher
import pickle as pkle
import os.path
import streamlit.components.v1 as stc
import numpy
import serial
import requests
import json
import gspread
from datetime import date
import sys
import os
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu
from matplotlib.pyplot import cm
import base64
import uuid
import re
import pandas as pd
import doc_gen
from PIL import Image


def homepage(calc_html, width=700, height=500):
    calc_file = codecs.open(calc_html, 'r')
    page = calc_file.read()
    stc.html(page, width=width, height=height, scrolling=True)


listing = ["ID", "DATE", "GENDER", "SYMPTOMS", "CONTACT WITH POSITIVE CASE", "HIST OF TRAVEL", "ATTENDED A GATHERED OR CROWD",
           "EXPOSURE TO CONTAINMENT AREA", "TESTED COVID BEFORE", "SYMPTOMS IN FAMILY", "COLOR CODE", "TEMPERATURE"]
st.set_page_config(
    page_title="Xiona Report",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.subheader("")
name = ""
name1 = ""
upload_string = ""
i = 1
next = st.sidebar.button('Next')
new_choice = ['Home', 'Generate Report', 'About Xiona']
if os.path.isfile('next.p'):
    next_clicked = pkle.load(open('next.p', 'rb'))

    if next_clicked == len(new_choice):
        next_clicked = 0
else:
    next_clicked = 0


if next:

    next_clicked = next_clicked + 1

    if next_clicked == len(new_choice):
        next_clicked = 0
st.sidebar.markdown(
    "This application is for the participants to download their report", 0)

choice = st.sidebar.radio(
    "go to", ('Home', 'Generate Report', 'About Xiona'), index=next_clicked)

if choice == 'Generate Report':
    print("inside the loop")

    user_input = st.number_input("Enter your unique id")
    if user_input > 0:
        print(user_input)

        result = doc_gen.main(int(user_input))
        print(user_input)

        text1 = str(user_input) + " - Please Wait"
        st.write(text1)

        result2 = []
        print(result)
        for i in range(10):
            result2.append(result[i])
        result2.append(result[-2])
        result2.append(result[-1])
        #df = pd.DataFrame(result2, listing)
        #st.table([listing, result2])
        #st.table((result2, listing))
        # st.columns()
        for i in range(len(listing)):
            cols = st.columns(2)
            cols[0].write(listing[i])
            cols[1].write(result2[i])

if choice == 'Home':
    # stc.html(html_temp)
    img = Image.open("unnamed.jpg")
    st.image(img)
    homepage('xiona1.html')

    # st.subheader("")
