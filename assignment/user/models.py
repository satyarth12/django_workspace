from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
import uuid

from .manager import CustomUserManager

from rest_framework.authtoken.models import Token

# Create your models here.


class CustomUser(AbstractUser, PermissionsMixin):

    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)

    username = models.CharField(
        max_length=50, default='Anonymous', unique=True)

    email = models.EmailField(max_length=254, unique=True)

    is_active = models.BooleanField(default=False, verbose_name="Active",
                                    help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.")
    is_staff = models.BooleanField(default=False, verbose_name="Staff Status",
                                   help_text="Designates whether the user can log into this admin site.")
    is_superuser = models.BooleanField(default=False, verbose_name="Superuser Status",
                                       help_text="Designates that this user has all permissions without explicitly assigning them.")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    class Meta:
        app_label = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def create_auth_token(self):
        """Creates a new authtoken key for a user
        """

        user_token = Token.objects.filter(user=self)

        if user_token.exists():
            # deleting the previous token for one device login only
            user_token.delete()
            return Token.objects.create(user=self).key

        return Token.objects.create(user=self).key
