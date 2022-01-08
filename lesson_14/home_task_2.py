class TestError(Exception):
    def __init__(self, message='Something went wrong...'):
        self.message = message
        super().__init__(self.message)


if __name__ == '__main__':
    raise TestError
