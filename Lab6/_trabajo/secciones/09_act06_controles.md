# 9. Actividad 6: controles de seguridad

La guía pide al menos tres controles, que pueden ser técnicos, administrativos o físicos, y la justificación de por qué cada uno es apropiado. El material del curso clasifica los controles de dos maneras. Por su función son preventivos, detectivos o correctivos. Por su naturaleza son administrativos, cuando definen cómo se gestiona la seguridad e involucran a personas y responsabilidades; técnicos, cuando son herramientas que operan de forma automática, y físicos, cuando protegen el entorno donde están los equipos (Ochoa Agudelo, 2026d). Uso las dos clasificaciones a la vez.

## 9.1 Del riesgo al control

Los controles de este capítulo no salen de un catálogo. Cada uno responde a un riesgo del capítulo 8 y a una vulnerabilidad del capítulo 6, que es el criterio que se dio en clase: primero se identifican los riesgos y después se decide qué controles hacen falta según el sistema, el tamaño y las dependencias de la empresa, porque eso es lo que luego se audita (Ochoa Agudelo, 2026c). El video sobre los controles tecnológicos visto en la misma sesión añade dos advertencias que he seguido. La norma no impone una herramienta ni una marca, de modo que cada control se describe por lo que hace y no por el producto que lo implementa. Y los controles físicos son "los grandes olvidados", aunque en un ataque que empieza en una toma de red son parte de la solución.

La Tabla [[t:controles]] presenta los dieciséis controles propuestos con su clasificación, los controles del Anexo A de 2022 que desarrollan, la función del marco NIST a la que contribuyen y los riesgos que tratan.

| ID | Control | Naturaleza | Función | Anexo A | NIST CSF | Riesgos |
|---|---|---|---|---|---|---|
| C1 | Segmentación del centro de datos: base de datos en una zona aislada tras un cortafuegos interno | Técnico | Preventivo | 8.22, 8.20 | PR.IR | R1, R2 |
| C2 | Protecciones de capa 2: DHCP snooping, inspección dinámica de ARP, IP Source Guard y seguridad de puertos | Técnico | Preventivo | 8.20, 8.21, 8.9 | PR.IR | R1, R10 |
| C3 | Filtrado antisuplantación (uRPF y filtros de entrada y salida) | Técnico | Preventivo | 8.20, 8.21 | PR.IR | R2 |
| C4 | Cifrado y autenticación mutua de las comunicaciones internas | Técnico | Preventivo | 8.24, 8.21, 5.14 | PR.DS | R1, R2, R8 |
| C5 | Autenticación fuerte y mínimo privilegio, sin confianza por dirección IP | Técnico y administrativo | Preventivo | 5.15 a 5.18, 8.2, 8.3, 8.5 | PR.AA | R2, R4, R8 |
| C6 | Control de acceso a la red (802.1X) y cierre de tomas sin uso | Técnico | Preventivo | 8.20, 8.1 | PR.AA | R10 |
| C7 | Protección del dato: cifrado en reposo y por campo, enmascaramiento y prevención de fuga | Técnico | Preventivo | 8.11, 8.12, 8.24, 5.34 | PR.DS | R1, R3 |
| C8 | Registro, monitoreo y detección | Técnico | Detectivo | 8.15, 8.16, 8.17 | DE.CM, DE.AE | R1, R2, R4, R8, R9 |
| C9 | Auditoría de cambios en datos críticos con doble validación | Técnico y administrativo | Detectivo y correctivo | 8.15, 5.3, 5.33, 8.32 | DE.CM, PR.DS | R4, R9 |
| C10 | Gobierno y normativa interna: política, normas, inventario y declaración de aplicabilidad | Administrativo | Preventivo | 5.1, 5.2, 5.9, 5.12, 5.31 | GV.PO, GV.RR, ID.AM | R6 |
| C11 | Gestión de incidentes y notificación | Administrativo | Correctivo | 5.24 a 5.28, 6.8 | RS.MA, RS.CO | R3, R5, R6, R7 |
| C12 | Continuidad y recuperación: análisis de impacto, plan, copias y pruebas | Administrativo y técnico | Correctivo | 5.29, 5.30, 8.13, 8.14 | RC.RP | R4, R5 |
| C13 | Formación y concienciación por perfil | Administrativo | Preventivo | 6.3, 6.2, 6.4 | PR.AT | R7 |
| C14 | Seguridad física del centro de datos y del cableado | Físico | Preventivo y detectivo | 7.1, 7.2, 7.4, 7.8, 7.12 | PR.AA | R10 |
| C15 | Gestión de vulnerabilidades y verificación independiente | Administrativo y técnico | Detectivo y correctivo | 8.8, 8.9, 5.35, 5.36, 8.34 | ID.RA, ID.IM | Todos |
| C16 | Gestión de terceros y transferencia del riesgo | Administrativo | Preventivo y correctivo | 5.19 a 5.22 | GV.SC | R3, R6 |

