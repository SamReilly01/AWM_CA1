from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile, TennisCourt  # Assuming TennisCourt model is defined

User = get_user_model()

# Helper function to set user location
def set_user_location(user_id, latitude, longitude):
    user = User.objects.get(id=user_id)
    location = Point(longitude, latitude)
    profile, created = Profile.objects.get_or_create(user=user)
    profile.location = location
    profile.save()
    return profile

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('tennis_map')  # Redirect to the tennis map view
    else:
        form = AuthenticationForm()
    return render(request, 'tennis/login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('tennis_login')  # Redirect to the login page after logout

# Main map view for displaying tennis courts
def tennis_map_view(request):
    if request.user.is_authenticated:
        try:
            user_profile = Profile.objects.get(user=request.user)
            location = user_profile.location
        except Profile.DoesNotExist:
            location = None
        return render(request, 'tennis/map.html', {'user': request.user, 'location': location})
    else:
        return redirect('tennis_login')

# JSON endpoint to fetch tennis court data
def tennis_court_data(request):
    if request.method == 'GET' and request.user.is_authenticated:
        courts = TennisCourt.objects.all()
        court_data = [{
            'id': court.id,
            'name': court.name,
            'address': court.address,
            # 'phone': court.phone,  # Uncomment if 'phone' exists in the model
            # 'email': court.email,  # Uncomment if 'email' exists in the model
            'latitude': court.location.y,
            'longitude': court.location.x
        } for court in courts]

        return JsonResponse(court_data, safe=False)
    else:
        return JsonResponse({'success': False, 'error': 'Unauthorized request'}, status=403)

# Update user location view
def update_location(request):
    if request.method == 'POST' and request.user.is_authenticated:
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')

        if latitude and longitude:
            try:
                latitude = float(latitude)
                longitude = float(longitude)
                location = Point(longitude, latitude)
                
                profile, created = Profile.objects.get_or_create(user=request.user)
                profile.location = location
                profile.save()

                return JsonResponse({'success': True})
            except ValueError:
                return JsonResponse({'success': False, 'error': 'Invalid coordinates'})
        else:
            return JsonResponse({'success': False, 'error': 'Missing coordinates'})
    return JsonResponse({'success': False, 'error': 'Invalid request'})
