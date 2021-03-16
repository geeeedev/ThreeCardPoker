# run: cd to folder, then `python3 200.highLevel.py`

# input file: get number of player





# Card obj
# - rank:
# - suit:

class Card:
    # def __init__(self, rank, suit):
    #     self.value = self.findVal(rank)  #=self.findVal(strCard[0])
    #     self.suit = suit                 #=strCard[1]

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

    def __repr__(self):         #printing the card object in string form
        return f"{self.value} of {self.suit}"



class Hand:

    def __init__(self, threeCards):   #['2c', 'As', '4d']
        self.handOfThree = []
        # self.allSuits = []
        self.sortedSuits = []
        # self.allValues = []
        self.sortedValues = []
        self.handScore = 0

        for item in threeCards:
            self.handOfThree.append(Card(item))     #[cardObj1, cardObj2, cardObj3]

        self.getAllSuit()
        self.getAllValue()

    def getAllSuit(self):
        for card in self.handOfThree:               #[cardObj1, cardObj2, cardObj3]
            self.sortedSuits.append(card.suit)      #['c','s','d']
        print(self.sortedSuits) #before-sorted      #Suits dont need sorting really!
        self.sortedSuits.sort()                     #sorting suit for my own testing convenience
        # self.sortedSuits = sorted(self.allSuits)
        print(self.sortedSuits)                     #['c','d','s']
        # list.sort() - sort in place

    def getAllValue(self):
        for card in self.handOfThree:               #[{card1},{card2},{card3}]
            self.sortedValues.append(card.value)    #['2','1','4']
        print(self.sortedValues) #before-sorted
        self.sortedValues.sort()
        # self.sortedValues = sorted(self.allValues)
        print(self.sortedValues)                    #['1','2','4']
        # list.sort() - sort in place


    def isStraightFlush(self):
        if self.isStraight() and self.isFlush():
            print(f'isStraightFlush: True')
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
        if self.sortedValues.count(self.sortedValues[0]) == 3:
            return True
        else:
            return False

    def isStraight(self):
        # Rank in a run
        # low, low+1, low+2
        # Q-K-A ok-highest, A as 14
        # 9-T-J ok
        # A-2-3 ok-lowest ------(2,3,14)
        # K-A-2 X Nope -----(2,13,14)
        lowestCard = min(self.sortedValues)
        print(lowestCard, self.sortedValues)
        if (self.sortedValues[0] == lowestCard and self.sortedValues[1] == lowestCard+1 and self.sortedValues[2] == lowestCard+2):
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
        if self.sortedSuits.count(self.sortedSuits[0]) == 3:
            return True
        else:
            return False

    def isPair(self):
        # two same rank ###, one is diff
        # 4c 4d 5h
        if self.sortedValues.count(self.sortedValues[1]) == 2:
            return True
        else:
            return False

    def isHighCard(self):
        #none of the above
        if not(self.isStraightFlush()) and not(self.isThreeOfKind()) and not(self.isStraight()) and not(self.isFlush()) and not(self.isPair()):
            return True
        else:
            return False

        # ... 
        # one highest ranked card 
        # Ah > Qd

    def findHandType(self):
        if self.isStraightFlush():  #500
            return 'StraightFlush'
        elif self.isThreeOfKind(): #400
            return 'ThreeOfKind'
        elif self.isStraight(): #300
            return 'Straight'
        elif self.isFlush(): #200
            return 'Flush'
        elif self.isPair(): #100
            return 'Pair'
        elif self.isHighCard(): #0
            return 'HighCard'
        else:
            return 'None: Something IS wrong!'

    def getScore(self):
        if self.isStraightFlush():  #500
            self.handScore = 5000000
            print(f'StraightFlush',self.handScore)
        elif self.isThreeOfKind(): #400
            self.handScore = 4000000
            print(f'ThreeOfKind',self.handScore)
        elif self.isStraight(): #300
            self.handScore = 3000000
            print(f'Straight',self.handScore)
        elif self.isFlush(): #200
            self.handScore = 2000000
            print(f'Flush',self.handScore)
        elif self.isPair(): #100
            self.handScore = 1000000
            print(f'Pair',self.handScore)
        elif self.isHighCard(): #0
            self.handScore = 0
            print(f'HighCard',self.handScore)
        else:
            self.handScore = 0
            print(f'None: Something IS wrong!',self.handScore)

        self.handScore += self.sortedValues[2]*10000
        self.handScore += self.sortedValues[1]*100
        self.handScore += self.sortedValues[0]

        return self.handScore


# create player - loop through based on n number of player
# capture inputStr.split() >> [id#, card1, card2, card3]
# inputStr[0] >> id
# inputStr[1] >> create card{}
# inputStr[2] >> create card{}      # create player.hand = Hand([x,x,x])
# inputStr[3] >> create card{}

# classes
# Player obj 
# - plyr1.id
# - plyr1.cards - [{rS},{rS},{rS}]
# - plyr1.hand -> score
#     ** hand is an obj/class,
#     - methods to eval which hand it is
#     - method to calc/give score
# - plyr1.score

# player >> hand

class Player:
    def __init__(self, id, hand):
        self.id = id
        self.hand = ""



# Game obj
# - load file
# - load/create players
# - play() 
#     - get player scores
#     - compare scores

# 0 2c As 4d

class Game:
    def __init__(self):
        
        self.loadFile(fPath)

    def loadFile(self, filepath):           ## filepath??
        with open(filepath) as file:            ## filepath??
            game = file.readlines()[2:-2]
            print(f'game: ', game)
        
        NumOfPlayer = int(game[0].rstrip('\n'))
        print(f'game: ', game)



#### WORKING - file loading in as ['0', 'Kh', '4d', '3c']

def loadFile(filepath):
    with open(filepath) as file:
        game = file.readlines()[2:-2]  #readlines() read into a List, skip first and last two lines
    
    print(f'game:', game)
    # game: ['3\n', '0 2c As 4d\n', '1 Kd 5h 6c\n', '2 Jc Jd 9s\n']
    NumOfPlayer = int(game[0].rstrip('\n'))
    print(f'NumOfPlayer: {NumOfPlayer}')
    for i in range(1,NumOfPlayer+1):
        plyrCard = game[i].rstrip("\n").split()
        print(f'plyrCard: {plyrCard}')

filepath = '02'
loadFile(filepath)


# plyrNum: 3
# plyrCard: ['0', '2c', 'As', '4d']
# plyrCard: ['1', 'Kd', '5h', '6c']
# plyrCard: ['2', 'Jc', 'Jd', '9s']

#########################################################################################




