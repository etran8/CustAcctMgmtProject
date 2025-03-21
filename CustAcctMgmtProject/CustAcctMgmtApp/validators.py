from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_balance(value):
    print("Validate Account Balance called = " + str(value))
    if value < 0:
        raise ValidationError(
            _('%Account Balance cannot be less than zero'),
            params={'value': value},
        )


def validate_amount(value):
    print("Validate Transaction Amount called = " + str(value))
    if value < 0:
        raise ValidationError(
            _('%(value)s cannot be less than zero'),
            params={'value': value},
        )

