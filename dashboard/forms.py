from django import forms
from users.models import CustomUser  # Ensure you're importing from the right place
from users.models import Profile

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']
