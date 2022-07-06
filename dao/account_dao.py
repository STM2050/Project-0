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

    def get_all_accounts_greater_by_customer_id(self, customer_id, query_value):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM accounts WHERE customer_id = %s and balance > %s", (customer_id, query_value))

                acc_g_list = []

                for row in cur:
                    acc_g_list.append(Account(row[0], row[1], row[2], row[3]))

                return acc_g_list

    #def get_all_accounts_less_by_customer_id(self, customer_id, value_2):
        #with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             #password="T@ti2019") as conn:
            #with conn.cursor() as cur:
               # cur.execute("SELECT * FROM accounts WHERE customer_id = %s and balance < %s", (customer_id, value_2))

                #account_list = []

                #for row in cur:
                    #account_list.append(Account(row[0], row[1], row[2], row[3]))

                #return account_list

    #def get_all_accounts_between_by_customer_id(self, customer_id, query_value1, query_value2):
        #with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             #password="T@ti2019") as conn:
            #with conn.cursor() as cur:
                #cur.execute("SELECT * FROM accounts WHERE customer_id = %s and balance BETWEEN %s AND %s",
                            #(customer_id,query_value1, query_value2))


                #acc_b_list = []

                #for row in cur:
                    #acc_b_list.append(Account(row[0], row[1], row[2], row[3]))

                #return acc_b_list