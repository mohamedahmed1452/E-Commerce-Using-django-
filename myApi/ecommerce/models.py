from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="products"
    )
    Brand = models.ForeignKey(
        "Brand", on_delete=models.CASCADE, related_name="products"
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]


class Order(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="orders"
    )
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} x {self.product.name}"

    class Meta:
        ordering = ["-order_date"]


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews"
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=5, choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"Review for {self.product.name} by {self.name}"

    class Meta:
        ordering = ["-date"]


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    products = models.ManyToManyField("Product", related_name="tags")

    def __str__(self):
        return self.name
