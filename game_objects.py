class Card:
    def __init__(self, id, points, type, price, img_url):
        self.id = id # int NOT NULL AUTO INCREMENT PRIMARY KEY
        self.points = points # int NOT NULL
        self.type = type # enum("Emerald", "Sapphire","Diamond","Onyx","Ruby") NOT NULL
        self.price = price # int NOT NULL FOREIGN KEY
        self.img_url = img_url # varchar(20) NOT NULL

    def __str__(self):
        return self.img_url

class Price:
    def __init__(self, id, emerald, sapphire, diamond, onyx, ruby):
        self.id = id # int NOT NULL AUTO INCREMENT PRIMARY KEY
        self.emerald = emerald # int NOT NULL
        self.sapphire = sapphire # int NOT NULL
        self.diamond = diamond # int NOT NULL
        self.onyx = onyx # int NOT NULL
        self.ruby = ruby # int NOT NULL

    def __str__(self):
        price = ""
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
        return price[:len(price)-1]


class Player:
    def __init__(self, name):
        self.name = name
        self.account = Account()
        self.set = Set()
        self.points = 0

class Set:
    def __init__(self):
        self.emerald_cards = []
        self.sapphire_cards = []
        self.diamond_cards = []
        self.onyx_cards = []
        self.ruby_cards = []

class Account:
    def __init__(self):
        self.emerald = 0
        self.sapphire = 0
        self.diamond = 0
        self.onyx = 0
        self.ruby = 0
        self.gold = 0