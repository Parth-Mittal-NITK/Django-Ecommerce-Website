from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth #User is like a predifined model
from accounts.models import Address
from django.contrib import messages #To use messages form Django
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name'] #inside '' is the same name as name in the form
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        addressline = request.POST['addressline1'] + " " + request.POST['addressline2']
        city = request.POST['city']
        state = request.POST['state']
        zip_code = request.POST['zip_code']
        phone = request.POST['phone']

        if User.objects.filter(username = username).exists():
            messages.info(request, 'Oops! User name already taken')
            return redirect('register')
        elif User.objects.filter(email = email).exists():
            messages.info(request, 'Oops! Email already taken')
            return redirect('register')
        else:
            if password1 == password2:
                user = User.objects.create_user(first_name= first_name, last_name = last_name, username= username, email= email, password=password1)
                user.save()
                adddress = Address(user=user, addressline = addressline, city = city, state = state, zip_code = zip_code, phone = phone)
                adddress.save() #need to save user and address separately even though they are linked
                auth.login(request, user) #Register and automatically login also
                return redirect('/')
            else:
                messages.warning(request, 'Password not matching')
                return redirect(register)
    else:    
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You have been successfully logged in!')
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have been successfully logged out!')
    return redirect('/')