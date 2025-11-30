class Pet:
    def __init__(self, nombre, especie, edad):
        self.validarNombre(nombre)
        self.validarEspecie(especie)
        self.validarEdad(edad)
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    @staticmethod
    def validarNombre(txt):
        if txt == "".strip() or txt == "perro":
            raise ValueError("Debes introducir un nombre")

    @staticmethod
    def validarEspecie(txt):
        if txt.isnumeric():
            raise ValueError("")

    @staticmethod
    def validarEdad(edad):
        try:
            if isinstance(edad, float):
                raise ValueError("Edad tiene decimal, debe ser entera")
            try:
                edad = int(edad)
            except ValueError as e:
                raise ValueError("Edad tiene que ser entera")
        except ValueError as e:
            print(e)
