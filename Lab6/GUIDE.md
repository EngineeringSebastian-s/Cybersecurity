# Guion de la exposición del Laboratorio 6

Presentación: `Presentación Laboratorio N.° 6 - Sebastián López Osorno.pptx` (10 diapositivas). Duración prevista: entre 5 y 7 minutos. El texto de cada diapositiva está también en sus notas del orador.

## Diapositiva 1. Políticas de Seguridad Informática (20 s)

Qué se muestra: las ideas en viñetas.

Qué decir: Buenas noches. Voy a presentar el análisis del incidente de Mapfre Seguros España. Lo trabajé como lo haría un auditor: primero entender la empresa, después los riesgos, y para cada control, cómo se demuestra.

## Diapositiva 2. El caso y la empresa (40 s)

Qué se muestra: las ideas en viñetas.

Qué decir: El 10 de marzo TI detecta accesos no autorizados a la base de datos de clientes. Mapfre es una entidad financiera supervisada que trata datos personales a gran escala, así que responde ante la Agencia de Protección de Datos y ante el supervisor de seguros. Hay un precedente real: en 2020 sufrió un ataque y la Agencia archivó el caso porque tenía medidas razonables y reaccionó bien. Lo uso como vara de medir.

## Diapositiva 3. Cómo funcionó el ataque (45 s)

Qué se muestra: la imagen `diagramas/01_anatomia_ataque.png` y las ideas en viñetas.

Qué decir: El atacante, ya dentro de la red, engaña con ARP al servidor de aplicaciones y a la base de datos y queda en medio. Como el tráfico iba sin cifrar, lo lee. Después se presenta con la IP del servidor, y como la base de datos autorizaba por dirección, entra. No hubo fallo de software: faltaban segmentación, protección de capa 2 y autenticación con cifrado. Cualquiera de las tres habría cortado el ataque.

## Diapositiva 4. Activos y vulnerabilidades (40 s)

Qué se muestra: las ideas en viñetas.

Qué decir: Identifiqué diez activos, desde la base de datos hasta la marca, y los clasifiqué con la tríada más dos dimensiones del material del curso: autenticidad, que es lo que ataca la suplantación, y trazabilidad. De ahí salen nueve vulnerabilidades. Ninguna se arregla con un parche: son decisiones de diseño. Y el hallazgo de gestión es que ese riesgo no tenía responsable.

## Diapositiva 5. Modelo normativo (45 s)

Qué se muestra: la imagen `diagramas/03_modelo_normativo.png` y las ideas en viñetas.

Qué decir: Como se insistió en clase, no metí todo en el mismo saco. La ley obliga: RGPD, la ley orgánica española, DORA y el Código Penal, con su espejo colombiano en las Leyes 1581 y 1273. La norma, ISO 27001, ordena la gestión. Los marcos, NIST, COBIT e ITIL, dan la estructura. Todo eso se traduce en política, normas internas, procedimientos y registros, que son la evidencia.

## Diapositiva 6. Riesgos antes y después (40 s)

Qué se muestra: la imagen `diagramas/04_mapa_calor.png` y las ideas en viñetas.

Qué decir: Valoré diez riesgos con la cadena activo, amenaza, vulnerabilidad y consecuencia. El día del incidente cuatro eran críticos y seis altos. Con los controles quedan ocho medios y dos bajos, una reducción del 66 por ciento. Usé las cuatro opciones de tratamiento: evitar, mitigar, transferir y aceptar. El residual no desaparece, lo acepta cada propietario.

## Diapositiva 7. 16 controles y su evidencia (45 s)

Qué se muestra: la imagen `diagramas/05_arquitectura_segura.png` y las ideas en viñetas.

Qué decir: Propongo dieciséis controles. Un equipo solo entra a la red si se autentica, el conmutador valida ARP, y a la base de datos se llega por una sola ruta con TLS mutuo. Para cada control indico la evidencia que pediría un auditor y un indicador, y los recojo en una declaración de aplicabilidad con sus exclusiones.

## Diapositiva 8. Impacto y plazos legales (45 s)

Qué se muestra: la imagen `diagramas/08_impacto_financiero.png` y las ideas en viñetas.

Qué decir: El escenario base cuesta 8,1 millones de euros. La mitad son tres partidas: la multa, los clientes perdidos y el refuerzo técnico aplazado. Y hay tres relojes legales: cuatro horas para el supervisor de seguros, setenta y dos para la Agencia y comunicación a los clientes. El plan incluye recuperación ante desastres y comunicación para las primeras 72 horas.

## Diapositiva 9. Auditoría de registros: ejemplo ejecutado (40 s)

Qué se muestra: la imagen `evidencias/02_consultas_deteccion.png` y las ideas en viñetas.

Qué decir: Para la actividad 13 construí y ejecuté un ejemplo. Tres cambios indebidos en pólizas se hacen con la cuenta y la IP legítimas, porque están robadas y suplantadas. Lo que los delata es el contexto: no tienen tique, ocurren de madrugada y con otro programa. Además el registro está encadenado por hash, así que si alguien borra una fila se nota.

## Diapositiva 10. Conclusiones (30 s)

Qué se muestra: las ideas en viñetas.

Qué decir: Cierro con tres ideas. El ataque fue posible por el diseño de la red interna. El problema de fondo es de gestión, porque ese riesgo no tenía dueño. Y un control solo vale si se puede demostrar. Muchas gracias, quedo atento a sus preguntas.

## Tiempos

Suma prevista: 6 min 30 s, con 582 palabras de guion (a unas 130 palabras por minuto, 4.5 minutos).

## Si algo falla en vivo

- Si no abre el archivo de PowerPoint, usar el PDF de la presentación que está en la misma carpeta.
- Si no se ven las imágenes, están una por una en `Lab6/diagramas/` y `Lab6/evidencias/`.
- Si piden ver el ejemplo de auditoría en vivo: `python Lab6/controles/auditoria_registros/demo_auditoria.py` (no necesita instalación ni red).
- Si el tiempo se acorta a 5 minutos, saltar las diapositivas 4 y 7 y decir su idea central en una frase.

## Preguntas probables

- ¿Por qué normativa española y no colombiana? Porque la empresa del caso es española; cada punto legal lleva su equivalente colombiano (apartado 7.3 del informe).
- ¿De dónde salen las cifras de costos? Son una estimación propia con supuestos explícitos en la tabla de costos; la referencia externa es el informe de IBM de 2026.
- ¿El incidente es real? La empresa sí. El incidente documentado es el de 2020; el del 10 de marzo es el escenario de la guía.
