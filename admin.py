from django.contrib.gis import admin
from lotxlot.models import PhlParcel, PhlPublicVacantLot

admin.site.register(PhlParcel, admin.GeoModelAdmin)
admin.site.register(PhlPublicVacantLot, admin.GeoModelAdmin)