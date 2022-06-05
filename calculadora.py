from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/suma/', methods=['GET', 'POST'])
def suma():
    if request.method == 'POST':
        data = request.get_json()
        return json.dumps(data['num1'] + data['num2'])

if __name__ == '__main__':
    app.run(debug=True, port=3000)