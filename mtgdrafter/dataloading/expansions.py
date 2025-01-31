import pandas as pd

# Stores the raw card data and features for a given expansion
class Expansion:
    def __init__(self, cards: pd.DataFrame):
        self.cards = cards
        self.num_cards = cards.shape[0]