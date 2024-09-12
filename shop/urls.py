from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('Category/<slug:category_title>', views.subcategory, name='subcategory'),
    path('<slug:subcategory_category_name>/<slug:subcategory_title>',
         views.products, name='products'),
    path('BLINK/<int:product_id>',
         views.item, name='item'),
    path('Account', views.account, name='account'),
    path('Registration', views.sign_up, name='sign_up'),






]
