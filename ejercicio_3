import re

print("""Validador de Contraseñas Seguras
        Criterios:
- Mínimo 8 caracteres
- Al menos una letra mayúscula
- Al menos una letra minúscula
- Al menos un número
- Al menos un carácter especial entre: @$!%*?&#
""")

# patrones
R_LONGITUD = re.compile(r'.{8,}')
R_MAYUS = re.compile(r'[A-Z]')
R_MINUS = re.compile(r'[a-z]')
R_NUM = re.compile(r'\d')
R_SPECIAL = re.compile(r'[@\$!\%\*\?\&#]')

def validar_contrasena(password: str):
    errores = []
    if not R_LONGITUD.search(password):
        errores.append("Mínimo 8 caracteres")
    if not R_MAYUS.search(password):
        errores.append("Al menos una letra mayúscula (A-Z)")
    if not R_MINUS.search(password):
        errores.append("Al menos una letra minúscula (a-z)")
    if not R_NUM.search(password):
        errores.append("Al menos un número (0-9)")
    if not R_SPECIAL.search(password):
        errores.append("Al menos un carácter especial: @$!%*?&#")
    return len(errores) == 0, errores

def mostrar_resultado(password: str):
    es_valida, errores = validar_contrasena(password)
    if es_valida:
        print(f' La contraseña "{password}" es VÁLIDA — cumple todos los requisitos.')
    else:
        print(f' La contraseña "{password}" es INVÁLIDA. Falta(n):')
        for e in errores:
            print(f'   - {e}')

if __name__ == "__main__":
    print(">>> Validador de contraseñas (escribe 'salir' para terminar):")
    while True:
        pwd = input("Introduce una contraseña para validar: ").strip()
        if pwd.lower() == 'salir':
            print("Saliendo. ¡Hasta luego!")
            break
        mostrar_resultado(pwd)
        print("-" * 40)
