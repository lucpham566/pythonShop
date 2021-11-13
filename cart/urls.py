from django.urls import path

from .views import Checkout
from .  import views

urlpatterns = [
    path('',Checkout.as_view(),name='checkout'), 
    path('process',views.process,name='send-checkout'), 
    path('add-cart',views.addToCart,name="add-to-cart"), 
    path('remove-cart',views.removeToCart,name="remove-to-cart"), 
]

