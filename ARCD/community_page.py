import sys
sys.path.append('community_helpers')

import streamlit as st
from helpers import *
from bigquery_helper import *
from shared_components.createTextBubble import createTextBubble
from PIL import Image

def main():
    # Import styles.css
    with open( "community_helpers/styles.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

    st.title("The Community")
    search_input = st.text_input(placeholder="What's on your mind?", label="")

    # Define your CSS
    css = """
    <style>
    .styled-container {
        background-color: black;
        border-radius: 10px;
        padding: 10px;
        margin: 10px;
    }
    </style>
    """

    # Inject CSS with Markdown
    st.markdown(css, unsafe_allow_html=True)

    if search_input:
        searchPosts(search_input)
    else:
        data = get_all_posts()
        displayPosts(data)
