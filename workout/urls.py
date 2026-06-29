from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.dashboard, name='dashboard'),

    # workout
    path('workout_list/', views.workout_list, name='workout_list'),
    path('add/', views.add_workout, name='add_workout'),
    path('detail/<int:id>/', views.workout_detail, name='workout_detail'),
    path('workout/edit/<str:pk>/', views.edit_workout, name='edit_workout'),
    path('delete/<int:id>/', views.delete_workout, name='delete_workout'),

    # profile
    path('profile/', views.profile, name='profile'),
    path('profile/create/', views.create_profile, name='create_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('delete_account/', views.delete_account, name='delete_account'),

    # plan
    path('plan/add/', views.add_plan, name='add_plan',),
    path('plan/list/', views.plan_list, name='plan_list',),
    ]