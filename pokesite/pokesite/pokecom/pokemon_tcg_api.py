from pokemontcgsdk import Card, Set, Type, Supertype, Subtype, Rarity

if __name__ == "__main__":
    print("This is the main page")

def proc_poke(poke, rar, col, sub):
    search = "name:" + poke
    for r in rar.split(' '):
        search += " rarity:" + r

    for c in col.split(' '):
        search += " set.name:" + c

    for s in sub.split(' '):
        search += " subtypes:" + s

    return Card.where(q=search)