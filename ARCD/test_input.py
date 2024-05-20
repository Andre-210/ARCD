from streamlit.runtime.uploaded_file_manager import UploadedFileRec, UploadedFile
from streamlit.proto.Common_pb2 import FileURLs as FileURLsProto

from streamlit.testing.v1 import AppTest

nav_mock = """ 
import streamlit as st
import nav_bar as utl
import input_page

#set the universal coniguration of the pages and the website title
st.set_page_config(layout="wide", page_title='ARCDapp')
st.set_option('deprecation.showPyplotGlobalUse', False)
# style the navigation bar
utl.inject_custom_css()
utl.navbar_component()

input_page.main()
"""


def test_image_not_inserted():
    app = AppTest.from_string(nav_mock).run()
    submit = app.button(key="submit_image")
    submit.click().run(timeout=10)

    assert app.error[0].value == "No image has been processed. Please upload an image and click submit."


def test_file_upload():
    app = AppTest.from_string(nav_mock).run()
    file_name = "./mock_image/small-bedroom-ideas-getty-0823-d982b46c35964a9cbd0c1d4f38bd665d.jpg"

    with open(file_name, "rb") as f:
        # Read the entire image data into a bytes object
        image_data = f.read()

    FILE_1 = UploadedFileRec(file_id="url1/jpg", name="file1", type="type", data=image_data)
    proto = FileURLsProto(file_id="url1/jpg", upload_url="/image/image")
    uploaded_file = UploadedFile(FILE_1, proto)
    uploaded_file.name = "room_pic"

    app.session_state.uploaded_file = uploaded_file
    app.run(timeout=10)

    oceanic = app.button(key="Oceanic")
    oceanic.click().run(timeout=10)

    submit = app.button(key="submit_image")
    submit.click().run(timeout=10)

    assert app.columns[15].children[0].children[1].proto.imgs[0].url == "/mock/media/6d0d6081048414251369d9051b2c488ed715c35ec4250ad24523a90b.jpg"
