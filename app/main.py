from abc import ABC


class IntegerRange:
    def __init__(self, min_amount: int, max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(self, owner: object, name: str) -> None:
        self.private_name = "_" + name

    def __get__(self, instance: type, owner: object) -> None:
        return setattr(instance, self.private_name)

    def __set__(self, instance: type, value: any) -> None:
        if not isinstance(value, int):
            raise TypeError()
        if self.min_amount < value < self.max_amount:
            raise ValueError()
        return setattr(instance, self.private_name)


class Visitor:

    def __init__(self,
                 name: str,
                 age: int,
                 weight: float | int,
                 height: float | int
                 ) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


class SlideLimitationValidator(ABC):
    def __init__(self,
                 age: int,
                 weight: float | int,
                 height: float | int
                 ) -> None:
        self.age = age
        self.weight = weight
        self.height = height


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    def __init__(self,
                 age: int,
                 weight: float | int,
                 height: float | int
                 ) -> None:
        if 4 < age < 14:
            raise ValueError("zły wiek")
        elif 80 < height < 120:
            raise ValueError("zły wzrost")
        elif 20 < weight < 50:
            raise ValueError("Zla waga")
        else:
            super().__init__(age=age, weight=weight, height=height)


class AdultSlideLimitationValidator(SlideLimitationValidator):
    def __init__(self,
                 age: int,
                 weight: float | int,
                 height: float | int
                 ) -> None:
        if 14 < age < 60:
            raise ValueError("zły wiek")
        elif 120 < height < 220:
            raise ValueError("zły wzrost")
        elif 50 < weight < 120:
            raise ValueError("Zla waga")
        else:
            super().__init__(age=age, weight=weight, height=height)


class Slide:
    def __init__(self, name: str, limitation_class: type) -> None:
        self.name = name
        self.limitation_class = limitation_class

    def can_acces(self) -> bool:
        # Jak mam się odwolać do instancji klasy Visitor,
        # jesli nie jest podana jako argument.
        # Bez tego nie wywołam innych metod.
        # Ogólnie nie czuję się pewnie i płynnie w pisaniu deskryptorów
        pass
