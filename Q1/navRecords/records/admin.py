from django.contrib import admin

from .models import NavigationRecord, Vehicle


class NavigationRecordAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'latitude', 'longitude', 'datetime']
    list_filter = ['datetime', 'vehicle']
    search_fields = ['vehicle', 'vehicle']

    class Meta:
        model = NavigationRecord


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['plate']
    list_filter = ['plate']
    search_fields = ['plate']

    class Meta:
        model = Vehicle


admin.site.register(NavigationRecord, NavigationRecordAdmin)
admin.site.register(Vehicle, VehicleAdmin)
