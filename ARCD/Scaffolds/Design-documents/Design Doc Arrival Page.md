# **[ACRD] Design Doc - Arrival Page**


**Status**: Active

**Reviewers**: Josue Rodriguez

**Authors**: Andre Melendez

**Last major revision**: 2024-02-16 


# **Objective**

Welcome to the ARCD Arrival Page - your gateway to inspired interior design. The ARCD Arrival Page is where users get a taste of what our web app can do to inspire interior design. The objective for this page in the ARCD web application is to deliver a captivating initial experience to users. The core challenge we aim to address is providing users with the ability to explore stock images of rooms and utilize AI for real-time generation of new styles. Additionally, users should have the flexibility to seamlessly toggle between the AI-generated images and the original images. Thearrival  page intends to inspire users with a curated display of 10 images.


# **Background**

In the dynamic landscape of interior design web applications, the ARCD Arrival Page stands out by seamlessly allowing users to interact with a set of stock images and witness real-time AI modifications. While the concept of user interaction with design visuals isn't entirely new, the execution of empowering not just professionals but everyone to breathe life into their interior design ideas within their own spaces departs away from the norm. 

Unlike other applications in the interior design realm, ARCD transcends the conventional approach. It democratizes the creative process, allowing users of all backgrounds to draw inspiration directly from their design visions applied to their specific rooms. This inclusive feature is a rarity among similar applications, making ARCD a pioneer in bringing design aspirations to life for a broader audience. While very helpful, these tools are technical and require detailed input from the user. While other tools may require technical expertise and detailed inputs, ARCD sets itself apart by leveraging the power of AI. This not only simplifies the process but also makes it more accessible and user-friendly.The ARCD Arrival Page showcases the ease of use, and the effectiveness of remixing interior images with a theme using AI. 


# **Requirements**

**Critical User Journey (CUJ)**

  **All Users**



   Users will open the ARCD web application and be greeted with sample images and a Remix button. Upon clicking the Remix button, users will witness AI generated renditions of the stock images of interiors. In doing so, users will gather inspiration for how they can utilize the tool to bring their ideas to life. 

**UI/UX:**



1. Image Display:
    * Display a curated set of 10 stock images on the Arrival Page (subject to change).
2. AI Image Generation:
    * Implement a remix button allowing users to initiate AI image generation for each of the displayed stock images.
    * Facilitate real-time generation of new styles for rooms using AI algorithms.
3. Revert Functionality:
    * Integrate a revert button enabling users to revert all images back to their original stock state after AI modifications.
    * Ensure a seamless and efficient process for users to undo AI-generated changes.
4. Navigation Bar:
    * Include a navigation bar to facilitate easy switching between the Arrival Page and other relevant pages for further user input.
    * Prioritize a user-friendly and intuitive design for the navigation bar to enhance overall user experience.


# **Design**
![Screenshot 2024-02-16 211236](https://github.com/Google-SDS/final-project-arc/assets/156269322/f17949c5-8677-4119-84d6-edf978f71b2d)

**Design Principles:**



1. Layout:
    * The Arrival Page should be well spaced with a clean, minimalist look.
    * Curated images displayed in a grid format for easy exploration.
2. Image Display:
    * Images should be of reasonable size and quality to showcase design variations effectively.
3. Button Visibility:
    * The Remix button should stand out prominently, using a contrasting color or larger size.
    * The Revert button should be easily visible but less prominent, ensuring users focus on the Remix functionality.
4. Navigation Bar:
    * Positioned for easy visibility, providing a clear pathway to other sections of the application.
    * Reasonable size and minimalistic design to maintain a clean interface.

 ![Screenshot 2024-02-16 211257](https://github.com/Google-SDS/final-project-arc/assets/156269322/919ba869-1da0-4590-9d5c-9f88232c7c16)



**User Experience Path:**



1. Introduction:
    * Users land on the page and are greeted with a curated selection of images.
2. Interactive Elements:
    * Users can easily spot the Remix and Revert buttons, emphasizing the AI-powered design exploration.
3. Testing Phase:
    * Users engage with the Remix button, experiencing real-time AI generation, and observe design variations.
4. Mission Understanding:
    * Through interaction, users grasp the app's mission of providing a platform for testing interior design renditions.

![Screenshot 2024-02-16 211312](https://github.com/Google-SDS/final-project-arc/assets/156269322/0b2ef175-657e-4fc1-9943-681c8d6d8c2e)

**Design Flow:**



1. User Interaction:
    * User clicks on Remix or Revert buttons.
2. API Integration:
    * Generative AI API, text embedding API, and the database are called upon based on user interaction.
3. Functionality:
    * The Remix button triggers AI image generation for all stock images simultaneously.
    * The Revert button restores all images to their original states.

![Screenshot 2024-02-16 211328](https://github.com/Google-SDS/final-project-arc/assets/156269322/3dd1f81d-6014-41d6-b30b-a82a32569922)

# **Alternatives Considered**

**Further AI Generation with Stock Images:**



   Allow users to generate renditions of all images in a single design style
   Discarded to prioritize showcasing various styles instead of repetitive variations on the same images.

**Single Image Unique Style Input:**



   Allow users to generate renditions for a single stock image with a unique design
   Discarded as it limits the diversity of styles showcased on the Arrival Page, contrary to the app's mission.


# **Prompts**


## **Prompt 1**


   Welcome to the ARCD Arrival Page - where users get a taste of what our web app can do to inspire interior design. The objective of the Arrival Page in the ARCD web application is to deliver a captivating initial experience to users. The core challenge we aim to address is providing users with the ability to explore stock images of rooms and utilize AI for real-time generation of new styles. Additionally, users should have the flexibility to seamlessly toggle between the AI-generated images and the original images. The landing page intends to inspire users with a curated display of 10 images.


## **Prompt 2**


   What can I do to improve this prompt?


   In the realm of interior design web applications, while the concept is not groundbreaking, the execution of allowing users to interact with a set of stock images and witness real-time AI modifications is not commonly explored. Allowing everybody, not just professionals, to draw inspiration from their interior design ideas being applied to their specific rooms, is not a common practice among other similar applications. 


   Other applications have been used to draw inspiration from interior design. Applications such as Pinterest and social platforms such as Instagram have been widely used to reference designs. Tools have emerged that allow creators and anybody with an idea for interior design to interact with their ideas through 3D models and images. While very helpful, these tools are technical and require detailed input from the user. With the utilization of AI, putting design ideas to an image has never been easier and more consumer friendly. The ARCD Arrival Page showcases the ease of use, and the effectiveness of remixing interior images with a specific theme using AI.
