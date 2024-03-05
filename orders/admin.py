from django.contrib import admin

from orders.models import Order, Payment, OrderProduct


# Register your models here.

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('payment', 'user', 'product', 'product_price', 'quantity',  'order')
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'phone', 'email', 'city', 'order_total', 'tax', 'status', 'is_ordered']
    list_filter = ('status', 'is_ordered')
    search_fields = ('order_number', 'first_name', 'last_name', 'email', 'phone')
    list_per_page = 20
    inlines = [OrderProductInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(OrderProduct)
