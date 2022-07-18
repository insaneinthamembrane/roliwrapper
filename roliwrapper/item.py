from dataclasses import dataclass


@dataclass
class Item:
    Id: int
    Name: str
    Acronym: str
    Rap: int
    Value: int
    Default_Value: int
    Demand: str
    Trend: str
    Projected: bool
    Hyped: bool
    Rare: bool

    def __eq__(self, other):
        return self.Value == other.Value

    def __gt__(self, other):
        return self.Value > other.Value

    def __lt__(self, other):
        return self.Value < other.Value
