import sys

# Función de validación
def validar_correo(correo: str) -> str:
    # Verificar que contenga exactamente un "@"
    if correo.count('@') == 0:
        return "X El correo debe contener el símbolo '@'."
    if correo.count('@') > 1:
        return "X El correo tiene más de un '@'."

    usuario, dominio = correo.split('@')

    # Validar que haya texto antes y después del "@"
    if not usuario:
        return "X Falta el nombre de usuario antes del '@'."
    if not dominio:
        return "X Falta el dominio después del '@'."

    # Validar que el dominio tenga punto
    if '.' not in dominio:
        return "X El dominio debe contener un punto (ejemplo: dominio.com)."

    # Validar terminación permitida
    if not (dominio.endswith(".com") or dominio.endswith(".org") or dominio.endswith(".mx") or dominio.endswith(".net")):
        return "X El correo solo puede terminar en '.com', '.org' , '.net' o '.mx'."

    return " El correo es válido."

# Programa principal
while True:
    correo = input("Escribe tu correo electrónico (o escribe 'salir' para terminar): ")

    if correo.lower() == "salir":
        print("👋 Programa finalizado.")
        sys.exit()

    print(validar_correo(correo))
    print()
