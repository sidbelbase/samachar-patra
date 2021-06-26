
from django.db import models


class SubscriptionEmail(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "subscription_emails"

    def __str__(self):
        return self.email
