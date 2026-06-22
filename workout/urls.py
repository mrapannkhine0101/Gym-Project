from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('workout_list/', views.workout_list, name='workout_list'),
    path('add/', views.add_workout, name='add_workout'),
    path('detail/<int:id>/', views.workout_detail, name='workout_detail'),
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.create_profile, name='create_profile'),
    # path('profile/edit/', views.edit_profile, name='edit_profile'),
    ]