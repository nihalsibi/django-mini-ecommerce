def cart_count(request):
    """Add cart_item_count to template context for the header."""
    cart = request.session.get('cart') or {}
    total_items = sum(cart.values())
    cart_bounce = request.session.pop('cart_bounce', False)
    return {
        'cart_item_count': total_items,
        'cart_bounce': cart_bounce,
    }
