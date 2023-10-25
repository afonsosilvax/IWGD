from pokemontcgsdk import Card, Set, Type, Supertype, Subtype, Rarity

if __name__ == "__main__":
    card = Card.find('xy1-1')
    cards = Card.where(q='set.name:ghjghj subtypes:mega')
    cards1 = Card.where(q='name:pikachu')
    rarity = Rarity.all()
    print("This is the main page")

def poke_validacao(poke, rar, col):
    pass