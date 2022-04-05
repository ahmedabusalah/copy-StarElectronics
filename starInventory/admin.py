from django.contrib import admin

# Register your models here.
from starInventory.models import Customer, Product, Part, Order, ProductPart

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Part)
admin.site.register(Order)
admin.site.register(ProductPart)
