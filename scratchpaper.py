from cards import Card, Deck

stock = Deck()
foundations = [[] for i in range(4)]
tableau = [[] for i in range(7)]
for j in range(7):
    for i in range(j,7):
        tableau[i].append(stock.deal())
        if j != i:
            tableau[i][-1].flip_card()
