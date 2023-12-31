from django.contrib.auth.models import AbstractUser


# ----------------------------------------------------------------
class User(AbstractUser):
    """
    Model representing a user
    """
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name: str = 'Пользователь'
        verbose_name_plural: str = 'Пользователи'
