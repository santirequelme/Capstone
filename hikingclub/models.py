from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Hiking(models.Model):
    locations = [
        ('San Martin de los Andes', 'San Martin de los Andes'),
        ('Bariloche', 'Bariloche'),
        ('Torres del Paine', 'Torres del Paine'),
        ('El Chalten','El Chalten'),
        ('El Bolson', 'El Bolson'),
        ('El Calafate', 'El Calafate')
    ]

    levels = [
        ('Easy', 'Easy'),
        ('Moderate', 'Moderate'),
        ('Strenuous', 'Strenuous'),
        ('Very difficult', 'Very difficult')
    ]

    
    title = models.CharField(max_length= 70)
    location = models.CharField(choices=locations, max_length= 64, blank=True, default='Select location')
    level = models.CharField(choices=levels, max_length= 64, blank=True, default='Select level')
    short_description = models.CharField(max_length=170, blank=True)
    description = models.CharField(max_length = 2000)
    image_url = models.URLField(blank=True)
    map_url = models.URLField(blank=True, max_length = 2000)
    status    = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"

class Favourite (models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE, related_name="use_favourite")
    hiking = models.ForeignKey(Hiking, on_delete=models.CASCADE, related_name="favourite_item")

    def __str__(self):
        return f"{self.user} {self.hiking}"

class Comment (models.Model):
    user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_hiker")
    hiking   = models.ForeignKey(Hiking, on_delete=models.CASCADE, related_name="comment_hiking") 
    comment    = models.CharField(max_length=1800)

    def __str__(self):
        return f"{self.user} on {self.hiking} say {self.comment}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    hike = models.CharField(max_length= 120, blank=True)
    name = models.CharField(max_length= 70)
    last_name = models.CharField(max_length= 70)
    date = models.DateField()
    phone = models.CharField(max_length=64)
    book_number = models.CharField(max_length=64)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def serialize(self):
        return {
            "id": self.id,
            "hike": self.hike,
            "name": self.name,
            "last_name": self.last_name,
            "date": self.date,
            "phone": self.phone,
            "book_number": self.book_number,
            "timestamp": self.timestamp.strftime("%b %-d %Y, %-I:%M %p")
        }

