#This V3 version includes all my Comments and test print()s kept for my own learning and review purposes
#This V3 version not yet has all validations
#V4 version is an EXACT copy of M43Poker.py as backup
#Keeping M43Poker.py copy for mimic integration test run 

import sys


class Card:
    def __init__(self, strCard):
        self.value = self.findVal(strCard[0])  
        self.suit = strCard[1]                 

    def findVal(self, rank):
        return {
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            'T':10,
            'J':11,
            'Q':12,
            'K':13,
            'A':14,
        }.get(rank)

    def __repr__(self):                             #printing card object in string form
        return f"{self.value} of {self.suit}"


class Hand:
    def __init__(self, lsThreeCards):               #['2c', 'As', '4d']
        self.handOfThree = []
        self.sortedSuits = []
        self.sortedValues = []
        self.handType = ""
        self.kicker = 0
        self.handScore = 0

        for item in lsThreeCards:
            self.handOfThree.append(Card(item))     #[cardObj1, cardObj2, cardObj3]

        self.getAllSuits()
        self.getAllValues()
        self.evaluateHandType()

    def __repr__(self):
        return f'{self.handOfThree}'                #printing hand object in string form


    def getAllSuits(self):
        for card in self.handOfThree:               #[cardObj1, cardObj2, cardObj3]
            self.sortedSuits.append(card.suit)      #['c','s','d']
        self.sortedSuits.sort()                     #Not needed for logic, sorting suit for my own testing convenience
        # print(" "*20)
        # print(self.sortedSuits)                     #['c','d','s']

    def getAllValues(self):
        for card in self.handOfThree:               #[{card1},{card2},{card3}]
            self.sortedValues.append(card.value)    #['2','1','4']
        self.sortedValues.sort()
        # print(self.sortedValues)                    #['1','2','4']


    def isStraightFlush(self):
        # print(f'isStraightFlush Ran')
        if self.isStraight() and self.isFlush():
            # self.handType = "StraightFlush"
            return True
        else:
            return False

    def isThreeOfKind(self):
        # 3 same Rank
        # 4c 4h 4d

        # currRank = self.handOfThree[0]['rank']
        # for card in self.handOfThree:
        #     if (currRank != card['rank']):
        #         print(f'currRank/[0]: {currRank}  card[rank]: {card['rank']}')
        #         return False
        # return True   

        # if self.allValues.count(self.allValues[0]) != 3:
        # print(f'isThreeKind Ran')
        if self.sortedValues.count(self.sortedValues[0]) == 3:
            # self.handType = "ThreeOfKind"
            return True
        else:
            return False

    def isStraight(self):
        # Rank in a run
        # low, low+1, low+2
        # Q-K-A ok-highest, A as 14
        # 9-T-J ok
        # A-2-3 ok-lowest ------(2,3,14)
        # K-A-2 X Nope    ------(2,13,14)
        # print(f'isStraight Ran')
        lowestCard = min(self.sortedValues)
        if (self.sortedValues[0] == lowestCard and self.sortedValues[1] == lowestCard+1 and self.sortedValues[2] == lowestCard+2):
            # self.handType = "Straight"
            return True
        elif (self.sortedValues[0] == 2 and self.sortedValues[1] == 3 and self.sortedValues[2] == 14):
            return True
        else:
            return False


    def isFlush(self):
        # 3 same Suit - h c d s
        # Ac 4c 8c
        
        # currSuit = self.handOfThree[0].suit
        # for card in self.handOfThree:
        #     if (currSuit != card.suit):
        #         print(f'currSuit/[0]: {currSuit}  card.suit: {card.suit}')
        #         return False
        # return True

        # if self.allSuits.count(self.allSuits[0]) != 3:
        # print(f'isFlush Ran')
        if self.sortedSuits.count(self.sortedSuits[0]) == 3:
            # self.handType = "Flush"
            return True
        else:
            return False

    def isPair(self):
        # two same rank ###, one is diff
        # 4c 4d 5h
        # print(f'isPair Ran')
        if self.sortedValues.count(self.sortedValues[1]) == 2:
            # self.handType = "Pair"
            if self.sortedValues.count(self.sortedValues[0]) == 1:
                self.kicker = self.sortedValues[0]
            else:
                self.kicker = self.sortedValues[2]
            return True
        else:
            return False

    # def isHighCard(self):
    #     #none of the above
    #     print(f'isHighCard Ran')
    #     if not(self.isStraightFlush()) and not(self.isThreeOfKind()) and not(self.isStraight()) and not(self.isFlush()) and not(self.isPair()):
    #         # self.handType = "HighCard"
    #         return True
    #     else:
    #         return False


    def evaluateHandType(self):
        if self.isStraightFlush():  
            self.handType = 'StraightFlush'
        elif self.isThreeOfKind(): 
            self.handType = 'ThreeOfKind'
        elif self.isStraight(): 
            self.handType = 'Straight'
        elif self.isFlush(): 
            self.handType = 'Flush'
        elif self.isPair(): 
            self.handType = 'Pair'
        # elif self.isHighCard():
        #     self.handType = 'HighCard'
        else:
            self.handType = 'HighCard'


    def calcScore(self):
        if self.handType == 'StraightFlush':    #500
            self.handScore = 5000000
        elif self.handType == 'ThreeOfKind':    #400
            self.handScore = 4000000
        elif self.handType == 'Straight':       #300
            self.handScore = 3000000
        elif self.handType == 'Flush':          #200
            self.handScore = 2000000
        elif self.handType == 'Pair':           #100
            self.handScore = 1000000
        elif self.handType == 'HighCard':       #0
            self.handScore = 0
        # else:
            # print(f'None: Something IS wrong!',self.handType, self.handScore)

        if self.handType == 'Pair':
            self.handScore += self.sortedValues[1]*10000
            self.handScore += self.sortedValues[1]*100
            self.handScore += self.kicker
        else:
            self.handScore += self.sortedValues[2]*10000
            self.handScore += self.sortedValues[1]*100
            self.handScore += self.sortedValues[0]

        # print(self.handType, self.handScore)
        return self.handScore


