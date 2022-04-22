
from flask import Flask
from flask_restful import Api
from flask_cors import CORS 

# employee



app = Flask(__name__)

CORS(app)
api = Api(app)

@app.route('/', methods=['GET'])
def home():
    return 'test'


if __name__ == '__main__':
    app.run(port=5000, debug=True)
