import random
SPADE = '♠'
HEART = '♥'
DIAMOND = '♦'
CLUB = '♣'

MARKS = [SPADE, HEART, DIAMOND, CLUB]
TRUMP_NUMBERS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Card:
    def __init__(self, val, mark):
        self.__val = val
        self.__trumpNumber = str(TRUMP_NUMBERS[val - 1])
        self.__mark = mark

    def __str__(self):
        return self.__mark + self.__trumpNumber
        
    @property
    def val(self)->int:
        return self.__val
    
    @property
    def trumpNumber(self)->str:
        return self.__trumpNumber

    @property
    def mark(self)->str:
        return self.__mark

class Deck:
    def __init__(self, n_deck = 1):
        self.__deck = []
        self.__nDeck = n_deck
        self.__createDeck()
        self.shuffledIdx = list(range(len(self.__deck)))
        self.__nDraw: int
        self.shuffleDeck()

    def __len__(self)->int:
        return len(self.__deck)

    def draw(self, n: int = None)->Card | list[Card | None] | None:
        if n is None:
            card = self.__deck[self.shuffledIdx[self.__nDraw]] if (self.__nDraw < len(self.__deck)) else None
            self.__nDraw += 1
        else:
            card = []
            for _ in range(n):
                card.append(self.__deck[self.shuffledIdx[self.__nDraw]] if (self.__nDraw < len(self.__deck)) else None)
                self.__nDraw += 1
        return card 

    def shuffleDeck(self)->None:
        random.shuffle(self.shuffledIdx)
        self.__nDraw = 0

    @property
    def deck(self)->list[Card]:
        return [self.__deck[idx] for idx in self.shuffledIdx]

    @property
    def sortedDeck(self)->list[Card]:
        return [card for card in self.__deck]

    @property
    def n_draw(self)->int:
        return self.__nDraw

    @property
    def n_remainingDeck(self)->int:
        return len(self.__deck) - self.__nDraw

    def __createDeck(self):
        numbers = range(1, len(TRUMP_NUMBERS) + 1)
        for m in MARKS:
            for n in numbers:
                for _ in range(self.__nDeck):
                    self.__deck.append(Card(n, m))


if __name__ == "__main__":
    deck = Deck()
    print("sortedDeck : ", end="")
    for card in deck.sortedDeck:
        print(f"{str(card)} ", end="")
    print("")
    for _ in range(3):
        print("shuffleDeck : ", end="")
        for _ in range(len(deck)):
            card = deck.draw()
            print(f"{str(card)} ", end="")
        print("")
        deck.shuffleDeck()