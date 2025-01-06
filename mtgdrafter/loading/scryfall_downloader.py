import requests
import pandas as pd
import urllib
from mtgdrafter.loading.cards import Card

def get_scryfall_cards(args: list[str]) -> pd.DataFrame:
    search_q = _get_scryfall_query(args)
    
    response = requests.get(search_q)
    json = response.json()
    
    print("Scryfall query:", urllib.parse.unquote(search_q))

    # Build the list of cards from the response's json
    cards = [] 
    while json:
        cards.extend(_get_card_data_from_json(json))

        next_page_query = json.get("next_page", None)
        json = requests.get(next_page_query).json() if (json.get("has_more", False) and next_page_query) else None

    unique_cards = set(cards)

    print("# of Cards obtained from scryfall:", len(cards))
    print("# of unique Cards obtained from Scryfall", len(unique_cards))

    # Ensure that no duplicates are returned
    return pd.DataFrame(unique_cards)

def _get_scryfall_query(args: list[str]) -> str:
    BASE_SEARCH_URL = "https://api.scryfall.com/cards/search?q="

    return BASE_SEARCH_URL + urllib.parse.quote(" & ".join([q for q in args]))

def _get_card_data_from_json(json) -> list[Card]:
    return [Card(c) for c in json.get("data", [])]
