# https://chat.openai.com/c/01074e4c-fc05-4eb6-b992-1f4eef973f2a
# https://chat.openai.com/c/edad9274-75c4-4640-9a55-3a36178ac3f6
class InvalidOperationError(Exception):
    """
    A custom exception class
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f"Method not allowed on empty collection"
