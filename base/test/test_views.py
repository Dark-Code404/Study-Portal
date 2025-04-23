from django.test import TestCase, Client
from django.urls import reverse
from base.models import User, Room

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.room = Room.objects.create(name='Test Room', host=self.user)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base/home.html')

    def test_create_room_view_authenticated(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('create_rooms'), {'name': 'New Room', 'topic': 'General'})
        self.assertEqual(response.status_code, 302) 
