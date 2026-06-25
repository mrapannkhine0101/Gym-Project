from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import User
from .models import Profile, Workout
from .forms import ProfileForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#authenticated
def register(request):
    message = ''
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        
        # username already exit
        if User.objects.filter(username=username).exists():
            message = 'Username already exists'
            
        else:
            user = User.objects.create_user(
                username=username,
                password=password
            )
            user.save()
            return redirect('login')

    return render(request, 'register/register.html', {'message': message})

def login_view(request):
    message = ''

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            message = 'Username or Password is wrong'
    context = {
        'message':message,
    }
    return render(request, 'login/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def workout_list(request):

    query = request.GET.get('q')

    workouts = Workout.objects.all()
    category = request.GET.get('category')

    if category:
        workouts = workouts.filter(
            category=category
        )

        if query:
            workouts = workouts.filter(
                Q(name__icontains=query)
        )

    return render(
        request,
        'workout/list.html',
        {'workouts': workouts}
    )

@login_required(login_url='login')
def dashboard(request):
    profile, created = Profile.objects.get_or_create(
    user=request.user
    )
    total_users = User.objects.count()

    total_workouts = Workout.objects.count()

    total_profiles = Profile.objects.count()
    total_chest_workouts = Workout.objects.filter(category='chest').count()
    total_legs_workouts = Workout.objects.filter(category='legs').count()
    recent_workouts = Workout.objects.order_by('-created_at')[:5]
    context = {
        'total_users': total_users,
        'total_workouts': total_workouts,
        'total_profiles': total_profiles,
        'total_chest_workouts': total_chest_workouts,
        'total_legs_workouts': total_legs_workouts,
        'recent_workouts': recent_workouts, 
        'profile': profile
    }
    print(Workout.objects.values_list('category', flat=True))
    return render(
        request,
        'dashboard/dashboard.html',
        context
    )

@login_required(login_url='login')
def workout_list(request):
    workouts = Workout.objects.all()
    context = {
        'workouts': workouts
    }

    return render(request, 'workout/workout_list.html', context)

@login_required(login_url='login')
def add_workout(request):
    if request.method == 'POST':
        workout_name = request.POST.get('workout_name')
        category = request.POST.get('category')
        sets = request.POST.get('set')
        reps = request.POST.get('rep')
        image = request.FILES.get('image')

        Workout.objects.create(
            workout_name=workout_name,
            category=category,
            sets=sets,
            reps=reps,
            image=image
        )
        return redirect('workout_list')
    return render(request, 'workout/add_workout.html')

@login_required(login_url='login')  
def workout_detail(request,id):

    workout = Workout.objects.get(id=id)

    return render(
        request,
        'workout/detail.html',
        {'workout': workout}
    )

@login_required(login_url='login')
def create_profile(request):
    profiles = Profile.objects.all()
    if request.method == 'POST':
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        address = request.POST.get('address')
        goal = request.POST.get('goal')
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        image = request.FILES.get('image')

        Profile.objects.create(
            user=request.user,
            phone=phone,
            address=address,
            goal=goal,
            age=age,
            weight=weight,
            height=height,
            image=image
        )
        return redirect('profile')
    return render(request, 'profile/create_profile.html', {'profiles': profiles})
  
@login_required(login_url='login')
def profile(request):
    profiles = Profile.objects.filter(user=request.user)
    return render(
        request,
        'profile/profile.html',
        {'profiles': profiles}
    )

def edit_profile(request):
    profile = get_object_or_404(
        Profile,
        user=request.user
    )

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile/edit_profile.html', {'form': form})

@login_required(login_url='login')
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        logout(request)
        user.delete()
        return redirect('login')
    return render(request, 'profile/delete_account.html')
    