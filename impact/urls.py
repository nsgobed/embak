from django.urls import path

from . import views
app_name = 'form'

urlpatterns = [
    path("", views.community_impact, name="community-impact"),
]
