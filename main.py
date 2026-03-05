from src.config import logger
from src.extract import fetch_data
from src.transform import transform_features
from src.load import load_to_bigquery


def main() -> None:
    """
    Orchestrates the ETL pipeline process: Fetch, Transform, and Load.
    """
    logger.info("--- Starting ETL Run ---")
    
    features = fetch_data()
    
    if not features:
        logger.warning("No data fetched from the API. Pipeline halted.")
        return
        
    try:
        rows = transform_features(features)
        load_to_bigquery(rows)
        logger.info("--- ETL Run Completed Successfully ---")
    except Exception as e:
        logger.error(f"Pipeline failed during load phase: {e}")


if __name__ == "__main__":
    main()