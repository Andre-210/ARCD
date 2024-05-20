import streamlit as st
import nav_bar as utl
import explore_page, input_page, community_page, community_post

#set the universal coniguration of the pages and the website title
st.set_page_config(layout="wide", page_title='ARCDapp')
st.set_option('deprecation.showPyplotGlobalUse', False)
# style the navigation bar
utl.inject_custom_css()
utl.navbar_component()

# function for switching pages in the navigation bar
def navigation():
    # call on the function that gets the rout
    route = utl.get_current_route()
    # if the rout is explore (called on by user input)
    if route == "explore":
        # call on the explore page
        explore_page.main()
    # elif the rout is input (called on by user input)
    elif route == "input":
        # call on the input page
        input_page.main()
    # if the rout is community (called on by user input)
    elif route == "community":
        # call on the community page
        community_page.main()
    elif route == "community_post":
        community_post.main()
    # otherwise, the default route/page is the explore page
    elif route == None:
        explore_page.main()
        
navigation() 
