from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data representing orders and customers
orders = [
    {"order_id": 1, "customer_id": 1, "amount": 6000, "country": "USA", "year": 2003},
    {"order_id": 2, "customer_id": 2, "amount": 7000, "country": "France", "year": 2003},
    {"order_id": 3, "customer_id": 3, "amount": 4000, "country": "USA", "year": 2003},
    {"order_id": 4, "customer_id": 1, "amount": 8000, "country": "USA", "year": 2003},
    {"order_id": 5, "customer_id": 2, "amount": 6000, "country": "France", "year": 2003},
]

customers = [
    {"customer_id": 1, "name": "John Doe"},
    {"customer_id": 2, "name": "Jane Smith"},
    {"customer_id": 3, "name": "Alice Johnson"},
]

@app.route('/customer-segmentation', methods=['GET'])
def customer_segmentation():
    filtered_customers = []
    for order in orders:
        if order['year'] == 2003 and order['amount'] > 5000 and order['country'] in ['USA', 'France']:
            customer = next((c for c in customers if c['customer_id'] == order['customer_id']), None)
            if customer:
                filtered_customers.append(customer)
    return jsonify(filtered_customers)

if __name__ == '__main__':
    app.run(debug=True)
