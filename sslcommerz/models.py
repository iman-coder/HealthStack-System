from django.db import models

# Create your models here.


class Payment(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)

    transaction_id = models.CharField(max_length=255, null=True, blank=True)
    val_transaction_id = models.CharField(
        max_length=255, null=True, blank=True)
    currency_amount = models.CharField(max_length=255, null=True, blank=True)
    card_type = models.CharField(max_length=255, null=True, blank=True)
    card_no = models.CharField(max_length=255, null=True, blank=True)
    bank_transaction_id = models.CharField(
        max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    transaction_date = models.CharField(max_length=255, null=True, blank=True)
    currency = models.CharField(max_length=255, null=True, blank=True)
    card_issuer = models.CharField(max_length=255, null=True, blank=True)
    card_brand = models.CharField(max_length=255, null=True, blank=True)

    # String representation of object
    def __str__(self):
        return str(self.name)