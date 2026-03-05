import logging
import os

# --- LOGGING ---
logging.basicConfig(
  level=logging.INFO, 
  format='%(asctime)s - %(levelname)s - %(message)s',
  filename='etl_pipeline.log',
  filemode='a' 
)
logger = logging.getLogger(__name__)

# --- CREDENTIALS ---
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp-key.json"


url = "https://services2.arcgis.com/5I7u4SJE1vUr79JC/arcgis/rest/services/UniversityChapters_Public/FeatureServer/0/query"
params = {
  "where": "1=1",
  "outFields": "ChapterID,University_Chapter,City,State",
  "outSR": "4326",
  "returnGeometry": "true",
  "f": "json"
}