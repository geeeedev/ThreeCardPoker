###############################################################################
### research as I code along
### below is code I end up NOT using but learned
### arranged oldest (top) first to latest (bottom)
### review and note later/after



## file = open("01")        # using `with` has better clean up
# with open("01") as file:
#     for i in range(2):
#         file.readline()  # read this line return to none and move next
#     for line in file:
#         if len(line.strip()) > 0 and len(line) < 3:
#             plyrNum = line
#             print(f'Total Players: {line}')
#         if len(line.strip()) > 2:
#             plyr = line.split()
#             print(plyr)


# game = file.read()        # read all lines and output as-is
# game = file.readlines()   # read whole file into a list/array
# ['Pair beats high cards\n', '\n', '3\n', '0 2c As 4d\n', '1 Kd 5h 6c\n', '2 Jc Jd 9s\n', '\n', '2\n']
# str.rstrip('\n')
# game = file.readlines()[:-2]  # skip last two elements
# game = file.readlines()[2:-2]  # skip first two and last two elements



# with open("01") as file:
#     game = file.readlines()[2:-2]  #read into a List, skip first and last two lines
#     print(f'game: {game}')
#     # game: ['3\n', '0 2c As 4d\n', '1 Kd 5h 6c\n', '2 Jc Jd 9s\n']
#     plyrNum = game[0].rstrip('\n')
#     plyr1Cards = game[1].rstrip('\n').split()
#     plyr2Cards = game[2].rstrip('\n').split()
#     plyr3Cards = game[3].rstrip('\n').split()
#     print(f'plyrNum: {plyrNum}')
#     print(f'plyr1Cards: {plyr1Cards}')
#     print(f'plyr2Cards: {plyr2Cards}')
#     print(f'plyr3Cards: {plyr3Cards}')


#### WORKING - file loading in as ['0', 'Kh', '4d', '3c']
# with open("01") as file:
#     game = file.readlines()[2:-2]  #read into a List, skip first and last two lines
#     print(f'game: {game}')
#     # game: ['3\n', '0 2c As 4d\n', '1 Kd 5h 6c\n', '2 Jc Jd 9s\n']
#     plyrNum = int(game[0].rstrip('\n'))
#     print(f'plyrNum: {plyrNum}')

#     for i in range(1,plyrNum+1):
#         plyrCard = game[i].rstrip("\n").split()
#         print(f'plyrCard: {plyrCard}')

# output: 
# plyrNum: 3
# plyrCard: ['0', '2c', 'As', '4d']
# plyrCard: ['1', 'Kd', '5h', '6c']
# plyrCard: ['2', 'Jc', 'Jd', '9s']


# https://realpython.com/python-main-function/
# __name__ == "__main__"
# __name__ == "__main__" when Python interpreter (python3) is directly executing 
#                         your .py file as a script from the command line and NOT importing it
#                         or with python -m (to execute a package’s __main__.py file)
# __name__ == "<name of .py file>" when you IMPORT to run your .py file

# so we can use __name__ to check and control the execution of our code
# - want to execute when running the script from the command line but not when it is imported!

# if __name__ == "__main__":      #determine the execution context
#     runSomeMethod()             #conditonally run only if True

# https://realpython.com/python-main-function/
# main() entry point function

# other languages C, C++, C#, Java, etc. have main() as the entry point function.
# This special function must be named main() so that an operating system automatically calls
# when it executes the compiled program.  
# entry point: because it is where execution enters the program

# Python, however, does not have such restriction. YOu can give the entry point 
# function in a Python script any name you desire!
# Still, it is best practice to name the entry point function in Python main().
# That said, main() should contain any code you want to run when the Python
# interpreter (python3) executes the file


# def main():
#     print(__name__)

# if __name__ == "__main__":
#     main()

# Run these in Python interpreter (after you access Python3 and see the >>> activated)
# >>> import subprocess
# >>> subprocess.check_output(['python3','<<fileName with the main() in it>>.py'], universal_newlines=True, input=inp).strip()
# '__main__' should be the output printed - GOOD RESULT


# ###Another full example:
#  1 from time import sleep
#  2
#  3 print("This is my file to demonstrate best practices.")
#  4
#  5 def process_data(data):
#  6    print("Beginning data processing...")
#  7    modified_data = data + " that has been modified"
#  8    sleep(3)
#  9    print("Data processing finished.")
# 10    return modified_data
# 11
# 12 def main():
# 13    data = "My data read from the Web"
# 14    print(data)
# 15    modified_data = process_data(data)
# 16    print(modified_data)
# 17
# 18 if __name__ == "__main__":
# 19    main()



# subprocess.check_output(sys.argv[1].split(), universal_newlines=True, input=InputDataString).strip()
# ...                    (['python3','runFilename.py'], uni...
# ...
# import sys                                        #using sys.stdin to receive subprocess's file input
#
#
# def main(strInput):
#     Game(strInput)

# if __name__ == "__main__":
#     main(sys.stdin.read().split('\n'))            #['3', '0 2c As 4d', '1 Kd 5h 6c', '2 Jc Jd 9s']




# sortedValues.sort(reverse=True)

# ['0', 'Kh', '4d', '3c']
# winner = ['0', '24', '27', '3']
# print(" ".join(sorted(winner))) 
# above does NOT sort string, will have to convert to number for sorting then back to string to print


# import sys

# game = ['3', '0 2c As 4d', '1 Kd 5h 6c', '2 Jc Jd 9s']

# print(len(game), file=sys.stderr)     # print as system standard error
# print(len(game))


# if len(game) > 3:                     # throw an exception
#     raise Exception("No more than 23 players are allowed")

# strSuit = 'H'
# strRank = '1'
# def findVal(strRank):
#     rankConversion = {
#         '2':2,
#         '3':3,
#         '4':4,
#         '5':5,
#         '6':6,
#         '7':7,
#         '8':8,
#         '9':9,
#         'T':10,
#         'J':11,
#         'Q':12,
#         'K':13,
#         'A':14,
#     }
#     print(rankConversion.keys())
#     if strRank in rankConversion.keys():
#         return rankConversion.get(strRank)
#     else:
#         raise Exception(f'Game Rule: {strRank} is not a valid rank!')

# def findSuit(strSuit):
#     if strSuit in ['h','d','s','c']:
#         return strSuit
#     else:
#         raise Exception(f'Game Rule: {strSuit} is not a valid suit!')


# print(findVal(strRank))
# print(findSuit(strSuit))

players = {"0":0,"1":1,"3":3,"5":5}
playersCard = ['3', 'Kh', '4d', '3c']
print(playersCard[0])
if playersCard[0] not in players:
    print('new player')
else:
    print('player exits')
    # players[newPlayer.id] = newPlayer.hand.calcScore()