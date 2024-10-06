class LoginError(Exception):
    """Invalid credentials when tried to login"""

class EmptyField(Exception):
    """Use if you need something important in a Field"""