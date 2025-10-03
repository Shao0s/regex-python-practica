import re

def extraer_telefonos(texto):
    # Expresión regular para los diferentes formatos
    patron = re.compile(r"""
        (?:                
            \(\d{3}\)\s?\d{3}[- ]?\d{4}   # (646) 123-4567 o (646)1234567
            | \d{3}[- ]\d{3}[- ]\d{4}     # 646-123-4567 o 646 123 4567
            | \d{10}                      # 6461234567
        )
    """, re.VERBOSE)
    return patron.findall(texto)

# Programa interactivo
while True:
    texto = input("\nEscribe un texto (o escribe 'salir' para terminar): ")

    if texto.lower() == "salir":
        print(" Programa finalizado.")
        break

    telefonos = extraer_telefonos(texto)

    if telefonos:
        print("📞 Teléfonos encontrados:", telefonos)
    else:
        print("⚠ No se encontraron números de teléfono.")
