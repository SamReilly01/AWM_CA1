from django.urls import path
from . import views

urlpatterns = [
    # Existing paths
    path('map/', views.tennis_map_view, name='tennis_map'),  # Map view
    path('login/', views.login_view, name='tennis_login'),   # Login view
    path('logout/', views.logout_view, name='tennis_logout'),  # Logout view
    path('signup/', views.signup_view, name='tennis_signup'),  # Signup view
    path('update_location/', views.update_location, name='tennis_update_location'),  # Update location
    path('tennis_court_data/', views.tennis_court_data, name='tennis_court_data'),  # Fetch tennis court data
]
