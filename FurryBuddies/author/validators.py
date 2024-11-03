from django.core.exceptions import ValidationError
import re


def validate_letters_only(value):
    if not re.match(r'^[A-Za-z]+$', value):
        raise ValidationError('Your name must contain letters only!')


def validate_six_digit_passcode(value):
    if not value.isdigit() or len(value) != 6:
        raise ValidationError('Your passcode must be a combination of 6 digits')
