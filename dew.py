import csv
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/customer-segmentation', methods=['GET'])
def customer_segmentation():
    orders = []
    customers = []

    # Read orders data from existing CSV file
    with open('sales_data_sample.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            orders.append(row)

    # Read customers data from existing CSV file
    with open('orders.csv.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customers.append(row)

    filtered_customers = []
    for order in orders:
        if int(order['YEAR_ID']) == 2003 and int(order['PRICEEACH']) > 5000 and order['COUNTRY'] in ['USA', 'France']:
            customer = next((c for c in customers if c['CONTACTLASTNAME'] == order['CONTACTLASTNAME']), None)
            if customer:
                filtered_customers.append(customer)
    return jsonify(filtered_customers)

if __name__ == '__main__':
    app.run(debug=True)
