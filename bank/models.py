from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Account(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='qrcode')
    account_id = models.IntegerField(editable=False, unique=True)
    
    def __str__(self):
        return str(self.user)


class Wallet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def __str__(self):
        return str(self.user)

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    qr_code_image = models.FileField(upload_to='success_transaction')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            random_alphabet = ''.join(random.choices(string.ascii_lowercase, k=20))
            self.slug = slugify(self.random_alphabet)
        super().save(*args, **kwargs)