import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

DEFAULT_USER_ID = get_user_model()


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    cover = models.ImageField(upload_to='cover_images/', blank=True)
    uploader = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        default=DEFAULT_USER_ID,
    )

    objects = models.Manager()

    class Meta:
        indexes = [models.Index(fields=['id'], name="id_index")]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[str(self.id)])


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    review = models.CharField(max_length=255)

    def __str__(self):
        return self.review