*Tabla [[t:controles]].* Controles propuestos, clasificados por naturaleza y por función, con su correspondencia en el Anexo A de ISO/IEC 27001:2022 y en el marco NIST CSF 2.0.

## 9.2 Por qué cada control es apropiado y cómo se demuestra

En seguridad de la información "no basta con decir que un control existe, hay que poder demostrar que está implementado y que funciona" (Ochoa Agudelo, 2026c). La Tabla [[t:controles_just]] justifica cada control frente al caso, indica la evidencia que pediría un auditor y propone un indicador para medirlo.

| ID | Por qué es apropiado en este caso | Evidencia para el auditor | Indicador |
|---|---|---|---|
| C1 | El atacante alcanzó la base de datos porque estaba en su mismo segmento. Aislarla reduce a un puñado los equipos que pueden hablarle. | Diagrama de red vigente, reglas del cortafuegos y prueba de alcance entre zonas | Porcentaje de flujos hacia la base de datos que pasan por el cortafuegos interno |
| C2 | Es la respuesta directa al ARP spoofing: el conmutador descarta las respuestas ARP que no cuadran con su tabla. | Configuración de los conmutadores y contadores de paquetes ARP descartados | Porcentaje de puertos de acceso con las cuatro protecciones activas |
| C3 | Impide que circulen paquetes con una dirección de origen que no corresponde a la interfaz por la que entran. | Configuración de las interfaces y registros de descartes | Paquetes con origen inválido descartados al mes |
| C4 | Aunque alguien desvíe el tráfico, solo ve datos cifrados y no puede hacerse pasar por ningún extremo. | Parámetros del servidor, inventario de certificados y captura de tráfico cifrado | Porcentaje de conexiones a la base de datos con TLS mutuo |
| C5 | Quita valor a la dirección IP como credencial y limita lo que puede hacer una cuenta comprometida. | Matriz de roles aprobada, revisión trimestral de accesos y configuración de autenticación | Porcentaje de cuentas privilegiadas con doble factor; cuentas con privilegios excesivos |
| C6 | Un equipo desconocido no obtiene red hasta autenticarse, lo que cierra la vía de entrada más probable. | Política de acceso a la red, lista de tomas deshabilitadas y registros de autenticación | Equipos no autorizados bloqueados al mes |
| C7 | Si los datos vuelven a salir, los campos sensibles son ilegibles, y eso reduce el daño a los clientes. | Esquema de cifrado, política de enmascaramiento e informes de prevención de fuga | Porcentaje de campos sensibles cifrados o enmascarados |
| C8 | El ataque no generó alertas a tiempo. Este control acorta la detección de días a minutos. | Casos de uso documentados, alertas atendidas y retención de registros | Tiempo medio de detección y de respuesta |
| C9 | Detecta y permite revertir un cambio indebido de beneficiario, cuenta o capital. | Registro de auditoría, tiques de cambio y acta de conciliación | Cambios críticos sin tique de autorización |
| C10 | Sin responsable ni norma, las protecciones técnicas dependen de la iniciativa de cada administrador. | Política firmada, inventario vigente, declaración de aplicabilidad y actas del comité | Porcentaje de activos con propietario y clasificación |
| C11 | Los plazos legales son de horas. Sin procedimiento ensayado no se cumplen. | Procedimiento aprobado, registro de incidentes, actas de simulacros y justificantes de notificación | Porcentaje de incidentes notificados dentro de plazo |
| C12 | La operación se interrumpió. Un plan probado acota la parada y permite restaurar datos íntegros. | Análisis de impacto, plan aprobado e informes de pruebas de restauración | Tiempos de recuperación alcanzados en la última prueba |
| C13 | Quienes configuran la red y quienes atienden al cliente deben conocer la norma y saber qué hacer ante un incidente. | Plan de formación, asistencia y resultados de simulaciones | Porcentaje de personal formado |
| C14 | El envenenamiento ARP exige estar en la red local. Controlar salas, armarios y tomas quita la oportunidad. | Registros de acceso físico, grabaciones e inventario de tomas | Accesos físicos no autorizados detectados |
| C15 | Una prueba interna habría encontrado las vulnerabilidades antes que el atacante, y confirma que el cierre es real. | Informes de escaneo y de pruebas de intrusión, plan de acciones e informe de auditoría | Porcentaje de hallazgos críticos cerrados en plazo |
| C16 | Parte del riesgo viene de terceros y parte del costo puede cubrirse con un seguro. | Contratos con cláusulas de seguridad, evaluaciones de proveedores y póliza vigente | Porcentaje de proveedores críticos evaluados en el año |

