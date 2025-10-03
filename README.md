Este repositorio contiene varios programas interactivos en Python diseñados para validación, extracción y análisis de datos comunes en textos, correos, URLs, fechas, contraseñas y números de teléfono. Todos son interactivos, fáciles de usar y educativos.

Contenido de los programas
1. Validador de Correos Electrónicos

Función: Valida correos electrónicos y reporta errores específicos.

Validaciones:

Contiene exactamente un @.

Tiene usuario antes del @ y dominio después.

El dominio contiene un punto y termina en .com, .org, .mx o .net.

Ejemplo de uso:

Escribe tu correo electrónico: usuario@dominio.com
✅ El correo es válido.

2. Extractor de Teléfonos

Función: Extrae números de teléfono mexicanos de un texto en distintos formatos.

Formatos soportados:

6461234567

646-123-4567

646 123 4567

(646) 123-4567

Ejemplo de uso:

Escribe un texto: Llama al (646) 123-4567 o al 646-987-6543
📞 Teléfonos encontrados:
- 646-123-4567
- 646-987-6543

3. Validador de Contraseñas Seguras

Función: Verifica que una contraseña cumpla con criterios de seguridad.

Criterios:

Mínimo 8 caracteres

Al menos una letra mayúscula

Al menos una letra minúscula

Al menos un número

Al menos un carácter especial @$!%*?&#

Ejemplo de uso:

Introduce una contraseña: Prueba123!
✅ La contraseña es VÁLIDA — cumple todos los requisitos.

4. Extractor de URLs y Dominios

Función: Extrae URLs de un texto y muestra:

URL completa

Protocolo (http o https)

Dominio

Ruta si existe

Ejemplo de uso:

Ingresa un texto: Visita https://www.google.com o www.ejemplo.com/pagina
1. URL: https://www.google.com
   Protocolo: https
   Dominio: www.google.com
2. URL: http://www.ejemplo.com/pagina
   Protocolo: http
   Dominio: www.ejemplo.com
   Ruta: /pagina

5. Analizador de Fechas

Función: Detecta fechas en diferentes formatos y las convierte a YYYY-MM-DD.

Formatos soportados:

DD/MM/YYYY → 01/12/2024

YYYY-MM-DD → 2024-12-01

DD-MMM-YYYY → 01-Dec-2024

Mes DD, YYYY → Diciembre 1, 2024

Ejemplo de uso:

Ingresa un texto con fechas: Hoy es 01/12/2024 y la cita será el 5-Mar-2025.
Fechas encontradas y convertidas:
- Formato original: 01/12/2024 → Estándar: 2024-12-01
- Formato original: 5-Mar-2025 → Estándar: 2025-03-05

Características generales

Todos los programas son interactivos: el usuario ingresa texto hasta que decida salir (salir).

Se usan expresiones regulares (re) para detección precisa de patrones.

Los programas incluyen mensajes claros y amigables, indicando errores o resultados correctos.

Algunos programas aplican normalización de datos, por ejemplo:

Números de teléfono se muestran todos en formato XXX-XXX-XXXX.

Fechas se convierten automáticamente al formato estándar YYYY-MM-DD.
