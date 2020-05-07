class Quality:
    """classe para salvar os dados de qualidade."""

    def __init__(self, parameter: str, value: float):
        self._parameter = parameter
        self._value = value

    def __repr__(self):
        return f'parameter: {self._parameter}\n' + \
               f'value: {self._value}\n'

    @property
    def parameter(self) -> str:
        """Quality parameter."""
        return self._parameter

    @parameter.setter
    def parameter(self, value: str):
        self._parameter = value

    @property
    def value(self) -> float:
        """Quality value."""
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value
