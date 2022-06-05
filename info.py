from flask import Flask, request
import json
app = Flask(__name__)

@app.route('/info/', methods=['GET'])
def info():
    return json.dumps("Diego Andres Obin Rosales - 201903865")

if __name__ == '__main__':
    app.run(debug=True, port=4000)