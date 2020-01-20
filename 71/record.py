class RecordScore():
    """Class to track a game's maximum score"""
    def __init__(self):
        self.max = float('-Inf')

    def __call__(self, *args, **kwargs):
        if args[0] > self.max:
            self.max = args[0]
        return self.max
