import yfinance as yf
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Render the form for capturing stock ticker and date range
    return render_template('./index.html')

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    # Get input data from the form
    ticker = ["AAPL"]
    start_date = "2018-12-31"
    end_date = "2023-12-31"
    benchmark = "^NDX"
    
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date, interval="1mo")['Adj Close']
        benchmark_data = yf.download(benchmark, start=start_date, end=end_date, interval="1mo")['Adj Close']
        
        data = {
            "stock_data": stock_data.to_dict(),
            "benchmark_data": benchmark_data.to_dict()
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
