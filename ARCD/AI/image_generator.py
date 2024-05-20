import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

# function to generate an image with parameters
def generate_image(project_id, location, prompt):
    # credentials
    vertexai.init(project=project_id, location=location)
    # model of Vertex AI Vision
    model = ImageGenerationModel.from_pretrained("imagegeneration@005")
    # generate the image
    images = model.generate_images(
        prompt=prompt,
        # additional parameters (to generate only 1 image)
        number_of_images=1,
    )
    print("Image generated successfully!")
    return images[0]._image_bytes
