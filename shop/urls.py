from django.urls import path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.index, name='index'),
    path('Category/<slug:category_title>', views.subcategory, name='subcategory'),
    path('<slug:subcategory_category_name>/<slug:subcategory_title>',
         views.products, name='products'),
    path('BLINK/<slug:product_category>/<slug:product_category_name>/<int:product_id>',
         views.item, name='item'),
    path('profile/', views.profile_view, name='profile'),
    path('loged_out/', views.user_logout, name='loged_out'),
    






]
