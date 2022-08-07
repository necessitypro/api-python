import json
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict
from geography.models import Country

from audit.models import Model


@receiver(post_save, sender=Country)
def create_audit(sender, instance, created, **kwargs):
    if created:
        Model.objects.create(
            operation="create",
            data_type="country",
            data_id=instance.id,
            data=model_to_dict(instance),
            user_agent=getattr(instance, "_user_agent", ""),
            remote_addr=getattr(instance, "_remote_addr", ""),
            account=getattr(instance, "_account", None),
        )
    else:
        Model.objects.create(
            operation="update",
            data_type="country",
            data_id=instance.id,
            data=model_to_dict(instance),
            user_agent=getattr(instance, "_user_agent", ""),
            remote_addr=getattr(instance, "_remote_addr", ""),
            account=getattr(instance, "_account", None),
        )