*Tabla [[t:controles_just]].* Justificación de cada control frente al caso, evidencia que lo demuestra e indicador de seguimiento.

Por naturaleza, once controles tienen componente técnico, ocho administrativo y uno es físico. Por función, once previenen, cuatro detectan y cinco corrigen (algunos cumplen dos funciones). El reparto busca que la prevención no sea la única línea, que es lo que falló en el caso: había protección y no había detección dentro de la red.

## 9.3 La arquitectura que resulta

La Figura [[f:arquitectura]] muestra cómo quedan los controles técnicos sobre la red. Un equipo solo entra si se autentica. El conmutador al que se conecta valida las respuestas ARP. Las aplicaciones llegan a la base de datos por una única ruta, a través del cortafuegos interno y con TLS mutuo. Los administradores entran por un bastión con doble factor y su sesión queda registrada. Todo deja registros en la plataforma de monitoreo.

![](diagramas/05_arquitectura_segura.png)

*Figura [[f:arquitectura]].* Arquitectura de red propuesta. Entre paréntesis, el control de la Tabla [[t:controles]] que actúa en cada punto.

Como ilustración de lo que significa el control C2 en la práctica, este es un extracto de configuración de referencia para un conmutador de acceso. La sintaxis corresponde a un fabricante concreto y es solo un ejemplo; el control vale igual con cualquier otro.

```
ip dhcp snooping
ip dhcp snooping vlan 20
ip arp inspection vlan 20
ip arp inspection validate src-mac dst-mac ip
!
interface range GigabitEthernet1/0/2 - 48
 switchport mode access
 switchport access vlan 20
 switchport port-security
 switchport port-security maximum 2
 switchport port-security violation restrict
 ip verify source port-security
 ip arp inspection limit rate 15
```

La evidencia de que funciona no es el archivo de configuración. Es el contador de paquetes ARP descartados que el propio conmutador mantiene y que debe llegar al SIEM.

## 9.4 Declaración de aplicabilidad

