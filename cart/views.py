from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from accounts.forms import AddressForm
from accounts.models import Address
from items.models import Item

from .models import Cart, CartItem


def _get_or_create_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


@login_required
def add_to_cart(request, item_id):
    if request.method != "POST":
        return redirect("items")

    item = get_object_or_404(Item, pk=item_id, is_active=True)
    cart = _get_or_create_cart(request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart_detail")


@login_required
def cart_detail(request):
    cart = Cart.objects.filter(user=request.user).first()

    return render(
        request,
        "cart.html",
        {
            "cart": cart,
        },
    )


@login_required
def update_cart_item(request, item_id):
    if request.method != "POST":
        return redirect("cart_detail")

    cart = _get_or_create_cart(request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, item_id=item_id)

    try:
        quantity = int(request.POST.get("quantity", cart_item.quantity))
    except (TypeError, ValueError):
        quantity = cart_item.quantity

    if quantity <= 0:
        cart_item.delete()
    else:
        cart_item.quantity = quantity
        cart_item.save()

    return redirect("cart_detail")


@login_required
def remove_cart_item(request, item_id):
    if request.method != "POST":
        return redirect("cart_detail")

    cart = _get_or_create_cart(request.user)
    CartItem.objects.filter(cart=cart, item_id=item_id).delete()
    return redirect("cart_detail")


@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        return redirect("items")

    address = Address.objects.filter(user=request.user).first()

    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            saved_address = form.save(commit=False)
            saved_address.user = request.user
            saved_address.save()
            return redirect("payment")
    else:
        form = AddressForm(instance=address)

    return render(
        request,
        "checkout.html",
        {
            "cart": cart,
            "form": form,
        },
    )


@login_required
def payment(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart or not cart.items.exists():
        return redirect("items")

    address = Address.objects.filter(user=request.user).first()
    if not address:
        return redirect("checkout")

    payment_completed = False
    if request.method == "POST":
        cart.items.all().delete()
        payment_completed = True

    return render(
        request,
        "payment.html",
        {
            "cart": cart,
            "address": address,
            "payment_completed": payment_completed,
        },
    )
