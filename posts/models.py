from django.db import models


# ----------------------------------------------------------------
class Post(models.Model):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    title = models.CharField(
        max_length=50,
        verbose_name='Заголовок'
    )
    body = models.TextField(
        max_length=1000,
        verbose_name='Содержание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
