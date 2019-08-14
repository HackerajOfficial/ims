from django.contrib import admin
from stock.models import StockDetails


#admin.site.register(StockDetails)
@admin.register(StockDetails)
class StockDetailsAdmin(admin.ModelAdmin):
    list_display    =   ('product_name','category','buying_rate','selling_rate','supplier_name','expire_date')
    list_filter     =   ('category',)
    date_hierarchy  =   ('expire_date')


