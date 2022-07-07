from dao.account_dao import AccountDao
from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError
from exception.account_not_found import AccountNotFoundError
class AccountService:

    def __init__(self):

        self.account_dao = AccountDao()
        self.customer_dao = CustomerDao()

    def get_all_accounts_by_customer_id(self, customer_id):

        # print(query_1.to_dict())
        # if self.customer_dao.get_customer_by_id(customer_id) is None:
        #     raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        #if query_1 is None and query_2 is None:
            #return list(map(lambda a:a.to_dict(), self.account_dao.get_all_accounts_customer_by_id(customer_id)))

        #elif query_1 is not None and query_2 is not None:
            # return list(map(lambda a: a.to_dict, self.account_dao.get_all_between_by_customer_id(customer_id,
            #                                                                                      query_1,
            #                                                                                      query_2)))


        # elif query_1 is not None:
        #     return list(map(lambda a: a.to_dict, self.account_dao.get_all_accounts_greater_by_customer_id(customer_id,
        #                                                                                                   query_1,
        #                                                                                                   query_2)))

        #elif query_2 is not None:
            # return list(map(lambda a: a.to_dict(self.account_dao.get_all_accounts_less_by_customer_id(customer_id,
            #                                                                                           query_1
            #                                                                                           query_2))))

        #else:
            #return []

        return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_customer_id(customer_id)))





    def get_account_by_customer_id_and_account_id(self, customer_id, account_id):
        if self.account_dao.get_account_by_customer_id(customer_id,) is None:

            if self.account_dao.get_account_by_account_id(account_id,) is None:

                raise AccountNotFoundError(f"Customer with id {customer_id} does not have account with id {account_id} ")

        return list(map(lambda a: a.to_dict(), self.account_dao.get_all_accounts_by_customer_id(customer_id),
                        self.account_dao.get_account_by_account_id(account_id)))