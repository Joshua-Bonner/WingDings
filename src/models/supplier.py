from pydantic import BaseModel, Field

# class Address(BaseModel):
#     street: str = Field(
#         default="",
#         description="Street address of the supplier",
#     )
#     city: str = Field(
#         default="",
#         description="City of the supplier",
#     )
#     state: str = Field(
#         default="",
#         min_length=2,
#         max_length=2,
#         pattern=r"^[A-Z]{2}$",
#         description="State of the supplier, represented by a two-letter code",
#     )
#     zip_code: str = Field(
#         default="",
#         min_length=5,
#         max_length=10,
#         pattern=r"^\d{5}(-\d{4})?$",
#         example="12345 or 12345-6789",
#         description="Zip code of the supplier",
#     )


class Supplier(BaseModel):
    name: str = Field(
        default="",
        description="Name of the supplier",
    )
    address: str = Field(
        default="",
        description="Address of the supplier",
    )
    products: list[str] = Field(
        default_factory=list,
        description="List of products supplied by the supplier",
    )
    point_of_contact: str = Field(
        default="",
        description="Point of contact at the supplier",
    )
    phone_number: str = Field(
        default="",
        description="Contact number for the supplier",
    )
