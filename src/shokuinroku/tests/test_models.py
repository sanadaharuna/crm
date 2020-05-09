from django.test import TestCase
from shokuinroku.models import Shokuin
from shokuinroku.tests.factories import ShokuinFactory


class ShokuinModelTests(TestCase):
    def test_no_item(self):
        item_list = Shokuin.objects.all()
        self.assertEqual(0, item_list.count())

    def test_1_item(self):
        ShokuinFactory.create()
        item_list = Shokuin.objects.all()
        self.assertEqual(1, item_list.count())
