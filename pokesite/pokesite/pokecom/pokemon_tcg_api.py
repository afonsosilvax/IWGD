from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
from pokemontcgsdk import Rarity

card = Card.find('xy1-1')
cards = Card.where(q='set.name:ghjghj subtypes:mega')
cards1 = Card.where(q='name:pikachu')
rarity = Rarity.all()