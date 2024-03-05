from django.contrib import admin

from django.contrib import admin

from .models import CommunityFeedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'name', 'email', 'message', 'approved')
    list_filter = ('date', 'name',)
    search_fields = ('date', 'name',)

    class Meta:
        model = CommunityFeedback


admin.site.register(CommunityFeedback, FeedbackAdmin)
