class InvalidTestResult(RuntimeError):
    def __init__(self):
        super().__init__("Invalid test result given")
