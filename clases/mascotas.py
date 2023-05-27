class Mascota:
    def __init__(self, id_mascota, animal, raza, danio, duenio):
        self._id_mascota = id_mascota
        self._animal = animal
        self._raza = raza
        self._danio = danio
        self._duenio = duenio
    
    def __str__(self):
        return f"{self._id_mascota};{self._animal};{self._raza};{self._danio};{self._duenio}"