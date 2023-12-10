from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect

from products.api_service import ApiService
from products.models import Product
from products.utils import generate_password_md5, generate_username
from products.forms import ProductForm



# Create your views here.
def index(request) :
    products = Product.objects.filter(status_id__status_name="bisa dijual")
    title = "Daftar Produk"
    context = {
        'products' : products,
        'title': title
    }

    return render(request, 'products/index.html', context)

def add_product(request):
    success_massage = 'Data berhasil disimpan.'
    title = "Tambah Produk"
    context = {
        "success_message": success_massage,
        'title': title
    }  

    if request.method == "POST":
        form = ProductForm(request.POST)
        context['form'] = form
        

        if form.is_valid():
            form.save()

            return render(request, 'products/add_product.html', context)
    else:
        form = ProductForm()
        context['form'] = form
    return render(request, 'products/add_product.html', context)


# for API 
class GetDataApi(View):
    def get(self, request, *args, **kwargs):
        # Make instance api service
        username= generate_username()
        password= generate_password_md5()
        api_service = ApiService(username= username, password= password)
        
        # get and save data from api
        api_data = api_service.fetch_data_and_save()

        if api_data:
            return HttpResponse("Data berhasil disimpan ke database.")
        else:
            return HttpResponse("Gagal menyimpan data ke database.")
    