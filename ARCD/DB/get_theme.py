from google.cloud import bigquery

# function to retrieve a random theme from the BigQuery database
def get_theme(client):
    # the query
    query = """
        SELECT theme
        FROM `robertvelasqueztechx2024.interior_designs.interior_designs_data`
        ORDER BY RAND()
        LIMIT 1
    """
    # return the result of the query
    results = client.query(query)
    for row in results:
        return row.theme
