from flask import Blueprint, request
from exception.customer_not_found import CustomerNotFoundError
from exception.account_not_found import AccountNotFoundError
from model.customer import Customer
from model.account import Account
from service.account_service import AccountService
from service.customer_service import CustomerService

ac = Blueprint('account_service', __name__)


customer_service = CustomerService()
account_service = AccountService()

@ac.route('/customers/<customer_id>/accounts')
def get_all_accounts_by_customer_id(customer_id):
    # info = request.args
    # amount_gt = info.get('amountGreaterThan')
    # # amount-lt = info.get()
    try:
        return {
            "accounts": account_service.get_all_accounts_by_customer_id(customer_id)
        }, 200
    except CustomerNotFoundError as e:
        return{
            "message" : str(e)
        }



@ac.route('/customers/<customer_id>/accounts/<account_id>')
def get_account_by_customer_id_and_account_id(customer_id, account_id):
    try:
        return customer_service.get_customer_by_id(customer_id), \
               account_service.get_account_by_id(account_id)
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404
    except AccountNotFoundError as e:
        return {
            "message": str(e)
        }, 404


@ac.route('/cusomters/<customer_id>/accounts', methods=['POST'])
def add_account_for_customer_by_customer_id(customer_id):
    customer_id_json_dictionary = request.get_json()
    customer_id_object = Customer(customer_id, customer_id_json_dictionary['account'],None)
    try:
        return customer_service.add_account_for_customer_by_customer_id(customer_id_object), 201
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 400

@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['PUT'])
def edit_account_by_customer_id_and_account_id(customer_id, account_id):
    try:

        return customer_service.edit_account_by_customer_id(customer_id),\
               account_service.edit_account_by_account_id(account_id)
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404
    except AccountNotFoundError as e:
        return {
            "message": str(e)
        }

@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['DELETE'])
def delete_account_by_customer_id_and_account_id(customer_id, account_id):
    try:
        customer_service.delete_customer_by_id(customer_id), account_service.delete_account_by_id(account_id)
        return {
            "message": f"Customer with id {customer_id} and account with id {account_id}  was deleted succefully"
        }
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404
    except AccountNotFoundError as e:
        return{
            "message": str(e)
        }, 404