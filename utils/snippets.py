import random
import string
from django.utils.text import slugify


def random_string_generator(size=4, chars=string.ascii_lowercase + string.digits):
    """[Generates random string]

    Args:
        size (int, optional): [size of string to generate]. Defaults to 4.
        chars ([str], optional): [characters to use]. Defaults to string.ascii_lowercase+string.digits.

    Returns:
        [str]: [Generated random string]
    """
    return "".join(random.choice(chars) for _ in range(size))


def generate_unique_username_from_email(instance, exists=False):
    """[Generates unique username from email]

    Args:
        instance ([model class object instance]): [model class object instance]

    Raises:
        ValueError: [If found invalid email]

    Returns:
        [str]: [unique username]
    """

    # get email from instance
    email = instance.email

    if not email:
        raise ValueError("Invalid email!")

    def generate_username(email):
        if exists:
            username = slugify(email.split("@")[0][:96]) + "-" + random_string_generator(size=4)
        else:
            username = slugify(email.split("@")[0][:100])
        return username

    generated_username = generate_username(email=email)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(username=generated_username).exists()

    if qs_exists:
        # recursive call
        generate_unique_username_from_email(instance=instance, exists=True)

    return generated_username


class CustomModelAdminMixin(object):
    """
    DOCSTRING for CustomModelAdminMixin:
    This model mixing automatically displays all fields of a model in admin panel following the criteria.
    code: @ Numan Ibn Mazid
    """

    def __init__(self, model, admin_site):
        self.list_display = [
            field.name
            for field in model._meta.fields
            if field.get_internal_type() != "TextField"
        ]
        super(CustomModelAdminMixin, self).__init__(model, admin_site)
