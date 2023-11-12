from django.urls import path
from .views import home_view

urlpatterns = [
    path('', home_view, name='home'),  # The root path is linked to `home_view`
]
