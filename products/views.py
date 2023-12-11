from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

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

# for CRUD

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
        context.pop("success_message")
        context['form'] = form
    return render(request, 'products/add_product.html', context)

def update_product(request, product_id):
    product = Product.objects.get(id = product_id)
    success_massage = 'Data berhasil diubah.'
    title = "Ubah Data Produk"
    context = {
        "success_message": success_massage,
        'title': title,
        "product_id" : product_id
    }  

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        context['form'] = form

        if form.is_valid():
            form.save()

            # return render(request, 'products/update_product.html', product_id = product_id, context=context )
            return render(request,'products/update_product.html', context )
    else :
        form = ProductForm(instance=product)
        context.pop("success_message")
        context['form'] = form

        print(product_id)
        print(form)
    
    return render(request, 'products/update_product.html', context)

# def delete_product(request, product_id):
#     product = Product.objects.filter(id= product_id)
#     product.delete()

#     return render('index')

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == "POST":
        product.delete()
        return redirect('index')
    
    title = "Hapus Produk"
    context = {
        'title': title,
        'product': product,
    }

    return render(request, 'products/delete_product.html', context)


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
            print("Data berhasil disimpan ke database.")
            return redirect('index')
        else:
            return HttpResponse("Gagal menyimpan data ke database.")
    