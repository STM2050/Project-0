from dao.account_dao import AccountDao
from dao.customer_dao import CustomerDao
from exception.account_already_exists import AccountAlreadyExistsError
from exception.account_not_found import AccountNotFoundError
from exception.customer_not_found import CustomerNotFoundError
from exception.invalid_parameter import InvalidParameterError

class AccountService:

    def __init__(self):

        self.account_dao = AccountDao()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id):


        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")
        #
        # if query_1 is None and query_2 is None:
        #     return list(map(lambda a:a.to_dict(), self.account_dao.get_all_accounts_customer_by_id(customer_id)))
        #
        # elif query_1 is not None and query_2 is not None:
        #     return list(map(lambda a: a.to_dict, self.account_dao.get_all_between_by_customer_id(customer_id,
        #                                                                                          query_1,
        #                                                                                          query_2)))
        #
        #
        # elif query_1 is not None:
        #     return list(map(lambda a: a.to_dict, self.account_dao.get_all_accounts_greater_by_customer_id(customer_id,
        #                                                                                                   query_1,
        #                                                                                                   query_2)))
        #
        # elif query_2 is not None:
        #     return list(map(lambda a: a.to_dict(self.account_dao.get_all_accounts_less_by_customer_id(customer_id,
        #                                                                                               query_1
        #                                                                                               query_2))))

        # else:
        #     return []

        return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_customer_id(customer_id)))


    def get_account_by_account_id(self, account_id):
        account_obj = self.account_dao.get_account_by_account_id(account_id)

        if account_obj is None:
            raise AccountNotFoundError(f"Account with id {account_id} was not found")

        return account_obj.to_dict()


    def delete_account_by_account_id(self, account_id):
        if not self.account_dao.delete_account_by_account_id(account_id):
            raise AccountNotFoundError(f"Account with {account_id} was not found")

        return None


    def add_account(self, account_object):
        if " " in account_object.account:
            raise InvalidParameterError("Account name cannot contain spaces")

        if self.account_dao.get_account_by_account(account_object.account) is not None:
            raise AccountAlreadyExistsError(f"Account with name {account_object.account} already exists")

        added_account_object = self.account_dao.add_account(account_object)
        return added_account_object.to_dict()


    def update_account_by_customer_id_and_account_id(self, account_object):
        updated_acount_object = self.account_dao.update_account_by_customer_id_and_account_id(account_object)
        if updated_acount_object is None:
            raise AccountNotFoundError(f"Account with id {account_object.id} was not found")

        return updated_acount_object.to_dict()



