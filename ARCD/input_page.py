import streamlit as st

import io
import time

from AI.text import generate_text as text_module # changed from API to AI
from AI.Image import transform_image as edit_image # changed from API to AI

from google.cloud import bigquery

from DB.upload_to_bucket import upload_file_to_bucket as upload_to_bucket
from DB.upload_to_bucket import make_blob_public as make_object_public 
from DB.upload_to_bucket import get_dynamic_public_url as get_url
from DB.upload_to_bucket import upload_processed_image_to_bucket as upload_new_image_to_bucket

from DB.bucket_to_query import record_complete_image_metadata as send_data_to_db

from PIL import Image
from dotenv import load_dotenv
import os

def main() :
    # Load environment variables from .env file
    load_dotenv()

    project_id = os.getenv("PROJECT_ID")
    location = os.getenv("LOCATION")

    # Ensure you use the correct selected type from the session state
    prompt = ""

    # read the css file to override the base css streamlit provides 
    with open("input_styles.css") as css:
        st.markdown(f'<style>{css.read()}</style>', unsafe_allow_html=True)

    # tracking the state of the button when not clicked
    if 'submit_clicked' not in st.session_state:
        st.session_state.submit_clicked = False

    if 'selected_type' not in st.session_state:
        st.session_state.selected_type = ""

    if 'processed_image' not in st.session_state:
        st.session_state.processed_image = None

    # parts of the page
    col1, spacer, col2 = st.columns([1, 0.1, 1])

    # left side of the page
    with col1:
        st.markdown(f"""<h1 class="page-header">Design Your Room</h1>""", unsafe_allow_html=True)
        st.markdown(f'''
            <p class="description">
                Explore an array of room styles to personalize your space! 
                From punk to traditional and everything in between, select the perfect style that reflects your taste. 
                Alternatively, craft your unique style by simply typing in the command below!
            </p>
            ''', unsafe_allow_html=True)

        uploaded_file = st.file_uploader("Upload an image of your room:", type=['png', 'jpg', 'jpeg'])
        if uploaded_file is not None and not st.session_state.submit_clicked:
            # Save uploaded file in session state when first uploaded and not yet submitted
            st.session_state.uploaded_file = uploaded_file
        
        st.markdown(f"""<h4 class="design-types">Select Interior Design Type:</h4>""", unsafe_allow_html=True)

        # list of button names
        button_labels = ["Punk", "Bohemian", "Oceanic", 
                        "Gothic", "Industrial", "Modern", 
                        "Futuristic", "Contemporary", "Southwestern"]
        
        selected_button = None

        # 3 buttons per row
        num_rows = len(button_labels) // 3 + (len(button_labels) % 3 > 0)

        # Loop through each row
        for i in range(num_rows):
            # Generate columns for the current row
            cols = st.columns(3)
            # Loop through each column in the current row
            for j in range(3):
                # Calculate the index of the current button
                index = i*3 + j
                # Check if the current index is within the range of button_labels
                if index < len(button_labels):
                    # Place a button in the current column with the current label
                    label = button_labels[index]
                    with cols[j]:
                        # Disable the button if submit has been clicked
                        button_disabled = st.session_state.submit_clicked
                        # Render a button and check if it's been clicked
                        if st.button(label, key=label, disabled=button_disabled):
                            # When clicked, update the selected design type in the session state
                            st.session_state.selected_type = label
                            selected_button = label

        if st.session_state.selected_type:
            st.markdown(f"Selected design type: **{st.session_state.selected_type}**")

        text_input = st.text_area (
            "Enter any additional requests to stylize your home 👇"
        )

        # setting some spacing to position the button
        inner_spacer1, inner_col_1, inner_col_2, inner_spacer2 = st.columns([1, 1, 1, 1])
        
        with inner_col_1:
            
            # placing the button 
            # TODO: change the color of the button to #1B4332
            if st.button("Submit", key='submit_image'):
                st.session_state.submit_clicked = True
                if uploaded_file is not None:

                    prompt = f"Using the selected design type '{st.session_state.selected_type}', the image, and the additional requests: {text_input}, redesign the home."
                    # Call the image transformation function and save the result in session_state
                    st.session_state.processed_image = edit_image(uploaded_file, prompt, location, project_id)
        with inner_col_2:        
                if st.button("Start Over", key='reset_session'):
                    # Reset session state variables
                    st.session_state.submit_clicked = False
                    st.session_state.selected_type = ""
                    st.session_state.processed_image = None
                    st.session_state.uploaded_file = None


    with col2:
        with st.container():

            st.markdown(f"""<h4 class="before-room">Before:</h4>""", unsafe_allow_html=True)


            if st.session_state.submit_clicked:
                if 'uploaded_file' in st.session_state and st.session_state.uploaded_file is not None:
                    # Display the uploaded file saved in session_state
                    st.image(st.session_state.uploaded_file, use_column_width=True)


                # Check if an image has been processed and set in session_state
                if 'processed_image' in st.session_state and st.session_state.processed_image is not None:

                    st.markdown(f"""<h4 class="after-room">After:</h4>""", unsafe_allow_html=True)
                    st.image(st.session_state.processed_image)

                    image_description = text_module(st.session_state.processed_image, f"make a detailed description of the room and from the {prompt}")
                    text_placeholder = st.empty()
                    text_stream = ""

                    if image_description is not None:
                        for i in range(len(image_description)):
                            text_stream += f"{image_description[i]}"
                            text_placeholder.text(text_stream)
                        time.sleep(0.005)
                    else:
                        st.error("No image description was generated.")

                else:
                    st.error("No image has been processed. Please upload an image and click submit.")


                # uploading the image to the bucket first 
                upload_to_bucket("initial_image_upload", uploaded_file, uploaded_file.name, "old_images")
                
                #location of where we are placing the old image in the bucket
                old_object_file_address = f"old_images/{uploaded_file.name}"

                # we make sure the image is public to obtain a public link which is later tracked in the db
                make_object_public("initial_image_upload", old_object_file_address)
                
                # we get the public url of the object
                old_url = get_url("initial_image_upload", old_object_file_address)

                # after processing the edited image will be passed to the bucket first 
                processed_image = st.session_state.processed_image
                processed_image_name = f"{uploaded_file.name}_processed_image"
                upload_new_image_to_bucket("initial_image_upload", processed_image, processed_image_name, "new_images")

                # we make sure the image is public
                new_object_file_address = f"new_images/{processed_image_name}"
                make_object_public("initial_image_upload", new_object_file_address) 

                # we get the public url for the bucket
                new_url = get_url("initial_image_upload", new_object_file_address) 

                # send the data to the db 
                send_data_to_db("Room_design_dataset", "image_upload_table", old_url, new_url, text_stream)
