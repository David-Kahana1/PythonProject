import unittest


class mutipleExample(unittest.TestCase):
    def setUp(self):
        print("into set up")
        self.num1 = 1
        self.num2 = 2

    def test_add(self):
        print("testing summery")

        assert self.num1 + self.num2 ==3, "The summery of 1 and 2 is not 3"

    def test_minus(self):
        print("testing diff")

        assert self.num1-self.num2==-1,"the diff of 4 and 1 is not 3"

    def test_multiple_with_error(self):
        num1=3
        num2= 2
        assert num1*num2==5, "The result of multiple action is not as expected"