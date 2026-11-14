from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from .models import Product, Order, OrderItem


def _cart_details(request):
    cart = request.session.get("cart", {})
    items, total = [], Decimal("0.00")
    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(pk=int(product_id))
        except (Product.DoesNotExist, ValueError):
            continue
        quantity = max(1, int(quantity))
        line_total = product.price * quantity
        items.append({"product": product, "quantity": quantity, "line_total": line_total})
        total += line_total
    return items, total


def home(request):
    query = request.GET.get("q", "").strip()
    products = Product.objects.all()
    if query:
        products = products.filter(name__icontains=query) | products.filter(category__icontains=query)
    return render(request, "shop/home.html", {"products": products.distinct(), "query": query})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "shop/product_detail.html", {"product": product})


def add_to_cart(request, product_id):
    if request.method != "POST":
        return redirect("home")
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get("cart", {})
    key = str(product.id)
    current = int(cart.get(key, 0))
    if product.stock < 1:
        messages.error(request, "This product is out of stock.")
    elif current >= product.stock:
        messages.warning(request, "You have reached the available stock limit.")
    else:
        cart[key] = current + 1
        request.session["cart"] = cart
        messages.success(request, f"{product.name} added to your cart.")
    return redirect(request.POST.get("next") or "cart")


def cart(request):
    items, total = _cart_details(request)
    return render(request, "shop/cart.html", {"items": items, "total": total})


def update_cart(request, product_id):
    if request.method == "POST":
        cart_data = request.session.get("cart", {})
        key = str(product_id)
        if key in cart_data:
            try:
                quantity = int(request.POST.get("quantity", 1))
                product = Product.objects.get(pk=product_id)
                if quantity <= 0:
                    cart_data.pop(key, None)
                elif quantity <= product.stock:
                    cart_data[key] = quantity
                else:
                    messages.error(request, f"Only {product.stock} item(s) are available.")
            except (ValueError, Product.DoesNotExist):
                cart_data.pop(key, None)
            request.session["cart"] = cart_data
    return redirect("cart")


def remove_from_cart(request, product_id):
    if request.method == "POST":
        cart_data = request.session.get("cart", {})
        cart_data.pop(str(product_id), None)
        request.session["cart"] = cart_data
        messages.info(request, "Item removed from cart.")
    return redirect("cart")


@login_required
def checkout(request):
    items, total = _cart_details(request)
    if not items:
        messages.info(request, "Your cart is empty.")
        return redirect("home")
    if request.method == "POST":
        full_name = request.POST.get("full_name", "").strip()
        email = request.POST.get("email", "").strip()
        phone = request.POST.get("phone", "").strip()
        address = request.POST.get("address", "").strip()
        if not all([full_name, email, phone, address]):
            messages.error(request, "Please complete all delivery details.")
            return render(request, "shop/checkout.html", {"items": items, "total": total})
        with transaction.atomic():
            for item in items:
                product = Product.objects.select_for_update().get(pk=item["product"].pk)
                if product.stock < item["quantity"]:
                    messages.error(request, f"Not enough stock for {product.name}. Please update your cart.")
                    return redirect("cart")
            order = Order.objects.create(
                user=request.user, full_name=full_name, email=email, phone=phone,
                address=address, total_amount=total
            )
            for item in items:
                product = Product.objects.get(pk=item["product"].pk)
                OrderItem.objects.create(
                    order=order, product=product, product_name=product.name,
                    price=product.price, quantity=item["quantity"]
                )
                product.stock -= item["quantity"]
                product.save(update_fields=["stock"])
        request.session["cart"] = {}
        messages.success(request, f"Order #{order.pk} placed successfully!")
        return redirect("order_history")
    return render(request, "shop/checkout.html", {"items": items, "total": total})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Your account has been created.")
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "shop/register.html", {"form": form})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).prefetch_related("items")
    return render(request, "shop/orders.html", {"orders": orders})
