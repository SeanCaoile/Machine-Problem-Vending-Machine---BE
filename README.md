# VENDING MACHINE API

 - Calculates the change for a given `bill` and `owed` amount and returns the denomination of bills based on the change.

## Endpoint

- Uses a **GET** Request using the query: `/calculate-change?bill=<amount>&owed=<amount>`
- Returns a json object which contains the status, status_code, and the calculated change in denominations (1000, 500, 200, 100, 50, 20)

## Query Parameters
- `bill`(int): The amount paid by the user. Must be one of the following: 20, 50, 100, 200, 500, or 1000.
- `owed`(int): The amount owed. Must be between 0 and 1000 and less than or equal to the `bill` amount 


### Sample Request
 - ```GET /calculate-change?bill=50&owed=23```
 - ```http://localhost:5000/calculate-change?bill=50&owed=23```

### Sample Response

```json
{
  "data": {
    "change": {
      "1": 2,
      "5": 1,
      "10": 0,
      "20": 1,
      "50": 0,
      "100": 0,
      "200": 0,
      "500": 0,
      "1000": 0
    }
  },
  "status": "success",
  "status_code": 200
}
```

### SETUP



### How to run the API
- In the console, navigate to the folder: Machine Problem Vending Machine - BE
- run: ```python app.py```
- use the sample request format show in the "Sample Request" section above

### How to run the test case checker
- In the console, navigate to the folder: Machine Problem Vending Machine - BE
- run:  ```python -m unittest test_app.py```



Clone the repository.
Navigate to the project folder.
Install dependencies: pip install -r requirements.txt.
Run the application: python app.py.
Access the endpoint at http://localhost:5000/api/change.
Run tests: python -m unittest test_app.py