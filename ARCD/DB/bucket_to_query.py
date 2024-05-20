import uuid
from google.cloud import bigquery
from datetime import datetime
import time
from google.api_core.exceptions import BadRequest

def record_complete_image_metadata(dataset_name, table_name, old_image_url, new_image_url, description):
    """Records complete metadata of an image to BigQuery in one go."""
    # Initialize BigQuery client
    bigquery_client = bigquery.Client(project="robertvelasqueztechx2024")

    # Generate unique IDs for both old and new images
    old_image_id = str(uuid.uuid4())
    new_image_id = str(uuid.uuid4())  # Generate even if new_image_url might be None

    # Prepare the data to be inserted
    rows_to_insert = [{
        "old_image_id": old_image_id,
        "old_image_url": old_image_url,
        "new_image_id": new_image_id,
        "new_image_url": new_image_url,
        "upload_date": datetime.now().isoformat(),
        "description": description,
    }]

    # Table ID composed from project, dataset, and table names
    table_id = f"{bigquery_client.project}.{dataset_name}.{table_name}"

    # Insert the row into BigQuery
    errors = bigquery_client.insert_rows_json(table_id, rows_to_insert)
    if errors == []:
        print("New rows have been added successfully. Old Image ID: ", old_image_id)
    else:
        print("Encountered errors while inserting rows: {}".format(errors))
