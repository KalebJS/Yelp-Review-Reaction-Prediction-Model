from datetime import datetime
from pathlib import Path


class PROPORTION:
    SM = 0.02
    MD = 0.2
    LG = 0.78
    XL = 1.0


proportion = PROPORTION.MD


class PATHS:
    CWD = Path.cwd()
    DB = CWD / "dns-db" / "database.db"

    RAW_JSON = CWD / "dns-raw-json"
    RAW_REVIEWS = RAW_JSON / "yelp_academic_dataset_review.json"
    RAW_USER = RAW_JSON / "yelp_academic_dataset_user.json"
    RAW_BUSINESS = RAW_JSON / "yelp_academic_dataset_business.json"

    OBJECTS_FOLDER = CWD / "dns-objects"
    CLEAN_DATA_PICKLE = OBJECTS_FOLDER / "clean_data.pickle"
    TRANSFORMED_DATA_PICKLE = OBJECTS_FOLDER / "transformed_data.pickle"

    KERAS_MODELS = CWD / "dns-keras-models"
    KERAS_MODEL = KERAS_MODELS / "keras_model.pkl"


DATE_COLLECTED = datetime.now()
