from django.urls import path
from . import views
from products.views import GetDataApi

urlpatterns = [
    path("", views.index, name="index"),
    path("tambah/", views.add_product, name="add_product"),
    path('ubah/<int:product_id>', views.update_product, name="update_product"),
    path('delete/<int:product_id>', views.delete_product, name="delete_product"),

    path('get-data-api/', GetDataApi.as_view(), name='GetDataApi'),
]
