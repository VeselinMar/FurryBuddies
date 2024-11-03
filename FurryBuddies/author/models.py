from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models

from FurryBuddies.author.validators import validate_letters_only, validate_six_digit_passcode


# Create your models here.


class Author(models.Model):
    first_name = models.CharField(
        blank=False,
        max_length=40,
        validators=[MinLengthValidator(4), MaxLengthValidator(40), validate_letters_only],
    )

    last_name = models.CharField(
        blank=False,
        max_length=50,
        validators=[MinLengthValidator(2), MaxLengthValidator(50), validate_letters_only],
    )

    passcode = models.CharField(
        blank=False,
        max_length=6,
        validators=[validate_six_digit_passcode],
        help_text="Your passcode must be a combination of 6 digits",
    )

    pets_number = models.SmallIntegerField(
        blank=False,
    )

    info = models.TextField(
        blank=True,
        null=True,
    )

    image_field = models.URLField(
        blank=True,
        null=True,
    )
