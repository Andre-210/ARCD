import argparse
import vertexai
from vertexai.preview.vision_models import Image as VertexImage, ImageGenerationModel
from PIL import Image as PILImage
import io

import tempfile
import os

def transform_image(input_image, prompt, location, project_id):
    """Transforms an image based on a provided text prompt using Vertex AI."""

    vertexai.init(project=project_id, location=location)
    model = ImageGenerationModel.from_pretrained("imagegeneration@002")
    
   # Save the uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix='.png', mode='wb') as tmp:
        # Write the content of the uploaded file into the temp file
        tmp.write(input_image.read())
        tmp.flush()  # Ensure all data is written
        tmp_path = tmp.name

    # Load image from the temporary file
    base_img = VertexImage.load_from_file(tmp_path)
    
    # Edit image based on the prompt
    transformed_images = model.edit_image(base_image=base_img, prompt=prompt, guidance_scale=21)
    
    # Save the transformed image temporarily to read back as PIL Image
    transformed_image_path = tmp_path + "_transformed.png"
    transformed_images[0].save(location=transformed_image_path)
    
    # Load the transformed image as PIL Image
    result_image = PILImage.open(transformed_image_path)

    # Clean up the temporary files
    os.remove(tmp_path)
    os.remove(transformed_image_path)

    return result_image
