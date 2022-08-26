import datetime
from dataclasses import dataclass
from typing import Union

tags = {
    1: "ANY",
    2: "RAP",
    3: "DEMAND",
    4: "RARES",
    5: "ROBUX",
    6: "UPGRADE",
    7: "DOWNGRADE",
    8: "WISHLIST",
    9: "PROJECTEDS",
    10: "ADDS",
}


@dataclass
class Ad:
    Id: int
    Date: datetime
    Roblox_Id: int
    Username: str
    Offering: Union[dict, list]
    Wanting: Union[dict, list]
    Link: str = ""

    def __post_init__(self):
        offering = self.Offering
        wanting = self.Wanting

        offering_items = offering.get("items", []) + [tags[i] for i in offering.get("tags", [])]
        if offering.get("robux", None):
            offering_items.append(f'Robux: {offering["robux"]}')

        wanting_items = wanting.get("items", []) + [tags[i] for i in wanting.get("tags", [])]
        if wanting.get("robux", None):
            wanting_items.append(f'Robux: {wanting["robux"]}')

        created = datetime.datetime.fromtimestamp(self.Date)

        self.Date = created.strftime("%r")
        self.Link = f"https://www.rolimons.com/tradead/{self.Id}"
        self.Offering = offering_items
        self.Wanting = wanting_items
