import streamlit as st
from Components.components import About
from Components.components import title
from Components.components import image_selector
from Components.components import possible
from Components.components import initialize_session_state

# main function
def main() :

    # initialize session state
    initialize_session_state()

    # inject CSS for the text bubble and buttons
    with open("styles.css") as css:
        st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

    # call on the title and header
    title()

    # initialize columns to set About/possible on left and Image_selector on right
    col1, col2, col3 = st.columns([1, 0.1, 1])

    # left column 
    with col1:
        # call on About
        About()
        # call on possible
        possible()

    # middle column
    with col3:
        # call on the image_selector
        image_selector()
