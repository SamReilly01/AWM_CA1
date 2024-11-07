from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.tennis_map_view, name='tennis_map'),  # This should be correct now
    path('login/', views.login_view, name='tennis_login'),
    path('logout/', views.logout_view, name='tennis_logout'),
    path('update_location/', views.update_location, name='tennis_update_location'),
    path('tennis_court_data/', views.tennis_court_data, name='tennis_court_data'),

]