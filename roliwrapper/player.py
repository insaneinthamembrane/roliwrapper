import datetime
from dataclasses import dataclass


@dataclass
class Player:
    Name: str
    Value: int
    Rap: int
    Rank: int
    Premium: bool
    Privacy_Enabled: bool
    Terminated: bool
    Stats_Uodated: datetime.datetime
    Last_Online: datetime.datetime
    Last_Location: str
    Rolibadges: dict[str, int]
