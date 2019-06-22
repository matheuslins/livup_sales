import os

from unittest import TestCase
from src.app import AppHandler


class TestAppHandler(TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = AppHandler()

    def test_read_local_file_wrong_path(self):
        items = self.app.read_local_file("files/sales2.json")
        assert items == []

    def test_read_local_file_empty(self):
        items = self.app.read_local_file('')
        assert items == []

    def test_read_local_file(self):
        items = self.app.read_local_file("files/sales.json")
        assert isinstance(items, list)
