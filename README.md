# AVoIP-Scripts

## Descripción

Este repositorio contiene scripts para gestionar dispositivos en una red AV-over-IP. Los scripts están organizados en carpetas según su utilidad y lenguaje de programación.

## Estructura del Repositorio

### Excel

- `CreateTabs.vba`: Este script crea y/o renombra pestañas en el Libro Rolls Royce Network assignment basándose en los valores de la columna B de la hoja activa.

### Switchers

- `change_av_source.py`: Este script realiza solicitudes HTTP POST para cambiar las fuentes de varios decodificadores AV-over-IP en una red.
- `novastar_input_switcher.py`: Script para cambiar las entradas (HDMI o DP) de una controladora LED Novastar utilizando comandos TCP.

### QSC-Plugins

(Aquí puedes describir los scripts y plugins relacionados con QSC que tienes en esta carpeta.)

## Cómo usar

### Prerequisitos

- Python 3.x
- Librería `requests` para Python
- Microsoft Excel

### Uso

#### Para los scripts en Python (Carpeta Switchers)

1. Modifica el diccionario `decoders` con la configuración de tus decodificadores.
2. Ejecuta el script.

#### Para el script en VBA (Carpeta Excel)

1. Abre el libro de Excel donde deseas crear las pestañas.
2. Ejecuta el macro.

## Contribuciones

Para contribuir a este proyecto, por favor crea un PR (Pull Request).

## Licencia

Este proyecto está bajo la licencia MIT.

## Contacto

- Nombre: Carlos Soto Pedreira
- Correo: <carlos.soto@trisonworld.com>
