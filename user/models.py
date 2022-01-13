from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator, MinLengthValidator
from django.db.models import *
from django.utils.translation import gettext_lazy as _
from .validators import GenderValidator, PhoneValidator
# Create your models here.


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
        """Create and save a User with the given phone and password."""
        if not phone:
            raise ValueError('The given phone must be set')
        self.phone = phone
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, password=None, **extra_fields):
        """Create and save a regular User with the given phone and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password, **extra_fields):
        """Create and save a SuperUser with the given phone and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_access_level', 1)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(phone, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = EmailField(unique=True, null=True)
    
    middle_name = CharField(max_length=60, null=True, blank=True)
    phone = CharField(_('phone number'), unique=True, max_length=13, 
        # validators=[PhoneValidator()]
    ) 
    image = ImageField(upload_to="user-images/", blank=True, default="default-user.png")
    gender = CharField(
        max_length=50,
        # validators=[GenderValidator()],
        choices=(
            ("male", _("Male")),
            ("female", _("Female"))

        ), null=True
    )

    join_date = DateField(auto_now_add=True)
    end_date = DateField(null=True, blank=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.phone)
