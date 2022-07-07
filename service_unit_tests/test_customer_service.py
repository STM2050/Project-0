import pytest

from exception.customer_already_exists import CustomerAlreadyExistsError
from exception.customer_not_found import CustomerNotFoundError
from model.customer import Customer
from service.customer_service import CustomerService


def test_get_all_customers(mocker):

    def mock_get_all_customers(self):
        return [Customer(1,'test123',True), Customer(2, 'test123', False)]
    mocker.patch("dao.customer_dao.CustomerDao.get_all_customers", mock_get_all_customers)

    customer_service = CustomerService()

    actual = customer_service.get_all_customers()

    assert actual == [
        {
            "id": 1,
            "customername": "test123",
            "active": True
        },
        {
            "id": 2,
            "customername": "test123",
            "active": False
        }
    ]

def test_get_customer_by_id_positive(mocker):

    def mock_get_customer_by_id(self, customer_id):
        if customer_id == "1":
            return Customer(1, "test123", True)
        else:
            return None

    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)

    customer_service = CustomerService()

    actual = customer_service.get_customer_by_id("1")

    assert actual == {
        "id": 1,
        "customername": "test123",
        "active": True
    }

def test_get_customer_by_id_negative(mocker):

    def mock_get_customer_by_id(self, customer_id):
        if customer_id == "1":
            return Customer(1, "test123", True)
        else:
            return None
    mocker.patch('dao.customer_dao.CustomerDao.get_customer_by_id', mock_get_customer_by_id)

    customer_service = CustomerService()

    with pytest.raises(CustomerNotFoundError) as excinfo:
        actual = customer_service.get_customer_by_id("2000")

    assert str(excinfo.value) == "Customer with id 2000 was not found"

def test_delete_customer_by_id_positive(mocker):

    def mock_delete_customer_by_id(self, customer_id):
        if customer_id == "1":
            return True
        else:
            return False

    mocker.patch('dao.customer_dao.CustomerDao.delete_customer_by_id', mock_delete_customer_by_id)

    customer_service = CustomerService()

    actual = customer_service.delete_customer_by_id("1")

    assert actual is None

def test_delete_customer_by_id_negative(mocker):

    def mock_delete_customer_by_id(self, customer_id):
        if customer_id == "1":
            return True
        else:
            return False

    mocker.patch("dao.customer_dao.CustomerDao.delete_customer_by_id", mock_delete_customer_by_id)

    customer_service = CustomerService()

    with pytest.raises(CustomerNotFoundError) as excinfo:
        customer_service.delete_customer_by_id("305")

    assert str(excinfo.value) == "Customer with id 305 was not found"

def test_add_customer_postive(mocker):

    def mock_get_customer_by_customername(self, customername):
        if customername == "Reed, Arthur":
            return None

    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_customername", mock_get_customer_by_customername)

    customer_object_to_add = Customer(None, "Reed, Arthur", None)

    def mock_add_customer(self, customer_object):
        if customer_object == customer_object_to_add:
            return Customer(1, "Reed, Arthur", True)
        else:
            return None

    mocker.patch("dao.customer_dao.CustomerDao.add_customer", mock_add_customer)

    customer_service = CustomerService()

    actual = customer_service.add_customer(customer_object_to_add)

    assert actual == {
        "id": 1,
        "customername": "Reed, Arthur",
        "active": True
    }

def test_add_customer_negative_customername_already_exists(mocker):
    customer_object_to_add = Customer(None, "DuPointe, Xander", None)

    def mock_get_customer_by_customername(self, customername):
        if customername == "DuPointe, Xander":
            return Customer(1, "DuPointe, Xander", False)

    mocker.patch("dao.customer_dao.CustomerDao.get_customer_by_customername", mock_get_customer_by_customername)

    customer_service = CustomerService()

    with pytest.raises(CustomerAlreadyExistsError) as excinfo:
        actual = customer_service.add_customer(customer_object_to_add)

    assert str(excinfo.value) == "Customer with name DuPointe, Xander already exists"

def test_update_customer_by_id_positive(mocker):

    updated_customer_object = Customer(10, "DuPointe, Xander", False)

    def mock_updated_cusomter_by_id(self, customer_object):
        if customer_object.id == 10:
            return Customer(10, "DuPointe, Xander", False)
        else:
            return None

    mocker.patch("dao.customer.CustomerDao.update_customer_by_id", mock_updated_cusomter_by_id)

    customer_service = CustomerService()

    actual = customer_service.update_customer_by_id(updated_customer_object)

    assert actual == {
        "id": 10,
        "customername": "DuPointe, Xander",
        "active": False
    }

def test_update_customer_by_id_negative(mocker):

    updated_customer_object = Customer(100, "DuPointe, Xander", False)

    def mock_updated_cusomter_by_id(self, customer_object):
        if customer_object == 10:
            return Customer(10, "DuPointe, Xander", False)
        else:
            return None

    mocker.patch("dao.customer_dao.CustomerDao.updated_customer_by_id", mock_updated_cusomter_by_id)

    customer_service = CustomerService()

    with pytest.raises(CustomerNotFoundError) as excinfo:
        actual = customer_service.update_customer_by_id(updated_customer_object)

    assert str(excinfo.value) == "User with id 100 was not found"