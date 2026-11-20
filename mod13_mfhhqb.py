import unittest
from datetime import datetime


class LearnTest(unittest.TestCase):

#symbol: capitalized: 1-7 aplha characters
    def test_symbol1(self):
        data = "GOOGL"

        #letters
        result = data.isalpha()
        self.assertEqual(result,True)

        #capitalized
        result = data.isupper()
        self.assertEqual(result,True)

        #1-7 lenght
        result = 1 <= len(data) <= 7
        self.assertEqual(result,True)


    def test_symbol2(self):

        #non alphabet
        data = "g00g1"
        result = data.isalpha()
        self.assertEqual(result,False)

        #not capital
        data = "googl"
        result = data.isupper()
        self.assertEqual(result,False)

        #not 1-7 in length
        data = "gooooooogl"
        result = 1 <= len(data) <= 7
        self.assertEqual(result,False)

#chart types: 1 numeric character, 1 or 2
    def test_chart1(self):
        #number
        data = "1"
        result = data.isdigit()
        self.assertEqual(result,True)

        #only 1 number 
        result = len(data) == 1
        self.assertEqual(result,True)

        #only 1 or 2
        result = data in ["1", "2"]
        self.assertEqual(result,True)

    def test_chart2(self):
        #letter
        data = "x"
        result = data.isdigit()
        self.assertEqual(result,False)

        #not either 1-2
        data = "21"
        result = len(data) == 1
        self.assertEqual(result,False)

        #not either 1 or 2
        data = "3"
        result = data in ["1", "2"]
        self.assertEqual(result,False)

# time series: 1 numeric character, 1-4
    def test_timeseries1(self):
        data = "3"

        #number
        result = data.isdigit()
        self.assertEqual(result,True)

        #only 1 number 
        result = len(data) == 1
        self.assertEqual(result,True)

        #only 1, 2, 3, or 4
        result = data in ["1", "2", "3", "4"]
        self.assertEqual(result,True)

    def test_timeseries2(self):
        #letter
        data = "y"
        result = data.isdigit()
        self.assertEqual(result,False)

        #not only 1 number 
        data = "1234"
        result = len(data) == 1
        self.assertEqual(result,False)

        #only 1, 2, 3, or 4
        data = "5"
        result = data in ["1", "2", "3", "4"]
        self.assertEqual(result,False)
    
# start date: date type YYYY-MM-DD
    def test_startdate1(self):
        data = "2021-09-14"
        result = datetime.strptime(data, "%Y-%m-%d")
        self.assertEqual(result, datetime(2021, 9, 14))

    def test_startdate2(self):
        data = "2021/09/14"
        with self.assertRaises(ValueError):
            result = datetime.strptime(data, "%Y-%m-%d")

# end date: date type YYYY-MM-DD
    def test_enddate1(self):
        data = "2022-09-14"

        result = datetime.strptime(data, "%Y-%m-%d")
        self.assertEqual(result, datetime(2022, 9, 14))

    def test_enddate2(self):
        data = "09-14-2022"
        with self.assertRaises(ValueError):
            result = datetime.strptime(data, "%Y-%m-%d")



if __name__ == "__main__":
    unittest.main()