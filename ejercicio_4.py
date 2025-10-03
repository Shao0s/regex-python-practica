import re
from urllib.parse import urlparse

# Expresión regular para detectar URLs
url_pattern = re.compile(r'(https?://[^\s]+|www\.[^\s]+)')

def analizar_url(url):
    # Si no tiene protocolo, agregamos http por defecto
    if not url.startswith('http'):
        url = 'http://' + url
    parsed = urlparse(url)
    return {
        'url': url,
        'protocolo': parsed.scheme,
        'dominio': parsed.netloc,
        'ruta': parsed.path if parsed.path else None
    }

while True:
    print("Extractor de URLs y Dominios")
    texto = input("Ingresa un texto (o escribe 'salir' para terminar): ")
    if texto.lower() == 'salir':
        print("Programa terminado.")
        break

    urls = url_pattern.findall(texto)
    if not urls:
        print("No se encontraron URLs en el texto.\n")
        continue

    for i, u in enumerate(urls, 1):
        info = analizar_url(u)
        print(f"URL {i}: {info['url']}")
        print(f"  Protocolo: {info['protocolo']}")
        print(f"  Dominio: {info['dominio']}")
        if info['ruta']:
            print(f"  Ruta: {info['ruta']}")
        print()
