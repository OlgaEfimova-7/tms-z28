from decimal import Decimal


def my_default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    else:
        return str(obj)
