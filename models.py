from msilib.schema import Property
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  null=True, blank=True,related_name="customer")
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    
    def __str__(self):
       return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=False, null=True, blank=False)
    digital =models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField( null=True, blank=True)

    def __str__(self):
       return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
        
class All(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=False, null=True, blank=False)
    digital =models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField( null=True, blank=True)

    def __str__(self):
       return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Mixed(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=False, null=True, blank=False)
    digital =models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField( null=True, blank=True)

    def __str__(self):
       return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Vegetable(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=False, null=True, blank=False)
    digital =models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField( null=True, blank=True)

    def __str__(self):
       return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Spice(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=False, null=True, blank=False)
    digital =models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField( null=True, blank=True)

    def __str__(self):
       return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Snack(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=False, null=True, blank=False)
    digital =models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField( null=True, blank=True)

    def __str__(self):
       return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Oil(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=False, null=True, blank=False)
    digital =models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField( null=True, blank=True)

    def __str__(self):
       return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Legumes(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=False, null=True, blank=False)
    digital =models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField( null=True, blank=True)

    def __str__(self):
       return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Fruit(models.Model):
    
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(default=False, null=True, blank=False)
    digital =models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField( null=True, blank=True)

    def __str__(self):
       return self.name
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

        
class Order(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    date_order=models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
       return str(self.id)
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping        

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product= models.ForeignKey(Product, on_delete=models.SET_NULL,blank=True,null=True)
    order= models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,null=True, blank=False)
    date_order=models.DateField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer= models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
    order= models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True,null=True)
    email = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    division= models.CharField(max_length=200, null=True)
    address= models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)

    def __str__(self):
       return str(self.address)

class UpdateOrder(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    desc = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id)

   


