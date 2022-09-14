# Rolimons API Wrapper

Used for fetching item and trade ad data from [Rolimons](https://www.rolimons.com/)

## Installation

```bash
pip install roliwrapper
```

## Usage

```python
import roliwrapper

ads = roliwrapper.AdCache()

# update ad cache
ads.update()

# find ads made by user id
ads.made_by(193283483)

# find ads containing item id
ads.containing(143984891)

items = roliwrapper.ItemCache()

# get item by acronym, keyword, name, or id
items["sttc"]

# update item cache
items.update()

# get all projected items
items.projecteds()

# get all valued items
items.valued()

# get all unvalued items
items.unvalued()

# get all rare items
items.rares()

# get all hyped items
items.hyped()

# get all items with specified demand value
# 'None', 'Terrible', 'Low', 'Normal', 'High', 'Amazing'
items.demand("amazing")

# get all items with specified trend value
# 'None', 'Lowering', 'Unstable', 'Stable', 'Raising', 'Fluctuating'
items.trend("stable")

# returns the cache sorted by the specified value
# Id', 'Name', 'Rap', 'Value', 'Trend', or 'Demand'
items.sort_by("rap")

# get all items found with keywords or acronyms provided
items.get("gucci", "ralph")

# create session to post trade ads
session = roliwrapper.session('verification')
session.post_ad('id', 'offering', 'requesting', 'tags')

# fetch player info by id
roliwrapper.fetch_player(298389293)
```