import streamlit as st
from google.cloud import storage
from PIL import Image
import io

def upload_file_to_bucket(bucket_name, file, file_name, folder_name=None):
    """Uploads the uploaded file to the specified GCP bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    if folder_name:
        blob_path = f"{folder_name}/{file_name}"
    else:
        blob_path = file_name

    blob = bucket.blob(blob_path)
    blob.upload_from_string(file.getvalue(), content_type=file.type)
    st.success(f"Uploaded {file_name} to {bucket_name}/{blob_path}")

def upload_processed_image_to_bucket(bucket_name, image, file_name, folder_name=None):
    """Uploads a processed PIL Image to the specified GCP bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Construct the blob path
    blob_path = f"{folder_name}/{file_name}" if folder_name else file_name

    # Convert PIL Image to byte stream
    img_byte_arr = io.BytesIO()
    image_format = image.format if image.format else 'PNG'  # Default to PNG if format is not available
    image.save(img_byte_arr, format=image_format)
    img_byte_arr = img_byte_arr.getvalue()

    # Determine content type based on image format
    content_type = f'image/{image_format.lower()}'

    # Create a blob and upload the byte stream
    blob = bucket.blob(blob_path)
    blob.upload_from_string(img_byte_arr, content_type=content_type)

    st.success(f"Uploaded {file_name} to {bucket_name}/{blob_path}")


def make_blob_public(bucket_name, object_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.make_public()



def get_dynamic_public_url(bucket_name, object_name):
    """Generate a public URL for a given object by fetching it directly from GCP."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(object_name)

    if blob.exists():
        blob.reload()  # Reload the latest metadata
        return blob.public_url  # This returns the direct URL if the object is public
    else:
        return "Object does not exist."
