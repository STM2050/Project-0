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

    try:
        return {
            "accounts": account_service.get_all_accounts_by_customer_id(customer_id)
        }, 200
    except CustomerNotFoundError as e:
        return {
            "message" : str(e)
        }

    # balance_gt = request.args.get('balanceGreaterThan', None)
    # balance_lt = request.args.get('balanceLessThan', None)
    # if balance_lt('amountLessThan') is not None and balance_gt('amountGreaterthan') is not None:
    #     return list(map(lambda a: a.to_dict, self.account_dao.get_all_between_by_customer_id(customer_id,
    #                                                                                              query_1,
    #                                                                                              query_2)))
    # elif balance_lt('amountLessThan') is not None:
    #     pass
    #
    # elif balance_gt('amountGreaterThan') is not None:
    #     pass
    #
    # else:
    #     pass
    # return jsonify()


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
    customer_id_json_dictionary = request.get_json()
    customer_id_object = Customer(customer_id, customer_id_json_dictionary['account'],None)
    try:
        return customer_service.add_account_by_customer_id(customer_id_object), 201
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 400
#
@ac.route('/customers/<customer_id>/accounts/<account_id>', methods=['PUT'])
def update_account_by_customer_id_and_account_id(customer_id, account_id):
    try:
        ac_json_dictionary = request.get_json()
        return {
            "accounts": account_service.update_account_by_customer_id_and_account_id(account_id,
                                                                                     ac_json_dictionary["balance"],
                                                                                     customer_id,
                                                                                     ac_json_dictionary["account"])

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
        account_service.delete_account_by_account_id(customer_id, account_id)

        return {
            "message": f"Customer id {customer_id}  with account id {account_id}  was deleted succefully"
        }
    except CustomerNotFoundError as e:
        return {
            "message": str(e)
        }, 404
    except AccountNotFoundError as e:
        return{
            "message": str(e)
        }, 404