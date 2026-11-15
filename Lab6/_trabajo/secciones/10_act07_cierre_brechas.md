# 10. Actividad 7: cierre de brechas de seguridad

La guía parte de que la empresa ya fue atacada y pregunta cómo deben cerrarse las brechas detectadas y cómo lograr que los sistemas resistan nuevos ataques. El material del curso define el cierre de brechas como "la identificación de vulnerabilidades en los sistemas tecnológicos y la implementación de medidas correctivas para prevenir que los atacantes exploten esas debilidades", y describe un proceso de tres pasos: análisis de la vulnerabilidad, desarrollo de la solución y validación de que la solución resolvió el problema (Ochoa Agudelo, 2026d). De los tipos de brecha que enumera, el caso reúne dos: una brecha de acceso, por la red sin segmentar, y una deficiencia en el sistema de autenticación, por fiarse de la dirección IP.

## 10.1 El proceso de cierre

Cada vulnerabilidad del capítulo 6 se cierra con los mismos tres pasos, a los que añado un cuarto que el caso hace necesario.

El análisis determina qué permitió exactamente el ataque y hasta dónde llega el problema. No basta con arreglar el conmutador donde se detectó el envenenamiento; hay que revisar todos los del centro de datos, porque la misma configuración de fábrica estará en todos.

La solución se diseña y se aplica como un cambio controlado. Cada modificación de la red o de la base de datos pasa por la gestión de cambios, con alguien que la pide, alguien que la aprueba y un plan de marcha atrás, que es lo que exige el control 8.32 del Anexo A (ISO/IEC, 2022b).

La validación comprueba que la brecha ya no se puede explotar. Es el paso que distingue cerrar una brecha de creer que se cerró, y se hace intentando de nuevo el ataque en condiciones controladas.

El cuarto paso es dejar evidencia. Una brecha se da por cerrada cuando existe la prueba de su validación y el propietario del activo la firma. Es la misma secuencia que la norma pide para cualquier no conformidad: se identifica, se corrige, se analiza la causa, se aplica la acción correctiva y se verifica su eficacia (Ochoa Agudelo, 2026c).

## 10.2 Plan de cierre por horizontes

Las brechas no se cierran todas a la vez. Unas medidas pueden activarse en horas y otras exigen compras, pruebas y ventanas de mantenimiento. La Tabla [[t:cierre]] ordena el trabajo en cuatro horizontes, y la Figura [[f:hojaruta]] lo sitúa en el calendario a partir del 10 de marzo.

| Horizonte | Acciones | Brechas | Responsable | Criterio de cierre |
|---|---|---|---|---|
| Contención, 0 a 7 días | Aislar la base de datos con listas de acceso provisionales. Rotar todas las credenciales de servicio y de administración. Activar la inspección de ARP y la seguridad de puertos en los conmutadores del centro de datos. Preservar las evidencias. Notificar a las autoridades y a los afectados. | V2 y, de forma provisional, V1 y V8 | Área de Redes y CISO | Contadores de descartes ARP activos; credenciales anteriores revocadas; justificantes de las notificaciones |
| Corrección, 8 a 30 días | TLS mutuo entre la aplicación y la base de datos. Retirar la autorización por dirección IP. Casos de uso de detección en el SIEM y relojes sincronizados. | V3, V4 y V7 | Dirección de Tecnología y SOC | Captura que muestra el tráfico cifrado; conexión sin certificado rechazada; alerta de prueba generada y atendida |
| Refuerzo, 31 a 90 días | Segmentación definitiva con cortafuegos interno y filtrado antisuplantación. Control de acceso a la red y cierre de tomas sin uso. Cifrado por campo y enmascaramiento. Auditoría de cambios con doble validación. | V1, V5, V6 y V8 | Área de Redes, Dirección de Tecnología y Dirección de Operaciones | Prueba de alcance entre zonas; equipo no registrado sin acceso a la red; campos sensibles ilegibles en una consulta directa |
| Consolidación, 91 a 180 días | Prueba de intrusión interna que reproduzca el ataque. Simulacro del plan de recuperación y de crisis. Auditoría interna y revisión por la Dirección. Actualización de las normas internas y de la declaración de aplicabilidad. | V9 | CISO, Auditoría Interna y Dirección General | Informe de la prueba sin hallazgos críticos; actas de la auditoría y de la revisión |

