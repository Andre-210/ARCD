import sys
sys.path.append('community_helpers')

import streamlit as st
from helpers import *
from bigquery_helper import *
from shared_components.createTextBubble import createTextBubble
from PIL import Image

test_post_title = "I didn’t know ARCD could do this!"
test_post_tags = "Modern, Traditional, French"
test_post_author = "Clyde"

def main():
    post_id = "1ce2354e-8d29-418c-bcd1-683e1c7eb45c"

    try:
        post_id = st.query_params["post_id"]
    except:
        pass

    # Import styles.css
    with open( "community_helpers/styles.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

    initialize_state()

    col1, col2 = st.columns([0.6, 0.4])

    post = get_post_by_id(post_id)

    # Post information Section
    with col1:
        st.title(post["title"])
        st.markdown(f"""
            <p style="font-size: 16px; color: #000000"><b>{", ".join(post["tags"])} | posted by {post["author"]}</b></p>
            """, unsafe_allow_html=True)
        st.image(post["image_url"])

        # Prevents excessive calls to repeatedly re-call AI
        object_detection = st.session_state[OBJECT_DETECTION_KEY] if st.session_state[IS_OBJECT_DETECTED_KEY] else detectObjectsInImage(post["image_url"])

        createTextBubble("AI Object Detection: " + object_detection, div_class="text-bubble")

        st.session_state[IS_OBJECT_DETECTED_KEY] = True
        st.session_state[OBJECT_DETECTION_KEY] = object_detection

        regenerate_obj_det_btn = st.button("Regenerate object detection", on_click=toggle_regenerate_obj_state)


    # Comments Section
    with col2:
        st.markdown(f"""
            <p class="comment-section-title">Comments</p>
            """, unsafe_allow_html=True)

        # Prevents excessive calls to repeatedly re-call bigquery API
        data = st.session_state[COMMENTS_KEY] if st.session_state[COMMENTS_KEY] else get_post_comments(post_id)

        print("DISPLAY COMMENTS")
        displayComments(data, post["author"])

        comment_input = col2.text_input(placeholder="What's on your mind?", label="")

        # Post comment only if there is input and the input is new
        if comment_input and comment_input != st.session_state[COMMENT_INPUT_KEY]:
            isAuthor = comment_input.startswith("admin:isAuthor") # Special privilege
            author = post["author"] if isAuthor else get_random_author()

            original_comment = comment_input

            if isAuthor: comment_input = comment_input.replace("admin:isAuthor", "")

            post_comment(post_id, get_random_avatar_url(), author, comment_input)
            st.session_state[COMMENT_INPUT_KEY] = original_comment
            st.experimental_rerun() # Show updated comment section