La declaración de aplicabilidad es el documento que indica qué controles del Anexo A necesita la organización, con su justificación, y cuáles excluye y por qué. En clase se presentó como uno de los conceptos que hay que aprender sí o sí, porque no significa implementar de forma indiscriminada los más de noventa controles de la norma, sino los que el análisis de riesgos justifica (Ochoa Agudelo, 2026c). En España tiene además respaldo legal: el Real Decreto 43/2021 pide que las medidas adoptadas se formalicen en una declaración de aplicabilidad suscrita por el responsable de seguridad de la información e incluida en la política que aprueba la Dirección. La Tabla [[t:soa]] resume la que corresponde al alcance de este trabajo.

| Controles del Anexo A | ¿Aplica? | Justificación | Se implementa con |
|---|---|---|---|
| 5.1, 5.2, 5.4 Políticas, funciones y responsabilidades de la dirección | Sí | La red interna y el dato necesitan responsables y reglas aprobadas | C10 |
| 5.9, 5.12, 5.13 Inventario, clasificación y etiquetado | Sí | Sin clasificación no hay criterio para exigir cifrado | C10 |
| 5.15 a 5.18 Control de acceso, identidades y autenticación | Sí | R2, R4 y R8 | C5 |
| 5.19 a 5.22 Seguridad con proveedores | Sí | Terceros con acceso a la red y a los datos | C16 |
| 5.24 a 5.28 Gestión de incidentes y recogida de evidencias | Sí | Plazos legales de 4 a 72 horas | C11 |
| 5.29, 5.30 Seguridad durante la interrupción y preparación de las TIC | Sí | R5 | C12 |
| 5.31, 5.34 Requisitos legales y protección de datos personales | Sí | RGPD, LOPDGDD y DORA | C7, C10 |
| 5.35, 5.36 Revisión independiente y cumplimiento | Sí | Verificar que el cierre de brechas es real | C15 |
| 6.3, 6.8 Formación y notificación de eventos | Sí | Personas que configuran, operan y atienden | C13, C11 |
| 7.1, 7.2, 7.4, 7.8, 7.12 Perímetro, acceso físico, vigilancia, ubicación de equipos y cableado | Sí | El ataque exige presencia en la red local | C14 |
| 8.2, 8.3, 8.5 Privilegios, restricción de acceso y autenticación segura | Sí | V3 y V8 | C5 |
| 8.8, 8.9 Vulnerabilidades técnicas y gestión de la configuración | Sí | Las debilidades eran de configuración | C15, C2 |
| 8.11, 8.12, 8.24 Enmascaramiento, prevención de fuga y criptografía | Sí | V4 y V8 | C4, C7 |
| 8.13, 8.14 Copias de seguridad y redundancia | Sí | R4 y R5 | C12 |
| 8.15, 8.16, 8.17 Registro, monitoreo y sincronización de relojes | Sí | V7 | C8, C9 |
| 8.20, 8.21, 8.22 Seguridad, servicios y segregación de redes | Sí | V1, V2 y V5: el origen del incidente | C1, C2, C3, C6 |
| 8.32 Gestión de cambios | Sí | Evitar que una protección se desactive sin aprobación | C9, C10 |
| 8.4, 8.25 a 8.31, 8.33 Código fuente, desarrollo seguro y datos de prueba | No, en este alcance | El alcance es la operación del servicio de pólizas; el desarrollo de software tiene su propio alcance | No procede |
| 7.9 Seguridad de los activos fuera de las instalaciones | No, en este alcance | Los activos del alcance no salen del centro de datos | No procede |
| 8.23 Filtrado web | No, en este alcance | Corresponde al alcance de puesto de trabajo, no al del centro de datos | No procede |

*Tabla [[t:soa]].* Resumen de la declaración de aplicabilidad para el servicio de pólizas de vida, con las inclusiones y las exclusiones justificadas.

Las exclusiones no son descuidos. Cada una remite al alcance definido en el apartado 2.2 y dejaría de valer si ese alcance cambiara.
