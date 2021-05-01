from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50, default = "")
    sub_category = models.CharField(max_length = 50, default = "")
    price = models.IntegerField(default = 0)
    desc = models.TextField(max_length = 500)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="images/", default = "")

    def __str__(self):  #Each 'Product' Object will now have a name same as name field
        return self.product_name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    desc = models.TextField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):  #Each 'Contact' Object will now have a name same as name field
        return self.name  

class Order(models.Model):
    items_json = models.CharField(max_length=5000, default="", null=True)
    name = models.CharField(max_length=100, default="")
    addressline = models.CharField(max_length=100 , default="")
    city = models.CharField(max_length=50 , default="")
    state = models.CharField(max_length=50 , default="")
    zip_code = models.CharField(max_length=10 , default="")
    phone = models.CharField(max_length=12 , default="")

    def __str__(self):
        return self.name