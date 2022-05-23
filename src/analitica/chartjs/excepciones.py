from artemangaweb.exceptions import ErrorBase

class ErrorChartJS(ErrorBase):
    """
    Clase base para las excepciones de la librería chartjs
    """
    pass


class ParamConstruccionInvalido(ErrorChartJS):
    """
    Excepción para indicar que los parámetros de construcción de un gráfico son inválidos
    """
    def __init__(self, razon):
        super().__init__(
            f"Los parámetros de construcción del gráfico son inválidos: {razon}"
        )