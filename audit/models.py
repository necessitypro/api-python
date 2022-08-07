from tabnanny import verbose
from django.db import models
from uuid import uuid4

from authentication.models import Account

OPERATION = [("create", "Create"), ("update", "Update"), ("delete", "Delete")]


class Model(models.Model):
    """model model"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    operation = models.CharField(max_length=255, choices=OPERATION, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True, editable=False)
    account = models.ForeignKey(Account, on_delete=models.RESTRICT, editable=False)
    data_type = models.CharField(max_length=255, editable=False)
    data_id = models.UUIDField(editable=False)
    data = models.JSONField(editable=False)
    user_agent = models.CharField(max_length=255, editable=False)
    remote_addr = models.CharField(max_length=255, editable=False)

    class Meta:
        ordering = ["-timestamp"]
        db_table = "audit_model"
        verbose_name = "Model"
        verbose_name_plural = "Models"

    def __str__(self):
        return self.data_type
