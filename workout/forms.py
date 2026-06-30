from django import forms
from .models import Workout, Profile, Workoutplan

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['workout_name', 'category', 'sets', 'reps', 'image']
        widgets = {
            'workout_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'workout name'}),
            'category': forms.Select(attrs={'class':'form-select'}),
            'sets': forms.NumberInput(attrs={'class':'form-control'}),
            'reps': forms.NumberInput(attrs={'class':'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'age', 'address', 'goal', 'height', 'weight', 'image']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control',}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'goal': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class WorkoutplanForm(forms.ModelForm):
    class Meta:
        model = Workoutplan
        fields = [
            'day',
            'workout',
            'title',
            'description'
        ]
        widgets = {
            'day': forms.Select(attrs={'class': 'form-select'}),
            'workout':forms.Select(attrs={'class':'form.select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'row': 4, 'placeholder': 'workout detail'}),     
                   }
