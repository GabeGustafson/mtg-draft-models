class Card:
    def __init__(self, *args, **kwargs):
        for dictionary in args:
            for k, v in dictionary.items():
                setattr(self, k, v)
        for key in kwargs:
            setattr(self, key, kwargs[key])
        if hasattr(self, "name"):
            self.name = self.name.lower()

    def __str__(self):
        return " ".join([k + ": " + str(v) for k, v in vars(self).items()])