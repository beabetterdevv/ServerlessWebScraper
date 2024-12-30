from dataclasses import dataclass
from decimal import Decimal
from models.store import Store

@dataclass
class Product:
    id: str
    name: str
    price: Decimal
    url: str
    store: Store
    in_stock: bool

    def __str__(self) -> str:
        status = "IN STOCK" if self.in_stock else "OUT OF STOCK"
        return f"{self.id} is {status} at {self.store.name} at price ${self.price}"