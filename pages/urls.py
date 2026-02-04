from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    ProductIndexView,
    ProductShowView,
    ProductCreateView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    path('products/', ProductIndexView.as_view(), name='products'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:id>/', ProductShowView.as_view(), name='product_detail'),
]
