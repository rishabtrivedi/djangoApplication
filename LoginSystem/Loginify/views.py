from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .forms import LoginForm,SignupForm
from . models import UserDetails
from django.http import HttpResponse, JsonResponse
from .Serializers import UserSerializer
import json
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'Loginify/index.html')


def signup(request):
    # form = SignupForm()
    # return render(request, 'Loginify/signup.html', {'form': form})

    # # return HttpResponse('Hello World Sign UP')
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else :
        form = SignupForm()
        return render(request, 'Loginify/signup.html', {'form': form})
    return render(request, 'Loginify/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Handle the login logic here
            return redirect('/')
    else:
        form = LoginForm()

    # form = LoginForm()
    return render(request, 'Loginify/login.html', {'form': form})

def logoutView(request):
    logout(request)
    return redirect('Loginify:login')

def getAllUsers(request):
    users = UserDetails.objects.all()
    print(users)
    return render(request, 'Loginify/allUsers.html', {'users': users})

@csrf_exempt
def getUserDetails(request):
    if request.method == 'GET':
        users = UserDetails.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def getUserByEmail(request):
    email = request.GET.get('email', None)
    if email:
        try:
            user = UserDetails.objects.get(email=email)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'})
    else:
        return JsonResponse({'error': 'No email provided'})

@csrf_exempt
def updateUserDetails(request):
    if request.method == 'PUT':
        email = request.GET.get('email', None)
        if email:
            try:
                user_data = json.loads(request.body)
                user = UserDetails.objects.get(email=email)
                
                serializer = UserSerializer(user, data=user_data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=200)
                return JsonResponse(serializer.errors, status=400)
            except UserDetails.DoesNotExist:
                return JsonResponse({'error': 'User not found'})
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'})
        else:
            return JsonResponse({'error': 'Email is required'})
    else:
        return JsonResponse({'error': 'Invalid request method'})

@csrf_exempt
def deleteUserByEmail(request):
    if request.method == 'DELETE':
        email = request.GET.get('email', None)
        if email:
            try:
                user = UserDetails.objects.get(email=email)
                user.delete()
                return JsonResponse({'message': 'User deleted successfully'})
            except UserDetails.DoesNotExist:
                return JsonResponse({'error': 'User not found'})
        else:
            return JsonResponse({'error': 'Email is required'})
    else:
        return JsonResponse({'error': 'Invalid request method'})