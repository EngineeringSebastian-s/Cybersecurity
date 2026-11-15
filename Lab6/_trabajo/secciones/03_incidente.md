# 3. El incidente: hechos, anatomía y principios afectados

## 3.1 Lo que dice el caso y lo que este informe supone

La guía describe el incidente en pocas líneas. El resto hay que reconstruirlo, y un análisis honesto debe dejar claro qué viene del enunciado y qué es una hipótesis de trabajo. La Tabla [[t:hechos]] hace esa separación. Los supuestos se identifican con una S para citarlos más adelante.

| Hechos que da la guía | Supuestos de este informe y su justificación |
|---|---|
| El 10 de marzo el equipo de TI detectó varios accesos no autorizados a la base de datos de clientes. | S1. El caso no indica el año. Se asume 2026 para aplicar la normativa vigente, en particular DORA, aplicable desde el 17 de enero de 2025. |
| Los accesos se hicieron con suplantación de direcciones IP y con un ataque de ARP spoofing. | S2. Para envenenar ARP hay que estar en la misma red local, así que el atacante tenía presencia interna: un equipo comprometido o una conexión a una toma de red. El caso no dice cuál. |
| Los atacantes interceptaron nombres, direcciones, números de identificación y detalles de pólizas. | S3. La base de datos compartía segmento de capa 2 con equipos menos confiables y el tráfico entre la aplicación y la base de datos viajaba sin cifrar. De otro modo lo interceptado no habría sido legible. |
| Hubo acceso no autorizado a información confidencial. | S4. La base de datos autorizaba las conexiones por la dirección IP de origen del servidor de aplicaciones. Por eso suplantar esa dirección dio acceso. |
| Hubo pérdidas económicas significativas por fraude. | S5. El caso no cuantifica los afectados. Para dimensionar se trabaja con tres escenarios: 50.000, 250.000 y 1.000.000 de clientes. |
| La brecha se divulgó públicamente y dañó la reputación. | S6. Los detalles de pólizas de vida incluyen beneficiarios, capitales y datos bancarios, y pueden incluir declaraciones de salud. S8. No se sabe si la divulgación partió de la empresa o de terceros. |
| La operación se interrumpió mientras se corregía el problema y se hacían auditorías. | S7. La degradación del servicio duró entre uno y siete días según el escenario. |

*Tabla [[t:hechos]].* Hechos del enunciado y supuestos de trabajo (S1 a S8).

## 3.2 Cómo funcionan las dos técnicas y por qué se combinan

El protocolo ARP resuelve qué dirección física (MAC) corresponde a una dirección IP dentro de una red local. Se definió en 1982 y no autentica las respuestas: un equipo acepta cualquier respuesta ARP que reciba, aunque no la haya pedido (Plummer, 1982). El ARP spoofing aprovecha esa confianza. El atacante envía respuestas falsas al servidor de aplicaciones y a la base de datos para que cada uno crea que la dirección IP del otro está en la tarjeta de red del atacante. Desde ese momento el tráfico entre ambos pasa por su equipo, que lo lee y lo reenvía para que nadie note el desvío. El catálogo MITRE ATT&CK lo recoge como la técnica T1557.002, envenenamiento de la caché ARP, una variante del adversario en el medio (MITRE, s. f.).

La suplantación de IP consiste en enviar paquetes con una dirección de origen que no es la propia. Sola sirve de poco contra una conexión TCP, porque las respuestas viajan hacia la dirección suplantada y el atacante no las ve. Combinada con el envenenamiento ARP el problema desaparece: el atacante ya recibe el tráfico destinado al servidor legítimo, así que puede abrir sus propias conexiones con la dirección de ese servidor y sostenerlas. Si la base de datos decide a quién deja entrar mirando la dirección de origen, el atacante entra como si fuera la aplicación. Esa debilidad tiene nombre propio en el catálogo de debilidades de software: confiar en la dirección IP para autenticar (CWE-291). La Figura [[f:anatomia]] resume las tres fases con direcciones de ejemplo.

![](diagramas/01_anatomia_ataque.png)

*Figura [[f:anatomia]].* Anatomía del ataque en tres fases: reconocimiento del segmento, envenenamiento ARP con interceptación del tráfico y suplantación de la IP del servidor de aplicaciones. Las direcciones son ilustrativas.

