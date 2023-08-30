from sanic_ext.exceptions import ValidationError


def is_valid_str(value, min_length=1, max_length=100) -> bool:
    if value and min_length <= len(value) <= max_length:
        return True
    else:
        raise ValidationError(f'Invalid string value. Allowed min length is {min_length} & max length is {max_length}')
