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
        max_length=20
    )

    age = models.IntegerField()

    address = models.CharField(
        max_length=255
    )

    goal = models.CharField(
        max_length=100
    )

    height = models.FloatField()

    weight = models.FloatField()

    image = models.ImageField(
        upload_to='profile/'
    )

    def __str__(self):
        return self.user.username
