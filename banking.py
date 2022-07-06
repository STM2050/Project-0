from flask import Flask
from controller.customer_controller import cc
from controller.account_controller import ac

if __name__ == '__main__':
    banking = Flask(__name__)

    banking.register_blueprint(cc)
    banking.register_blueprint(ac)

    banking.run(port=8080, debug=True)
