def validar_persona(nombre, apellido, edad):
    if not nombre or not apellido or not isinstance(edad, int):
        return False
    return True