*Tabla [[t:cierre]].* Plan de cierre de brechas por horizontes, con responsable y criterio de cierre.

![](diagramas/06_hoja_ruta.png)

*Figura [[f:hojaruta]].* Hoja de ruta de cierre de brechas. Las tareas en rojo son las de contención de la primera semana.

El orden responde a dos criterios. Primero va lo que corta el ataque con menos cambios: activar funciones que los conmutadores ya tienen y cambiar credenciales que hay que dar por comprometidas. Después va lo que elimina la causa, que es el cifrado con autenticación mutua y la retirada de la confianza por dirección. La segmentación definitiva y el control de acceso a la red llegan en el tercer horizonte porque tocan la arquitectura y necesitan pruebas previas para no interrumpir el servicio.

## 10.3 Validar que el cierre es real

Cada horizonte termina con una comprobación y no con una declaración. Tres técnicas se complementan. La primera es repetir el ataque: un equipo de pruebas intenta envenenar ARP y suplantar la dirección del servidor de aplicaciones, y el resultado esperado es que el conmutador descarte los paquetes y la base de datos rechace la conexión. La segunda es auditar la configuración de todos los equipos contra la línea base aprobada, porque basta un conmutador sin proteger para reabrir la brecha. La tercera es mirar los indicadores del capítulo 9 durante varias semanas: si el porcentaje de conexiones con TLS mutuo no llega al cien por cien, queda algún sistema fuera.

El precedente de la propia compañía muestra que este trabajo es posible bajo presión. Tras el ataque de agosto de 2020, Mapfre extendió en tres días el doble factor a todos los accesos remotos, reforzó la protección de sus copias de seguridad y ejecutó un plan de fortificación de su entorno, medidas que la AEPD valoró al archivar el expediente (AEPD, 2021).

## 10.4 Mitigar futuras brechas y ganar resiliencia

Cerrar las brechas del incidente no impide que aparezcan otras. Cuatro prácticas mantienen el cierre en el tiempo.

La línea base de configuración, con detección de desviaciones, evita que un cambio posterior desactive una protección sin que nadie lo note. La gestión de vulnerabilidades, hecha de forma proactiva, revisa de manera periódica los sistemas en busca de debilidades nuevas, tanto de software como de configuración. Las pruebas periódicas confirman desde fuera lo que la organización cree de sí misma; DORA dedica sus artículos 24 a 27 a las pruebas de resiliencia operativa digital y prevé pruebas de penetración basadas en amenazas para las entidades de mayor tamaño. Y las auditorías periódicas, que el material del curso señala como necesarias "para detectar nuevas brechas de seguridad" (Ochoa Agudelo, 2026d), comprueban que las normas internas se cumplen.

La resiliencia va un paso más allá de cerrar brechas. El curso la define como la capacidad de una organización para "resistir, absorber, recuperarse y adaptarse a eventos adversos", y propone un marco de tres momentos (Ochoa Agudelo, 2026e). La anticipación comprende el análisis de riesgos del capítulo 8 y los simulacros de mesa. La respuesta aguda es la toma de decisiones bajo presión, que se entrena con el plan de recuperación del capítulo 14. La evolución es "la adaptación de la arquitectura de red tras la crisis", que en este caso es literal: la red que salga del plan de cierre no será la misma que tenía la compañía el 10 de marzo. La pregunta que ese marco propone ya no es si habrá otro ataque, es cuándo llegará y cómo lo superará la organización.
