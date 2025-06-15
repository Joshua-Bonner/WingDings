from typing import List

from helpers.file_io import read_in_suppliers, read_in_wingdings
from helpers.validate import validate_wingding_supplier
from models.supplier import Supplier
from models.wingding import Wingding


def main():
    wingdings: List[Wingding] = read_in_wingdings("db/wingdings.json")
    suppliers: List[Supplier] = read_in_suppliers("db/suppliers.json")

    # wingdings.sort(key=lambda x: x.price, reverse=True)
    print(validate_wingding_supplier(suppliers, wingdings))


if __name__ == "__main__":
    main()
