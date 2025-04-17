from typing import Literal


class Produto(object):
    def __init__(self, name: str, quantity: int, **kwargs) -> None:
        self.name  = name
        self.quantity = quantity
        self.info = kwargs
        
    def __str__(self) -> str:
        return f"Nome: {self.name}, Quantidade: {self.quantity}"
    
    def __repr__(self):
        return f"Product[{self.name}, {self.quantity}]"
    
    def __iter__(self) -> iter:
        return iter([self.name, self.quantity, self.info.values()])

    def __dict__(self):
        return {
            "nome": self.name,
            "quantidade": self.quantity,
            **self.info
        }
        
    def __len__(self):
        return len(list(self.__iter__()))
    
    def __getitem__(self, key: Literal["nome", "quantidade",  "info"]):
        return getattr(self, key)