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

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        return super(Customer, self).save(*args, **kwargs)


class Part(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    stock = models.IntegerField(null=False, blank=False, default=0)
    cost = models.FloatField(null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(null=False, blank=False, max_length=20)
    price = models.FloatField(null=False, blank=False)
    part = models.ManyToManyField(Part, through='ProductPart')

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through='OrderProduct')

    def __str__(self):
        return f"{self.id} - {self.customer.name} order"


class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)

    def __str__(self):
        return f"{self.order.id} - {self.product.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('product', 'order'), name='once_per_order_product')
        ]


class ProductPart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=1)

    def __str__(self):
        return f"{self.product.name} - {self.part.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('product', 'part'), name='once_per_product_part')
        ]
