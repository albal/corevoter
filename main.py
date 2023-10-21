'''
This file contains the tests for our application.
'''
import unittest
from models import Course
from app import create_app, db
app = create_app()
class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    def test_index(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    # More tests can be added here as per requirements
if __name__ == '__main__':
    unittest.main()