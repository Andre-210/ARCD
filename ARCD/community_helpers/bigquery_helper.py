import uuid
from google.cloud import bigquery
from datetime import datetime
import time
from google.api_core.exceptions import BadRequest
import streamlit as st
from helpers import *

POSTS_DATASET = "posts_dataset"
POSTS_TABLE = "posts_table"

COMMENTS_DATASET = "comments_dataset"
COMMENTS_TABLE = "comments_table"

PROJECT_ID = "robertvelasqueztechx2024"

def post_comment(post_id, avatar_url, author, text):
    """Records complete metadata of an image to BigQuery in one go."""
    # Initialize BigQuery client
    bigquery_client = bigquery.Client(project=PROJECT_ID)

    # Prepare the data to be inserted
    data = [{
        "post_id": post_id,
        "avatar_url": avatar_url,
        "author": author,
        "text": text,
        "comment_date": datetime.now().isoformat(),
    }]

    # Table ID composed from project, dataset, and table names
    table_id = f"{PROJECT_ID}.{COMMENTS_DATASET}.{COMMENTS_TABLE}"

    # Insert the row into BigQuery
    errors = bigquery_client.insert_rows_json(table_id, data)
    if errors == []:
        print("Comment successfully posted")
        add_comment_locally(data[0])
    else:
        print("Encountered errors while posting comment: {}".format(errors))

def create_post(title, image_url, tags, author):
    # Initialize BigQuery client
    bigquery_client = bigquery.Client(project=PROJECT_ID)

    post_id = str(uuid.uuid4())

    # Prepare the data to be inserted
    data = [{
        "post_id": post_id,
        "image_url": image_url,
        "title": title,
        "tags": tags,
        "author": author,
        "post_date": datetime.now().isoformat(),
    }]

    # Table ID composed from project, dataset, and table names
    table_id = f"{PROJECT_ID}.{POSTS_DATASET}.{POSTS_TABLE}"

    # Insert the row into BigQuery
    errors = bigquery_client.insert_rows_json(table_id, data)
    if errors == []:
        print("Post successfully posted")
    else:
        print("Encountered errors while posting post: {}".format(errors))

def get_all_posts():
    client = bigquery.Client(project=PROJECT_ID)

    query = f"""
    SELECT * FROM `{PROJECT_ID}.{POSTS_DATASET}.{POSTS_TABLE}`
    """

    query_job = client.query(query)  # Make an API request
    results = query_job.result()  # Waits for the job to complete

    dict_results = [dict(result) for result in results]

    savePosts(dict_results)

    return dict_results

def get_post_by_id(post_id):
    client = bigquery.Client(project=PROJECT_ID)

    query = f"""
    SELECT * FROM `{PROJECT_ID}.{POSTS_DATASET}.{POSTS_TABLE}`
    WHERE post_id = '{post_id}'
    """

    query_job = client.query(query)  # Make an API request
    results = query_job.result()  # Waits for the job to complete

    dict_results = [dict(result) for result in results]

    return dict_results[0]

def get_post_comments(post_id):
    client = bigquery.Client(project=PROJECT_ID)

    query = f"""
    SELECT * FROM `{PROJECT_ID}.{COMMENTS_DATASET}.{COMMENTS_TABLE}`
    WHERE post_id = '{post_id}'
    """

    query_job = client.query(query)  # Make an API request
    results = query_job.result()  # Waits for the job to complete

    dict_results = [dict(result) for result in results]

    sorted_results = sorted(dict_results, key=lambda x: x['comment_date'])

    save_comments(sorted_results)

    return sorted_results
