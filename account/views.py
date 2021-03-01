from user.models import CustomerUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .form import RegisterForm, UserEditForm, ProfileEditForm, Profile
from django.http import HttpResponseRedirect 
from django.conf import settings
import re,os
# register
def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'pages/register.html'
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            username=form.cleaned_data['username']
            if not re.search(r'^\w+$', username):
                return render(request, template, {
                    'form': form,
                    'error_message': 'Tài khoản có kí tự đặc biệt'
                })
                # raise form.ValidationError("Tên tài khoản có kí tự đặc biệt")
            if CustomerUser.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Tài khoản đã tồn tại'
                })
            # elif CustomerUser.objects.filter(username=form.cleaned_data['username']).exists():

            elif CustomerUser.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email đã tồn tại'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                # raise form.ValidationError("Mật khẩu không hợp lệ")
                return render(request, template, {
                    'form': form,
                    'error_message': 'Mật khẩu không trùng nhau'
                })
            else:
                # Create the user:
                profile = CustomerUser.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password'],
                )
                # user.first_name = form.cleaned_data['first_name']
                # user.last_name = form.cleaned_data['last_name']
                profile.phone_number = form.cleaned_data['phone_number']

                profile.save()
               
                # Login the user
                login(request, profile)
               
                # redirect to accounts page:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Đăng kí thành công'
                })
    else:
        form = RegisterForm()
    return render(request, template, {'form': form})
# login
def user_login(request):
    if request.method == 'POST':
    # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
    # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if profile is not None:
            # Save session as cookie to login the user
            login(request, profile)
            # Success, now let's login the user.
            return render(request, 'pages/index.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'pages/login.html', {'error_message': 'Tài khoản hoặc mật khẩu sai.'})
    else:
    # No post data availabe, let's just show the page to the user.
        return render(request, 'pages/login.html')
@login_required
# def load_profile(user):
#     try:
#         return user.profile
#     except:  # this is not great, but trying to keep it simple
#         profile = User.objects.create(user=user)
#         return profile
def user_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data=request.POST,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request,'pages/profile_user.html',{'user_form': user_form,'profile_form': profile_form})