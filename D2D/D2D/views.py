# I created this file - Krushil.
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.shortcuts import render, redirect




def index(request):
    return render(request, 'index.html')


def handlesignup(request):
    if request.method == 'POST':
        # Get the post paraameters
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        choice = request.POST.get('utype')
        if (choice == 'user'):
            if len(username) > 10:
                messages.error(request, "Username must under 10 characters")
                return redirect("home")
            if not username.isalnum():
                messages.error(request, "Username should only contain letters and numbers")
                return redirect("home")
            if(pass1==pass2):
                if(User.objects.filter(username=username).exists()):
                    messages.error(request,username + 'This username alredy taken please try again')
                    return redirect('home')
                elif (User.objects.filter(email=email).exists()):
                    messages.error(request, email +" This E-mail alredy taken please try again")
                    return redirect('home')
                else:
                    user=User.objects.create_user(username=username ,password=pass1,email=email,
                    first_name=fname,last_name=lname)
                    group = Group.objects.get(name="Users")
                    user.groups.add(group)
                    user.save()
                    messages.success(request, fname + 'Your D2D Account has been Successfully Created')
                    return redirect('home')
            else:
                messages.error(request,"Password does not matched")
                return redirect("home")
        else:
            if (choice == 'delivery_person'):
                if len(username) > 10:
                    messages.error(request, "Username must under 10 characters")
                    return redirect("home")
                if not username.isalnum():
                    messages.error(request, "Username should only contain letters and numbers")
                    return redirect("home")
                if (pass1 == pass2):
                    if (User.objects.filter(username=username).exists()):
                        messages.error(request, username + 'This username alredy taken please try again')
                        return redirect('home')
                    elif (User.objects.filter(email=email).exists()):
                        messages.error(request, email + " This E-mail alredy taken please try again")
                        return redirect('home')
                    else:
                        user = User.objects.create_user(username=username, password=pass1, email=email,
                                                        first_name=fname, last_name=lname)
                        # User_group = Group.objects.get_or_create(name='User')
                        group = Group.objects.get(name="Delivery_person")
                        user.groups.add(group)
                        user = user.save()
                        messages.success(request, fname + 'Your D2D Account has been Successfully Created')
                        return redirect('home')
                else:
                    messages.error(request, "Password does not matched")
                    return redirect("home")
    else:
        return HttpResponse('404')


    #     if pass1 != pass2:
    #         messages.error(request, "Passwords do not match")
    #         return redirect("home")
    #     # Create the user
    #     myuser = User.objects.create_user(username, email, pass1)
    #     myuser.first_name = fname
    #     myuser.last_name = lname
    #     myuser.phone_number = tel
    #     myuser.save()
    #     messages.success(request, "Your D2D account has been successfully created")
    #     return redirect('home')
    # else:
    #     return HttpResponse('404 - Not Found')




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
            return redirect('home')

#
# @user_passes_test(is_user)
# def handlelogin(request):
#     if request.method == 'POST':
#         loginusername = request.POST['loginusername']
#         loginpass = request.POST['loginpass']
#         choice = request.POST.get('utype')
#         user = authenticate(username=loginusername, password=loginpass)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "You are successfully Logged In")
#             return redirect('')
#         else:
#             messages.error(request, "Invalid credentials, Please try again")
#             return redirect('home')
    #   else:
    #       if user is not None:
    #       login(request, user)
    #       messages.success(request, "You are successfully Logged In")
    #       return redirect('delivery_dashboard')
    #   else:
    #       messages.error(request, "Invalid credentials, Please try again")
    #             return redirect('home')
    # return HttpResponse('404 - Not Found')

def handlelogout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Successfully Logged Out")
        return redirect('home')
    else:
        HttpResponse('404 - Not Found')
