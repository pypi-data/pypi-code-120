from paradoxdjango.contrib.gis import admin


class UnmodifiableAdmin(admin.OSMGeoAdmin):
    modifiable = False
