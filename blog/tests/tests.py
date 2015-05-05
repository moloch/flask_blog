__author__ = 'Dario Coco'

import unittest
from blog import db
from blog.src import config
from blog.src.models import User
from blog.src.server import create_app
from blog.src.config import TEST_URI


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(TEST_URI)
        self.client = self.app.test_client()
        db.create_all()

    def test_db(self):
        dario = User('dario', 'dario.coco@gmail.com')
        db.session.add(dario)
        db.session.commit()

    def test_app(self):
        print(self.client.get("/create"))
        print(self.client.get("/create"))
        print(self.client.get("/delete"))
        print(self.client.get("/create"))

    def tearDown(self):
        db.drop_all()
        db.session.close()
