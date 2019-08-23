from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    # path('get_bias/', GetBias, name="get_bias"),
]