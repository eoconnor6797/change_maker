import unittest

def change_making(amount, denominations):
    min_coins = {} #dict of value to min coins used to make value
    #skips double for-loop if given amount is one of the coin denominations
    if amount in denominations:
        return 1

    # for every amount up to amount given find min number of coins
    for ii in range(amount + 1):
        coin_added = ii in denominations # boolean to make sure amount is a valid number made from combinations of denominations
        min_coins[ii] = (0, coin_added)
        change = ii # current amount we are calculating min number of coins for

        for jj in denominations:# for every denomination of coins
            if not (jj > ii): # other than ones larger than the current amount
                if min_coins[ii - jj][0] + 1 < change and (min_coins[ii - jj][1] or jj == ii): # check if min coins for (current amount - current denomination) + 1
                    # is less than current number of coins for this amount
                    change = min_coins[ii - jj][0] + 1 # if yes update current min coins for given amount
                    coin_added = True
            min_coins[ii] = (change, coin_added)
    least_number_of_coins = min_coins[amount][0] # return value
    return least_number_of_coins

class Testchange_making(unittest.TestCase): # tests


    def testChange0(self):
        self.assertEqual(change_making(6, [1,3,4]), 2)

    def testChange1(self):
        self.assertEqual(change_making(6, [1,4,3]), 2)

    def testChange2(self):
        self.assertEqual(change_making(42, [1,4,2,7,8,9,33]), 2)

    def testChange3(self):
        self.assertEqual(change_making(42, [1,4,2,7,8,9,42]), 1)

    def testChange4(self):
        self.assertEqual(change_making(100, [4,2,7,8,9,33]), 6)

    def testChange5(self):
        self.assertEqual(change_making(255,[254, 5]), 51)

    def testChange6(self):
        self.assertEqual(change_making(10, [9,2]), 5)


unittest.main()
