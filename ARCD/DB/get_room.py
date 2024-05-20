from google.cloud import bigquery

# function to retrieve a random room type from the BigQuery database
def get_room(client):
    # the query
    query = """
        SELECT room_types
        FROM `robertvelasqueztechx2024.room_types.room_types_data`
        ORDER BY RAND()
        LIMIT 1
    """
    # return the result of the query
    results = client.query(query)
    for row in results:
        return row.room_types
