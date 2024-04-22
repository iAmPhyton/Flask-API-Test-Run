from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GENDERIZE_API_URL = "https://api.genderize.io/"

@app.route('/get_gender', methods=['POST'])
def get_gender():
    order_id = request.json.get('order_id')
    customer_name = get_customer_name(order_id)
    if customer_name:
        gender = predict_gender(customer_name)
        return jsonify({'gender': gender})
    else:
        return jsonify({'error': 'Customer name not found for the given order ID'}), 404

def get_customer_name(order_id):
    orders = {
        'order123': 'John',
        'order456': 'Emily'
    }
    return orders.get(order_id)

def predict_gender(name):
    response = requests.get(GENDERIZE_API_URL, params={'name': name})
    if response.status_code == 200:
        data = response.json()
        if 'gender' in data:
            return data['gender']
    return 'Unknown'

if __name__ == '__main__':
    app.run(debug=True)
