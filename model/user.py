class Usuario():
    def __init__(self, nombre="", usuario="", clave=""):
        self._nombre = nombre
        self._usuario = usuario
        self._clave = clave
    
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if len(valor) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        self._nombre = valor

    @property
    def usuario(self):
        return self._usuario
    
    @usuario.setter
    def usuario(self, valor):
        if len(valor) < 3:
            raise ValueError("El usuario debe tener al menos 3 caracteres.")
        self._usuario = valor

    @property
    def clave(self):
        return self._clave
    
    @clave.setter
    def clave(self, valor):
        if len(valor) < 6:
            raise ValueError("La clave debe tener al menos 6 caracteres.")
        self._clave = valor

   
    def __str__(self):
        return f"Usuario: {self._usuario}, Nombre: {self._nombre}"

