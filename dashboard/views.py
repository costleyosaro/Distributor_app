from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfilePictureForm
from django.shortcuts import render, redirect
from users.models import Profile
import logging
import os


@login_required
def dashboard(request):
    user_name = request.user.username  # Fetch the username instead of first_name
    return render(request, 'dashboard/Ghadco_Users_Dashboard!.html', {'user_name': user_name})


from django.core.files.storage import default_storage

def upload_profile_picture(request):
    if request.method == "POST" and request.FILES.get("profile_picture"):
        uploaded_file = request.FILES["profile_picture"]
        user_profile = request.user.profile  # Assuming a Profile model
        user_profile.profile_picture.save(uploaded_file.name, uploaded_file)
        print('profile picture upload succesful')
        user_profile.save()
        return redirect("dashboard")  # Adjust as needed
    return render(request, "dashboard/Ghadco_Users_Dashboard!.html")


import os
import logging
from django.conf import settings

logger = logging.getLogger(__name__)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.forms import ProfilePictureForm  # Import from users app
from users.models import CustomUser  # Import your user model

@login_required
def dashboard_picture(request):
    user = request.user  # Get the logged-in user
    form = ProfilePictureForm(instance=user)  # Pre-fill with existing image

    if request.method == "POST":
        form = ProfilePictureForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('dashboard_picture')  # Reload page to show updated image

    return render(request, 'dashboard/Ghadco_Users_Dashboard!s.html', {'form': form, 'user': user})








from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_user(request):
    logout(request)
    return redirect('home')  # Make sure 'home' is defined in your main urls.py


def beverage_list(request):
    return render(request, 'dashboard/Beverage_list.html')

def food_list(request):
    return render(request, 'dashboard/Food_list.html')

def care_list(request):
    return render(request, 'dashboard/Care_list.html')




def generate_invoice(request):
    return render(request, 'dashboard/invoice_page.html')
