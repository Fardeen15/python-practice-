from flask import Flask, jsonify
from rest_framework.views import APIView
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/sum/<int:num>&&<int:num2>')
def sum(num,num2):
    add = num2 + num
    result ={
        "number":add
        } 
    return result


if __name__ == "__main__":
    app.run(debug=True)
