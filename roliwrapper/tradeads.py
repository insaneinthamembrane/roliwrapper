from .ad import Ad

from typing import Union

import requests


class AdCache:
    cache: list[Ad] = []

    def __init__(cls) -> None:
        cls.update()

    def __str__(cls) -> str:
        return f'{len(cls.cache)} cached trade ads'

    def __iter__(cls) -> Ad:
        for i in cls.cache:
            yield i

    @classmethod
    def __getitem__(cls, identifier: Union[int, str]) -> Ad:
        for i in cls.cache:
            if i.Id == identifier or i.Roblox_Id == identifier:
                return i

    @classmethod
    def update(cls) -> None:
        """Updates current trade ad cache"""

        req = requests.get('https://www.rolimons.com/tradeadsapi/getrecentads')
        if req.status_code != 200:
            return

        res = req.json()
        trade_ads = res.get('trade_ads', [])

        cls.cache = [Ad(*i) for i in trade_ads]

    @classmethod
    def containing(cls, item_id: int) -> list[Ad]:
        """Returns all ads found with provided item id

        Args:
            item_id (int): Item id to search for

        Returns:
            list[Ad]: List of ads found that contain the item id
        """

        found_ads = [ad for ad in cls.cache if item_id in ad.Offering or item_id in ad.Wanting]
        return found_ads

    @classmethod
    def made_by(cls, player_id: int) -> list[Ad]:
        """Returns all ads created by the provided player id

        Args:
            player_id (int): Player Id to search for

        Returns:
            list[Ad]: List of ads found that were created by the player
        """

        found_ads = [ad for ad in cls.cache if player_id == ad.Roblox_Id]
        return found_ads
