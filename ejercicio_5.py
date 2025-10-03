import re

# Diccionario para meses en español e inglés abreviado
meses = {
    'enero': '01', 'febrero': '02', 'marzo': '03', 'abril': '04',
    'mayo': '05', 'junio': '06', 'julio': '07', 'agosto': '08',
    'septiembre': '09', 'octubre': '10', 'noviembre': '11', 'diciembre': '12',
    'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06',
    'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
}

# Patrones regex para fechas
patrones = [
    (r'\b(\d{2})/(\d{2})/(\d{4})\b', 'DD/MM/YYYY'),
    (r'\b(\d{4})-(\d{2})-(\d{2})\b', 'YYYY-MM-DD'),
    (r'\b(\d{2})-([A-Za-z]{3})-(\d{4})\b', 'DD-MMM-YYYY'),
    (r'\b([A-Za-z]+) (\d{1,2}), (\d{4})\b', 'Mes DD, YYYY')
]

def convertir_fecha_regex(texto):
    resultados = []
    for patron, tipo in patrones:
        for m in re.finditer(patron, texto):
            if tipo == 'DD/MM/YYYY':
                dia, mes, anio = m.groups()
            elif tipo == 'YYYY-MM-DD':
                anio, mes, dia = m.groups()
            elif tipo == 'DD-MMM-YYYY':
                dia, mes_abrev, anio = m.groups()
                mes = meses.get(mes_abrev.capitalize(), '01')
            elif tipo == 'Mes DD, YYYY':
                mes_nombre, dia, anio = m.groups()
                mes = meses.get(mes_nombre.capitalize(), '01')
                dia = f"{int(dia):02d}"  # Asegurar dos dígitos
            resultados.append((m.group(0), f"{anio}-{mes}-{dia}"))
    return resultados

# Programa interactivo
print("Analizador de Fechas con Regex - Formato estándar: YYYY-MM-DD")
print("Escribe 'salir' para finalizar.\n")

while True:
    texto = input("Ingresa un texto con fechas: ")
    if texto.lower() == 'salir':
        break

    fechas = convertir_fecha_regex(texto)

    if fechas:
        print("\nFechas encontradas y convertidas:")
        for original, estandar in fechas:
            print(f"- Formato original: {original} → Estándar: {estandar}")
    else:
        print("No se encontraron fechas en el texto.")
    print()
