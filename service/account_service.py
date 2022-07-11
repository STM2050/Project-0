from dao.account_dao import AccountDao
from dao.customer_dao import CustomerDao
from exception.account_not_found import AccountNotFoundError
from exception.customer_not_found import CustomerNotFoundError


class AccountService:

    def __init__(self):

        self.account_dao = AccountDao()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id, amount_gt, amount_lt):
        if self.customer_dao.get_customer_by_id(customer_id) is None:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        if amount_gt is None and amount_lt is None:
            return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_customer_id(customer_id)))
        elif amount_gt is not None and amount_lt is not None:
            return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_between_by_customer_id(customer_id,
                                                                                                    amount_gt, amount_lt)))
        elif amount_gt is not None and amount_lt is None:
            return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_greater_than(customer_id,
                                                                                                    amount_gt)))
        elif amount_gt is None and amount_lt is not None:
            return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_less_than(customer_id,
                                                                                                    amount_lt)))
        else:
            return[]
    def get_account_by_account_id(self, account_id):
        account_obj = self.account_dao.get_account_by_account_id(account_id)

        if account_obj is None:
            raise AccountNotFoundError(f"Account with id {account_id} was not found")

        return account_obj.to_dict()


    def delete_customer_account_by_account_id(self, customer_id, account_id):
        if not self.customer_dao.get_customer_by_id(customer_id):
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")
        if not self.account_dao.get_account_by_account_id(account_id):
            raise AccountNotFoundError(f"Accounte with id {account_id} was not found")

        return self.account_dao.delete_customer_account_by_account_id(customer_id, account_id)

    def add_account_by_customer_id(self, account_object, customer_id):
        if self.customer_dao.get_customer_by_id(account_object.customer_id) is None:
            raise CustomerNotFoundError(f"Customer with id {customer_id} not found")

        # if " " in account_object.account:
        #     raise InvalidParameterError("Account name cannot contain spaces")

        # if self.account_dao.get_account_by_account(account_object.account) is not None:
        #     raise AccountAlreadyExistsError(f"Account with name {account_object.account} already exists")

        added_account_object = self.account_dao.add_account_by_customer_id(account_object, customer_id)
        return added_account_object.to_dict()


    def update_account_by_customer_id_and_account_id(self, account_object):
        updated_acount_object = self.account_dao.update_account_by_customer_id_and_account_id(account_object)
        if updated_acount_object is None:
            raise AccountNotFoundError(f"Account with id {account_object.id} was not found")

        return updated_acount_object.to_dict()

