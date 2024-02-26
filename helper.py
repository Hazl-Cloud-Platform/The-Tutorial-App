import streamlit as st
from PIL import Image

def removeStreamlitElements():
    '''remove all streamlit element shown by default 
    such as the hambergur menu and deploy button
    '''
    img_logo = Image.open('images/hazl_logo.png')
    st.set_page_config(page_title='Hazl', page_icon=img_logo)
    st.markdown("""
        <style>
            .reportview-container {
                margin-top: -2em;
            }
            #MainMenu {visibility: hidden;}
            .stDeployButton {display:none;}
            footer {visibility: hidden;}
            #stDecoration {display:none;}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
               .block-container {
                    padding-top: 3.5rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
        </style>
        """, unsafe_allow_html=True)
    


def extraSpace():
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')
    st.text('')