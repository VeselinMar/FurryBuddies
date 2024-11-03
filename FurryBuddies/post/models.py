from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from FurryBuddies.author.models import Author


# Create your models here.


class Post(models.Model):
    title = models.CharField(
        blank=False,
        unique=True,
        max_length=50,
        validators=[MinLengthValidator(5), MaxLengthValidator(50)],
        error_messages={'unique': 'Oops! That title is already taken. How about something fresh and fun?'},
    )

    image_url = models.URLField(
        blank=False,
        help_text='Share your funniest furry photo URL!'
    )

    context = models.TextField(
        blank=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    author = models.ForeignKey(
        to=Author,
        on_delete=models.CASCADE,
        editable=False,
    )
