    Ducks Unlimited University Chapters ETL Pipeline

A professional Python-based ETL pipeline designed to synchronize university chapter data from the ArcGIS REST API to Google BigQuery. This project demonstrates production-grade code structure, observability, and idempotency.

    Architecture & Flow
The pipeline follows a modular Extraction-Transformation-Load (ETL) pattern to ensure a clean separation of concerns:

1.   Extract: Queries the ArcGIS REST API with robust timeout and error handling.
2.   Transform: Flattens nested JSON features, enforces schema types (casting IDs to strings), and extracts coordinate geometry.
3.   Load: Uses an idempotent `WRITE_TRUNCATE` strategy to load data into BigQuery, ensuring no duplicate records.



 Key Deliverables Met

 1. Quality & Readability
    Type Hinting: All functions utilize Python's `typing` module for clarity and IDE support.
    Docstrings: Follows Google-style documentation to explain function intent, parameters, and return types.

 2. Appropriate Tooling & Structure
    Logging: Implements a persistent file-based logger (`etl_pipeline.log`) for operational monitoring.
    Folder Structure: Organized for local execution with a clear entry point in `du_main.py`.

 3. Error Handling & Validation
    Handles network-level exceptions (Request timeouts/HTTP errors).
    Validates API responses before attempting transformation.
    Explicit BigQuery schema definition prevents "data drift" or auto-detection errors.

  4. Reproducibility & Setup
     The pipeline is designed to be set up and run locally by a reviewer in under 2 minutes.


 Setup & Usage Instructions

 Prerequisites
   Python 3.9+
   A Google Cloud Service Account key (`gcp-key.json`) with BigQuery Data Editor permissions.

 Local Installation
  1. Clone and Navigate:
   bash
   git clone [https://github.com/enuwa/du-university-chapters-etl.git](https://github.com/enuwa/du-university-chapters-etl.git)
   cd du-university-chapters-etl