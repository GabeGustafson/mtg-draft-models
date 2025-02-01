import pandas as pd

BASICS = ["plains", "island", "swamp", "mountain", "forest"]

# Stores the raw card data and features for a given expansion
class Expansion:
    def __init__(self, cards: pd.DataFrame):
        self.cards = cards
        self.num_cards = cards.shape[0]

        card_names = BASICS + [c.name for c in self.cards[0]]
        self.card_name_to_id = {n: i for i, n in enumerate(card_names)}