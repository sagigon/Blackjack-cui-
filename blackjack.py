import trump
from trump import Deck, Card 

class Hand():
    def __init__(self, cards: list[Card] = [], sort = False):
        self.__cards = cards
        self.sort = sort
        if self.sort:
            self.__cards.sort(key=lambda c:(c.val, c.mark))

    def __str__(self):
        s = ""
        for card in self.__cards:
            s += f"{str(card)} "
        return s

    def addHand(self, card: Card):
        self.__cards.append(card)
        if self.sort:
            self.__cards.sort(key=lambda c:(c.val, c.mark))

    def isBlackJack(self)-> bool:
        return (self.score[-1] == 21) and (len(self.__cards) == 2)

    def isBust(self)-> bool:
        return self.score[0] > 21

    @property
    def cards(self)-> list[Card]:
        return self.__cards

    @property
    def score(self)-> list[int]:
        if self.__cards:         
            sumScores = [0]
            for card in self.cards:
                sumScores[0] += card.val if card.val <= 10 else 10 
            if min(self.cards, key=lambda x: x.val).val == 1 and sumScores[0] + 10 <= 21:
                sumScores.append(sumScores[0] + 10)
            return sumScores
        else:
            return [0]   
        

class Blackjack():
    WIN = "win"
    LOSE = "lose"
    DRAW = "draw"
    def __init__(self):
        self.__deck = Deck()
        self.__dealerHand = Hand(self.__deck.draw(2))
        self.__playerHand = Hand(self.__deck.draw(2))        
    
    def hit(self)-> Hand :     
        if self.__playerHand.score[0] > 21:
            print("bust")
            return
        self.__playerHand.addHand(self.__deck.draw())
        return self.__playerHand

    def dealerTurn(self)-> Hand:
        while self.__dealerHand.score[-1] < 17:
            self.__dealerHand.addHand(self.__deck.draw())
            yield self.__dealerHand

    def winLose(self)-> str:
        if self.__dealerHand.isBust():
            return self.LOSE if self.__playerHand.isBust() else self.WIN
        elif self.__playerHand.isBust():
            return self.LOSE
        d_score = self.__dealerHand.score[-1]
        p_score = self.__playerHand.score [-1]
        if d_score != p_score:
            return self.LOSE if (d_score > p_score) else self.WIN
        elif d_score != 21:
            return self.DRAW
        else:
            if self.__dealerHand.isBlackJack():
                return self.DRAW if self.__playerHand.isBlackJack() else self.LOSE
            else:
                return self.WIN if self.__playerHand.isBlackJack()  else self.DRAW 
                
    @property
    def playerHand(self):
        return self.__playerHand
    
    @property
    def dealerHand(self):
        return self.__dealerHand
    
if __name__ == "__main__":
    bj = Blackjack()
    print(f"player : {bj.playerHand.score[-1]} \n {str(bj.playerHand)}")

    print(f"dealer : {bj.dealerHand.score[-1]} \n {str(bj.dealerHand)}")