from django.utils.deconstruct import deconstructible
from django.contrib.auth.validators import ASCIIUsernameValidator


@deconstructible()
class UsernameValidator(ASCIIUsernameValidator):
    # concuerda con username que tenga a lo menos 3 caracteres, letras, numeros y guiones bajos
    regex = r"^[a-zA-Z0-9.-](?!.* {2})[ \w.-]{2,}$"
    message = (
        "Ingresa un nick valido. Este campo solo puede ser rellenado con caracteres latinos, "
        "numeros, guion, guion bajo, puntos, y espacios."
    )
