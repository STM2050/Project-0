from dao.customer_dao import CustomerDao
from exception.customer_not_found import CustomerNotFoundError
from exception.customer_already_exists import CustomerAlreadyExistsError

class CustomerService:

    def __init__(self):
        self.customer_dao = CustomerDao()

    def get_all_customers(self):
        list_of_customer_objects = self.customer_dao.get_all_customers()

        return list(map(lambda x: x.to_dict(), list_of_customer_objects))

    def get_customer_by_id(self, customer_id):
        customer_obj = self.customer_dao.get_customer_by_id(customer_id)

        if not customer_obj:
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        return customer_obj.to_dict()

    def delete_customer_by_id(self, customer_id):
        if not self.customer_dao.delete_customer_by_id(customer_id):
            raise CustomerNotFoundError(f"Customer with id {customer_id} was not found")

        return None

    def add_customer(self, customer_object):
        if self.customer_dao.get_customer_by_customername(customer_object.customername) is not None:
            raise CustomerAlreadyExistsError(f"Customer with name {customer_object.customername} already exists")

        added_customer_object = self.customer_dao.add_customer(customer_object)
        return added_customer_object.to_dict()

    def update_customer_by_id(self, customer_object):
        updated_customer_object = self.customer_dao.update_customer_by_id(customer_object)

        if updated_customer_object is None:
            raise CustomerNotFoundError(f"Customer with id {customer_object.id} was not found")

        return updated_customer_object.to.dict()
