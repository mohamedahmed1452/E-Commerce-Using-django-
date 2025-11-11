from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE)

    Brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} x {self.product.name}"



class Review(models.Model):
        product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="reviews")
        name = models.CharField(max_length=255)
        description = models.TextField()
        date=models.DateField(auto_now_add=True)

        def __str__(self):
          return f"Order of {self.quantity} x {self.product.name}"




