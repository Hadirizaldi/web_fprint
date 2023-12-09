import requests
from products.serializers import CategorySerializer, ProductSerializer, StatusSerializer
from products.models import Category, Status


class ApiService:
  API_URL = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

  def __init__(self, username, password):
    self.username = username
    self.password = password

  def fetch_product_from_api(self):
    url = self.API_URL
    form = {
      "username" : self.username,
      "password" : self.password
    }

    response = requests.post(url=url, data=form)
    print(response)

    if response.status_code == 200:
      api_data= response.json()['data']
      return api_data

    else:
      print(f"Failed to fetch data. Status code: {response.status_code}")
      print(f"Response Text: {response.text}")
      return None

  def save_data_to_database(self, api_data):
    for product_data in api_data:
      # Deserialize data from API
      category_data = product_data['kategori']
      status_data = product_data['status']

      # for Category
      category_serializer = CategorySerializer(data={'category_name': category_data})
      if category_serializer.is_valid():
        existing_category = Category.objects.filter(category_name=category_data).first()

        # Check that the category name already exists
        if existing_category:
          # Category already exists
          category = existing_category
        else:
          # Category does not exist yet, save data
          category = category_serializer.save()
          # category = category_serializer.instance
      else:
        print(f"Error in serializing category for product {product_data.get('nama_produk')}: {category_serializer.errors}")
        continue


      # For Status
      status_serializer = StatusSerializer(data={'status_name': status_data})
      if status_serializer.is_valid():
        existing_status = Status.objects.filter(status_name = status_data).first()

        # Check that the status name already exists
        if existing_status:
          # status already exists
          status = existing_status
        else:
          # status does not exist yet, save data
          status = status_serializer.save()
          # status = status_serializer.instance
      else:
        print(f"Error in serializing status for product {product_data.get('nama_produk')}: {status_serializer.errors}")
        continue

      # For Product
      product_serializer = ProductSerializer(data={
        'id': product_data.get('id_produk'),
        'product_name': product_data.get('nama_produk'),
        'price': product_data.get('harga'),
        'category_id': category.id,
        'status_id': status.id,
      })

      if product_serializer.is_valid():
        product_serializer.save()
        print(f"Product {product_data.get('nama_produk')} saved successfully.")
      else:
        print(f"Error in serializing product: {product_serializer.errors}")

  def fetch_data_and_save(self):
    # get data from API
    api_data = self.fetch_product_from_api()
  
    if api_data:
    # Save data to database
      self.save_data_to_database(api_data)
      return api_data
    else:
      return False

