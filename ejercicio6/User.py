class User:
    def __init__(self, username, email, age, active = True):
        try:
            self.verify_username(username)
            self.verify_email(email)
            self.verify_age(age)
            self.__username=  username
            self.__email = email
            self.__age = age
            self.__active = active
        except ValueError as e:
            print(e)

    @staticmethod
    def verify_username(name):
        if len(name) == 0:
            raise ValueError("username no puede ser vacío.")
        if name != name.strip():
            raise ValueError("username no puede tener espacio al inicio o al final.")
        if name.isnumeric():
            raise ValueError("username no puede ser numérico.")

    @staticmethod
    def verify_email(email):
        if "@" not in email or "." not in email:
            raise ValueError("email debe tener '@', y '.'.")

    @staticmethod
    def verify_age(age):
        if age != int(age):
            raise ValueError("Edad debe ser entera.")
        if age < 14 or age > 120:
            raise ValueError("Debes tener entre 14 o 120 años.")

    def set_email(self, email):
        self.__email = email

    def set_age(self, age):
        self.__age = age

    def desactivate(self):
        self.__active = False

    def activate(self):
        self.__active = True

    def get_name(self):
        return self.__username

    def get_active(self):
        return self.__active

    def __str__(self):
        if self.__active:
            return f"User: {self.__username} ({self.__age} años) -- Activo"
        else:
            return f"User: {self.__username} ({self.__age} años) -- Inactivo"


class Activity:
    def __init__(self, user, type, duration):
        try:
            self.validate_user(user)
            self.validate_type(type)
            self.validate_duration(duration)
            self.__user = user
            self.__type = type
            self.__duration = duration
        except ValueError as e:
            print(e)

    @staticmethod
    def validate_user(user):
        if not isinstance(user, User):
            raise ValueError("Usuario inválido.")
        return user

    @staticmethod
    def validate_type(type):
        if type.lower() not in ("login", "compra", "comentario", "visita"):
            raise ValueError("type debe ser, login, compra, comentario o visita.")

    @staticmethod
    def validate_duration(duration):
        if duration < 0:
            raise ValueError("Duración debe ser un número mayor que 0.")

    def set_duration(self, duration):
        self.__duration = duration

    def get_duration(self):
        return self.__duration

    def __str__(self):
        return f"Actividad: {self.__type} -- Usuario: {self.__user} -- Duración: {self.__duration} min"