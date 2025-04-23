from django.test import TestCase

from base.models import User, Room, Topic,Message

class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.topic = Topic.objects.create(name='Testing', creator=self.user)
        self.room = Room.objects.create(name='Test Room', host=self.user, topic=self.topic)
        self.message=Message.objects.create(user=self.user,room=self.room,body="hello")
       
    def test_user(self):
        self.assertEqual(str(self.user),'testuser')
    def test_room(self):
        self.assertEqual(str(self.room), 'Test Room')

    def test_topic_creator(self):
        self.assertEqual(str(self.topic.creator), 'testuser')
   
    def test_message(self):
        self.assertEqual(self.message.user, self.user)
