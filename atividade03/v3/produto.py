from typing import Annotated, Any, Callable, Dict, Generic, Literal, TypeVar

T = TypeVar("T")

class Variable(Generic[T]):
    variables = {}
    def __init__(self, value: T) -> None:
        self.name = self.__class__.__name__
        self.value: T = value
        self.variables[self.name] = {"v": self, "c": self.get_callbacks}
        
        self.__callback_on_change__: list[Callable[[Annotated[T, "old_value"], Annotated[T, "new_value"]], None]] = []
        self.__callback_on_get__: list[Callable[[Annotated[T, "value"]], None]] = []
        self.__callback_on_deletion__: list[Callable[[Annotated[T, "last_value"]], None]] = []
    
    def get_callbacks(self) -> dict[str, Callable]:
        return {
            "on_change": self.__callback_on_change__,
            "on_get": self.__callback_on_get__
        }
        
    def new_on_change(self, callback: Callable[[Annotated[T, "old_value"], Annotated[T, "new_value"]], None]) -> None:
        self.__callback_on_change__.append(callback)
        
    def new_on_get(self, callback: Callable[[Annotated[T, "value"]], None]) -> None:
        self.__callback_on_get__.append(callback)
    
    def new_on_deletion(self, callback: Callable[[Annotated[T, "last_value"]], None]) -> None:
        self.__callback_on_deletion__.append(callback)
        
    def trigger_on_change(self, old_value: T, new_value: T) -> None:
        for callback in self.__callback_on_change__:
            callback(old_value, new_value)
    def trigger_on_get(self, value: T) -> None:
        for callback in self.__callback_on_get__:
            callback(value)
            
    def trigger_on_deletion(self, last_value: T) -> None:
        for callback in self.__callback_on_deletion__:
            callback(last_value)
        
    def set(self, value: T) -> None:
        self.trigger_on_change(self.value, value)
        self.value = value
    
    def get(self) -> T:
        self.trigger_on_get(self.value)
        return self.value
    
    def delete(self) -> None:
        self.trigger_on_deletion(self.value)
        del self
        
    def __str__(self):
        return super().__str__()
    
    def __repr__(self):
        return super().__repr__()

class Produto(object):
    def __init__(self, name: str, quantity: int, **kwargs: T) -> None:
        self.__name__: Variable[str]  = Variable(name)
        self.__quantity__: Variable[int] = Variable(quantity)
        self.__info__: Variable[Dict[str, Any]] = Variable(kwargs)
        
    @property
    def name(self) -> str:
        return self.__name__.get()
    
    @name.getter
    def name(self) -> str:
        return self.__name__.get()
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name__.set(name)
        
    @property
    def quantity(self) -> int:
        return self.__quantity__.get()
    
    @quantity.getter
    def quantity(self) -> int:
        return self.__quantity__.get()
    
    @quantity.setter
    def quantity(self, quantity: int) -> None:
        self.__quantity__.set(quantity)
        
    def __str__(self) -> str:
        return f"Nome: {self.name}, Quantidade: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"Product[{self.name}, {self.quantity}]"
    
    def __iter__(self) -> iter:
        return iter([self.name, self.quantity, self.__info__.value.values()])

    def __dict__(self) -> Dict[str, Any]:
        return {
            "nome": self.name.value,
            "quantidade": self.quantity.value,
            **self.info.value
        }
        
    def __len__(self) -> int:
        return len(list(self.__iter__()))
    
    def __getitem__(self, key: Literal["nome", "quantidade",  "info"]) -> Any:
        return getattr(self, key)
    
CurrencyUnit = Literal["USD", "EUR", "BRL"]
USD, EUR, BRL = ["USD", "EUR", "BRL"]
class Currency:
    def __init__(self, value: float, unit: CurrencyUnit) -> None:
        self.value: Variable[float] = Variable(value)
        self.__unit__: Variable[CurrencyUnit] = Variable(unit)
        
    def __str__(self) -> str:
        return f"{self.value.value} {self.__unit__.value}"