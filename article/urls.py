from django.urls import path
from .views import NewsPage, NewDetail

urlpatterns = [
    path('',NewsPage.as_view(),name='news'), 
    path('detail/<int:id>',NewDetail.as_view(),name='new-detail'), 
]
