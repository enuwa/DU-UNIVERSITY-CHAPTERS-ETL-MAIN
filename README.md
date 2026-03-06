## Ducks Unlimited University Chapters ETL Pipeline

The project implements a production-grade data pipeline that extracts university chapter data from the ArcGIS REST API, transforms the geospatial features into a structured format, and loads them into a Google BigQuery data warehouse.

## Data Pipeline Architecture

The pipeline follows a modular Extraction-Transformation-Load (ETL) pattern to ensure a clean separation of concerns:

Extract: Queries the Ducks Unlimited ArcGIS FeatureServer.

Transform: Flattens nested JSON, maps coordinates (Longitude/Latitude), and enforces schema types.

Load: Uses an idempotent WRITE_TRUNCATE strategy to load data into BigQuery.

[**Data Source**](https://services2.arcgis.com/5I7u4SJE1vUr79JC/arcgis/rest/services/UniversityChapters_Public/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json)

API Base URL: DU University Chapters ArcGIS REST API

### Business Understanding

Organization: Ducks Unlimited (DU) is a world leader in wetlands and waterfowl conservation.

### Business Challenge
- **Data Silos:** Valuable university chapter location data is locked in external ArcGIS feature servers, making it difficult for the broader organization to access for cross-platform reporting.

- **Manual Reporting:** Lack of automation leads to delayed insights regarding regional chapter growth and student engagement.

- **Reproducibility:** The organization requires a standardized, well-structured codebase that can be audited and run reliably by any member of the data engineering team.

### Project Objectives
- **Develop a Scalable ETL Pipeline:** Implement a modular Python system to automate data synchronization from ArcGIS to the cloud.

- **Enhance Data Quality:** Implement logging and error handling to ensure data integrity and observability during the transformation phase.

- **Cloud Integration:** Centralize data in Google BigQuery to enable advanced spatial analytics and Power BI reporting.

### Project Deliverable
The goal is to provide Places for People with a reliable "Single Source of Truth" for University Chapter data, ensuring stakeholders can make data-driven decisions based on accurate, real-time location metrics.

## Project Stack
- **API:** ArcGIS REST API (JSON source).

- **Language:** Python 3.9+ (Modular structure).

- **Warehouse:** Google BigQuery (Cloud destination).

- **Observability:** Structured Logging and Error Handling.

## Project Setup
### Clone The Repository
```Bash
# Clone the repository
git clone https://github.com/enuwa/du-university-chapters-etl-main.git

# Navigate to project directory
cd du-university-chapters-etl-main
```
### Setup Environment Variables & Security

# Create a service account key in Google Cloud Console with BigQuery Data Editor permissions.

# Save the file as gcp-key.json in the project root.

# Note: This file is ignored by Git for security via .gitignore to prevent unauthorized cloud spend.

### Create And Activate The Virtual Environment
```PowerShell

 python -m venv .venv

# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate
```

### Install Project Dependencies
```Bash

pip install -r requirements.txt
```

## Run The ETL Pipeline
```Bash
python main.py
```

### Quality & Reliability Features
- **Error Handling:** Robust try-except blocks for network timeouts and BigQuery load failures.

- **Logging:** All runs generate a persistent etl_pipeline.log for operational auditing.

- **Idempotency:** The loader replaces the table each run to prevent duplicate records.

- **Separation of Concerns:** Modular code residing in the src/ directory for high maintainability.

## Further Additions
- **CI/CD:** Implementation of GitHub Actions for linting and automated testing.

- **Testing:** Adding unit tests for coordinate mapping validation.
