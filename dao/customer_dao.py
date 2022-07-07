from model.customer import Customer
import psycopg


class CustomerDao:

    def get_all_customers(self):

        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers")

                bank_list_of_customer_obj = []

                for customer in cur:
                    c_id = customer[0]
                    customername = customer[1]
                    active = customer[2]

                    bank_customer_obj = Customer(c_id, customername, active)
                    bank_list_of_customer_obj.append(bank_customer_obj)

                return bank_list_of_customer_obj

    def delete_customer_by_id(self, customer_id):
        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM customers WHERE id = %s", (customer_id,))

                rows_deleted = cur.rowcount

                if rows_deleted != 1:
                    return False
                else:
                    conn.commit()
                    return True

    def add_customer(self, customer_object):
        customername_to_add = customer_object.customername

        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO customers (customername) VALUES (%s) RETURNING *", (customername_to_add,))

                customer_row_inserted = cur.fetchone()

                conn.commit()

                return Customer(customer_row_inserted[0], customer_row_inserted[1],
                                customer_row_inserted[2])

    def get_customer_by_id(self, customer_id):

        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))

                customer_row = cur.fetchone()
                if not customer_row:
                    return None

                c_id = customer_row[0]
                customername = customer_row[1]
                active = customer_row[2]

                return Customer(c_id, customername, active)

    def update_customer_by_id(self, customer_object):

        with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                             password="T@ti2019") as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE customers SET customername = %s, active_customer = %s WHERE id = %s RETURNING *",
                            (customer_object.customername, customer_object.active, customer_object.id))

                conn.commit()

                updated_customer_row = cur.fetchone()
                if updated_customer_row is None:
                    return None

                return Customer(updated_customer_row[0], updated_customer_row[1],
                                updated_customer_row[2])

    def get_customer_by_customername(self, customername):
      with psycopg.connect(host="localhost", port="5432", dbname="postgres", user="postgres",
                                 password="T@ti2019") as conn:

          with conn.cursor() as cur:
                cur.execute("SELECT * FROM customers WHERE customername = %s", (customername,))

                customer_row = cur.fetchone()
                if not customer_row:
                    return None

                c_id = customer_row[0]
                customername = customer_row[1]
                active = customer_row[2]

                return Customer(c_id, customername, active)