Las dos técnicas explican los dos daños del caso. La interceptación viene del envenenamiento ARP, que solo rinde si el tráfico va sin cifrar. El acceso directo a la base de datos viene de la suplantación de IP, que solo rinde si la autorización depende de la dirección. Las dos explotan decisiones de diseño de la red, sin necesidad de vulnerar una contraseña ni de aprovechar un fallo de programación.

## 3.3 Cronología reconstruida

La guía solo da una fecha, el 10 de marzo, que es la de la detección. La Figura [[f:cronologia]] ordena lo que tuvo que ocurrir antes, que es una reconstrucción, y lo que la ley obliga a hacer después, que son plazos ciertos.

![](diagramas/02_cronologia.png)

*Figura [[f:cronologia]].* Cronología reconstruida del incidente. Las fechas previas a la detección son supuestas; los plazos posteriores provienen del RGPD y del Reglamento Delegado (UE) 2025/301.

## 3.4 El incidente en las ocho preguntas del caso de clase

En clase se trabajó un caso de fuga de datos con ocho preguntas de auditor (Ochoa Agudelo, 2026c). Aplicadas al incidente de Mapfre dan el mapa de este informe, que la Tabla [[t:ochopreguntas]] recoge junto con el capítulo donde se desarrolla cada respuesta.

| Pregunta | Respuesta breve | Se desarrolla en |
|---|---|---|
| ¿Qué activo estaba en riesgo? | La base de datos de clientes y pólizas de vida (A1) y el núcleo asegurador que la usa (A2). | Capítulos 4 y 5 |
| ¿Qué amenaza ocurrió? | Un atacante con presencia en la red interna interceptó el tráfico y suplantó a un servidor de confianza. | Capítulo 3 |
| ¿Qué vulnerabilidad permitió el ataque? | Red sin segmentar ni proteger en capa 2, tráfico sin cifrar y autorización basada en la dirección IP (V1 a V5). | Capítulo 6 |
| ¿Qué principio se afectó? | La confidencialidad de forma directa; la autenticidad como vía de entrada; la integridad y la disponibilidad quedaron comprometidas. | Apartado 3.5 |
| ¿Qué controles deberían existir? | Segmentación, protecciones de capa 2, cifrado con autenticación mutua, mínimo privilegio y monitoreo (C1 a C16). | Capítulo 9 |
| ¿Qué debería hacer el sistema de gestión? | Tratar estos riesgos con un plan aprobado, medir los controles y auditarlos. | Capítulos 8 y 17 |
| ¿Qué evidencias debería conservar la empresa? | Registros de red y de base de datos, tablas ARP, capturas de tráfico, imágenes forenses y la cadena de custodia. | Capítulos 11, 15 y 16 |
| ¿Qué debería revisar después del incidente? | La eficacia de cada control, el plan de recuperación, los tiempos de notificación y la declaración de aplicabilidad. | Capítulos 10 y 17 |

*Tabla [[t:ochopreguntas]].* El incidente analizado con las ocho preguntas del caso de clase.

## 3.5 Principios de seguridad afectados

La confidencialidad fue el principio dañado de forma directa. Información que solo debía conocer personal autorizado, incluidos documentos de identidad y detalles de pólizas, llegó a terceros. El material del curso define la confidencialidad como la garantía de que la información no sea conocida por personas, organizaciones o procesos sin autorización (Merino Bada, s. f.), y eso es lo que falló.

La vía de entrada fue un fallo de autenticidad. Esa dimensión, que el mismo material añade a la tríada clásica, garantiza la identidad de quien origina una información. Tanto la respuesta ARP falsa como el paquete con IP suplantada son mentiras sobre la identidad de un equipo, y la red las creyó porque no tenía forma de comprobarlas.

La integridad no consta como alterada en el enunciado, pero quedó comprometida. Quien está en medio de una conversación puede modificarla, y quien entra a la base de datos como si fuera la aplicación puede cambiar un beneficiario o una cuenta de cobro igual que puede leerlos. El docente puso en clase el ejemplo del atacante que cambia el salario de un empleado en la base de datos como problema típico de integridad (Ochoa Agudelo, 2026c). Por eso la actividad 13 se toma en serio aunque el caso no describa cambios.

La disponibilidad se afectó por la respuesta y no por el ataque: la operación se interrumpió mientras se contenía el problema y se auditaban los sistemas. Por último, la trazabilidad, la capacidad de determinar quién hizo qué y cuándo, quedó en entredicho. Si los accesos se detectaron después de producirse y no antes, los registros no estaban generando alertas a tiempo, y sin buenos registros tampoco se puede acotar con certeza qué datos salieron.
