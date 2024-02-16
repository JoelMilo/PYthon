import GameStore
import os.path
import re
import operator
import random
import optparse


def gameGenerator(num):
    """Our game generator which takes an argument number"""
    discount = random.randint(0, 100)
    if discount < 30:
        discount = 0
        """ we have set discounts lowers than 30 to 0 inorder for our generator to generate
        games which can only be bought"""
    return ("Game {}, Category {}, {}, {}, {}\n".format(num + 1,
                                                        num + 1,
                                                        random.randint(0, 70),
                                                        random.randint(0, 300),
                                                        discount))


parser = optparse.OptionParser('f <Filename>')
parser.add_option('-f', '--file', dest='filename', type='string')
(options, args) = parser.parse_args()
if options.filename:
    filename = options.filename
else:
    filename = "Games"

file = None  # string saving lines
all_lines = []  # list of saved lines
lines_read = 0  # number of lines saved(1 less because starts from 0)
myGamesToBuy = {}  # list of games that can be bought, objects to be created.
myGamesToRent = {}  # list of games that can be rented, objects to be created.
gamesNumber = 12
gamesToBuyNumber = 0
gamesToRentNumber = 0

if filename == 'Games':
    """will write to file our generated games in this case 12 games """
    f = open(filename + ".txt", "w")
    for i in range(gamesNumber):
        f.write(gameGenerator(i))
    f.close()

if os.path.isfile(filename + ".txt"):
    with open(filename + '.txt') as file:
        for line in file:
            # Assigning each line to all_lines and
            # stripping the file from '\n' chars at the end of each line.
            all_lines.append(line[:-1])
            lines_read += 1


pattern = re.compile('^([A-Za-z0-9 ]+),([A-Za-z0-9 ]+),([0-9 ]+),([0-9 ]+),([0-9 ]+)$')
for n in range(len(all_lines)):
    game = pattern.search(all_lines[n])
    if game:
        if game[5].strip() == '0':
            # create buy object with game strips
            myGamesToBuy[gamesToBuyNumber] = GameStore.Buy(game[1].strip(),
                                                           game[2].strip(),
                                                           float(game[3].strip()),
                                                           float(game[4].strip()),
                                                           float(game[5].strip()))
            gamesToBuyNumber += 1
        else:
            # create rent object with game strips.
            myGamesToRent[gamesToRentNumber] = GameStore.RentIt(game[1].strip(),
                                                                game[2].strip(),
                                                                float(game[3].strip()),
                                                                float(game[4].strip()),
                                                                float(game[5].strip()))
            gamesToRentNumber += 1
            pass

    else:
        print("You encountered some mistake in separation of each line.")


def getPrices(myGamesToBuyC, myGamesToRentC):
    prices = {}
    """dictionary to save our generated games after discount has been applied"""
    for n in range(len(myGamesToBuyC)):
        prices[n] = myGamesToBuyC[n].getNewPrice()
    for i in range(len(myGamesToRentC)):
        prices[len(myGamesToBuyC) + i] = myGamesToRentC[i].getNewPrice()
    return prices


def findHighestPrice(prices_list):
    """"sorts prices and returns highest"""
    sorted_prices = sorted(prices_list.items(), key=operator.itemgetter(1))
    return int(sorted_prices[len(sorted_prices) - 1][1])


def findLowestPrice(prices_list):
    """sorts prices and returns lowest"""
    sorted_prices = sorted(prices_list.items(), key=operator.itemgetter(1))
    return int(sorted_prices[0][1])


prices = getPrices(myGamesToBuy, myGamesToRent)
print("Highest price game after discount: {}".format(findHighestPrice(prices)))
print("Lowest price game after discount: {}".format(findLowestPrice(prices)))
with open("Games.txt", "r") as f:
    list = []
    for line in f:
        list.append(line[0:-1].split(","))
        list.sort(key=lambda x: int(x[3]))  # sorts games based on price from lowest to highest
    print(*list, sep="\n")