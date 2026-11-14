from django.contrib import admin
from .models import Product, Order, OrderItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "stock", "created_at")
    search_fields = ("name", "category")
    list_filter = ("category",)
    prepopulated_fields = {"slug": ("name",)}

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ("product", "product_name", "price", "quantity")

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "full_name", "total_amount", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("full_name", "email", "user__username")
    inlines = [OrderItemInline]
