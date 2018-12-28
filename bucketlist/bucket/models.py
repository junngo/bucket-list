from django.db import models
from bucketlist.users import models as user_models

# Create your models here.

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Bucket(TimeStampedModel):

    """ Bucket Model """

    my_wish = models.CharField(max_length=140)
    memo = models.TextField(null=True, blank=True)
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.CASCADE, related_name='buckets')

    def __str__(self):
        return self.my_wish
