import streamlit as st

def createTextBubble(text, container=st, div_style="", div_class=""):
    # Construct the div tag with optional parameters
    div_tag = f'<div style="{div_style}" class="{div_class}">' if div_style or div_class else '<div>'
    
    # Render the text bubble with the specified div tag
    container.markdown(f"""{div_tag}
    <p style="font-weight: bold;">{text}</p></div>""", unsafe_allow_html=True)
