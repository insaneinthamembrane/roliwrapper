from typing import Generator, Union

import requests

from .item import Item


def camel(string: str) -> str:
    if not isinstance(string, str):
        raise TypeError("argument must be a string")

    return string[0].upper() + string[1:]


class ItemCache:
    cache: list[Item] = []
    demands = ["None", "Terrible", "Low", "Normal", "High", "Amazing"]
    trends = ["None", "Lowering", "Unstable", "Stable", "Raising", "Fluctuating"]

    def __init__(cls) -> None:
        cls.update()

    def __str__(cls) -> str:
        return f"{len(cls.cache)} cached items"

    def __iter__(cls) -> Generator[Item, None, None]:
        yield from cls.cache

    @classmethod
    def __getitem__(cls, identifier: Union[int, str]) -> Item:
        is_string = isinstance(identifier, str)
        if is_string:
            identifier = identifier.lower()

        for i in cls.cache:
            item_attrs = [i.Name, i.Name.lower(), i.Acronym, i.Acronym.lower()]
            if is_string and any(identifier in i for i in item_attrs) or i.Id == identifier:
                return i

    @classmethod
    def update(cls) -> None:
        """Updates current Item Cache"""

        req = requests.get("https://rolimons.com/itemapi/itemdetails")
        if req.status_code != 200:
            return

        res = req.json()
        items = res.get("items", [])
        trend, demand = cls.trends, cls.demands

        for item in items:
            data = items[item]

            data[5] = demand[data[5] + 1]
            data[6] = trend[data[6] + 1]
            data[7] = data[7] > 0
            data[8] = data[8] > 0
            data[9] = data[9] > 0
            data.insert(0, int(item))

        cls.cache = [Item(*items[i]) for i in items]

    @classmethod
    def get(cls, *keywords) -> list[Item]:
        keywords = [i.lower() for i in keywords]
        return [item for item in cls.cache if any(True for word in keywords if word in item.Name.lower() or item.Acronym.lower() == word)]


    @classmethod
    def projecteds(cls) -> list[Item]:
        """Returns all projected item ids"""
        return [item for item in cls.cache if item.Projected]

    @classmethod
    def valued(cls) -> list[Item]:
        """Returns all valued item ids"""
        return [item for item in cls.cache if item.Value > item.Rap]

    @classmethod
    def unvalued(cls) -> list[Item]:
        """Returns all unvalued item ids"""
        return [item for item in cls.cache if item.Value == -1]

    @classmethod
    def rares(cls) -> list[Item]:
        """Returns all rare item ids"""
        return [item for item in cls.cache if item.Rare]

    @classmethod
    def hyped(cls) -> list[Item]:
        """Returns all hyped item ids"""
        return [item for item in cls.cache if item.Hyped]

    @classmethod
    def demand(cls, demand: str = "None") -> list[Item]:
        """Returns all items with specified demand value
        Demand values: 'None', 'Terrible', 'Low', 'Normal', 'High', 'Amazing'

        Args:
            demand (str): Demand value to match

        Raises:
            ValueError: If wrong data type is given

        Returns:
            list[Ad]: List of items found with specified demand value
        """

        formatted = camel(demand)
        return [item for item in cls.cache if item.Demand == formatted]

    @classmethod
    def trend(cls, trend: str = "None") -> list[Item]:
        """Returns all Item Ids with specified trend value
        Trend values: 'None', 'Lowering', 'Unstable', 'Stable', 'Raising', 'Fluctuating'

        Args:
            trend (str): Trend value to match

        Raises:
            ValueError: If wrong data type is given

        Returns:
            list[Ad]: List of items found with specified trend value
        """

        formatted = camel(trend)
        return [item for item in cls.cache if item.Trend == formatted]

    @classmethod
    def sort_by(cls, sort_by: str = "Name") -> list[Item]:
        """Duplicates the cache and sorts by the specified identifier.
        Can be sorted by 'Id', 'Name', 'Rap', 'Value', 'Trend', or 'Demand'

        Args:
            sort_by (str, optional): What identifier to sort the list by. defaults to 'Name'.

        Raises:
            ValueError: If wrong data type is given

        Returns:
            list[Item]: Returns sorted list of items
        """

        cache = cls.cache
        origin, sort_by = sort_by, camel(sort_by)

        if sort_by == "Id":
            return sorted(cache)

        elif sort_by == "Name":
            return sorted(cache, key=lambda item: item.Name)

        elif sort_by in ["Rap", "Value"]:
            highest = max(item.Id for item in cls.cache)
            return sorted(cache, key=lambda item: highest - getattr(item, sort_by))

        elif sort_by in ["Trend", "Demand"]:
            sort = cls.__dict__[f"{origin}s"]
            return sorted(cache, key=lambda item: sort.index(getattr(item, sort_by)))
