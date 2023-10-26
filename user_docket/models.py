from django.contrib.postgres.fields import ArrayField
from django.db import models
import uuid
    

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    po_no =  ArrayField(models.CharField(max_length=750), blank=True)
    
    def __str__(self):
        return self.name
    
class Worker_docket(models.Model):
    name = models.CharField(max_length=200)
    start_time = models.TimeField(auto_now_add=False, auto_now=False)
    end_time = models.TimeField(auto_now_add=False, auto_now=False)
    work_hours = models.IntegerField()
    wages = models.IntegerField(default=0)
    supplier_name = models.ForeignKey(Supplier, related_name='supplier', on_delete=models.CASCADE, null=True, blank=True)
    po_no = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
