import unittest
from app import app

class ChangeApiTestCase(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_change_various_cases(self):
        test_cases = [
            {"bill": 50, "owed": 23, "expected_status": 200, "expected_change": {"20": 1, "5": 1, "1": 2}},
            
            # sample tests
            # success
            {"bill": 1000, "owed": 1, "expected_status": 200, "expected_change": {"500": 1, "200":2, "50":1,"20":2,"5":1,"1":4}},
            {"bill": 100, "owed": 27, "expected_status": 200, "expected_change": {"50": 1, "20":1, "1":3}},
            # fails
            {"bill": 0, "owed": 0, "expected_status": 400, "expected_error": "Bills must be 20,50,100,200,500,or 1000; Owed must be from 0 to 1000."},
            {"bill": 500, "owed": 600, "expected_status": 400, "expected_error": "Bill amount must be greater than owed amount."},
            {"bill": "bill", "owed": "owed", "expected_status": 400, "expected_error": "Invalid input. Please provide numeric values for 'bill' and 'owed'."},
            {"bill": -100, "owed": -50, "expected_status": 400, "expected_error": "Bills must be 20,50,100,200,500,or 1000; Owed must be from 0 to 1000."},
            
            
            # # other tests
            {"bill": 1001, "owed": 10, "expected_status": 400, "expected_error": "Bills must be 20,50,100,200,500,or 1000; Owed must be from 0 to 1000."},
            {"bill": 100, "owed": "owed", "expected_status": 400, "expected_error": "Invalid input. Please provide numeric values for 'bill' and 'owed'."},
            {"bill": "bill", "owed": 50, "expected_status": 400, "expected_error": "Invalid input. Please provide numeric values for 'bill' and 'owed'."},
            {"bill": 1000, "owed": 1001, "expected_status": 400, "expected_error": "Bill amount must be greater than owed amount."},
            {"bill": -100, "owed": 50, "expected_status": 400, "expected_error": "Bills must be 20,50,100,200,500,or 1000; Owed must be from 0 to 1000."},
            {"bill": 100, "owed": -50, "expected_status": 400, "expected_error": "Bills must be 20,50,100,200,500,or 1000; Owed must be from 0 to 1000."}
        ]

        for case in test_cases:
            with self.subTest(case=case):
                response = self.client.get(f"/calculate-change?bill={case['bill']}&owed={case['owed']}")
                data = response.get_json()
                
                self.assertEqual(response.status_code, case["expected_status"])

                if response.status_code == 200:
                    self.assertEqual(data["status"], "success")
                    for denom, count in case["expected_change"].items():
                        self.assertEqual(data["data"]["change"].get(str(denom)), count)
                else:
                    self.assertEqual(data["status"], "error")
                    self.assertEqual(data["message"], case["expected_error"])

if __name__ == '__main__':
    unittest.main()
