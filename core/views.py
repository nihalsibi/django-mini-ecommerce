from django.shortcuts import render
from products.models import Category


def home(request):
    """Home page view for the e-commerce site."""
    categories = Category.objects.filter(products__isnull=False).distinct().order_by("name")
    return render(request, "home.html", {"categories": categories})
