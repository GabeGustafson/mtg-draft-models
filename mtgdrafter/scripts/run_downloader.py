from mtgdrafter.dataloading.scryfall_downloader import *
from mtgdrafter.dataloading.expansions import Expansion
import pandas as pd

if __name__ == "__main__":
    cards = get_scryfall_cards(["set=fdn", "is:booster"])

    # print(cards)

    exp = Expansion(cards)
    print(exp.card_name_to_id)