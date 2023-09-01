from .models import Wallet, Account
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from PIL import Image, ImageDraw, ImageFont
import qrcode
import random
import string
User = settings.AUTH_USER_MODEL

@receiver(post_save, sender=User)
def create_account_number(sender, instance, created, **kwargs):
    if created:
        random_number = ''.join(random.choices(string.digits, k=10))

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4
        )
        qr.add_data(f"User: {instance.username}\nRandom: {random_number}")
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color='black', back_color='white')

        draw = ImageDraw.Draw(qr_img)
        text = random_number
        font = ImageFont.load_default()
        text_width, text_height = draw.textsize(text, font)
        qr_width, qr_height = qr_img.size
        text_position = (( qr_width - text_width ) // 2, ( qr_height - text_height ) // 2)
        draw.text(text_position, text, fill='black', font=font)

        #qr_code_content = f"cullize_{instance.username}"
        #img = qrcode.make(qr_code_content)

        img_dir = os.path.join(settings.MEDIA_ROOT, 'qrcode')
        os.makedirs(img_dir, exist_ok=True)

        img_path = os.path.join(img_dir, f'{instance.username}_qrcode.png')
        qr_img.save(img_path)
        Account.objects.create(
            user=instance, qr_code=os.path.relpath(img_path, settings.MEDIA_ROOT),
            account_id=random_number
            )

@receiver(post_save, sender=User)
def create_account_number(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(
                user=instance,
            )