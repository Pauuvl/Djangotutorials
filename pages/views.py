from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django.urls import reverse
from django import forms
from django.core.exceptions import ValidationError  # <-- Agregar esta línea

# ---------- PAGES ----------

class HomePageView(TemplateView):
    template_name = 'pages/home.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page",
            "author": "Developed by: Paulina Velásquez",
        })
        return context


class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact - Online Store",
            "email": "onlinestore@gmail.com",
            "phone": "+57 234567890",
            "address": "123 calle 34, Medellín",
        })
        return context


# ---------- PRODUCTS ----------

class Product:
    products = [
        {"id": "1", "name": "TV", "description": "Best TV", "price": 120},
        {"id": "2", "name": "iPhone", "description": "Best iPhone", "price": 999},
        {"id": "3", "name": "Chromecast", "description": "Best Chromecast", "price": 80},
        {"id": "4", "name": "Glasses", "description": "Best Glasses", "price": 60},
    ]


class ProductIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        return render(request, self.template_name, {
            "title": "Products - Online Store",
            "subtitle": "List of products",
            "products": Product.products
        })


class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        try:
            product = Product.products[id - 1]
        except (IndexError, ValueError):
            return HttpResponseRedirect(reverse('home'))

        return render(request, self.template_name, {
            "title": product["name"],
            "product": product
        })


# ---------- FORM ----------

class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise ValidationError("El precio debe ser mayor a cero.")
        return price


class ProductCreateView(View):
    template_name = 'products/create.html'

    def get(self, request):
        form = ProductForm()
        return render(request, self.template_name, {
            "title": "Create product",
            "form": form
        })

    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():
            Product.products.append({
                "id": str(len(Product.products) + 1),
                "name": form.cleaned_data["name"],
                "description": "New product",
                "price": form.cleaned_data["price"],
            })
            return HttpResponseRedirect(reverse('products'))

        return render(request, self.template_name, {
            "title": "Create product",
            "form": form
        })