# Django
from django.db import models
from django.contrib.auth.models import AbstractUser

# Core
from core.base_model import FacturaModel


class User(AbstractUser, FacturaModel):
    email = models.EmailField(
        'Email',
        unique=True,
        error_messages={
            'unique': 'Ya existe un usuario con este email.'
        }
    )

    address = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        db_table = 'user'
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

        permissions = (
            ('view_profile', 'Ver Perfil'),
        )