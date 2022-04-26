from django.utils.deconstruct import deconstructible
from django.contrib.auth.validators import ASCIIUsernameValidator


@deconstructible()
class UsernameValidator(ASCIIUsernameValidator):
    # concuerda con username que tenga a lo menos 3 caracteres, letras, numeros y guiones bajos
    regex = r"^[a-zA-Z0-9.-](?!.* {2})[ \w.-]{2,}$"
    message = (
        "Ingresa un nick válido. Este campo sólo puede ser rellenado con caracteres latinos, "
        "números, guión, guión bajo, puntos, y espacios."
    )
