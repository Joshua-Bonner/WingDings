import json
from typing import List

from src.models.wingding import Wingding


def read_in_wingdings(file_path) -> List[Wingding]:
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

    wingdings: List[Wingding] = [Wingding(**item) for item in data]
    return wingdings
