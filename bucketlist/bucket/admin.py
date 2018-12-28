from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Bucket)
class BucketAdmin(admin.ModelAdmin):
    
    list_display = (
        'created_at',
        'updated_at',
        'completed_at',
        'my_wish',
        'creator',
        'memo',
    )
