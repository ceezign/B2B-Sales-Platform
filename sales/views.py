from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product, ProductRequest
from .forms import ProductRequestForm
from .emails import send_company_notification, send_customer_confirmation


def product_list(request):
    """Public product listing — only active products."""
    products = Product.objects.filter(is_active=True)
    return render(request, 'sales/product_list.html', {'products': products})


def product_detail(request, slug):
    """Product detail page with B2B request form."""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    form = ProductRequestForm()

    if request.method == 'POST':
        form = ProductRequestForm(request.POST)
        if form.is_valid():
            product_request = form.save(commit=False)
            product_request.product = product
            product_request.save()

            # Send emails
            send_company_notification(product_request)
            send_customer_confirmation(product_request)

            messages.success(
                request,
                f'Your request has been submitted successfully. '
                f'Reference ID: {str(product_request.request_id).upper()[:8]}. '
                f'We will contact you shortly.'
            )
            return redirect('product_list')

    return render(request, 'sales/product_detail.html', {
        'product': product,
        'form': form,
    })
