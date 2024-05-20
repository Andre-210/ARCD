# **[ACRD] Design Doc - Community Pages**

**Status**: Active

**Reviewers:** Josue Rodriguez

**Authors**:  Clyde Tandjong

**Last major revision**: 2024-02-16  


## Objective

Welcome to the ARCD Community Page – where inspiration meets innovation in the world of interior design. The goal is to build a vibrant community where ARCD users can connect, collaborate, and create together, transforming the way we approach home design. Beyond just finding inspiration, here you can actively engage with other users' designs: comment, discuss, and even remix them using our AI tools. The challenge that these pages address is the hardship that comes with interior design. Other products such as Pinerest offer a catalog of design ideas that people use to get inspiration for their own designs; the community pages offer the same opportunity and more. With the community pages, users can not only view others’ work, but comment and remix their designs! <sub><sup>**[Prompt 1]**</sup></sub>

When a user clicks on a post on the community page, they’ll be brought to the page with more details on each post, with a chance to comment and remix (The Post Page).


## Background


The ARCD Community Pages emerge in a digital era where home design is increasingly becoming a collaborative and interactive process. The concept of sharing and remixing design ideas online has been influenced by several key platforms and technological advancements in the field.


**Prior Art:**



* **Social Media and Design Platforms**: Platforms like Pinterest and Instagram have revolutionized the way people seek and share design inspiration. These sites provide a vast catalog of visual ideas but often lack direct interaction or customization tools specific to interior design.
* **Collaborative Design Software:** Tools like SketchUp and Autodesk's Homestyler have introduced the concept of interactive design, but these are often more technical and less community-focused.
* **AI in Design:** The use of artificial intelligence for aesthetic decisions and simulations has been a game-changer. AI's ability to understand and replicate design elements has led to more personalized and adaptable design experiences.

What sets the ARCD Community Page apart is its unique synthesis of these elements. It combines the social sharing and inspiration aspects of platforms like Pinterest with the interactive, AI-powered customization capabilities seen in advanced design software. Unlike other tools, ARCD is not just for professionals; it’s designed for a wide range of users, from homeowners to interior designers. This approach empowers interior design, making it more accessible and engaging. <sub><sup>**[Prompt 2]**</sup></sub>

## Requirements

**Critical User Journeys (CUJs)**
<sub><sup>**[Prompt 3]**</sup></sub>

**Adam - Discovering Design Inspiration:**

**Goal:** Adam wants to find inspiration for their home redesign project.

**Journey:** Adam logs into ARCD and navigates to the Community Page. He browses through various user-generated designs, using filters to narrow down styles, room types, and color schemes. He saves several designs to his favorites for later reference. Some designs are very interesting and he decides to comment on some of them.

**Kolena - Remixing a Design:** 

**Goal:** Kolena finds a design they like and wants to customize it for their space.

**Journey:** While browsing, the user discovers a design that closely matches their vision. They select the 'Remix' option, which opens the ARCD AI tool. Here, she uploads an image of her existing room and the AI generates a new image combining the two images. She saves the new image on her account.

**User Requirements**
<sub><sup>**[Prompt 4]**</sup></sub>


**UI/UX:**

* Intuitive and clear navigation paths for users to find and engage with content.

**Functional Requirements:**



* **Search and Filters:** Allow users to search and filter by room type, design style, etc, to allow them to easily find specific designs.
* **Remix Tools (AI):** Integrated AI that allows users to remix and personalize existing designs.
* **Collaboration Tools:** Messaging or forums for users to communicate and collaborate.
* **User Profiles:** Ability for users to create profiles for replying to and posting designs.
* **Database:** Calls will need to be made to the database in order to pull posts made from other users.
* **(Maybe) AI Text-Embeddings:** Might be a cool use of AI to use text-embeddings for the search bar.


## Design

