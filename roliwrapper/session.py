from typing import Union

import requests


class Session:
    def __init__(self, roli_verification: str) -> None:
        self.session = requests.Session()
        self.session.cookies.update({'_RoliVerification': roli_verification})

    def post_ad(self, player_id: int, offering: Union[list[int], None], requesting: Union[list[int], None], tags: Union[list[str], str, None]) -> str:
        req = self.session.post('https://www.rolimons.com/tradeapi/create', data={
            'player_id': player_id,
            'offer_item_ids': offering,
            'request_item_ids': requesting,
            'request_tags': tags
        })

        res = req.json()
        return req.status_code != 200 and f'Couldn\'t post ad (Reason: {res.get("message")})' or 'Success'
