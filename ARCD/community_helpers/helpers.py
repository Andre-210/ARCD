import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
import os
import random
import requests
from PIL import Image
from io import BytesIO
from shared_components.createTextBubble import createTextBubble

load_dotenv()

IS_OBJECT_DETECTED_KEY = 'is_object_detected'
OBJECT_DETECTION_KEY = "object_detection"
COMMENTS_KEY = "comments"
COMMENT_INPUT_KEY = "comment_input"
POSTS_KEY = "posts"

random_comment_names = [
    "BlueSkyWalker",
    "CosmicRaven",
    "EchoWanderer",
    "FrostByte",
    "MysticOrchid",
    "NeonFox",
    "QuantumMoose",
    "ShadowPenguin",
    "TwilightCyclone",
    "VelvetThunder"
]

# Config Gemini
genai.configure(api_key=os.environ["API_KEY"])

def download_image(image_url):
    response = requests.get(image_url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    image_data = response.content
    image = Image.open(BytesIO(image_data))  # Convert the image data to a Pillow image
    return image

def detectObjectsInImage(image_url):
    file = download_image(image_url)
    task = """Gemini, I'm going to give you an image. 
    I want you to detect the pieces of furniture in the image. 
    Be descriptive in the pieces of furniture and say exactly what types of furniture they are.
    The purpose of this is being able to buy my own furniture that closely resembles the ones in
    the image.

    Examples: A tall fern plant, a short-headed bed of X style
    Don't tell me anything more. Simply return to me a list of these items."""

    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([task, file])

    return response.text

def savePosts(posts):
    st.session_state[POSTS_KEY] = posts

def initialize_state():
    # Initialize states
    if IS_OBJECT_DETECTED_KEY not in st.session_state:
        st.session_state[IS_OBJECT_DETECTED_KEY] = False

    if OBJECT_DETECTION_KEY not in st.session_state:
        st.session_state[OBJECT_DETECTION_KEY] = None

    if POSTS_KEY not in st.session_state:
        st.session_state[POSTS_KEY] = None

    if COMMENTS_KEY not in st.session_state:
        st.session_state[COMMENTS_KEY] = ""

    if COMMENT_INPUT_KEY not in st.session_state:
        st.session_state[COMMENT_INPUT_KEY] = ""

def toggle_regenerate_obj_state():
    st.session_state[IS_OBJECT_DETECTED_KEY] = not st.session_state[IS_OBJECT_DETECTED_KEY]

def save_object_detection_response(response):
    st.session_state[OBJECT_DETECTION_KEY] = response

def save_comments(comments):
    st.session_state[COMMENTS_KEY] = comments

def get_saved_object_detection_response():
    return st.session_state[OBJECT_DETECTION_KEY]
""" 
Displays comments from a post
"""
def displayComments(comments, post_author):
    for comment in comments:
        name_element = ""

        # Special effect for author comments
        if comment["author"] == post_author:
            name_element = f'<p class="name-author">{comment["author"]} 👑</p>'
        else:
            name_element = f'<p class="name">{comment["author"]}</p>'

        st.markdown(f"""
        <div class="comment">
            <div class="avatar">
                <img src={comment['avatar_url']} alt="User Avatar">
            </div>
            <div class="content">
                {name_element}
                <p class="comment-text">{comment["text"]}</p>
            </div>
    </div>
        """, unsafe_allow_html=True)


def add_comment_locally(comment):
    if st.session_state[COMMENTS_KEY]:
        st.session_state[COMMENTS_KEY].append(comment)
    else:
        st.session_state[COMMENTS_KEY] = [comment]

""" 
Displays posts in grid format
"""
def displayPosts(posts):
    row1 = st.columns(3, gap="large")
    row2 = st.columns(3, gap="large")
    row3 = st.columns(3, gap="large")
    row4 = st.columns(3, gap="large")
    index = 0

    for col in row1 + row2 + row3 + row4:
        if index == len(posts): break
        post = posts[index]
        tile = col.container(height=450)
        tile.markdown(f"<p class='post-author-card'>Posted by {post['author']}</p>", unsafe_allow_html=True)
        tile.markdown(f"<img src='{post['image_url']}' class='post-image-card'/>", unsafe_allow_html=True)
        tile.markdown(f"<p class='post-title-card'>{post['title']}</p>", unsafe_allow_html=True)
        createTextBubble("Tags: " + ", ".join(post['tags']), div_class="post-tag-bubble-card", container=tile)
        tile.write(" ")
        col1, col2, col3 = tile.columns([1.1,0.7,0.9])

        tile.markdown(f"""<a target="_self" href="/?nav=community_post&post_id={post['post_id']}" class="post-card-link">See More</a>""", unsafe_allow_html=True)

        index += 1

""" 
Searches posts by query and displays them
"""
def searchPosts(query):
    query = str(query).lower()
    posts_to_display = []

    for post in st.session_state[POSTS_KEY]:
        # Check if query is in title, author, or any tag
        if (query in post['title'].lower() or 
            query in post['author'].lower() or 
            any(query in tag.lower() for tag in post['tags'])):
            posts_to_display.append(post)

    displayPosts(posts_to_display)

def get_random_avatar_url():
    return f"https://storage.googleapis.com/arcd-posts-images-bucket/avatars/avatar_image_{random.randint(1, 5)}.png"

def get_random_author():
    return random.choice(random_comment_names)
