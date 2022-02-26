from google.cloud import bigquery

SERVICE_ACCOUNT_JSON = r'/Users/mikeqiu/keys/valued-lyceum-341108-b090826f2edc.json'

# Construct a BigQuery client object.
client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)

query = 'SELECT * FROM `valued-lyceum-341108.dataset_py.table_py` LIMIT 100'

query_job = client.query(query)
print(query_job)

for row in query_job:
    print(str(row[0]))