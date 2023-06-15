from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    Category = models.CharField(max_length=50, default="")
    subCategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    product_desc = models.CharField(max_length=500)
    pub_date = models.DateField()
    image= models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    Mmsg_id = models.AutoField(primary_key=True)
    Mname = models.CharField(max_length=50)
    Memail = models.CharField(max_length=50)
    Mphone = models.IntegerField(default="")
    Mdesc = models.CharField(max_length=5000,default="")

    def __str__(self):
        return self.Mname
    

class Orders(models.Model):
    Morder_id =models.AutoField(primary_key=True)
    Mamount= models.IntegerField(default=1)
    Mitems_json =models.CharField(max_length=5000)
    Mname =models.CharField(max_length=100)
    Memail =models.EmailField(max_length=100)
    Maddress =models.CharField(max_length=1000)
    Mcity =models.CharField(max_length=500)
    Mstate =models.CharField(max_length=500)
    Mzip_code =models.CharField(max_length=8, default="")
    Mphone = models.CharField(max_length=12, default="")

    def __str__(self):
        return self.Mname
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc =models.CharField(max_length=1000)
    timestamp =models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:35] +"...."
