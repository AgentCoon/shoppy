from django.contrib import admin
from .models import User
from .models import Product
from .models import ProductCategory
from .models import ProductReview
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    fields = ["name", "category", "description", "price", "created_by"]
    list_display = ("name", "category", "price", "created_at", "created_by")
    search_fields = ["name", "category__name"]
    list_filter = ("category__name",)


class ProductReviewAdmin(admin.ModelAdmin):
    fields = ["product", "content", "rating", "created_by"]
    list_display = ("product", "rating", "created_at", "created_by")
    search_fields = ["product__name", "rating"]
    list_filter = ("product__category__name",)

admin.site.register(Product, ProductAdmin)
admin.site.register(User)
admin.site.register(ProductCategory)
admin.site.register(ProductReview, ProductReviewAdmin)