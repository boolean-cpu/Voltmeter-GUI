from flask import Flask, send_from_directory, Response
import time

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/index.html')
def static_files(path):
    return send_from_directory('.', path)

@app.route('/voltage-stream')
def voltage_stream():
    def generate():
        while True:
            voltage = read_last_line('web_log.log')
            yield f"data: {voltage}\n\n"
            time.sleep(1)  # Check for new data every second

    return Response(generate(), mimetype='text/event-stream')

def read_last_line(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if lines:
                return lines[-1].strip()
            else:
                return "0.00"  # Default value if file is empty
    except FileNotFoundError:
        return "0.00"  # Default value if file doesn't exist

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
