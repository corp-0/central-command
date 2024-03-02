from django.contrib.auth.validators import ASCIIUsernameValidator
from django.utils.deconstruct import deconstructible

IDENTIFIER_REGEX = r"^[a-zA-Z0-9_\-\.]{3,}$"


@deconstructible()
class AccountNameValidator(ASCIIUsernameValidator):
    # match account identifier that only has letters, numbers, dash, underscore
    # and at least 3 characters
    regex = IDENTIFIER_REGEX
    message = (
        "Enter a valid account identifier. This value may contain only English letters, numbers, and -/_ characters."
    )
