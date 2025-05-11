# python3 src/main/python/my_gcp_ops.py
# Intellij File/Project Structure/Project Settings/Modules/Right click on maven module/Add/Python
# folder python right click Mark directory as Source Root

import os
from my_package import my_add
PROJECT = os.getenv("GCP_PROJECT")
OWNER = os.getenv("GCP_OWNER")
DATASET = f"{OWNER}_dataset"
TABLE = f"{OWNER}_table"
BUCKET = f"{PROJECT}-{OWNER}"


def main():
    from utils.my_util import one
    print(one())
    print(my_add(1, 4))
    print(f"{PROJECT}, {OWNER}, {BUCKET}, {DATASET}, {TABLE}")
#    my_python_bq_load_files_from_gcs_to_bq()
    my_python_delete_dataset(PROJECT, DATASET)
    my_python_create_dataset(PROJECT, DATASET)
    my_python_create_table(PROJECT, DATASET, TABLE)
    my_python_select_records_count(PROJECT, DATASET, TABLE)
    my_python_list_gcs(BUCKET)

def my_python_create_dataset(project, dataset_name):
    # noinspection PyPackageRequirements
    from google.cloud import bigquery
    client = bigquery.Client(project=project)
    dataset_id = "{}.{}".format(client.project, dataset_name)
    # noinspection PyTypeChecker
    dataset = bigquery.Dataset(dataset_id)
    client.create_dataset(dataset)
    print("Created dataset '{}.{}'".format(client.project, dataset.dataset_id))


def my_python_delete_dataset(project, dataset_name):
    # noinspection PyPackageRequirements
    from google.cloud import bigquery
    client = bigquery.Client(project=project)
    dataset_id = "{}.{}".format(client.project, dataset_name)
    # noinspection PyTypeChecker
    dataset = bigquery.Dataset(dataset_id)
    client.delete_dataset(dataset=dataset, delete_contents=True, not_found_ok=True)
    print("Deleted dataset '{}'.".format(dataset.dataset_id))


def my_python_create_table(project, dataset_name, table_name):
    # noinspection PyPackageRequirements
    from google.cloud import bigquery
    client = bigquery.Client(project=project)
    table_id = "{}.{}.{}".format(client.project, dataset_name, table_name)
    schema = [
        bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("age", "INTEGER", mode="NULLABLE"),
    ]
    # noinspection PyTypeChecker
    table = bigquery.Table(table_id, schema=schema)
    client.create_table(table)
    print(
        "Created table '{}.{}.{}'".format(table.project, table.dataset_id, table.table_id)
    )


def my_python_select_records_count(project, dataset, table):
    # noinspection PyPackageRequirements
    from google.cloud import bigquery
    # noinspection SqlDialectInspection,SqlNoDataSourceInspection
    query = f"SELECT * FROM `{project}.{dataset}.{table}` LIMIT 10"
    # noinspection PyTypeChecker
    client = bigquery.Client(project=PROJECT)
    query_job = client.query(query=query, location='US')
    results = query_job.result()
    print(f"Got {results.total_rows} record(s)")


def my_python_bq_load_files_from_gcs_to_bq():
    # noinspection PyPackageRequirements
    from google.cloud import bigquery
    parquet_options = bigquery.format_options.ParquetOptions()
    parquet_options.enable_list_inference = True
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
        parquet_options=parquet_options
    )
    # noinspection PyTypeChecker
    client = bigquery.Client(project=PROJECT)
    job = client.load_table_from_uri(f"gs://{BUCKET}/parquet/{TABLE}/*.parquet",
                                     destination=f"{PROJECT}.{DATASET}.{TABLE}", location="US",
                                     job_config=job_config)
    job.result()
    print(job.output_rows)


def my_python_list_gcs(bucket_name):
    # noinspection PyPackageRequirements
    from google.cloud import storage
    client = storage.Client(PROJECT)
    bucket = storage.Bucket(client, bucket_name)
    blobs = list(client.list_blobs(bucket))
    print(f"Found {len(blobs)} blob(s)")
    print(f"blobs={blobs[0:10]}")


if __name__ == "__main__":
    main()
