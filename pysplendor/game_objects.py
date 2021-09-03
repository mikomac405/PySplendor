from typing import List


class Price:
    def __init__(self, price_id: int, emerald: int, sapphire: int, diamond: int, onyx: int, ruby: int):
        self.id: int = price_id  # int NOT NULL AUTO INCREMENT PRIMARY KEY
        self.emerald: int = emerald  # int NOT NULL
        self.sapphire: int = sapphire  # int NOT NULL
        self.diamond: int = diamond  # int NOT NULL
        self.onyx: int = onyx  # int NOT NULL
        self.ruby: int = ruby  # int NOT NULL

    def __str__(self) -> str:
        price: str = ""
        if self.emerald > 0:
            price += "Emeralds: {}\n".format(self.emerald)
        if self.sapphire > 0:
            price += "Sapphires: {}\n".format(self.sapphire)
        if self.diamond > 0:
            price += "Diamonds: {}\n".format(self.diamond)
        if self.onyx > 0:
            price += "Onyxes: {}\n".format(self.onyx)
        if self.ruby > 0:
            price += "Rubies: {}\n".format(self.ruby)
        return price[:len(price) - 1]


class Card:
    def __init__(self, card_id: int, points: int, card_type: str, price: Price, img_url: str, tier: int):
        self.id: int = card_id  # int NOT NULL AUTO INCREMENT PRIMARY KEY
        self.points: int = points  # int NOT NULL
        self.type: str = card_type  # enum("Emerald", "Sapphire","Diamond","Onyx","Ruby", "VIP") NOT NULL
        self.price: Price = price  # int NOT NULL FOREIGN KEY
        self.img_url: str = img_url  # varchar(20) NOT NULL
        self.tier: int = tier  # int

    def __str__(self: object) -> str:
        return self.img_url


class Player:
    def __init__(self, name: str):
        self.name: str = name
        self.account: Account = Account()
        self.set: Set = Set()
        self.points: int = 0


class Set:
    def __init__(self):
        self.emerald_cards: List[Card] = []
        self.sapphire_cards: List[Card] = []
        self.diamond_cards: List[Card] = []
        self.onyx_cards: List[Card] = []
        self.ruby_cards: List[Card] = []


class Account:
    def __init__(self):
        self.emerald: int = 0
        self.sapphire: int = 0
        self.diamond: int = 0
        self.onyx: int = 0
        self.ruby: int = 0
        self.gold: int = 0
