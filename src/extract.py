import requests
from typing import List, Dict, Any, Optional
from .config import logger, url, params

def fetch_data() -> List[Dict[str, Any]]:
  """
  Queries the Ducks Unlimited ArcGIS REST API to retrieve university chapter data.
  Returns:
      List[Dict[str, Any]]: A list of features (dictionaries) from the API response.
      Returns an empty list if the request fails.
  """
  
  try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    
    data = response.json()
    return data.get("features", [])
  
  except requests.exceptions.RequestException as e:
    logger.error(f"API Error: {e}")
  return []
