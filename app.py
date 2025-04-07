from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/mylotto')
def my_lotto():
    result = []
    while len(result) < 6:
        num = random.randint(1, 45)
        if num not in result:
            result.append(num)
    return jsonify(sorted(result))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

