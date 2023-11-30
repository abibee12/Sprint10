# tests/test_routes.py
from flask import Flask
from flask.testing import FlaskClient
from flask_sqlalchemy import SQLAlchemy
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

if __name__ == '__main__':
    unittest.main()
