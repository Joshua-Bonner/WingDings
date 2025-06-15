import json
import tempfile
from pathlib import Path

from src.helpers.file_io import read_in_wingdings
from src.models.wingding import Wingding


def test_read_in_wingdings():
    data = [
        {
            "uuid": "b3c1e8e2-2e7a-4c7c-9c1a-1f2e4a7b8c9d",
            "name": "Zantrix",
            "serial_num": 12345678,
            "type": "whozat",
            "supplier": "WingDingsRUs",
            "count": 5,
            "out_of_stock": False,
            "price": 54.23,
        }
    ]

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        json.dump(data, tmp)
        tmp_path = tmp.name

    wingdings = read_in_wingdings(tmp_path)

    assert isinstance(wingdings, list)
    assert isinstance(wingdings[0], Wingding)
    assert wingdings[0].name == "Zantrix"
    assert wingdings[0].price == 54.23

    Path(tmp_path).unlink(missing_ok=True)
