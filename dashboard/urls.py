from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import dashboard, logout_user, dashboard_picture, upload_profile_picture,beverage_list,care_list, food_list,generate_invoice  # Added upload_profile_picture

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_user, name='logout_user'),
    path('dashboard/upload-picture/', dashboard_picture, name='dashboard_picture'),
    path('dashboard/upload/', upload_profile_picture, name='upload_profile_picture'),
    path('beverage_list/', beverage_list, name='beverage_list'),
    path('food_list/', food_list, name='food_list'),
    path('care_list/', care_list, name='care_list'),
    path('generate_invoice/', generate_invoice, name='generate_invoice'),
]




