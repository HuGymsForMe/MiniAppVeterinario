class Cliente:
    def __init__(self, dni, nombre, apellidos, telefono):
        self._dni = dni  
        self._nombre = nombre
        self._apellidos = apellidos
        self._telefono = telefono
    
    def __str__(self):
        return f"{self._dni};{self._nombre};{self._apellidos};{self._telefono}"

    def __eq__(self, other): #DNI TIENE QUE SER ÚNICO
        if isinstance(other, Cliente):
            return self._dni == other._dni
        return False