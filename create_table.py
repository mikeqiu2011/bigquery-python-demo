from google.cloud import bigquery

SERVICE_ACCOUNT_JSON = r'/Users/mikeqiu/keys/valued-lyceum-341108-b090826f2edc.json'

# Construct a BigQuery client object.
client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)

table_id = "valued-lyceum-341108.dataset_py.table_py"

job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("name", "STRING"),
        bigquery.SchemaField("gender", "STRING"),
        bigquery.SchemaField("count", "INTEGER")
    ],
    source_format=bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=True,
)
file_path = r'names/yob2018.txt'
source_file = open(file_path, "rb")
job = client.load_table_from_file(source_file, table_id, job_config=job_config)

job.result()  # Waits for the job to complete.

table = client.get_table(table_id)  # Make an API request.
print(
    "Loaded {} rows to {}".format(
        table.num_rows, table_id
    )
)
