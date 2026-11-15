# Guion de la exposición del Laboratorio 6

Presentación: `Presentación Laboratorio N.° 6 - Sebastián López Osorno.pptx` (10 diapositivas). Duración prevista: entre 5 y 7 minutos. El texto de cada diapositiva está también en sus notas del orador.

## Diapositiva 1. Políticas de Seguridad Informática (20 s)

Qué se muestra: las ideas en viñetas.

Qué decir: El 14 de agosto de 2020, a las nueve y once de la noche, el centro de control de Mapfre vio caer varias aplicaciones a la vez. Nueve minutos después su comité de crisis ya estaba reunido. Ese ataque fue real, y la Agencia Española de Protección de Datos lo archivó sin multa. El caso que nos dejó el profe es otro, el del 10 de marzo. Me pregunté por qué la misma compañía no vio venir este.

## Diapositiva 2. El caso y la empresa (40 s)

Qué se muestra: las ideas en viñetas.

Qué decir: El 10 de marzo el equipo de TI encuentra accesos no autorizados a la base de datos de clientes de vida. Salieron nombres, direcciones, documentos y pólizas. Antes de proponer nada respondí las siete preguntas que el profe dictó en clase: qué hace la empresa, qué datos maneja, quiénes son sus clientes. La respuesta corta es que Mapfre es una aseguradora supervisada por dos autoridades, y eso pone relojes de horas.

## Diapositiva 3. Cómo funcionó el ataque (45 s)

Qué se muestra: la imagen `diagramas/01_anatomia_ataque.png` y las ideas en viñetas.

Qué decir: Así fue el ataque. El atacante ya está dentro de la red. Le dice por ARP al servidor de aplicaciones que él es la base de datos, y a la base de datos que él es el servidor. Los dos le creen, porque ARP es de 1982 y no comprueba nada. El tráfico iba sin cifrar, así que lo lee. Después se presenta con la IP del servidor y la base de datos lo deja entrar. Aquí no hubo contraseña rota. Faltaban tres barreras, y con una sola habría bastado.

## Diapositiva 4. Activos y vulnerabilidades (40 s)

Qué se muestra: las ideas en viñetas.

Qué decir: Saqué diez activos, y el que más me costó valorar fue la red. Uno tiende a pensar que lo valioso es la base de datos, y la red parece tubería. Pero el ataque entró por ahí. De los activos salen nueve vulnerabilidades. Cinco eran necesarias para que el ataque funcionara, y ninguna se arregla con un parche: son configuración. Lo que más me llamó la atención es que ese riesgo no tenía dueño.

## Diapositiva 5. Modelo normativo (45 s)

Qué se muestra: la imagen `diagramas/03_modelo_normativo.png` y las ideas en viñetas.

Qué decir: El profe insistió en no meter todo en el mismo saco, y este diagrama es mi intento de no hacerlo. Arriba a la izquierda, la ley, que obliga: el RGPD, DORA, el Código Penal, y en Colombia la 1581 y la 1273. Debajo, la norma, ISO 27001. Luego los marcos: NIST, COBIT, ITIL. A la derecha está lo que la empresa escribe en su casa, y termina en registros, que es lo que pide un auditor.

## Diapositiva 6. Riesgos antes y después (40 s)

Qué se muestra: la imagen `diagramas/04_mapa_calor.png` y las ideas en viñetas.

Qué decir: Diez riesgos. El día del incidente, cuatro críticos y seis altos, todos arriba a la derecha. Con los controles bajan: quedan ocho medios y dos bajos, de 181 puntos a 61. Fíjense en R2 y R4, arriba a la izquierda en la segunda matriz. El impacto sigue siendo el máximo. Si alguien vuelve a entrar a la base de datos, el daño es el mismo. Lo que cambia es lo difícil que es llegar.

## Diapositiva 7. 16 controles y su evidencia (45 s)

Qué se muestra: la imagen `diagramas/05_arquitectura_segura.png` y las ideas en viñetas.

Qué decir: Dieciséis controles. El diagrama se lee de arriba hacia abajo. Un equipo no entra a la red si no se autentica. El conmutador descarta el ARP falso. A la base de datos se llega por un solo camino y con certificado en los dos extremos. Para cada control escribí con qué lo demostraría ante un auditor. El conmutador, por ejemplo, se demuestra con su contador de paquetes descartados, no con el archivo de configuración.

## Diapositiva 8. Impacto y plazos legales (45 s)

Qué se muestra: la imagen `diagramas/08_impacto_financiero.png` y las ideas en viñetas.

Qué decir: Esto cuesta. Mi estimación para 250.000 afectados es de 8,1 millones de euros. Es una estimación mía, con supuestos que están en el informe, y queda cerca del promedio que IBM publicó este año para el sector financiero, 6,3 millones de dólares. La mitad se va en tres cosas: la multa, los clientes que se van y la red que no se arregló a tiempo. Y los plazos: cuatro horas para el supervisor de seguros, 72 para la Agencia.

## Diapositiva 9. Auditoría de registros: ejemplo ejecutado (40 s)

Qué se muestra: la imagen `evidencias/02_consultas_deteccion.png` y las ideas en viñetas.

Qué decir: Para la actividad 13 no quise quedarme en describir, así que armé una base de datos de prueba y la ejecuté. A las 02:47 de la madrugada alguien cambia el beneficiario de una póliza. Usa la cuenta de la aplicación y la IP del servidor, las dos robadas. En el registro se ve igual que un cambio legítimo. Lo que lo delata es que no tiene tique, la hora y que no vino de la aplicación. La consulta lo encuentra en una línea.

## Diapositiva 10. Qué queda claro y qué no (30 s)

Qué se muestra: las ideas en viñetas.

Qué decir: Me quedan dudas. No sé cuántos clientes resultaron afectados, por eso trabajé con tres escenarios. Y la arquitectura real de Mapfre no es pública, así que parte de lo que dije es supuesto y así está marcado. Lo que sí pude comprobar es que con la red como estaba el ataque se repite en una tarde. El ejemplo de auditoría corre con un solo comando. Si quieren lo ejecutamos ahora.

## Tiempos

Suma prevista: 6 min 30 s, con 768 palabras de guion (a unas 130 palabras por minuto, 5.9 minutos).

## Si algo falla en vivo

- Si no abre el archivo de PowerPoint, usar el PDF de la presentación que está en la misma carpeta.
- Si no se ven las imágenes, están una por una en `Lab6/diagramas/` y `Lab6/evidencias/`.
- Si piden ver el ejemplo de auditoría en vivo: `python Lab6/controles/auditoria_registros/demo_auditoria.py` (no necesita instalación ni red).
- Si el tiempo se acorta a 5 minutos, saltar las diapositivas 4 y 7 y decir su idea central en una frase.

## Preguntas probables

- ¿Por qué normativa española y no colombiana? Porque la empresa del caso es española; cada punto legal lleva su equivalente colombiano (apartado 7.3 del informe).
- ¿De dónde salen las cifras de costos? Son una estimación propia con supuestos explícitos en la tabla de costos; la referencia externa es el informe de IBM de 2026.
- ¿El incidente es real? La empresa sí. El incidente documentado es el de 2020; el del 10 de marzo es el escenario de la guía.
