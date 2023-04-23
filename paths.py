from pathlib import Path


CWD = Path.cwd()

RAW_DATA_FOLDER = CWD / "dns-raw-data"

RAW_REVIEWS = RAW_DATA_FOLDER / "yelp_academic_dataset_review.json"
RAW_BUSINESS = RAW_DATA_FOLDER / "yelp_academic_dataset_business.json"
RAW_USER = RAW_DATA_FOLDER / "yelp_academic_dataset_user.json"

DB_FOLDER = CWD / "dns-db"

DB_FILE = DB_FOLDER / "database.db"

OBJECTS_FOLDER = CWD / "dns-objects"

POPULAR_REVIEWS_PREPARED = OBJECTS_FOLDER / "popular_reviews.pkl"
POPULAR_REVIEWS_TRANSFORMED = OBJECTS_FOLDER / "popular_reviews_transformed.pkl"
POPULAR_EMBEDDINGS = OBJECTS_FOLDER / "popular_embeddings.pkl"
UNPOPULAR_REVIEWS_PREPARED = OBJECTS_FOLDER / "unpopular_reviews.pkl"
UNPOPULAR_REVIEWS_TRANSFORMED = OBJECTS_FOLDER / "unpopular_reviews_transformed.pkl"
UNPOPULAR_EMBEDDINGS = OBJECTS_FOLDER / "unpopular_embeddings.pkl"