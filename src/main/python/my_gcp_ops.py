# python3 src/main/python/my_gcp_ops.py
# Intellij File/Project Structure/Project Settings/Modules/Right click on maven module/Add/Python
# folder python right click Mark directory as Source Root

import os
from my_package import my_add
PROJECT = os.getenv("GCP_PROJECT")
OWNER = os.getenv("GCP_OWNER")
DATASET = ''
TABLE = ''
BUCKET = f"{PROJECT}-{OWNER}"


def main():
    from utils.my_util import one
    print(one())
    print(my_add(1, 4))
    print(f"{PROJECT}, {OWNER}, {BUCKET}")
#    my_python_bq_load_files_from_gcs_to_bq()
#    my_python_select_count()
    my_python_list_gcs()


def my_python_select_count():
    # noinspection PyPackageRequirements
    from google.cloud import bigquery
    # noinspection SqlDialectInspection,SqlNoDataSourceInspection
    query = f"SELECT * FROM `{PROJECT}.{DATASET}.{TABLE}` LIMIT 10"
    # noinspection PyTypeChecker
    client = bigquery.Client(project=PROJECT)
    query_job = client.query(query=query, location='US')
    results = query_job.result()
    print(f"Got {results.total_rows}")


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


def my_python_list_gcs():
    # noinspection PyPackageRequirements
    from google.cloud import storage
    client = storage.Client(PROJECT)
    bucket = storage.Bucket(client, BUCKET)
    blobs = list(client.list_blobs(bucket))
    print(f"Found {len(blobs)} blob(s)")
    print(f"blobs={blobs[0:10]}")


if __name__ == "__main__":
    main()
