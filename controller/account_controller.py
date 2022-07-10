from flask import Blueprint, request
from exception.customer_not_found import CustomerNotFoundError
from exception.account_not_found import AccountNotFoundError


from model.account import Account
from service.account_service import AccountService
from service.customer_service import CustomerService


ac = Blueprint('account_service', __name__)


customer_service = CustomerService()
account_service = AccountService()

@ac.route('/customers/<customer_id>/accounts')
def get_all_accounts_by_customer_id(customer_id):
    amount_gt = request.args.get('amountGreaterThan')
    amount_lt = request.args.get('amountLessThan')

    try:
        return {
            "accounts": account_service.get_all_accounts_by_customer_id(customer_id, amount_gt, amount_lt)
        }, 200
    except CustomerNotFoundError as e:
            return {
            "message" : str(e)
        }, 404






@ac.route('/customers/<customer_id>/accounts/<account_id>')
def get_accounts_by_customer_id_and_account_id(customer_id, account_id):
    try:
        return {
            "accounts": account_service.get_account_by_account_id(account_id)
        }


    except AccountNotFoundError as e:
        return {
            "message": str(e)
        }, 404


@ac.route('/customers/<customer_id>/accounts', methods=['POST'])
def add_account_by_customer_id(customer_id):
    account_json_dictionary = request.get_json()
    account_object = Account(None, account_json_dictionary['account'],
                              account_json_dictionary['balance'], customer_id)
    try:
        return account_service.add_account_by_customer_id(account_object, customer_id), 201
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404
    except AccountNotFoundError as e:
        return {
            "message": str(e)
        }, 404
#

@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['PUT'])
def update_account_by_customer_id_and_account_id(customer_id, account_id):
    try:
        json_dictionary = request.get_json()
        return {
            "accounts": account_service.update_account_by_customer_id_and_account_id(Account(customer_id,
                                                                                             json_dictionary['account'],
                                                                         json_dictionary['balance'], account_id))
        }

    except AccountNotFoundError as e:
        return {
            "message": str(e)
        }, 404
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }
#
@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['DELETE'])
def delete_customer_account_by_account_id(customer_id, account_id):
        try:
            account_service.delete_customer_account_by_account_id(customer_id,account_id)
            return {
                "message": f"Account with id {account_id} associated with customer id {customer_id} deleted successfully"
            }
        except CustomerNotFoundError as e:
            return {
                       "message": str(e)
                   }, 404
        except AccountNotFoundError as e:
            return {
                "messager": str(e)
            }, 404