from django.db import migrations


def seed_categories_and_products(apps, schema_editor):
    Category = apps.get_model("products", "Category")
    Product = apps.get_model("products", "Product")

    categories = {
        "tech-digital": "Tech & Digital",
        "fashion-lifestyle": "Fashion & Lifestyle",
        "books": "Books",
        "fitness-gym": "Fitness & Gym",
        "gaming": "Gaming",
        "beauty-skincare": "Beauty & Skincare",
    }

    category_map = {}
    for slug, name in categories.items():
        category, _ = Category.objects.update_or_create(
            slug=slug,
            defaults={"name": name},
        )
        category_map[slug] = category

    products = [
        {
            "name": "Wireless Noise-Canceling Headphones",
            "slug": "wireless-noise-canceling-headphones",
            "description": "Premium over-ear headphones with 40-hour battery life.",
            "price": "199.99",
            "category": "tech-digital",
        },
        {
            "name": "Portable 2TB SSD",
            "slug": "portable-2tb-ssd",
            "description": "Ultra-fast USB-C external storage for work and travel.",
            "price": "149.00",
            "category": "tech-digital",
        },
        {
            "name": "Classic Denim Jacket",
            "slug": "classic-denim-jacket",
            "description": "Timeless denim jacket for all-season casual style.",
            "price": "79.50",
            "category": "fashion-lifestyle",
        },
        {
            "name": "Minimal Leather Wallet",
            "slug": "minimal-leather-wallet",
            "description": "Slim handcrafted wallet with RFID protection.",
            "price": "45.00",
            "category": "fashion-lifestyle",
        },
        {
            "name": "Atomic Habits",
            "slug": "atomic-habits-book",
            "description": "A practical guide to building good habits and breaking bad ones.",
            "price": "16.99",
            "category": "books",
        },
        {
            "name": "Deep Work",
            "slug": "deep-work-book",
            "description": "Rules for focused success in a distracted world.",
            "price": "14.99",
            "category": "books",
        },
        {
            "name": "Adjustable Dumbbell Set",
            "slug": "adjustable-dumbbell-set",
            "description": "Space-saving dumbbells with quick weight adjustment.",
            "price": "229.00",
            "category": "fitness-gym",
        },
        {
            "name": "Non-Slip Yoga Mat",
            "slug": "non-slip-yoga-mat",
            "description": "Extra-thick eco-friendly mat for home workouts.",
            "price": "34.99",
            "category": "fitness-gym",
        },
        {
            "name": "Mechanical Gaming Keyboard",
            "slug": "mechanical-gaming-keyboard",
            "description": "RGB backlit keyboard with tactile switches.",
            "price": "89.99",
            "category": "gaming",
        },
        {
            "name": "Wireless Gaming Mouse",
            "slug": "wireless-gaming-mouse",
            "description": "Lightweight high-precision mouse for competitive gaming.",
            "price": "59.99",
            "category": "gaming",
        },
        {
            "name": "Hydrating Face Serum",
            "slug": "hydrating-face-serum",
            "description": "Daily serum with hyaluronic acid for deep hydration.",
            "price": "24.99",
            "category": "beauty-skincare",
        },
        {
            "name": "SPF 50 Sunscreen Gel",
            "slug": "spf-50-sunscreen-gel",
            "description": "Lightweight broad-spectrum sun protection for all skin types.",
            "price": "18.50",
            "category": "beauty-skincare",
        },
    ]

    for item in products:
        Product.objects.update_or_create(
            slug=item["slug"],
            defaults={
                "name": item["name"],
                "description": item["description"],
                "price": item["price"],
                "category": category_map[item["category"]],
                "in_stock": True,
            },
        )


def noop_reverse(apps, schema_editor):
    # Keep seeded data on rollback to avoid deleting user-edited records.
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_categories_and_products, noop_reverse),
    ]
