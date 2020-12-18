from django.urls import path
from tours import views

urlpatterns = [
    path('', views.get_data, name='get_data'),
]
