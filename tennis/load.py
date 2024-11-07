from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import TennisCourt

tennis_club_mapping = {
    'name': 'Name',
    'address': 'Address',
    #'Phone': 'Phone',
    #'email': 'Email',
    #'itm_x': 'ITM_X',
    #'itm_y': 'ITM_Y',
    'location': 'POINT',
}

tennis_club_geojson = Path(__file__).resolve().parent / 'data' / 'tennis.geojson'

def run(verbose=True):
    lm = LayerMapping(TennisCourt, tennis_club_geojson, tennis_club_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)