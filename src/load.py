from typing import List, Dict, Any
from google.cloud import bigquery

from .config import logger


# --- CONFIGURATION ---
PROJECT_ID: str = "duchapter-project" 
DATASET_ID: str = "du_dataset"
TABLE_ID: str = "du_university_chapters"


def load_to_bigquery(rows: List[Dict[str, Any]]) -> None:
    """
    Loads transformed data into a Google BigQuery table using WRITE_TRUNCATE.

    Args:
        rows (List[Dict[str, Any]]): The list of transformed dictionaries to load.
    
    Raises:
        google.cloud.exceptions.GoogleCloudError: If the load job fails.
    """
    
    client = bigquery.Client(project=PROJECT_ID)
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("chapter_id", "STRING"), 
            bigquery.SchemaField("university_chapter", "STRING"),
            bigquery.SchemaField("city", "STRING"),
            bigquery.SchemaField("state", "STRING"),
            bigquery.SchemaField("latitude", "FLOAT"),
            bigquery.SchemaField("longitude", "FLOAT"),
        ],
        write_disposition="WRITE_TRUNCATE",
    )

    load_job = client.load_table_from_json(
        rows, 
        table_ref, 
        job_config=job_config,
        location="US"  
    )
    
    load_job.result()  # Waits for the job to complete
    logger.info(f"Loaded {load_job.output_rows} rows into {table_ref} (US)")
