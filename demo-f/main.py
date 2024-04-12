from flask import Flask, send_from_directory, request, jsonify
from server import CrimePredictor
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
app = Flask(__name__, static_url_path='/')
app.static_folder = 'dist'


@app.route('/')
def root():
    logging.info('serving the home page!')  # will not print anything
    return send_from_directory('dist', 'index.html')

@app.route('/health')
def health():
    logging.info('health check is called now~')  # will not print anything
    return "OK"


@app.route('/predict', methods=['POST'])
def predict():
    logging.info('serving the predictor')  # will not print anything
    try:
        data = request.json
        csv = data.get('csv')
        predict = CrimePredictor.predict(data.get('algorithm'), csv)
        return jsonify(predict)
    except ZeroDivisionError:
        return jsonify({"error": "unexpected error"})


if __name__ == '__main__':
    logging.info('=== STARTING CRIME RATE APPLICATION===')  # will not print anything
    app.run(host='0.0.0.0', port=80, debug=False)
