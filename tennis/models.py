from django.contrib.gis.db import models  # Use GeoDjango models for geospatial fields
from django.contrib.auth import get_user_model

class TennisCourt(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    location = models.PointField()  # Geospatial field for the court location
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name


User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tennis_profile')
    location = models.PointField(null=True, blank=True)

    def __str__(self):
        return self.user.username
