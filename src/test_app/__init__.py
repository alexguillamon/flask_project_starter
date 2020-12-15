import unittest
from app import create_app
from database import db
from utils.db_data_init import seed


class inheritedTestCase(unittest.TestCase):
    __abstract__ = True

    def setUp(self):
        """
        This method creates a new app using the test configuration together with 
        instantiating a test client to be used for request.

        At every test seed data is created.
        """
        self.app = create_app(test=True)
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()
            seed()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def check_success(self, code, data, expected_code=200):
        """
        This method abstract assertions for successfull status codes
        and `success`from JSON data.

        Parameters:
            code: status code from the request
            data: JSON parsed data from the request
            expected_code: the expected code from the request
        """
        self.assertEqual(code, expected_code)
        self.assertTrue(data["success"])
        return True

    def check_failure(self, code, data, expected_code):
        """
        This method abstract assertions for unsuccessfull status codes
        and `success` from JSON data.

        Parameters:
            code: status code from the request
            data: JSON parsed data from the request
            expected_code: the expected code from the request
        """
        self.assertEqual(code, expected_code)
        self.assertEqual(data["error"], expected_code)
        return True

    def client_request(self, path, options=None):
        """
        This method abstracts client request code.

        Parameters:
            path: path to the desired endpoint
            options: dictionary of parameters to be passed to the test client
                    This dictionary will allow any parameter that
                    flask.testing.FlaskClient's `open` method takes.
                    For reference see https://flask.palletsprojects.com/en/1.1.x/api/#flask.testing.FlaskClient
        """
        if options is None:
            options = {
                "method": "GET",
                "json": {},
                "headers": self.header
            }
        elif "headers" not in options:
            options["headers"] = self.header
        res = self.client.open(path, **options)
        data = res.get_json()
        return [res.status_code, data]


class TestingCase (inheritedTestCase):
    pass


if __name__ == "__main__":
    unittest.main()
