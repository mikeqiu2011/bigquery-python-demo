from google.cloud import bigquery

SERVICE_ACCOUNT_JSON = r'/Users/mikeqiu/keys/valued-lyceum-341108-b090826f2edc.json'

client = bigquery.Client.from_service_account_json(SERVICE_ACCOUNT_JSON)

dataset_id = 'valued-lyceum-341108.dataset_py'

dataset = bigquery.Dataset(dataset_id)

dataset.location = 'asia-northeast1'
dataset.description = 'dataset from Python'

dataset_ref = client.create_dataset(dataset, timeout=30)

print('successful created dataset {}.{}'.format(client.project, dataset_ref.dataset_id))
