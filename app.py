from flask import Flask, jsonify, request

app = Flask(__name__)

# different bill values
DENOMINATIONS = [1000, 500, 200, 100, 50, 20, 10, 5, 1]

def calculate_change(bill, owed):

    change_amount = bill - owed         # Change amount
    change_distribution = {denom: 0 for denom in DENOMINATIONS}     # set up mapping of count each change

    # Calculate change for each denomination
    for denom in DENOMINATIONS:
        count = int(change_amount // denom)
        change_distribution[denom] = count
        change_amount -= count * denom

    return change_distribution

@app.route('/calculate-change', methods=['GET'])
def get_change():
    try:
        # get parameters
        bill = float(request.args.get('bill'))
        owed = float(request.args.get('owed'))

        valid_bills = [20, 50, 100, 200, 500, 1000] # different bill values
        
        # Validate inputs
        if (bill not in valid_bills) or owed < 0:   
            return jsonify({
                "status": "error",
                "status_code": 400,
                "message": "Bills must be 20,50,100,200,500,or 1000; Owed must be from 0 to 1000."
            }), 400
            
        if bill < owed:                 
            return jsonify({
                "status": "error",
                "status_code": 400,
                "message": "Bill amount must be greater than owed amount."
            }), 400

        # run the function
        change_distribution = calculate_change(bill, owed)      # denomination mapping
        
        return jsonify({
            "status": "success",
            "status_code": 200,
            "data": {
                "change": change_distribution
            }
        }), 200

    except (TypeError, ValueError):
        return jsonify({
            "status": "error",
            "status_code": 400,
            "message": "Invalid input. Please provide numeric values for 'bill' and 'owed'."
        }), 400

if __name__ == "__main__":
    app.run(debug=True)
