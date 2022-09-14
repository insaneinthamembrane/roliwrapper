import requests

from .player import Player


def fetch_player(player_id: int) -> Player:
    req = requests.get(f"https://www.rolimons.com/playerapi/player/{player_id}")
    res = req.json()

    if not res['success']:
        return print(f'Unsuceessful request (Reason: {res["message"]})')

    res.pop('success')
    return Player(*res.values())
