import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

DATA_RAW = os.path.join(BASE_DIR, "data/raw")
DATA_PROCESSED = os.path.join(BASE_DIR, "data/processed")

MODEL_PATH = os.path.join(BASE_DIR, "models/model.pkl")