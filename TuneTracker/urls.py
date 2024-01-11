from TuneTracker import views
from django.urls import path

urlpatterns = [
    path("", views.Tune.as_view(), name='dashboard'),  
]