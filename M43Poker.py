import sys



class Card:
    def __init__(self, strCard):
        self.value = self.findVal(strCard[0])  
        self.suit = self.findSuit(strCard[1])                 

    def findVal(self, strRank):
        rankConversion = {
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
        }
        if strRank in rankConversion.keys():        #validation: rank value
            return rankConversion.get(strRank)
        else:
            raise Exception(f'Game Rule: "{strRank}" is not a valid rank.')

    def findSuit(self, strSuit):
        if strSuit in ['h','d','s','c']:            #validation: suit value
            return strSuit
        else:
            raise Exception(f'Game Rule: "{strSuit}" is not a valid suit.')

    def __repr__(self):                             #printing Card object in string form
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

    def __repr__(self):                             #printing Hand object in string form
        return f'{self.handOfThree}'                


    def getAllSuits(self):                          
        for card in self.handOfThree:                   
            self.sortedSuits.append(card.suit)      #Not needed for logic, just sorting suit to be 
        self.sortedSuits.sort()                     #consistent and for my own testing convenience

    def getAllValues(self):
        for card in self.handOfThree:               
            self.sortedValues.append(card.value)    
        self.sortedValues.sort()                    


    def isStraightFlush(self):
        if self.isStraight() and self.isFlush():
            return True
        else:
            return False


    def isThreeOfKind(self):
        # Same Rank - 5d 5h 5s
        if self.sortedValues.count(self.sortedValues[0]) == 3:
            return True
        else:
            return False


    def isStraight(self):
        # Rank in a Run - 2s 3h 4c
        lowestCard = min(self.sortedValues)
        if (self.sortedValues[0] == lowestCard and 
            self.sortedValues[1] == lowestCard+1 and 
            self.sortedValues[2] == lowestCard+2):
            return True
        elif (self.sortedValues[0] == 2 and 
                self.sortedValues[1] == 3 and 
                self.sortedValues[2] == 14):
            return True
        else:
            return False


    def isFlush(self):
        # Same Suit - Ac 4c 8c
        if self.sortedSuits.count(self.sortedSuits[0]) == 3:
            return True
        else:
            return False


    def isPair(self):
        # 2 Same Rank - 8c 8d 5h
        if self.sortedValues.count(self.sortedValues[1]) == 2:
            if self.sortedValues.count(self.sortedValues[0]) == 1:
                self.kicker = self.sortedValues[0]
            else:
                self.kicker = self.sortedValues[2]
            return True
        else:
            return False


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
        else:
            self.handType = 'HighCard'


    def calcScore(self):
        if self.handType == 'StraightFlush':    
            self.handScore = 5000000
        elif self.handType == 'ThreeOfKind':    
            self.handScore = 4000000
        elif self.handType == 'Straight':       
            self.handScore = 3000000
        elif self.handType == 'Flush':          
            self.handScore = 2000000
        elif self.handType == 'Pair':           
            self.handScore = 1000000
        elif self.handType == 'HighCard':       
            self.handScore = 0

        if self.handType == 'Pair':
            self.handScore += self.sortedValues[1]*10000
            self.handScore += self.sortedValues[1]*100
            self.handScore += self.kicker
        else:
            self.handScore += self.sortedValues[2]*10000
            self.handScore += self.sortedValues[1]*100
            self.handScore += self.sortedValues[0]

        return self.handScore



class Player:
    def __init__(self, lsPlayersCard):              #['0', 'Kh', '4d', '3c']
        self.id = lsPlayersCard[0]
        self.hand = Hand(lsPlayersCard[1:])

    def __repr__(self):                             #printing Player object in string form
        return f'PlayerID: {self.id} | PlayerHand: {self.hand}'         
        # PlayerID: 0 | PlayerHand: [ # of suit, # of suit, # of suit ] 



class Game:
    def __init__(self, lsInput):
        self.game = lsInput                         #['3', '0 2c As 4d', '1 Kd 5h 6c', '2 Jc Jd 9s']
        self.players = {}           
        self.winner = []
        self.checkNumberOfPlayer(self.game)
        self.createPlayer(self.game)
        self.play()

    def checkNumberOfPlayer(self, lsGame):          #validation: number of players
        if len(lsGame) < 2:
            raise Exception("Game Rule: There must be at least one player.")
        elif len(lsGame) > 24:
            raise Exception("Game Rule: No more than 23 players are allowed.")

    def createPlayer(self, lsGame):     
        numOfPlayer = int(lsGame[0])

        for i in range(1, numOfPlayer+1):
            playersCard = lsGame[i].split()         #['0', 'Kh', '4d', '3c']
            if playersCard[0] not in self.players:  #validation: duplicate player id
                newPlayer = Player(playersCard)
                self.players[newPlayer.id] = newPlayer.hand.calcScore()
            else:
                raise Exception("Game Rule: Duplicate player id not allowed.")

        # Now created: all the players and their hands with scores!
        # self.player
        # {
        #     '0': 120502
        #     '1': 3120803
        #     '2': ...
        #     '3': 
        #     '4': 
        #     '5': 
        #     '6': 
        # }

    def play(self): 
        maxScore = max(self.players.values())
        
        for playerId, playerScore in self.players.items():
            if( playerScore == maxScore):
                self.winner.append(playerId)

        print(" ".join(self.winner))





def main(strInput):
    Game(strInput)

if __name__ == "__main__":
    main(sys.stdin.read().split('\n'))              #['3', '0 2c As 4d', '1 Kd 5h 6c', '2 Jc Jd 9s']

