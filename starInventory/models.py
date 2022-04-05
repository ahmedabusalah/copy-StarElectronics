from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    phoneNumber = models.CharField(null=False, blank=False, max_length=15)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )


class Part(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    stock = models.IntegerField(null=False, blank=False, default=0)
    cost = models.FloatField(null=False, blank=False)


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    price = models.FloatField(null=False, blank=False)
    part = models.ManyToManyField(Part, through='ProductPart')


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through='CustomerOrder')


class CustomerOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('product', 'order'), name='once_per_customer_order')
        ]


class ProductPart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('product', 'part'), name='once_per_product_part')
        ]
