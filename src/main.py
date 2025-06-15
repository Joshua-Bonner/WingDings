from typing import List

from helpers.file_io import read_in_wingdings
from models.wingding import Wingding


def main():
    wingdings: List[Wingding] = read_in_wingdings("db/wingdings.json")
    wingdings.sort(key=lambda x: x.price, reverse=True)
    for wingding in wingdings:
        print(
            f"{wingding.name} - ${wingding.price:.2f} - {'Out of Stock' if wingding.out_of_stock else 'In Stock'}"
        )


if __name__ == "__main__":
    main()
