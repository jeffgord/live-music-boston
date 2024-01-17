class Venue:
    def __init__(self, name, location, frequency, genre, link):
        self._name = name
        self._location = location
        self._frequency = frequency
        self._genre = genre
        self._link = link

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._property

    @property
    def frequency(self):
        return self._frequency

    @property
    def genre(self):
        return self._genre

    @property
    def link(self):
        return self._link
