# **[ACRD] Design Doc - Input Page**

**Status**: Active

**Reviewers:** Josue Rodriguez

**Authors**:  Robert Velasquez

**Last major revision**: 2024-02-16


## Objective

Users can upload images of their rooms and specify design preferences. The system will then generate and display multiple redesign options using AI, allowing users to visualize potential changes to their space.

## Background


Homeowners and renters often struggle to visualize how design changes could transform their living spaces. Traditional methods involve consulting with professional designers, which can be costly and time-consuming. The ACRD Input Page aims to leverage AI technology to offer instant, personalized interior design suggestions, making interior design more accessible and interactive.

## Requirements

- **Image Upload**: Users must be able to upload images of their rooms easily.
- **Design Preference Input**: Users should have the option to specify their design style preferences (e.g., industrial, bohemian, rustic, coastal).
- **AI-Generated Designs**: The system must generate multiple design options based on the user's input.
- **Display Options**: Generated images and descriptions of redesigned rooms should be displayed clearly to the user.
- **User Interaction**: Users should be able to interact with the generated designs, such as viewing different options and selecting favorites.
- **Data Storage**: Uploaded images and generated designs must be stored securely in a database.
- **Performance**: The page should load quickly, and AI generation should occur within a reasonable time frame to ensure a smooth user experience.


## Design

<img src="https://github.com/Google-SDS/final-project-arc/blob/main/Design-document-images/Input-Page-Sequence-Flow.png"/>

### Explanation of Design Sequence Flow

The design flow has been captured in the sequence diagram, illustrating the interaction between the user, the Input Page UI, the AI Image Generator, and the database. This flow ensures a seamless user experience from image upload to viewing AI-generated design options: 

**User Interaction with Input Page UI**: The user initiates the design process by uploading a photograph of their room onto the ACRD Input Page. Alongside the image, the user also inputs their design preferences, which may include style (e.g., industrial, bohemian, rustic, coastal), color schemes, and any specific furniture or decor requests. This step is crucial for tailoring the AI's output to the user's personal taste and room specifications.

**Transmission to AI Image Generator**: Once the user submits their image and design preferences, the Input Page UI securely transmits this data to the AI Image Generator. This transmission includes not only the raw image file but also structured data representing the user's design preferences, ensuring the AI has all necessary context to generate relevant design options.

**AI-Driven Design Generation**: Upon receiving the user's input, the AI Image Generator processes the information using advanced algorithms trained on interior design principles and styles. It creatively generates several design options that align with the specified preferences, transforming the original room image into multiple redesigned visuals. This step involves complex computational processes, including image recognition, style transfer, and generative design techniques.

**Data Storage and Association**: The AI Image Generator then stores the newly generated images and their corresponding textual descriptions in the Database. To maintain coherence and ease of access, each set of generated designs is linked to the original user input (both the uploaded image and the text-based preferences). This ensures that the results are easily retrievable and can be associated with the correct user session. Additionally, the original user inputs are saved alongside the generated results, facilitating future reference or modification requests.

**Display of Results**: After the design options are generated and stored, the AI Image Generator sends this data back to the Input Page UI. The UI, in turn, dynamically displays the generated images and descriptions to the user. This presentation allows users to visually compare their current room with the potential redesigns, providing a clear and engaging overview of the possibilities envisioned by the AI based on their preferences.

**User Engagement and Interaction**: Finally, the user can interact with the displayed results on the Input Page UI. They can browse through the different AI-generated design options, zoom in on specific details, and read the accompanying descriptions to understand the design choices. This interactive experience empowers users to envision how their room could be transformed, facilitating a deeper connection with the design process and enabling informed decision-making regarding their interior design project.


<img src="https://github.com/Google-SDS/final-project-arc/blob/main/Design-document-images/Input-Page-System-Design.png"/>

### System Design (focused on the Input Page): 

**User Interaction with Input Page UI**: First, the user opens the A.R.C.D. application by accessing the Input Page. Here, they upload a photograph of their room and input their design preferences, such as desired style, color schemes, and specific elements they wish to incorporate. This step is crucial for creating the design suggestions to the user's personal taste and requirements.

**Data Transmission to AI Image Generator**: Once the user submits their image and preferences, the Input Page UI sends this data to the AI Image Generator. This backend component is designed to interpret the user's input and use it as a basis for generating design options.

**AI-Driven Design Generation and Storage**: Then, the AI Image Generator processes the user's input, applying machine learning and image processing techniques to create multiple design options that align with the specified preferences. These generated designs, along with descriptive text, are then stored in the Database. This ensures that the designs are not only generated in real-time but also saved for future retrieval and reference.

**Display of Generated Designs**: After the design options are generated and stored, the AI Image Generator sends this information back to the Input Page UI. The UI then dynamically displays these options to the user, allowing them to visually compare their current room with the potential redesigns. This interactive presentation helps users to envision how their space could be transformed.

**Community Engagement**: Beyond the Input Page, users have the opportunity to engage with the broader A.R.C.D. community through the Community Page and Post Page. Here, users can browse, interact with, and contribute to a collection of posts showcasing design projects, ideas, and discussions. Both pages facilitate community interaction and inspiration, with the Database serving as the backbone for storing and managing the shared content.

## Alternatives Considered

**Manual Design Suggestions**: Instead of leveraging AI to generate design options automatically, this alternative approach would involve creating a comprehensive database of interior design ideas, categorized by various styles (e.g., industrial, bohemian, rustic, coastal). Users could upload images of their rooms and manually browse through the database to find design suggestions that align with their preferences.

**Collaborative Design Sessions**: Enabling real-time collaboration features where users can invite friends or family members to contribute ideas and feedback on design options within the app. This approach fosters a more interactive and social design process but introduces complexity in managing sessions and could distract from the core AI-driven experience.

**Virtual Interior Designer Consultation**: Integrating a feature for users to schedule virtual consultations with professional interior designers for personalized advice, complementing the AI suggestions. This hybrid model combines AI efficiency with human expertise but could increase operational costs and complicate the service model.

**Machine Learning Personalization**: Beyond generating designs based on immediate input, implementing a machine learning algorithm that learns from user interactions over time to suggest designs even before a user specifies preferences. While offering a highly personalized experience, this approach raises privacy concerns and requires a substantial dataset to be effective.


## Prompts

#### **Prompt 1 for Alternative Considerations**

  Imagine a project where a user will upload a basic image of their home and also provide some text based on how the user would prefer to have the room look (e.g. Bohemian, Steam Punk, Oceanic, and more). Understand? 

  If so, what would some alternative approaches be towards a project of this nature? 
