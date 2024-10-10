class LoginError(Exception):
    """Invalid credentials when tried to login."""

class EmptyFieldError(Exception):
    """Use if you need something important in a Field."""

class PasswordIsNotEqualError(Exception):
    """The password isn't equal to his verification."""