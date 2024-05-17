from django.db import models
from auditlog.registry import auditlog


class ALModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    json_content = models.JSONField(
        verbose_name="Content",
        blank=True,
        null=True,
        help_text="Some json content",
    )


auditlog.register(ALModel)