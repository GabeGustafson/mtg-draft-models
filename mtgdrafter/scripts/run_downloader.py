from mtgdrafter.dataloading.scryfall_downloader import *
import pandas as pd

if __name__ == "__main__":
    cards = get_scryfall_cards(["set=fdn", "is:booster"])

    print(cards)
    print(cards.shape)