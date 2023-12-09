from django.views import View
from django.http import HttpResponse
from products.api_service import ApiService
from products.utils import generate_password_md5, generate_username



# Create your views here.
def index(request) :
    return HttpResponse("Hello, world. You're at the products index.")

class GetDataApi(View):
    def get(self, request, *args, **kwargs):
        # Make instance api service
        username= generate_username()
        password= generate_password_md5()
        api_service = ApiService(username= username, password= password)

        print(f"Username yang dikirim ke ApiService: {username}")
        print(f"Password yang dikirim ke ApiService: {password}")
        
        # get and save data from api
        api_data = api_service.fetch_data_and_save()

        if api_data:
            return HttpResponse("Data berhasil disimpan ke database.")
        else:
            return HttpResponse("Gagal menyimpan data ke database.")
    