from django.db import models
from django.utils.translation import gettext_lazy as _
from user.validators import PhoneValidator

class Category(models.Model):
    subcategory = models.ForeignKey("SubCategory", on_delete=models.PROTECT)
    title = models.CharField(max_length=100, verbose_name=_('title'))
    image = models.ImageField(upload_to='book-image/', verbose_name=_('image'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))


class SubCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    image = models.ImageField(upload_to='book-image/', verbose_name=_('image'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))


class Contact(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_('first_name'))
    last_name = models.CharField(max_length=100, verbose_name=_('last_name'))
    email = models.EmailField(unique=True,verbose_name=_('email'))
    phone = models.CharField(max_length=14, verbose_name=_('phone'), validators=[PhoneValidator()])