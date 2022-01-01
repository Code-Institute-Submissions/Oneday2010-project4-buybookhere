from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('books'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K81yOIeaCsGdWpZnwy9DcLfLaLHWYdD8xg7lrXjAGU88j7ibMKaI6yxiZcpjDBsumNg0rWZ1hzJV6CWcJuqETxl00oTrsCGqS',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)