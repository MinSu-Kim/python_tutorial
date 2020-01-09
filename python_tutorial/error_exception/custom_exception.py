class Error(Exception):
    """Base class for exceptions in this module."""
    pass


class InputError(Error):
    def __init__(self, expression, message):
        super().__init__(message)
        self.expression = expression
        self.message = message

    def __str__(self) -> str:
        return 'expression -> {} \nmessage -> {}'.format(self.expression, self.message)


class TransitionError(Error):
    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

    def __str__(self) -> str:
        return 'previous -> {} \nnext -> {} \nmessage -> {}'.format(self.previous, self.next, self.message)


try:
    raise InputError(2 * 'a', '입력 에러')
except InputError as err:
    print('Custom Input Error!\n', err)

print()
try:
    raise TransitionError(2, 3 * 2, "Not Allowed")
except TransitionError as err:
    print('Exception occured: \n', err)
