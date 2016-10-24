import string
import random

from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    EMAIL_FIELD = 'email'
    CONTACT_FIELD = 'contact_number'
    USERNAME_FIELD = 'username'

    def create(self, data):
        username = data.get("username", None)

        if not username:
            username = generate_random_username_or_password()
            data["username"] = username

        if "email" in data and data["email"] != "":
            data["email"] = self.normalize_email(data.get("email"))
        else:
            data["email"] = None
        password = data.get("password", generate_random_username_or_password())
        user = self.model(**data)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        """
        Creates and saves a Superuser
        """
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
        kwargs['is_active'] = True

        return self.create(kwargs)

    def get_by_natural_key(self, username):
        if username.find("@") != -1:
            username = username.lower()
            return self.get(**{CustomUserManager.EMAIL_FIELD: username})
        elif username.isdigit():
            return self.get(**{CustomUserManager.CONTACT_FIELD: username})
        else:
            return self.get(**{CustomUserManager.USERNAME_FIELD: username})


def generate_random_username_or_password(size=10, chars=string.ascii_uppercase + string.digits):
    """
    Autogenerate username or password if not found
    """
    return ''.join(random.choice(chars) for _ in range(size))
