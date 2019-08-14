from django.db import models
from category.models import Category
from supplier.models import Supplier

class StockDetails(models.Model):
    product_name        =   models.TextField(verbose_name="product_name")
    category            =   models.OneToOneField(Category, to_field='category_name', on_delete=models.SET_NULL, null=True)
    buying_rate         =   models.IntegerField()
    selling_rate        =   models.IntegerField()
    supplier_name       =   models.ForeignKey(Supplier,  on_delete=models.SET_NULL, null=True)
    expire_date         =   models.DateField()

    class Meta:
        verbose_name_plural =   "StockDetails"
        db_table            =   "stock_db"
