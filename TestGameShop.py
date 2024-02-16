import unittest
from GameStore import GameShop
from GameStore import Buy
from GameStore import RentIt


class TestBuyRentIt(unittest.TestCase):
    def setUp(self):
        self.buy_1 = Buy("Game 1", "Category 1", 33, 75, 0)
        self.buy_2 = Buy("Game 2", "Category 2", 25, 40, 0)
        self.rent_1 = RentIt("Game 1", "Category 1", 20, 60, 20)
        self.rent_2 = RentIt("Game 2", "Category 2", 10, 27, 10)

    def test_getNewPrice(self):
        buy_price_1 = (float(self.buy_1.getPrice())*0.2)
        self.assertEqual(self.buy_1.getNewPrice(), float(75*0.2))
        self.assertEqual(self.buy_1.getNewPrice(), buy_price_1)

        buy_price_2 = (float(self.buy_2.getPrice()) * 0.2)
        self.assertEqual(self.buy_2.getNewPrice(), float(40 * 0.2))
        self.assertEqual(self.buy_2.getNewPrice(), buy_price_2)

        rent_price_1 = (float(self.rent_1.getPrice())-(float(self.rent_1.getNewPrice()))*(float(self.rent_1.getDiscount(
            ) * 0.01)))
        self.assertEqual(self.rent_1.getNewPrice(), (float(60) - (float(60) * (20 * 0.01))))
        self.assertEqual(self.rent_1.getNewPrice(), rent_price_1)

        rent_price_2 = (float(self.rent_2.getPrice())-(float(self.rent_2.getNewPrice()))*(float(self.rent_2.getDiscount(
        ) * 0.01)))
        self.assertEqual(self.rent_2.getNewPrice(), (float(27) - (float(27) * (10 * 0.01))))
        self.assertEqual(self.rent_2.getNewPrice(), rent_price_2)


if __name__ == '__main__':
    unittest.main()
