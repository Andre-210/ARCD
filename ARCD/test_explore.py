from streamlit.testing.v1 import AppTest
from AI import image_generator
from DB.get_room import get_room
from DB.get_theme import get_theme
from google.cloud import bigquery
from unittest.mock import Mock

nav_mock = """ 
import streamlit as st
import nav_bar as utl
import explore_page

#set the universal coniguration of the pages and the website title
st.set_page_config(layout="wide", page_title='ARCDapp')
st.set_option('deprecation.showPyplotGlobalUse', False)
# style the navigation bar
utl.inject_custom_css()
utl.navbar_component()

explore_page.main()
"""

# testing the initial page (and in turn, the presence of the 'Generate Image' button)
def test_initial_page() :
    app = AppTest.from_string(nav_mock) # initializing an AppTest object from the file containing the app
    app.run(timeout=10)  # run the app for 10 seconds
    # check if only the 'Generate Image' button is displayed
    assert len(app.button) == 1
    assert "Generate Image" in app.button[0].label  # check if the button label contains "Generate Image"
    
# testing the image_generator function (checks if an image is generated)
def test_userInput_image_generation() :
    # running the page
    app = AppTest.from_string(nav_mock)
    app.run(timeout=10)
    assert len(app.button) == 1
    # checking and clicking the 'Generate Image' button
    assert "Generate Image" in app.button[0].label
    app.button[0].click().run(timeout=30)
    # getting the captions list from the session state
    captions = app.session_state.captions
    # checking if there is a caption in the list
    assert len(captions) == 1
    # getting the generated_images list from the session state
    images = app.session_state.generated_images
    # check if there is an image in the list
    assert len(images) == 1

# testing the download button
def test_userInput_downloadButton() : # test from user input
    # running the page
    app = AppTest.from_string(nav_mock)
    app.run(timeout=10)
    assert len(app.button) == 1
    # checking and clicking the 'Generate Image' button
    assert "Generate Image" in app.button[0].label
    app.button[0].click().run(timeout=30)
    # getting the captions list from the session state
    captions = app.session_state.captions
    print(captions)#DELETE
    # checking if there is a caption in the list
    assert len(captions) == 1
    # getting the generated_images list from the session state
    images = app.session_state.generated_images
    ##print(images)#DELETE
    # check if there is an image in the list
    assert len(images) == 1
    # check if the number of buttons on the page is 3
    assert len(app.button) == 3
    # check if the tags of the buttons are correct
    assert "◄ Prev" in app.button[1].label
    assert "Next ►" in app.button[2].label
    # get the download button by its label
    download_button = app.get("download_button")[0]
    # check the download button
    assert "download_button" in download_button.type

# testing get_theme function (is used for the prompt in image_generator)
def test_get_theme() :
    # initialize BigQuery client
    client = bigquery.Client()
    # call the get_theme function
    theme = get_theme(client)
    # check if a theme was found
    assert theme is not None

# testing get_room function (is used for the prompt in image_generator)
def test_get_room() :
    # initialize BigQuery client
    client = bigquery.Client()
    # call the get_room function
    room = get_room(client)
    # check if a room was found
    assert room is not None
