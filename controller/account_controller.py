from flask import Blueprint, request
from exception.customer_not_found import CustomerNotFoundError
from model.customer import Customer
from model.account import Account
from service.account_service import AccountService
from service.customer_service import CustomerService

ac = Blueprint('account_service', __name__)


customer_service = CustomerService()
account_service = AccountService()

@ac.route('/customers/<customer_id>/accounts')
def get_all_accounts_by_customer_id(customer_id):
    info = request.args
    amount-gt = info.get('amountGreaterThan')
    amount-lt = info.get()
    try:
        return {
            "accounts": account_service.get_all_accounts_by_customer_id(customer_id, info)
        }, 200
    except CustomerNotFoundError as e:
        return{
            "message" : str(e)
        }



@ac.route('/customers/<customer_id>/accounts/<account_id>')
def get_account_by_customer_id_and_account_id(customer_id, account_id):
    pass


@ac.route('/cusomters/<customer_id>/accounts', methods=['POST'])
def add_account_for_customer_by_customer_id(cusomter_id):
    pass


@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['PUT'])
def edit_account_by_customer_id_and_account_id(customer_id, account_id):

    pass

@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['DELETE'])
def delete_account_by_customer_id_and_account_id(customer_id, account_id):
    pass