class Cita:
    def __init__(self, cod_cita, fecha_cita, hora, establecimiento, dni):
        self._cod_cita = cod_cita
        self._fecha_cita = fecha_cita
        self._hora = hora
        self._establecimiento = establecimiento
        self._dni = dni
    
    def __str__(self):
        return f"{self._cod_cita};{self._fecha_cita};{self._hora};{self._establecimiento};{self._dni}"
        