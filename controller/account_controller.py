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
    amount_gt = request.args.get('amountGreaterThan')
    amount_lt = request.args.get('amountLessThan')
    if amount_gt is not None and amount_lt is not None:
        pass
    elif amount_gt is not None and amount_lt is None:
        pass
    elif amount_gt is None and amount_lt is not None:
        pass
    else:
        try:
            return {
            "accounts": account_service.get_all_accounts_by_customer_id(customer_id)
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


@ac.route('/cusomters/<customer_id>/accounts', methods=['POST'])
def add_account_by_customer_id(customer_id):
    account_json_dictionary = request.get_json()
    account_object = Account(customer_id, account_json_dictionary['account'],
                              account_json_dictionary['balance'])
    try:
        return account_service.add_account_by_customer_id(account_object), 201
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
def delete_account_by_account_id(customer_id, account_id):
    try:

        return{
            "accounts": account_service.delete_account_by_account_id(account_id)
        }


        return
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404
    except AccountNotFoundError as e:
        return{
            "message": str(e)
        }, 404