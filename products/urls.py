from django.urls import path
from . import views
from products.views import GetDataApi

urlpatterns = [
    path("", views.index, name="index"),
    path('get-data-api/', GetDataApi.as_view(), name='GetDataApi'),
]
