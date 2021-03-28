# I created this file - Krushil.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.models import UserProfile
from delivery_person.models import DeliveryPersonProfile
from D2D.decorators import unauthenticated_user



@unauthenticated_user
def index(request):
    return render(request, 'index.html')

@unauthenticated_user
def Login(request):
    return render(request, 'login.html')

@unauthenticated_user
def signup(request):
    return render(request, 'signup.html')


def handlesignup(request):
    if request.method == 'POST':
        # Get the post paraameters
        username = request.POST.get('user_username')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        email = request.POST.get('email')
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
                    u.userprofile.Phone_Number = request.POST['number']
                    u.save()
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
                        user.deliverypersonprofile.Phone_Number = request.POST['number']
                        user.deliverypersonprofile.Address = request.POST['address']
                        user.deliverypersonprofile.Aadhaar_Number = request.POST['aadhar']
                        user.deliverypersonprofile.PAN_Number = request.POST['PAN']
                        user.deliverypersonprofile.Driving_licence_number = request.POST['driving_licence']
                        user.deliverypersonprofile.Vehicle_RC_number = request.POST['vehicle_rc']
                        user.save()
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
