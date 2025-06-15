from uuid import UUID

from pydantic import BaseModel, Field, NonNegativeInt, computed_field


class Wingding(BaseModel):
    uuid: UUID = Field(
        default_factory=UUID,
        description="Unique identifier for the wingding",
    )
    name: str = Field(
        default="",
        description="Name of the wingding",
    )
    serial_num: NonNegativeInt = Field(
        default=00000000,
        description=(
            "Serial number of the wingding, must be a positive integer greater than or equal to 0"
        ),
    )
    type: str = Field(
        default="",
        description="Type of the wingding",
    )
    supplier: str = Field(
        default="",
        description="Supplier of the wingding",
    )
    count: NonNegativeInt = Field(
        default=0,
        description="Count of the wingding, must be a positive integer greater than or equal to 0",
    )
    price: float = Field(
        default=0.0,
        description="Price of the wingding",
    )

    @computed_field
    @property
    def out_of_stock(self) -> bool:
        """Returns True if the count is 0, otherwise False."""
        return self.count == 0