![Screenshot 2024-02-16 191402](https://github.com/Google-SDS/final-project-arc/assets/157425127/702b7d61-c6d2-49e6-8d08-bbeb44e45e81)

**(The Community Page)**

![Screenshot 2024-02-16 193001](https://github.com/Google-SDS/final-project-arc/assets/157425127/55290b98-1256-4ba4-a1d7-4ab0e67cb7e8)

**(The Post Page)**


### **The Community Page:**

As seen in the design mockup, the user has the ability to search up things in the search bar. They’ll also have the option to filter any results that the application may give them. The filter parameters will include things such as design type, room type, etc. The results section will display the designs pulled from the database, thus, they’ll need to be able to scroll through the results. Each result card will offer the following data points:

* Post Author
* Post Image
* Post Title
* Post Tags

### **The Post Page:**

As seen in the design mockup, after the user clicks on a particular post from the community page, they’ll be able to see a more detailed view of the post. The more detailed view of the post will include the following data points:

* Post Author
* Post Image
* Post Title
* Post Tags
* User comments

Here, the user will be able to freely interact with the ARCD community through the use of comments, and they’ll be able to get design inspiration from the AI-generated image and tags. If the user likes what they see, they’ll be able to remix the image coupled with an image of their own to produce an AI-generated image that the user will like.

![image (1)](https://github.com/Google-SDS/final-project-arc/assets/157425127/53a4671d-3c07-47ea-8fb1-3eebebe3b234)

System Design (focused on the The Community & Post Page): 

**Database Call - Community Page:** When the user opens the community page, the top results using an algorithm (TBD) will be displayed in a list view for the user to browse through.

**Database Call - Post Page:** When the user clicks on a particular post from the community page, the app will make another database call to get comments for the particular post. Also, any time a user comments _(user input) _on a post, a new entry will be made in the database.

**AI Remix Feature - Post Page:** For remixing an image on the post page, once the user submits a pairing image with the current image from the post, the Post Page securely transmits this data to the AI Image Generator in order to spit back out a newly generated image.


## Alternatives Considered

**Virtual Reality (VR) Room Tours:**

  **Idea:** Allow users to create and share VR tours of their designed spaces in order to create an immersive space for interior design inspiration and admiration. 


  **Rebuttal:** It is not feasible to do so for this project, however, it would be a great feature to have.

**User Blogs:** 

  **Idea:** Allow users to create blog posts or stories about their design journeys, sharing experiences, challenges, and outcomes.


  **Rebuttal:** Though it is a great feature, it would lose focus of what ARCD is meant to do. It wouldn’t be wise to include this in the MVP.


## Prompts

#### **Prompt 1**

  This is what ARCD is: Transform your room with ease with the help of the ARCD web application. This web app allows homeowners, interior designers, and creative enthusiasts to bring their desired aesthetic to life. By submitting a picture of their desired room to remodel, and inputting their preferences for the design, the web app will generate AI-powered rom simulations that bring their visions to life. Using AI, the creator can simulate realistic rooms before committing to their ideas. By inspiring creativity through previously simulated rooms, designers will never run out of ideas. 
  I'm writing an objective for the community page for this application. For context, the community page offers users the chance to look at designs made from other users in the app, comment on them, and remix their designs into their own using AI. Here's what I have so far, make it better:
  Transform your room with ease with the help of the ARCD web application. This web app allows homeowners, interior designers, and creative enthusiasts to bring their desired aesthetic to life. By submitting a picture of their desired room to remodel, and inputting their preferences for the design, the web app will generate AI-powered rom simulations that bring their visions to life. Using AI, the creator can simulate realistic rooms before committing to their ideas. By inspiring creativity through previously simulated rooms, designers will never run out of ideas. 


#### **Prompt 2**


  Write a background, &lt;What is the context? Any related prior art?>


#### **Prompt 3**

  Come up with some critical user journeys for these pages


#### **Prompt 4**

 What are some requirements for this pages?
