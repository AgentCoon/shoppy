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
    fieldsets = [
        (None, {"fields": ["product", "content", "rating"]}),
        ("Date information", {"fields": ["created_by", "created_at"], "classes": ["collapse"]}),
    ]

admin.site.register(Product, ProductAdmin)
admin.site.register(User)
admin.site.register(ProductCategory)
admin.site.register(ProductReview, ProductReviewAdmin)