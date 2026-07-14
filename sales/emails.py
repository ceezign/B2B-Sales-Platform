from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string


def send_company_notification(product_request):
    """Send notification email to company admin on new request."""
    subject = f"[New B2B Request] {product_request.company_name} — {product_request.product.name}"
    context = {
        'request': product_request,
        'company_name': settings.COMPANY_NAME,
    }
    html_message = render_to_string('emails/company_notification.html', context)
    plain_message = render_to_string('emails/company_notification.txt', context)
    try:
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.COMPANY_ADMIN_EMAIL],
            html_message=html_message,
            fail_silently=False,
        )
    except Exception as e:
        print(f"[EMAIL ERROR] Company notification failed: {e}")


def send_customer_confirmation(product_request):
    """Send confirmation email to customer after submitting request."""
    subject = f"Request Received — {product_request.product.name} | {settings.COMPANY_NAME}"
    context = {
        'request': product_request,
        'company_name': settings.COMPANY_NAME,
    }
    html_message = render_to_string('emails/customer_confirmation.html', context)
    plain_message = render_to_string('emails/customer_confirmation.txt', context)
    try:
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[product_request.email],
            html_message=html_message,
            fail_silently=False,
        )
    except Exception as e:
        print(f"[EMAIL ERROR] Customer confirmation failed: {e}")


def send_status_update(product_request):
    """Send status update email to customer when admin changes status."""
    status_display = dict(product_request.STATUS_CHOICES).get(product_request.status, product_request.status)
    subject = f"Request Update — {status_display} | {settings.COMPANY_NAME}"
    context = {
        'request': product_request,
        'company_name': settings.COMPANY_NAME,
        'status_display': status_display,
    }
    html_message = render_to_string('emails/status_update.html', context)
    plain_message = render_to_string('emails/status_update.txt', context)
    try:
        send_mail(
            subject=subject,
            message=plain_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[product_request.email],
            html_message=html_message,
            fail_silently=False,
        )
    except Exception as e:
        print(f"[EMAIL ERROR] Status update failed: {e}")
