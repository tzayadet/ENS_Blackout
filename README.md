# ENS BLACKOUT

[![Static application checks](https://github.com/tzayadet/ENS_Blackout/actions/workflows/quality.yml/badge.svg)](https://github.com/tzayadet/ENS_Blackout/actions/workflows/quality.yml) [![GitHub Pages](https://github.com/tzayadet/ENS_Blackout/actions/workflows/static.yml/badge.svg)](https://github.com/tzayadet/ENS_Blackout/actions/workflows/static.yml)

Simulador interactivo de formación sobre auditoría y gestión de riesgos, inspirado en el **Esquema Nacional de Seguridad (ENS), Real Decreto 311/2022**, MAGERIT v3 y marcos relacionados.

**Demo:** https://tzayadet.github.io/ENS_Blackout/  
**Código:** https://github.com/tzayadet/ENS_Blackout

## Qué incluye

- Recorrido didáctico por fases de auditoría.
- Catálogo reducido e ilustrativo de controles.
- Escenarios ficticios, entrevistas simuladas y decisiones.
- Hallazgos y evidencias de ejemplo.
- Matriz de riesgos simplificada.
- Inventario de activos y documentación ficticios.
- Generación de un resumen JSON de la sesión.

## Uso

Abre la [demo pública](https://tzayadet.github.io/ENS_Blackout/) en un navegador moderno. No necesita backend ni instalación.

Para validar el código localmente:

```bash
python scripts/validate_site.py
```

Requiere Python 3.11+ y Node.js 20+ para comprobar la sintaxis del JavaScript.

## Alcance y precisión

**ENS BLACKOUT es una simulación formativa, no una herramienta de auditoría ni una plataforma GRC de producción.**

- Los organismos, activos, actores, conversaciones, hallazgos y evidencias son ficticios.
- Los hashes mostrados son datos de demostración; no se calculan sobre archivos reales.
- El catálogo de controles y sus correspondencias con ISO 27001/NIS2 son ejemplos simplificados, no una implementación completa ni una declaración de aplicabilidad.
- Las puntuaciones y el dictamen se generan con reglas didácticas y valores aleatorios. No representan una evaluación de conformidad.
- La aplicación no consulta el CCN, el BOE, repositorios, sistemas corporativos ni fuentes externas.
- No existe persistencia de evidencias ni trazabilidad probatoria.

Contrasta siempre las referencias con el texto normativo y las guías oficiales vigentes. No introduzcas datos reales, información personal, vulnerabilidades ni evidencias confidenciales en la demo pública.

## Tecnologías

- HTML5
- CSS3
- JavaScript
- APIs del navegador

## Validación continua

GitHub Actions comprueba que el HTML contiene las secciones esperadas, que no se cargan scripts JavaScript remotos, que el JavaScript embebido compila y que los puntos de entrada de chat y terminal no insertan directamente texto del usuario como HTML.

## Despliegue

La interfaz está publicada como sitio estático mediante GitHub Pages. No existe un backend asociado.

## Licencia

Consulta [LICENSE](LICENSE).
