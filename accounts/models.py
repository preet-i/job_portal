from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('employee', 'Employee'),
        ('employer', 'Employer'),
    ]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='employee')

    groups = models.ManyToManyField(
        Group,
        related_name='custom_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )
