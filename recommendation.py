from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# demo dataset
data = pd.DataFrame({
    'Date': pd.date_range(start='2022-01-01', end='2024-12-31', freq='D'),
    'Value': [100 + i * 10 if i % 30 != 0 else 200 for i in range(1096)]
})

# Preprocessing the data

@app.route('/recommendation', methods=['POST'])
def recommendation():
    req_data = request.get_json()

    if 'month' not in req_data:
        return jsonify({'error': 'Month not provided'}), 400

    month = req_data['month']

    # Filter data for the given month
    data_month = data[data['Date'].dt.month == month]

    # Perform analysis to identify trends or anomalies
    # checking if the median value is higher than average
    median_value = data_month['Value'].median()
    average_value = data['Value'].median()  # Using median instead of mean

    if median_value > average_value:
        recommendation_text = "The median value for this month is higher than usual."
    else:
        recommendation_text = "No significant trend or anomaly detected for this month."

    return jsonify({'recommendation': recommendation_text})


if __name__ == '__main__':
    app.run(debug=True) 
