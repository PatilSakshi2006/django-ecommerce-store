# Generated for the Simple E-commerce Store demo.
import django.conf
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = [migrations.swappable_dependency(django.conf.settings.AUTH_USER_MODEL)]
    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=180)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("image_url", models.URLField(blank=True)),
                ("stock", models.PositiveIntegerField(default=10)),
                ("category", models.CharField(default="General", max_length=80)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("full_name", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=20)),
                ("address", models.TextField()),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("status", models.CharField(choices=[("Pending", "Pending"), ("Processing", "Processing"), ("Shipped", "Shipped"), ("Delivered", "Delivered"), ("Cancelled", "Cancelled")], default="Pending", max_length=20)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="orders", to=django.conf.settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ["-created_at"]},
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("product_name", models.CharField(max_length=180)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("order", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="items", to="shop.order")),
                ("product", models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to="shop.product")),
            ],
        ),
    ]
