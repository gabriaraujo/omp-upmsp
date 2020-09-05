class Quality:
    """This class represents a Quality parameter. The attributes indicate the
    parameter name and its percentage.
    """

    def __init__(self: 'Quality', parameter: str, value: float):
        """Instantiates a new Quality parameter.

        Args:
            parameter (str): The quality parameter name.
            value (float): The percentage of the quality parameter.
        """

        self._parameter: str = parameter
        self._value: float = value

    def __repr__(self: 'Quality') -> str:
        """This method returns the string representation of a Quality parameter.
        
        Returns:
            str: The string representation of this class.
        """

        return f'parameter: {self._parameter}\n' + \
               f'value: {self._value}\n'

    # region simple getters and setters
    @property
    def parameter(self: 'Quality') -> str:
        """str: The quality parameter name."""
        return self._parameter

    @parameter.setter
    def parameter(self: 'Quality', value: str) -> None:
        self._parameter = value

    @property
    def value(self: 'Quality') -> float:
        """float: The percentage of the quality parameter."""
        return self._value

    @value.setter
    def value(self: 'Quality', value: float) -> None:
        self._value = value
