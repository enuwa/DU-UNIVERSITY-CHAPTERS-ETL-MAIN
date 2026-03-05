from typing import List, Dict, Any
from .config import logger

def transform_features(features: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Cleans and flattens raw API features into a format suitable for BigQuery.

    Args:
        features (List[Dict[str, Any]]): The raw feature list from the ArcGIS API.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries with flattened chapter attributes 
        and coordinate data.
    """

    transformed_rows: List[Dict[str, Any]] = []

    for feature in features:
        attributes = feature.get("attributes", {})
        geometry = feature.get("geometry", {})

        row = {
            "chapter_id": str(attributes.get("ChapterID")),
            "university_chapter": attributes.get("University_Chapter"),
            "city": attributes.get("City"),
            "state": attributes.get("State"),
            "latitude": geometry.get("y"),
            "longitude": geometry.get("x"),
        }
        transformed_rows.append(row)

    logger.info(f"Transformed {len(transformed_rows)} records")

    return transformed_rows