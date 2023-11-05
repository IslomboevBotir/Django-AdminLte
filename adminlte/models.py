from django.db import models


class AxCoreLeadsModel(models.Model):
    name = models.CharField(max_length=100, default='undefined')
    phone = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    book_date = models.DateField(null=True)
    ip = models.CharField(max_length=255)
    message = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    data = models.JSONField(null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    session_id = models.CharField(max_length=200, null=True, blank=True)
    hash_data = models.TextField(null=True)

    class Meta:
        db_table = 'ax_core_axleads'
