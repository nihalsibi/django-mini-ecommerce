from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Product, Category


def product_list(request):
    """Display list of all products."""
    categories = Category.objects.filter(products__isnull=False).distinct().order_by("name")
    selected_category_slug = request.GET.get("category", "").strip()
    search_query = request.GET.get("q", "").strip()

    products = Product.objects.select_related("category")
    if selected_category_slug:
        products = products.filter(category__slug=selected_category_slug)
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query)
            | Q(description__icontains=search_query)
            | Q(category__name__icontains=search_query)
        )

    context = {
        "products": products,
        "categories": categories,
        "selected_category_slug": selected_category_slug,
        "search_query": search_query,
    }
    return render(request, "product_list.html", context)


def product_detail(request, slug):
    """Display single product detail."""
    product = get_object_or_404(Product, slug=slug)
    categories = Category.objects.filter(products__isnull=False).distinct().order_by("name")
    return render(request, "product.html", {"product": product, "categories": categories})
