# I created this file - Krushil.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import UserProfile
from D2D.decorators import unauthenticated_user

# @user_passes_test(lambda u: u.groups.filter(name='Delivery_person').exists(),   login_url='/delivery/')
# @user_passes_test(lambda u: u.groups.filter(name='User').exists(),   login_url='/user/')
@unauthenticated_user
def index(request):
    return render(request, 'index.html')


# @user_passes_test(lambda u: u.groups.filter(name='Delivery_person').exists(), login_url='/delivery/')
# @user_passes_test(lambda u: u.groups.filter(name='User').exists(),   )
def Login(request):
    return render(request, 'login.html')


# @user_passes_test(lambda u: u.groups.filter(name='Delivery_person').exists(), login_url='/delivery/')
# @user_passes_test(lambda u: u.groups.filter(name='User').exists(),   login_url='/user/')
def signup(request):
    return render(request, 'signup.html')


def handlesignup(request):
    if request.method == 'POST':
        # Get the post paraameters
        username = request.POST.get('user_username')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
        Phone_Number = request.POST.get('number')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        choice = request.POST.get('user_type')
        if (choice == 'user'):
            if len(username) > 10:
                messages.error(request, "Username must under 10 characters")
                return redirect("Signup")
            if not username.isalnum():
                messages.error(request, "Username should only contain letters and numbers")
                return redirect("Signup")
            if (pass1==pass2):
                if (User.objects.filter(username=username).exists()):
                    messages.error(request, '"' + username + '"' + ' This username alredy taken please try again')
                    return redirect('Signup')
                elif (User.objects.filter(email=email).exists()):
                    messages.error(request,'"'+email+'"'+ " This E-mail alredy taken please try again")
                    return redirect('Signup')
                else:
                    u = User.objects.create_user(username=username, password=pass1, email=email, first_name=fname, last_name=lname)
                    group = Group.objects.get(name="Users")
                    u.groups.add(group)
                    # profile = user.UserProfile.objects.get_or_create(user=u,Phone_Number=Phone_Number)
                    # profile.save()
                    u.save()
                    # print(u)
                    # print(group)
                    messages.success(request, fname + ' Your D2D Account has been Successfully Created')
                    return redirect('Login')
            else:
                messages.error(request, "Password does not matched")
                return redirect("Signup")
        else:
            if (choice=='delivery_person'):
                if len(username) > 10:
                    messages.error(request, "Username must under 10 characters")
                    return redirect("Signup")
                if not username.isalnum():
                    messages.error(request, "Username should only contain letters and numbers")
                    return redirect("Signup")
                if (pass1 == pass2):
                    if (User.objects.filter(username=username).exists()):
                        messages.error(request, '"' + username + '"' + ' This username already taken please try again')
                        return redirect('Signup')
                    elif (User.objects.filter(email=email).exists()):
                        messages.error(request,'"' + email + '"'+ " This E-mail already taken please try again")
                        return redirect('Signup')
                    else:
                        user = User.objects.create_user(username=username, password=pass1, email=email,
                                                        first_name=fname, last_name=lname)
                        group = Group.objects.get(name="Delivery_person")
                        user.groups.add(group)

                        user = user.save()
                        messages.success(request, fname + ' Your D2D Account has been Successfully Created')
                        return redirect('Login')
                else:
                    messages.error(request, "Password does not matched")
                    return redirect("Signup")
    else:
        return HttpResponse('404')


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']
        user = authenticate(username=loginusername, password=loginpass)
        if user is not None:
            login(request, user)
            messages.success(request, "You are successfully Logged In")
            if user.groups.filter(name='Delivery_person').exists():
                return redirect('delivery_dashboard')
            else:
                return redirect('userdashboard')
        else:
            messages.error(request, "Invalid credentials, Please try again")
            return redirect('Login')


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')
