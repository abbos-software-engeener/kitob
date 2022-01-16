from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from category.models import Category, SubCategory
from user.models import User
from user.validators import PhoneValidator


class Book(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100, verbose_name=_('title'))
    isbn = models.IntegerField(default=0, verbose_name=_('isbn'))
    author = models.CharField(max_length=100, verbose_name=_('author'))
    publishing = models.CharField(max_length=150, verbose_name = _('publishing'))
    description = RichTextField(verbose_name= _('description'))
    count_sell = models.IntegerField(verbose_name=_('count_sell'))
    price = models.BigIntegerField(default=0, verbose_name=_('price'))
    seen = models.BooleanField(default=False, verbose_name=_('seen'))
    image = models.ImageField(upload_to='book-image/', verbose_name=_('image'))
    rating = models.IntegerField(default=0, verbose_name=_('rating'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('book')
        verbose_name_plural = _('books')


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('user'))
    address = models.TextField(verbose_name=('address'))
    book = models.ForeignKey(Book, on_delete=models.PROTECT, verbose_name=_('book'))
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name=_('category'))
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT, verbose_name=_('subcategory'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))


class Achievement(models.Model):
    title = models.CharField(max_length=100,verbose_name=_('title'))
    description = models.TextField(verbose_name=_('description'))
    image = models.ImageField(upload_to='AboutUs/', verbose_name='image')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))


class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('title'))
    address = models.TextField(verbose_name=_("address"))
    phone = models.CharField(max_length=14,  verbose_name=_("phone"), validators=[PhoneValidator()])
    email = models.EmailField(unique=True, verbose_name=_("email"))
    achievements = models.ForeignKey(Achievement, on_delete=models.PROTECT, verbose_name=_('achievements'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('about-us')
        verbose_name_plural = _('about-us')


class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name=_('user'))
    booking = models.ForeignKey(Booking, on_delete=models.PROTECT, verbose_name=_('booking'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('updated_at'))
