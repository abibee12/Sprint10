# tests/test_routes.py

import unittest
from app import create_app, db
from app.models import Data


class MyTestCase(unittest.TestCase):

    def setUp(self):

        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_insert_data(self):
        response = self.client.post(
            "/data",
            json={"name": "John Doe"},
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 200)
        with self.app.app_context():
            self.assertEqual(Data.query.count(), 1)

    def test_insert_duplicate_data(self):
        # Test inserting duplicate data
        response1 = self.client.post(
            "/data",
            json={"name": "John Doe"},
            content_type="application/json",
        )
        self.assertEqual(response1.status_code, 200)

        response2 = self.client.post(
            "/data",
            json={"name": "John Doe"},
            content_type="application/json",
        )
        # Expecting a conflict (HTTP 409) for duplicate data
        self.assertEqual(response2.status_code, 409)

    def test_get_all_data(self):
        # Test getting all data
        # First, insert some data
        with self.app.app_context():
            db.session.add(Data(name="Alice"))
            db.session.add(Data(name="Bob"))
            db.session.commit()

        response = self.client.get("/data")
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        # Expecting two items in the response
        self.assertEqual(len(data), 2)

    def test_delete_data(self):
        # Test deleting data
        # First, insert some data
        with self.app.app_context():
            db.session.add(Data(name="Alice"))
            db.session.commit()

        response = self.client.delete("/data/1")
        self.assertEqual(response.status_code, 200)
        with self.app.app_context():
            # Expecting the data to be deleted
            self.assertEqual(Data.query.count(), 0)


if __name__ == '__main__':
    unittest.main()
