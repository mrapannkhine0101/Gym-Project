from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    CATEGORY = (
        ('Chest', 'Chest'),
        ('Back', 'Back'),
        ('Shoulder', 'Shoulder'),
        ('Biceps', 'Biceps'),
        ('Triceps', 'Triceps'),
        ('Legs', 'Legs'),
    )

    workout_name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY)
    sets = models.IntegerField()
    reps = models.IntegerField()
    image = models.ImageField(upload_to='workouts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.workout_name
    

class Profile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(
        max_length=20, null=True, blank=True
    )

    age = models.IntegerField(null=True, blank=True)

    address = models.CharField(
        max_length=255, null=True, blank=True
    )

    goal = models.CharField(
        max_length=100, null=True, blank=True
    )

    height = models.FloatField(null=True, blank=True)

    weight = models.FloatField(null=True, blank=True)

    image = models.ImageField(
        upload_to='profile/'
    )

    def __str__(self):
        return self.user.username
