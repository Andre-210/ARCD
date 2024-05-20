# **Final Project Part 1: One-Pager**

**Unique Team Name:** ARC (Andre, Robert, Clyde)

**Project Name:** A.R.C.D. (Andre Robert Clyde Design)

**Project Idea**

**_A.R.C.D. (Andre Robert Clyde Design)_** is an interior design application for homes wherein users upload pictures of their room and specify a design style (industrial, bohemian, rustic, coastal, etc…) and get suggestions of a redesigned room layout with text descriptions and generative images of the room with new furniture and decor.

**Landing Page (HOME PAGE)**

_Input:_ The landing page is a page in A.R.C.D wherein users would be able to see how the AI could transform an image from one style to another. Users would be able to transform stock images to AI generated ones. (Display like 10 images) Have two buttons to switch between generated image and original image.

_Database Query:_ Get stock images from the database to display on the explore page. 

_Gen AI:_ Allow users to remix an image from the explore page as well (use generated image and associated text for calls). 2 AI Calls for image and text

**Community Page (Subpage)**

_Input:_ The user can view posts by different accounts and scroll through a feed.

_Database Query:_ The community will make a query to a posts collection in the database to display all of the posts from all users in a list.

Gen AI: Use text embeddings in conjunction with a text-embedding database for clustering the posts for searching.

**Post Page (Subpage of Community Page)**

_Input:_ Users can view a detailed view of a post from the community page. Users can also post comments on images and view others’ comments. 

_Database Query:_ The AI generated images are uploaded to the database query. 

_Gen AI:_ Users can click on users' posts and generate images similar to the one on the post. The images will be AI generated and use a similar implementation to the AI Page. Remix feature.

**Input Page (Subpage)**

_Input:_ The Input page is a page where users can go into the details of what design they are looking for. Users can input an image to be modified and prompt for the AI image generation for any modifications to the room. Also have a button for posting the generated images to a forum.

_Database Query:_ All the AI generated images will be added to the database.

_Gen AI_: Multiple AI generated images will be returned from the user prompt coupled with a text description of the image.

## **EXTRA CREDIT:**

How will multiple gen AI calls be string together…



* The user will request the AI to create several images/descriptions of ideas that the user has based on the input description and uploaded image.

More than 3 pages… 



* The website will consist of 4 pages. The landing page that introduces example images from the AI. The input page where the user can make custom requests and can make community posts. The community page will be the hub of all the user posts. The post page will display a detailed view of the post made by the user.
