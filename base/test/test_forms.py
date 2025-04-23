from django.test import TestCase
from base.forms import RoomForm

class TestForms(TestCase):
    def test_room_form_valid(self):
        form = RoomForm(data={'name': 'Valid Room', 'description': 'Test description'})
        self.assertTrue(form.is_valid())

    def test_room_form_invalid(self):
        form = RoomForm(data={})
        self.assertFalse(form.is_valid())
