import json
from typing import List

from models.supplier import Supplier
from models.wingding import Wingding


def read_in_wingdings(file_path) -> List[Wingding]:
    """
    Read in wingding data from a JSON file and return a list of Wingding objects.

    :param file_path: Path to the JSON file containing wingding data.
    :return: List of Wingding objects.
    """
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

    return [Wingding(**item) for item in data]


def read_in_suppliers(file_path) -> List[str]:
    """
    Read in supplier data from a JSON file and return a list of Supplier objects.

    :param file_path: Path to the JSON file containing supplier data.
    :return: List of Supplier objects.
    """
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

    return [Supplier(**supplier) for supplier in data]
