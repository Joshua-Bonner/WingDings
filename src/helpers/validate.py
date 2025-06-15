from typing import List

from src.models.supplier import Supplier
from src.models.wingding import Wingding


def validate_wingding_supplier(suppliers: List[Supplier], wingdings: List[Wingding]) -> bool:
    """
    Validate that each wingding is supplied by the correct supplier.

    :param suppliers (List[Supplier]): List of suppliers to validate.
    :param wingdings (List[Wingding]): List of valid wingdings.
    :return: bool: True if all suppliers are valid, False otherwise.
    """
    # Build a mapping from supplier name to set of wingding names they actually supply
    supplier_to_products = {}
    for wd in wingdings:
        supplier_to_products.setdefault(wd.supplier, set()).add(wd.name)

    # Check each supplier's products
    for supplier in suppliers:
        actual_products = supplier_to_products.get(supplier.name, set())
        for product in supplier.products:
            if product not in actual_products:
                return False
    return True
