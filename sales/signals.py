from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import ProductRequest
from .emails import send_status_update


@receiver(pre_save, sender=ProductRequest)
def notify_status_change(sender, instance, **kwargs):
    """Trigger status update email when admin changes the request status."""
    if not instance.pk:
        # New object — skip (confirmation email handled in view)
        return

    try:
        previous = ProductRequest.objects.get(pk=instance.pk)
    except ProductRequest.DoesNotExist:
        return

    if previous.status != instance.status:
        send_status_update(instance)
