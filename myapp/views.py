from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm
from django.contrib import messages
from .models import CustomUser, Class

def register(request, class_id):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Extract data from the POST request
            roll_number = form.cleaned_data['roll_number']
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            parents_number = form.cleaned_data['parents_number']

            # Get the current user
            user = request.user

            # Determine the appropriate class based on class_id
            try:
                class_instance = Class.objects.get(id=class_id)
            except Class.DoesNotExist:
                return HttpResponse("Invalid class ID")

            # Create a new student instance for the specified class
            student = class_instance.registered_students.create(
                roll_no=roll_number,
                name=name,
                age=age,
                parents_number=parents_number,
            )

            # Associate the student with the current user
            user.registered_classes.add(class_instance)

            return HttpResponse("Registration successful!")

    # If the method is not POST, render the registration form
    form = RegistrationForm()  # Create an instance of the form
    context = {'form': form, 'class_id': class_id}
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Login failed. Please check your username and password.')
        else:
            messages.error(request, 'Login failed. Please correct the errors below.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')  # Adjust the URL name accordingly
