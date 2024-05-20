from streamlit.testing.v1 import AppTest

community_page_mock = """ 
import streamlit as st
import nav_bar as utl
import community_page

#set the universal coniguration of the pages and the website title
st.set_page_config(layout="wide", page_title='ARCDapp')
st.set_option('deprecation.showPyplotGlobalUse', False)
# style the navigation bar
utl.inject_custom_css()
utl.navbar_component()

community_page.main()
"""

NO_RESULT_SEARCH = ""

def test_search_bar_loads():
    at = AppTest.from_string(community_page_mock).run()

    # Test that search bar loads
    assert at.text_input[0].placeholder == "What's on your mind?"

    # Search query
    at.text_input[0].set_value("clyde").run()

def test_search_logic_single_correct():
    at = AppTest.from_string(community_page_mock).run()

    # Search query
    at.text_input[0].set_value("clyde").run()
    
    foundClyde = False

    # Clyde should be found as one of the cards
    for md in at.markdown:
        if "clyde" in md.value and "<p class='post-author-card'>" in md.value:
            foundClyde = True
            break
            
    assert foundClyde, "Searching did not return appropriate result"

def test_search_logic_single_incorrect():
    at = AppTest.from_string(community_page_mock).run()

    # Search query
    at.text_input[0].set_value("Techno Mechanicus").run()
    
    foundTechno = False

    # There should be no cards named 'Techno Mechanicus'
    for md in at.markdown:
        if "Techno Mechanicus" in md.value and "<p class='post-author-card'>" in md.value:
            foundTechno = True
            break
            
    assert not foundTechno, "Searching did not return appropriate result"

def test_search_logic_multiple_correct():
    at = AppTest.from_string(community_page_mock).run()

    # Search query
    at.text_input[0].set_value("j").run()
    
    num_of_found_cards = []

    # Multiple cards should be shown on the webpage
    for md in at.markdown:
        if "j" in md.value and "<p class='post-author-card'>" in md.value:
            num_of_found_cards.append(True)
            
    assert len(num_of_found_cards) > 1, "Searching did not return multiple results"

def test_search_logic_multiple_incorrect():
    at = AppTest.from_string(community_page_mock).run()

    # Search query
    at.text_input[0].set_value("Techno Mechanicus").run()
    
    num_of_found_cards = []

    # Multiple cards should be shown on the webpage
    for md in at.markdown:
        if "Techno Mechanicus" in md.value and "<p class='post-author-card'>" in md.value:
            num_of_found_cards.append(True)
            
    assert len(num_of_found_cards) == 0, "Searching incorrectly returned multiple results"
