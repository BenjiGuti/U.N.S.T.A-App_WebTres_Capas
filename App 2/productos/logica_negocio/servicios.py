def validar_producto(nombre, descripcion, precio):
    if not nombre or not descripcion or not isinstance(precio, float):
        return False
    return True
