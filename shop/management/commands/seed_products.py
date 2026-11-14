from django.core.management.base import BaseCommand
from shop.models import Product

SAMPLES = [
    ("Classic White Sneakers", "Comfortable everyday sneakers with a clean design.", "1499.00", "Footwear", 18, "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=700"),
    ("Minimal Wrist Watch", "A simple everyday watch with a modern finish.", "2199.00", "Accessories", 12, "https://images.unsplash.com/photo-1524592094714-0f0654e20314?w=700"),
    ("Everyday Backpack", "A spacious backpack for college, work and travel.", "999.00", "Bags", 20, "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=700"),
    ("Wireless Headphones", "Enjoy your favourite music with comfortable ear cushions.", "1799.00", "Electronics", 15, "https://images.unsplash.com/photo-150 자?w=700"),
    ("Ceramic Coffee Mug", "A durable ceramic mug for your daily coffee or tea.", "299.00", "Home", 30, "https://images.unsplash.com/photo-1514228742587-6b1558f6023d?w=700"),
    ("Classic Sunglasses", "Lightweight sunglasses for a timeless everyday look.", "799.00", "Accessories", 16, "https://images.unsplash.com/photo-1511499767150-a48a237f0083?w=700"),
]

class Command(BaseCommand):
    help = "Create sample products for the store"

    def handle(self, *args, **options):
        for name, description, price, category, stock, image_url in SAMPLES:
            if " " not in image_url or "unsplash.com" in image_url:
                Product.objects.get_or_create(
                    name=name,
                    defaults={"description": description, "price": price, "category": category,
                              "stock": stock, "image_url": image_url}
                )
        self.stdout.write(self.style.SUCCESS("Sample products are ready."))
