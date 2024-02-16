import unittest
import main
from GameStore import Buy
from GameStore import RentIt


class Test(unittest.TestCase):
    def setUp(self):

        self.buy_1 = Buy("Game 1", "Category 1", 30, 75, 0)
        self.buy_2 = Buy("Game 2", "Category 2", 25, 40, 0)
        self.rent_1 = RentIt("Game 1", "Category 1", 20, 60, 20)
        self.rent_2 = RentIt("Game 2", "Category 2", 10, 27, 10)
        self.game1_getNewPrice = float(75) * 0.2
        self.game2_getNewPrice = float(40) * 0.2
        self.game3_getNewPrice = (float(60)) - (float(60*20*0.01))
        self.game4_getNewPrice = (float(27)) - (float(27*10*0.01))
        self.prices = {0: self.game1_getNewPrice,
                               1: self.game2_getNewPrice,
                               2: self.game3_getNewPrice,
                               3: self.game4_getNewPrice}
        self.myGamesToBuy = {0: self.buy_1, 1: self.buy_2}
        self.myGamesToRent = {0: self.rent_1, 1: self.rent_2}

    def test_house_generation(self):
        self.assertRegex(main.gameGenerator(1), '^([A-Za-z0-9 ]+),([A-Za-z0-9 ]+),([0-9 ]+),([0-9 ]+),([0-9 ]+)$')

    def test_get_prices(self):

        self.assertEqual(main.getPrices(self.myGamesToBuy, self.myGamesToRent), self.prices)

    def test_find_highest_price(self):
        self.assertEqual(main.findHighestPrice(self.prices), int(self.game3_getNewPrice))

    def test_find_lowest_price(self):
        self.assertEqual(main.findLowestPrice(self.prices), int(self.game2_getNewPrice))


if __name__ == '__main__':
    unittest.main()