from django.urls import path
from .views import HomeView
from . import views

urlpatterns = [
    path('',HomeView.as_view(),name='index'), 
    path('add-subscriber',views.addSubscriber,name='add-subscriber'), 
]

