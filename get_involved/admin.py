from django.contrib import admin

from django.contrib import admin

from .models import VolunteerData, DonationData


class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'name', 'email', 'phone_number',
                    'message', 'approved', 'opportunity_name')
    list_filter = ('date', 'name', 'opportunity_name',)
    search_fields = ('date', 'name', 'opportunity_name',)

    class Meta:
        model = VolunteerData


admin.site.register(VolunteerData, VolunteerAdmin)


class DonationAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'first_name', 'last_name', 'city', 'country', 'email', 'phone_number',)
    list_filter = ('date', 'last_name', 'country',)
    search_fields = ('date', 'last_name', 'country',)

    class Meta:
        model = DonationData


admin.site.register(DonationData, DonationAdmin)
