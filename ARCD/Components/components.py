import streamlit as st 
from shared_components.createTextBubble import createTextBubble
from DB.get_room import get_room
from DB.get_theme import get_theme
from google.cloud import bigquery
from AI.image_generator import generate_image

# function to display the User Guide and About sections
def About() :

    st.write("")
    # user guide section
    st.markdown("<h2 style='text-align:left; color:#081C15; font-size: 28px;'>User Guide: </h2>", unsafe_allow_html=True)
    # lst with guide
    lst = ["Use the 'Generate' button to generate new images with a random theme each time its clicked.",
           "The 'Next' button and the ‘Previous’ button can be used to navigate the last 10 generated images. ", 
           "If you've generated 10 images and click 'Generate' again, the viewer resets, clearing the previous 10 images and starting the cycle anew.", 
           "Download any of the displayed images by clicking on the 'Download' button located next to each image."]
    # initialize the String to hold an element from the lst and the number to display for each corresponding element
    s = ''
    num = 0
    # for loop to traverse the lst and create the String
    for i in lst:
        num += 1
        s += f'<p style="color:#081C15; margin-left: 20px;">{str(num)}. {i}</p>'
    # display the String
    st.markdown(s, unsafe_allow_html=True)
    return s

# function for creating the title
def title() :
        # center the text bubble using Streamlit columns
        col1, col2, col3 = st.columns([1, 1, 1])

        # place the text bubble in the middle column
        with col2:
            formatted_text = '<div style="text-align: center; "><span class="source-sans" style="font-size: 40px; color: #081C15; font-weight: bold;">Explore ARCD</span><br><span class="source-sans" style="font-size: 16px; color: #081C15;">Discover Interior Design Inspiration: Your Personal Room Theme Generator!</span></div>'
            createTextBubble(formatted_text, div_style="text-align: center;", div_class="text-bubble")
        st.write("\n")

# function for displaying the image and traversing the lists
def image_selector():

    # styling the buttons/download buttons
    st.markdown("""
        <style>
            .stButton button, .stDownloadButton button {
                width: 100%; /* set the button width to 100% */
            }
        </style>
    """, unsafe_allow_html=True)

    # initialize a var to hold the database
    client = bigquery.Client()
    # get a random room and theme from database
    room = get_room(client)
    theme = get_theme(client)
    # construct prompt
    prompt = f"Generate a photorealistic image of a {room} with {theme} interior design"
    # input fields for project ID and location
    project_id = "robertvelasqueztechx2024"
    location = "us-central1"
    # add an empty line to create some space
    st.write("") 
    # display the 'Generate Image' button centered in the page (in column)
    col1, col2, col3, = st.columns([1, 1, 1])

    # center the 'Generate Image' button on the right column
    with col2:
        # display the 'Generate Image' button centered in the page (in column)
        button = st.button("Generate Image")
        if button : 
            try:
                # if 10 images have yet to be generated
                if len(st.session_state.generated_images) != 10 : 
                    # generate the image
                    image_bytes = generate_image(project_id, location, prompt)
                    # append the image to the generated_images list
                    st.session_state.generated_images.append(image_bytes)
                    # update the index
                    st.session_state.index = len(st.session_state.generated_images) - 1
                    # create the caption for the image
                    caption = "Room Type: " + room + " | Interior Design theme: " + theme
                    # append the caption to the captions list
                    st.session_state.captions.append(caption)
                # otherwise, 10 images have been generated already
                else :
                    # reset the generated_images list
                    st.session_state.generated_images = []
                    # reset the captions list
                    st.session_state.captions = []
                    # generate the image
                    image_bytes = generate_image(project_id, location, prompt)
                    # append the image to the generated_images list
                    st.session_state.generated_images.append(image_bytes)
                    # update the index
                    st.session_state.index = len(st.session_state.generated_images) - 1
                    # create the caption for the image
                    caption = "Room Type: " + room + " | Interior Design theme: " + theme
                    # append the caption to the captions list
                    st.session_state.captions.append(caption)
            # catch any errors
            except Exception as e:  
                st.error(f"Error generating image: {e}") # display the error to the user elegantly

    # display the generated image from the generated_images list at the current index alongside its caption
    if st.session_state.generated_images:
        caption = st.session_state.captions[st.session_state.index]
        st.image(st.session_state.generated_images[st.session_state.index], use_column_width=True)
        st.markdown(f'<div style="text-align: center;"><span style="color:#081C15">{caption}</span></div>', unsafe_allow_html=True) # displaying the caption with a custom style

        # display navigation buttons
        col1, col2, col3 = st.columns([1, 1, 1])

        # 'Previous' button logic
        if col1.button('◄ Prev', key='previous') and st.session_state.index > 0: # works only if the index is greater than 0
            # update the index
            st.session_state.index -= 1

        with col2:
            # download button to download the currently displayed image
            if st.download_button(label="Download Image", data=st.session_state.generated_images[st.session_state.index], file_name="generated_image.png"): 
                st.success("Image downloaded successfully!") # let the user know the download was successful

        # 'Next' button logic
        if col3.button('Next ►', key='next') and st.session_state.index < len(st.session_state.generated_images) - 1: # works only if the index is less than the length of the generated_images list
            st.session_state.index += 1

# function to initialize the possible section
def possible():
        # initialize a subheader
        st.markdown("<h2 style='text-align: center; color:#081C15; font-size: 28px;'>Possible Room Types and Themes</h2>", unsafe_allow_html=True)
        # initialize columns for alignment
        col1, col2, col3, col4= st.columns([1, 1, 1, 1])

        # column 1 with examples
        with col1: 
            st.write("")
            formatted_text = ("Victorian Modern Kitchen")
            createTextBubble(formatted_text, div_style="text-align: center; width: 100%", div_class="text-bubble")
            st.write("")
            formatted_text = ("Desert Minimalist Bedroom")
            createTextBubble(formatted_text, div_style="text-align: center; width: 100%", div_class="text-bubble")
            st.write("")
           
        # column 2 with examples
        with col2:
            st.write("")
            formatted_text = ("Country Cottage Laundry Room")
            createTextBubble(formatted_text, div_style="text-align: center; width: 100%", div_class="text-bubble")
            st.write("")
            formatted_text = ("Hollywood Regency Modern Foyer")
            createTextBubble(formatted_text, div_style="text-align: center; width: 100%", div_class="text-bubble")

        # column 3  with examples
        with col3:
            st.write("")
            formatted_text = ("Victorian Gothic Home Office")
            createTextBubble(formatted_text, div_style="text-align: center; width: 100%", div_class="text-bubble")
            st.write("")
            formatted_text = ("Mediterranean Bohemian Library")
            createTextBubble(formatted_text, div_style="text-align: center; width: 100%", div_class="text-bubble")
        
        # column 4 with examples
        with col4:
            st.write("")
            formatted_text = ("Country Cottage Laundry Room")
            createTextBubble(formatted_text, div_style="text-align: center; width: 100%", div_class="text-bubble")
            st.write("")
            formatted_text = ("Japanese Zen Theme Kids Bedroom")
            createTextBubble(formatted_text, div_style="text-align: center; width: 100%", div_class="text-bubble")

# function to initialize session state
def initialize_session_state():
    if 'generated_images' not in st.session_state:
        st.session_state.generated_images = [] # list to store images
    if 'index' not in st.session_state:
        st.session_state.index = 0 # index to access the images
    if "captions" not in st.session_state :
        st.session_state.captions = [] # list to store the captions of the images
