from streamlit.testing.v1 import AppTest
import time
import random
import string

community_post_mock = """ 
import streamlit as st
import nav_bar as utl
import community_post

#set the universal coniguration of the pages and the website title
st.set_page_config(layout="wide", page_title='ARCDapp')
st.set_option('deprecation.showPyplotGlobalUse', False)
# style the navigation bar
utl.inject_custom_css()
utl.navbar_component()

community_post.main()
"""

def test_object_redetection():
    at = AppTest.from_string(community_post_mock, default_timeout=20).run()

    # Save initial object detection result
    initial_obj_detection = None

    # Get object detection text
    for md in at.markdown:
        if "AI Object Detection:" in md.value:
            initial_obj_detection = md.value[md.value.index("AI Object Detection:"):md.value.index("</p>")]

    obj_detect_btn = at.button[0]

    # Rerun objection detection
    obj_detect_btn.click().run(timeout=20)

    new_obj_detection = None

    # Get object detection text
    for md in at.markdown:
        if "AI Object Detection:" in md.value:
            new_obj_detection = md.value[md.value.index("AI Object Detection:"):md.value.index("</p>")]

    # Test that new objection detection result does not equal the previous one
    assert initial_obj_detection != new_obj_detection, "New Object Detection is not being made"

def test_new_comment_is_displayed():
    # Helper function
    def generate_random_string(max_length=20):
        # Define the characters to include in the string
        characters = string.ascii_letters + string.digits

        # Generate a random length for the string, up to max_length
        length = random.randint(1, max_length)

        # Generate the random string
        random_string = ''.join(random.choice(characters) for _ in range(length))
        return random_string

    at = AppTest.from_string(community_post_mock, default_timeout=20).run()

    test_commment = generate_random_string()
    comment_input_field = at.text_input[0]

    # Enter test comment
    comment_input_field.set_value(test_commment).run(timeout=10)

    found_test_comment = False

    # Check for if test comment is displayed on screen
    for md in at.markdown:
        if '<p class="comment-text">' in md.value and test_commment in md.value:
            found_test_comment = True

    assert found_test_comment, "Comment was not successfully displayed"
