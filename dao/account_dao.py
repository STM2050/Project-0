import psycopg
from model.account import Account

class AccountDao:
    def get_all_accounts_by_customer_id(self, customer_id):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s", (customer_id,))

                account_list = []

                for row in cur:
                    account_list.append(Account(row[0], row[1], row[2], row [3]))

                return account_list


    def get_all_accounts_between_by_customer_id(self, customer_id, amount_gt, amount_lt):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                         password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s AND balance > %s AND balance < %s",
                        (customer_id, amount_gt, amount_lt))

                account_between_list = []

                for row in cur:
                    account_between_list.append(Account(row[0], row[1], row[2], row[3]))


                return account_between_list

    def get_all_accounts_by_greater_than(self, customer_id, amount_gt):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s AND balance > %s",
                            (customer_id, amount_gt))
                account_greater_list = []

                for row in cur:
                    account_greater_list.append(Account(row[0], row[1], row[2], row[3]))

                return account_greater_list

    def get_all_accounts_by_less_than(self, customer_id, amount_lt):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s AND balance < %s",
                            (customer_id, amount_lt))
                account_less_list = []

                for row in cur:
                    account_less_list.append(Account(row[0], row[1], row[2], row[3]))

                return account_less_list

    def get_account_by_account_id(self, account_id):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE id = %s", (account_id,))

                account_row = cur.fetchone()
                if not account_row:
                    return None

                a_id = account_row[0]
                account = account_row[1]
                balance = account_row[2]
                customer_id = account_row[3]

                return Account(a_id, account, balance, customer_id)


    def delete_customer_account_by_account_id(self, customer_id, account_id):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM accounts WHERE customer_id = %s AND id = %s",
                            (customer_id, account_id))

                rows_deleted = cur.rowcount

                if rows_deleted != 1:
                    return False
                else:
                    conn.commit()
                    return True

    def add_account_by_customer_id(self, account_object, customer_id):
        account_to_add = account_object.account
        balance_to_add = account_object.balance

        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO  accounts (account, balance, customer_id) VALUES (%s, %s, %s) RETURNING*", (account_to_add,
                                                                                                    balance_to_add,customer_id))

                account_row_that_was_just_inserted = cur.fetchone()

                conn.commit()

                return Account(account_row_that_was_just_inserted[0], account_row_that_was_just_inserted[1],
                               account_row_that_was_just_inserted[2], account_row_that_was_just_inserted[3])

    def update_account_by_customer_id_and_account_id(self, account_object):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE accounts SET account = %s, balance = %s WHERE customer_id = %s AND id = %s RETURNING*",
                            (account_object.account, account_object.balance, account_object.id,
                             account_object.customer_id))

                conn.commit()

                updated_account_row = cur.fetchone()

                if updated_account_row is None:
                    return None

                return Account(updated_account_row[0], updated_account_row[1],
                               updated_account_row[2], updated_account_row[3])

    # def get_account_by_account(self, account):
    #     with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
    #                          password="T@ti2019") as conn:
    #         with conn.cursor() as cur:
    #             cur.execute("SELECT * FROM accounts WHERE account = %s", (account,))
    #
    #             account_row = cur.fetchone()
    #
    #             if not account_row:
    #                 return None
    #
    #             a_id = account_row[0]
    #             account = account_row[1]
    #             balance = account_row[2]
    #             customer_id = account_row[3]
    #
    #             return Account(a_id, account, balance, customer_id)