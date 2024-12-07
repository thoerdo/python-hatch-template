#!/user/bin/env python3

# import string

PI = 3.14

"""_summary_

    Returns:
        _type_: _description_
"""


class Circle:
    """
    _summary_
    """

    def __init__(self, radius: int) -> None:
        assert radius > 0, "circle radius must be a positive number"
        self.radius = radius

        """_summary_
        """

    def area(self) -> str:
        return PI * self.radius**2

    def perimeter(self) -> str:
        return 2 * PI * self.radius

    def __repr__(self):
        return f"{self.__class__.__name__}(radius={self.radius})"
