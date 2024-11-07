from django.contrib.gis import admin
from .models import TennisCourt

# Register the TennisCourt model using GISModelAdmin for geospatial features
admin.site.register(TennisCourt, admin.GISModelAdmin)
