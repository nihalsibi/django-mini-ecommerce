from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product


def _get_cart(request):
    """Get cart from session. Cart is {product_id: quantity}."""
    cart = request.session.get('cart')
    if cart is None:
        request.session['cart'] = {}
        cart = {}
    return request.session['cart']


def cart_view(request):
    """Display the cart page with items, quantities, and total."""
    cart = _get_cart(request)
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(pk=int(product_id), in_stock=True)
            line_total = product.price * quantity
            total += line_total
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'line_total': line_total,
            })
        except (Product.DoesNotExist, ValueError):
            continue

    context = {
        'cart_items': cart_items,
        'cart_total': total,
    }
    return render(request, 'cart.html', context)


def add_to_cart(request, product_id):
    """Add a product to the cart (quantity 1 or from GET param)."""
    product = get_object_or_404(Product, pk=product_id, in_stock=True)
    cart = _get_cart(request)
    key = str(product_id)
    qty = int(request.GET.get('quantity', 1))
    if qty < 1:
        qty = 1
    cart[key] = cart.get(key, 0) + qty
    request.session['cart'] = cart
    request.session['cart_bounce'] = True
    request.session.modified = True
    messages.success(request, f'"{product.name}" added to cart.')
    return redirect('cart:cart')


def update_cart(request, product_id):
    """Update quantity for a cart item. POST: quantity (0 to remove)."""
    if request.method != 'POST':
        return redirect('cart:cart')
    cart = _get_cart(request)
    key = str(product_id)
    try:
        quantity = int(request.POST.get('quantity', 0))
    except ValueError:
        quantity = 0
    if quantity <= 0:
        cart.pop(key, None)
        messages.success(request, 'Item removed from cart.')
    else:
        product = get_object_or_404(Product, pk=product_id)
        cart[key] = quantity
        messages.success(request, 'Cart updated.')
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('cart:cart')


def remove_from_cart(request, product_id):
    """Remove one product from the cart."""
    cart = _get_cart(request)
    key = str(product_id)
    if key in cart:
        product = get_object_or_404(Product, pk=product_id)
        del cart[key]
        request.session['cart'] = cart
        request.session.modified = True
        messages.success(request, f'"{product.name}" removed from cart.')
    return redirect('cart:cart')
