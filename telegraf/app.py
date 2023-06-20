from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def get_metrics():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent

    metrics = {
        'cpu_percent': cpu_percent,
        'memory_usage': memory_usage
    }

    return jsonify(metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

