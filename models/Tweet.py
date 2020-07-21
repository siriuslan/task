class Tweet:
    def __init__(self, id, created_at, text):
        self._id = id
        self._created_at = created_at
        self._text = text

    @property
    def id(self):
        return self._id

    @property
    def created_at(self):
        return self._created_at

    @property
    def text(self):
        return self._text
