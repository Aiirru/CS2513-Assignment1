#Student Number: 125521049

class Instruments:
    def __init__(self, name, family):
        self._name = name
        self._family = family

    @property
    def name(self):
        return self._name

    def description(self):
        return f"{self._name}, {self._family}"
    

class StringInstrument(Instruments):
    def __init__(self, name):
        super().__init__(name, "String")  


class KeyInstrument(Instruments):
    def __init__(self, name):
        super().__init__(name, "Keyboard")


class Mood:
    def __init__(self, name, energy, description):
        self._name = name
        self._energy = energy
        self._description = description


    @property
    def name(self):
        """name inputted through other file"""
        return self._name

    @property
    def energy(self):
        return self._energy

    @property
    def description(self):
        return self._description

    def mood_descirption(self):
        return f"{self._name} , Energy Level:{self._energy}, {self.description}"


class Artist:
    def __init__(self, name):
        self._name = name
        self._genre = []
        self._instruments = []

    @property
    def gernres(self):
        return list(self._genre)

    def add_genre(self, genre):
        self._genre.append(genre)

    def add_instrument(self, instrument):
        self._instruments.append(instrument)