class Player:
    def __init__(self, lsPlayersCard):       #['0', 'Kh', '4d', '3c']
        self.id = lsPlayersCard[0]
        self.hand = Hand(lsPlayersCard[1:])  #['Kh', '4d', '3c']
    # player.hand.calcScore()

    def __repr__(self):
        return f'PlayerID: {self.id} | PlayerHand: {self.hand}'
        # PlayerID: 0 | PlayerHand: [ # of suit, # of suit, # of suit ]



class Game:
    def __init__(self, lsInput):
        self.game = lsInput      #['3', '0 2c As 4d', '1 Kd 5h 6c', '2 Jc Jd 9s']
        self.players = {}       #{'0':##score##, '1':##score##, '2':##score##, '3':##score## }
        self.winner = []
        # self.loadFile(strInp)
        self.checkNumberOfPlayer(self.game)
        self.createPlayer(self.game)
        self.play()


    # def loadFile(self, strGame):            #'3\n0 2c As 4d\n1 Kd 5h 6c\n2 Jc Jd 9s'   
    #     self.game = strGame.split('\\n')     #['3', '0 2c As 4d', '1 Kd 5h 6c', '2 Jc Jd 9s']
    #     # print(f'game: ', self.game)

    def checkNumberOfPlayer(self, lsGame):
        if len(lsGame) < 2:
            raise Exception("Game Rule: There must be at least one player.")
        elif len(lsGame) > 24:
            raise Exception("Game Rule: No more than 23 players are allowed.")

    def createPlayer(self, lsGame):     
        numOfPlayer = int(lsGame[0])
        # print(f'numOfPlayer: ', numOfPlayer)

        for i in range(1, numOfPlayer+1):
            # print('2',lsGame)
            playersCard = lsGame[i].split()  #['0', 'Kh', '4d', '3c']
            currPlayer = Player(playersCard)
            self.players[currPlayer.id] = currPlayer.hand.calcScore()

        # Now I created all the players and their hands with scores!
        # print(self.players)
        # # self.player{}
        # {
        #     '0': 120502
        #     '1': 
        #     '2': 
        #     '3': 
        #     '4': 
        #     '5': 
        #     '6': 
        # }

    def play(self): #findWinner
        maxScore = max(self.players.values())
        
        for playerId, playerScore in self.players.items():
            if( playerScore == maxScore):
                self.winner.append(playerId)

        print(" ".join(self.winner))
        return " ".join(self.winner)


# game1 = Game("03")
# Game('3\n0 2c As 4d\n1 Kd 5h 6c\n2 Jc Jd 9s')
# game2 = Game('3\n0 Kh 4d 3c\n1 Jd 5c 7s\n2 9s 3h 2d')
# game3 = Game('6\n0 Kd 5h 6c\n1 Jd 5c 7s\n2 8s 2h 2d\n3 6s 4h 3s\n4 5c 5d 4s\n5 4h 5s 5c')
# 3\n0 2c As 4d\n1 Kd 5h 6c\n2 Jc Jd 9s


def main(strInput):
    # print('run main strInput')
    # print('1',strInput)
    Game(strInput)

if __name__ == "__main__":
    # print('--main--')
    main(sys.stdin.read().split('\n'))      #['3', '0 2c As 4d', '1 Kd 5h 6c', '2 Jc Jd 9s']
    # print(sys.stdin.readlines())          #['3\n', '0 2c As 4d\n', '1 Kd 5h 6c\n', '2 Jc Jd 9s']
    # for line in sys.stdin:
    #     print(f'M43Poker')
    #     print(line)
    #     main(line)

# # test successful
# # python3 ./test.py 'python3 M43Poker.py'
# # 3
# # \n
# # 0 2c As 4d
# # \n
# # 1 Kd 5h 6c
# # \n
# # 2 Jc Jd 9s
