from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    pic = models.ImageField(
        upload_to="Profile/", null=True, blank=True, default="Profile/default_pic.jpg"
    )

    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        try:
            this = User.objects.get(id=self.id)
            if this.pic != self.pic:
                this.pic.delete()
        except:
            pass
        super(User, self).save(*args, **kwargs)


class Topic(models.Model):
    name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return f"{self.name}"


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="message_images/", null=True, blank=True)
    file = models.FileField(upload_to="files/", null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def __str__(self):
        return self.body[0:20]
