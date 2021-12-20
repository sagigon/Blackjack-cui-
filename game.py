from blackjack import Blackjack
import time

class Game():
    HIT = "hit"
    STAND = "stand"
    def __init__(self):
        self.bj = Blackjack()
        print(f"dealer : ** {str(self.bj.dealerHand.cards[1])}")
        self.printPlayerScore()

    def play(self)-> None:
        while self.action():
            pass
        self.printDealerScore()
        for _ in self.bj.dealerTurn():
            self.printDealerScore()
        self.printResult()

    def action(self)-> bool:
        print(f"{self.HIT} or {self.STAND}")
        userInput = input()
        while userInput != self.HIT and userInput != self.STAND:
            print(f'Please input "{self.HIT}" or "{self.STAND}"')
            userInput = input()
        
        if userInput == self.STAND:
            return False
        else:
            self.bj.hit()
            self.printPlayerScore()
            if self.bj.playerHand.isBust():
                print("bust!!!!!")
                return False
        return True

    def printResult(self)-> None:
        print("\n" * 3 + "!-" * 10 + "!")
        time.sleep(2)
        print(f"you : {str(self.bj.playerHand)}\nscore : {self.bj.playerHand.score[-1]}", )
        self.printDealerScore()
        print("-" * 20 )
        print(f"result : {self.bj.winLose()}")
        print("!-" * 10 + "!")

    def printPlayerScore(self)-> None:
        print('-' * 20)
        time.sleep(1)
        print(f"you : {str(self.bj.playerHand)}\nscore : ", end ="")
        for score in self.bj.playerHand.score:
            print(f"{score} ", end="")
        print("")

    def printDealerScore(self)-> None:
        print('-' * 20)
        time.sleep(1)
        print(f"dealer : {str(self.bj.dealerHand)}")
        print(f"score : {self.bj.dealerHand.score[-1]}")

if __name__ == "__main__":
    game = Game()
    game.play()