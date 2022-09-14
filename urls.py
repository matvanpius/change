from django.urls import path
from .import views

urlpatterns = [
    path('web/', views.index, name='index'),
    path('web/signup', views.signup, name='signup'),
    path('web/signin', views.signin, name='signin'),
    path('web/signout', views.signout, name='signout'),
    path('web/home', views.home, name='home'),
    path('web/cart', views.cart, name='cart'),
    path('web/products', views.products, name='products'),
    path('web/item', views.item, name='item'),
    path('web/main', views.main, name='main'),
    path('web/summary', views.summary, name='summary'),
    path('web/allproducts', views.allproducts, name='allproducts'),
    path('web/packages', views.packages, name='packages'),
    path('web/vegetable', views.vegetable, name='vegetable'),
    path('web/fruit', views.fruit, name='fruit'),
    path('web/oil', views.oil, name='oil'),
    path('web/snack', views.snack, name='snack'),
    path('web/spice', views.spice, name='spice'),
    path('web/legumes', views.legumes, name='legumes'),
    path('update_item', views.updateItem, name='update_item'),





    
    
    
]
