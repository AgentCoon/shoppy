from django.db import models
from datetime import datetime


class User(models.Model):
    username = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.username


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % self.name


class Product(models.Model):
    created_by = models.ForeignKey(User, related_name="products")
    category = models.ForeignKey(ProductCategory, related_name="products")
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now)
    price = models.FloatField()
    description = models.CharField(max_length=500)

    def __unicode__(self):
        return u'%s' % self.name


class ProductReview(models.Model):
    created_by = models.ForeignKey(User, related_name="product_reviews")
    product = models.ForeignKey(Product, related_name="reviews")
    content = models.CharField(max_length=500)
    rating = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)

    def __unicode__(self):
        return u'%s - %s' % (self.created_by.username, self.product.name)
