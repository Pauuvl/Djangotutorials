from django.urls import path
from .views import CartView, CartRemoveAllView
from .views import (
    CartRemoveAllView,
    HomePageView,
    AboutPageView,
    ContactPageView,
    ProductIndexView,
    ProductShowView,
    ProductCreateView)
from .factories import ImageViewFactory
from .utils import ImageLocalStorage
from django.urls import path
from .views import ImageViewNoDI


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('products/', ProductIndexView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:id>/', ProductShowView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart_index'),
    path('cart/add/<str:product_id>', CartView.as_view(), name='cart_add'),
    path('cart/removeAll', CartRemoveAllView.as_view(), name='cart_removeAll'),
    path('image/', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_index'),
    path('image/save', ImageViewFactory(ImageLocalStorage()).as_view(), name='image_save'),
     path('image-not-di/', ImageViewNoDI.as_view(), name='imagenodi_index'),
    path('image-not-di/save/', ImageViewNoDI.as_view(), name='imagenodi_save')
]
