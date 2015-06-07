from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /shoppy/product_id/
    url(r'^(?P<product_id>[0-9]+)/$', views.product, name='product'),
    # ex: /shoppy/product_id/
    url(r'^(?P<product_id>[0-9]+)/review/$', views.product_review, name='review'),
]


