from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5500,debug=True)