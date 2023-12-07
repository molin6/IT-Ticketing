from controllers import main_controller
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

main_controller.load_data_and_start_api()
