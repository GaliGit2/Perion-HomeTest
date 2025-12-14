import json
from utils.config import USERS_PATH
import csv
from typing import List, Dict

def load_checkout_data(path: str) -> List[Dict[str, str]]:
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        raise AssertionError(f"Checkout CSV is empty: {path}")
    return rows

def load_users():
    with open(USERS_PATH, encoding="utf-8") as f:
        return json.load(f)