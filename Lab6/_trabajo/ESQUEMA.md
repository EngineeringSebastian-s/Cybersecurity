# ESQUEMA definitivo del informe (checkpoint mayor de F3, 13/11/2026)

Concilia la guía (13 actividades), las indicaciones de clase (`Lab6/guias/instrucciones_clase.md`) y el material (`Lab6/_trabajo/notas/`). Todo lo que se redacte debe usar los identificadores y valores de este archivo.

## Enfoque

- **Voz:** auditor o consultor de seguridad que analiza el caso ("piense como auditor, no como hacker"). Cada control lleva la evidencia que lo demuestra.
- **Énfasis pedido por el docente:** riesgo, declaración de aplicabilidad (SoA), Anexo A, auditoría, evidencia, incidentes y mejora continua, más que explicar controles sueltos.
- **Marco:** España y Unión Europea como eje (empresa del caso; el docente proyectó RD-ley 12/2018 y RD 43/2021) con espejo colombiano (Ley 1581, 1266, 1273, SIC, SFC). Distinguir siempre ley, norma, marco y buena práctica.
- **Versiones:** ISO/IEC 27001:2022 y 27002:2022 (93 controles; A.5 organizacionales, A.6 personas, A.7 físicos, A.8 tecnológicos), dejando la equivalencia con la guía NQA de 2013 (114 controles); NIST CSF 2.0 (seis funciones; la clase citó las cinco clásicas).
- **Dimensiones:** C, I, D como pide la guía, más autenticidad y trazabilidad (material de UNIR): la suplantación ataca la autenticidad y la auditoría de registros es trazabilidad.
- **Honestidad del caso:** Mapfre es real y se usan sus datos públicos verificados; los hechos del 10 de marzo se toman de la guía; lo que la guía no dice se declara como supuesto. El incidente real documentado es el ransomware de agosto de 2020 (AEPD E/09159/2020), que se usa como referencia de buena respuesta.
- **Estilo:** prosa ampliada, sin rayas largas, reglas de humanizer. Citas APA 7 dentro del texto.

## Supuestos de trabajo (declararlos en la sección 3)

- S1. El caso no dice el año: se asume 2026 para aplicar la normativa vigente (DORA es aplicable desde el 17/01/2025).
- S2. El atacante logró presencia en la red interna (equipo comprometido o conexión a una toma de red); el caso no dice cómo.
- S3. La base de datos compartía dominio de difusión de capa 2 con equipos menos confiables y el tráfico entre aplicación y base de datos no iba cifrado.
- S4. El acceso a la base de datos se autorizaba por la dirección IP de origen del servidor de aplicaciones.
- S5. El caso no da volumen: para dimensionar se usan tres escenarios de clientes afectados: 50.000 (bajo), 250.000 (base) y 1.000.000 (alto).
- S6. Los "detalles de pólizas" de vida incluyen beneficiarios, capitales y datos bancarios de cobro, y pueden incluir declaraciones de salud (categoría especial, art. 9 RGPD).
- S7. Interrupción operativa: 1, 3 y 7 días de servicio degradado según escenario.
- S8. La "divulgación pública" pudo venir de la empresa o de terceros; el caso no lo aclara.

## Identificadores

### Activos (actividades 1 y 2). Escala: Alto 3, Medio 2, Bajo 1. Valor del activo = suma de C, I y D (de 3 a 9).

| ID | Activo | Tipo | Propietario | C | I | D | A | T | Etiqueta |
|---|---|---|---|---|---|---|---|---|---|
| A1 | Base de datos de clientes y pólizas de vida | Información | Dirección de Negocio Vida | Alto | Alto | Alto | Alto | Alto | Restringida |
| A2 | Sistema central de gestión de pólizas (núcleo asegurador) | Aplicación | Dirección de Operaciones | Alto | Alto | Alto | Alto | Alto | Restringida |
| A3 | Aplicaciones y canales digitales (servidores de aplicación, portal y app de clientes, API de mediadores) | Aplicación y servicio | Dirección de Tecnología | Medio | Alto | Alto | Alto | Medio | Uso interno |
| A4 | Red interna del centro de datos (conmutadores, encaminadores, cortafuegos, VLAN) | Infraestructura | Área de Redes | Medio | Alto | Alto | Alto | Medio | Uso interno |
| A5 | Identidades y credenciales (directorio, cuentas de servicio y de administración) | Información y servicio | CISO | Alto | Alto | Alto | Alto | Alto | Reservada |
| A6 | Registros de auditoría y plataforma de monitoreo | Información | CISO (SOC) | Medio | Alto | Medio | Alto | Alto | Restringida |
| A7 | Copias de seguridad y centro de respaldo | Información e infraestructura | Dirección de Tecnología | Alto | Alto | Alto | Medio | Medio | Restringida |
| A8 | Centro de proceso de datos e instalaciones (salas técnicas, cableado, tomas de red) | Instalación | Seguridad Corporativa | Medio | Medio | Alto | Medio | Medio | Uso interno |
| A9 | Personas (equipos de TI y seguridad, empleados y red de mediadores) | Personas | Recursos Humanos | Medio | Medio | Alto | Medio | Medio | Uso interno |
| A10 | Marca y confianza de clientes y supervisores | Intangible | Dirección General | Bajo | Alto | Alto | Alto | Bajo | Pública |

Etiquetas de clasificación (modelo del temario de Renfe): Reservada, Restringida, Uso interno, Pública.

### Vulnerabilidades (actividad 3)

| ID | Vulnerabilidad | Tipo de evidencia | Mitigación (control) |
|---|---|---|---|
| V1 | Segmentación insuficiente: la base de datos comparte dominio de difusión con equipos menos confiables | Condición necesaria del ARP spoofing | C1 |
| V2 | Conmutadores sin protecciones de capa 2 (DHCP snooping, inspección dinámica de ARP, IP Source Guard, seguridad de puertos) | Condición necesaria | C2 |
| V3 | Confianza basada en la dirección IP para autorizar el acceso a la base de datos | Condición necesaria del IP spoofing | C5 |
| V4 | Tráfico interno sin cifrar ni autenticar entre aplicación y base de datos | Condición necesaria de la interceptación legible | C4 |
| V5 | Sin filtrado antisuplantación (uRPF, filtros de entrada) en encaminadores y cortafuegos internos | Condición necesaria del IP spoofing entre segmentos | C3 |
| V6 | Sin control de acceso a la red (802.1X/NAC) y tomas de red activas sin control | Probable (S2) | C6, C14 |
| V7 | Registro y monitoreo insuficientes (sin alertas de anomalías ARP ni de consultas masivas; registros sin proteger; relojes sin sincronizar) | Probable: la detección fue posterior al acceso | C8, C9 |
| V8 | Privilegios excesivos de las cuentas de servicio y datos legibles en reposo (sin enmascarar ni cifrar por campo) | Probable | C5, C7 |
| V9 | Debilidades de gobierno: políticas sin comunicar, sin inventario y clasificación vigentes, sin pruebas internas de intrusión ni simulacros | Probable | C10, C13, C15 |

### Riesgos (actividad 5). Probabilidad e impacto de 1 a 5; nivel = P x I: 1 a 4 Bajo, 5 a 9 Medio, 10 a 16 Alto, 17 a 25 Crítico. Criterio de aceptación: residual menor o igual a 9, aprobado por el propietario del riesgo.

| ID | Riesgo | Activos | Amenaza | Vuln. | Consecuencia | P | I | Inherente | Tratamiento | Controles | P res. | I res. | Residual | Propietario |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | Interceptación de datos personales en tránsito por un intermediario | A1, A4 | ARP spoofing | V1, V2, V4 | Pérdida de confidencialidad; violación de datos | 5 | 5 | 25 Crítico | Mitigar | C1, C2, C4, C8 | 2 | 4 | 8 Medio | Dirección de Tecnología |
| R2 | Acceso no autorizado a la base de datos suplantando la IP de un servidor de confianza | A1, A2 | IP spoofing | V3, V5 | Consulta y extracción masiva | 5 | 5 | 25 Crítico | Evitar y mitigar | C3, C5, C1 | 1 | 5 | 5 Medio | CISO |
| R3 | Fraude a clientes con los datos sustraídos | A1, A10 | Uso fraudulento de datos | V8 | Pérdidas económicas e indemnizaciones | 4 | 5 | 20 Crítico | Mitigar y transferir | C7, C11, C16 | 2 | 4 | 8 Medio | Dirección de Negocio Vida |
| R4 | Modificación no autorizada de datos de pólizas (beneficiarios, cuentas de pago, capitales) | A1, A2 | Manipulación de datos | V3, V7, V8 | Pérdida de integridad; pagos indebidos | 3 | 5 | 15 Alto | Mitigar | C5, C9, C12 | 1 | 5 | 5 Medio | Dirección de Operaciones |
| R5 | Interrupción de la operación durante la contención y las auditorías | A2, A3, A4 | Indisponibilidad | V9 | Emisión, cobros y siniestros detenidos | 4 | 4 | 16 Alto | Mitigar | C12, C11 | 2 | 3 | 6 Medio | Dirección de Operaciones |
| R6 | Sanción regulatoria y reclamaciones por medidas insuficientes o notificación tardía | A10 | Incumplimiento | V7, V9 | Multas e indemnizaciones | 4 | 4 | 16 Alto | Mitigar y transferir | C10, C11, C16 | 2 | 4 | 8 Medio | DPD y Asesoría Jurídica |
| R7 | Daño reputacional y pérdida de clientes y mediadores | A10 | Divulgación pública | V9 | Cancelaciones y menor nueva producción | 4 | 5 | 20 Crítico | Mitigar | C11, C13 | 2 | 4 | 8 Medio | Dirección General |
| R8 | Robo de credenciales de servicio o de administración capturadas en tránsito | A5 | Captura de credenciales | V4, V8 | Movimiento lateral y persistencia | 4 | 4 | 16 Alto | Mitigar | C4, C5, C8 | 2 | 3 | 6 Medio | CISO |
| R9 | Detección tardía e imposibilidad de reconstruir lo ocurrido | A6 | Registros insuficientes o alterables | V7 | Pérdida de trazabilidad; alcance indeterminado | 4 | 4 | 16 Alto | Mitigar y aceptar el residual | C8, C9 | 1 | 3 | 3 Bajo | CISO (SOC) |
| R10 | Conexión de un equipo no autorizado a la red interna | A4, A8 | Acceso físico o equipo comprometido | V6 | Punto de partida de nuevos ataques | 3 | 4 | 12 Alto | Mitigar y aceptar el residual | C6, C14, C2 | 1 | 4 | 4 Bajo | Área de Redes |

Las cuatro opciones de tratamiento quedan representadas: evitar (R2: retirar la autorización por IP y el acceso directo), mitigar (todos), transferir (R3 y R6: póliza de ciberriesgo y cláusulas contractuales) y aceptar (residuales de R9 y R10).

### Controles (actividad 6). Naturaleza: T técnico, A administrativo, F físico. Función: P preventivo, D detectivo, C correctivo.

| ID | Control | Nat. | Func. | Anexo A (2022) | NIST CSF 2.0 | Riesgos | Evidencia para el auditor | Indicador |
|---|---|---|---|---|---|---|---|---|
| C1 | Segmentación del centro de datos: base de datos en zona aislada tras cortafuegos interno, alcanzable solo desde los servidores de aplicación | T | P | 8.22, 8.20 | PR.IR | R1, R2 | Diagrama de red vigente, reglas del cortafuegos, prueba de alcance entre zonas | % de flujos hacia la base de datos que pasan por el cortafuegos interno |
| C2 | Protecciones de capa 2: DHCP snooping, inspección dinámica de ARP, IP Source Guard, seguridad de puertos | T | P | 8.20, 8.21, 8.9 | PR.IR | R1, R10 | Configuración de los conmutadores y contadores de paquetes ARP descartados | % de puertos de acceso con las cuatro protecciones activas |
| C3 | Filtrado antisuplantación: uRPF y filtros de entrada y salida en encaminadores y cortafuegos internos | T | P | 8.20, 8.21 | PR.IR | R2 | Configuración de interfaces y registros de paquetes descartados por origen inválido | Paquetes con origen falso descartados por mes |
| C4 | Cifrado y autenticación mutua de las comunicaciones internas (TLS mutuo aplicación a base de datos; IPsec o MACsec en enlaces críticos) | T | P | 8.24, 8.21, 5.14 | PR.DS | R1, R2, R8 | Parámetros del servidor de base de datos, inventario de certificados, captura que muestre tráfico cifrado | % de conexiones a la base de datos con TLS mutuo |
| C5 | Autenticación fuerte y mínimo privilegio: sin confianza por IP, cuentas de servicio con certificado y rotación, MFA y gestión de accesos privilegiados, RBAC | T, A | P | 5.15, 5.17, 5.18, 8.2, 8.3, 8.5 | PR.AA | R2, R4, R8 | Matriz de roles aprobada, revisión trimestral de accesos, configuración de autenticación | % de cuentas privilegiadas con MFA; cuentas con privilegios excesivos |
| C6 | Control de acceso a la red (802.1X/NAC) y cierre de tomas sin uso | T | P | 8.20, 8.1 | PR.AA | R10 | Política de NAC, lista de puertos deshabilitados, registros de autenticación de equipos | Equipos no autorizados bloqueados por mes |
| C7 | Protección del dato: cifrado en reposo, cifrado por campo de identificadores y datos bancarios, enmascaramiento, prevención de fuga | T | P | 8.11, 8.12, 8.24, 5.34 | PR.DS | R1, R3 | Esquema de cifrado, política de enmascaramiento, informes de la herramienta de prevención de fuga | % de campos sensibles cifrados o enmascarados |
| C8 | Registro, monitoreo y detección: SIEM, sensor de red con reglas de ARP, monitoreo de actividad de base de datos, relojes sincronizados, registros inmutables | T | D | 8.15, 8.16, 8.17 | DE.CM, DE.AE | R1, R2, R4, R8, R9 | Casos de uso documentados, alertas generadas y atendidas, retención de registros | Tiempo medio de detección y de respuesta |
| C9 | Auditoría de cambios en datos críticos: tabla de auditoría con disparadores, doble validación de cambios de beneficiario y cuenta, conciliación diaria | T, A | D, C | 8.15, 5.3, 8.32, 5.33 | DE.CM, PR.DS | R4, R9 | Registro de auditoría, tiques de cambio, acta de conciliación | Cambios críticos sin tique de autorización |
| C10 | Gobierno y normativa interna: política aprobada y comunicada, normas de red, acceso, cifrado y clasificación, inventario y clasificación de activos, SoA | A | P | 5.1, 5.2, 5.9, 5.12, 5.13, 5.31 | GV.PO, GV.RR, ID.AM | R6 | Política firmada por la dirección, inventario vigente, SoA, actas del comité | % de activos inventariados con propietario y clasificación |
| C11 | Gestión de incidentes y notificación: CSIRT, procedimiento, plantillas para AEPD, DGSFP y afectados, simulacros | A | C | 5.24, 5.25, 5.26, 5.27, 5.28, 6.8 | RS.MA, RS.CO | R3, R5, R6, R7 | Procedimiento aprobado, registro de incidentes, actas de simulacros, justificantes de notificación | % de incidentes notificados dentro de plazo |
| C12 | Continuidad y recuperación: BIA, DRP, copias cifradas e inmutables, pruebas de restauración, centro de respaldo | A, T | C | 5.29, 5.30, 8.13, 8.14 | RC.RP, PR.IR | R4, R5 | BIA y DRP aprobados, informes de pruebas de restauración | RTO y RPO alcanzados en la última prueba |
| C13 | Formación y concienciación de empleados, administradores y mediadores | A | P | 6.3, 6.4, 6.2 | PR.AT | R7 | Plan de formación, listas de asistencia, resultados de simulaciones | % de personal formado; tasa de clic en simulaciones |
| C14 | Seguridad física del centro de datos y del cableado: acceso con tarjeta y biometría, videovigilancia, armarios cerrados, protección de tomas | F | P, D | 7.1, 7.2, 7.4, 7.8, 7.12 | PR.AA | R10 | Registros de acceso físico, grabaciones, inventario de armarios y tomas | Accesos físicos no autorizados detectados |
| C15 | Gestión de vulnerabilidades y verificación: configuración base, escaneos, pruebas de intrusión internas (incluida la capa 2), auditoría interna | A, T | D, C | 8.8, 8.9, 5.35, 5.36, 8.34 | ID.RA, ID.IM | Todos (reincidencia) | Informes de escaneo y de pruebas de intrusión, plan de acciones correctivas, informe de auditoría | % de hallazgos críticos cerrados en plazo |
| C16 | Gestión de terceros y transferencia del riesgo: contratos de encargado, cláusulas de seguridad, póliza de ciberriesgo | A | P, C | 5.19, 5.20, 5.21, 5.22 | GV.SC | R3, R6 | Contratos con cláusulas, evaluaciones de proveedores, póliza vigente | % de proveedores críticos evaluados en el año |

## Estructura y archivos de sección (`Lab6/_trabajo/secciones/`)

| Archivo | Sección | Contenido clave | Tablas y figuras |
|---|---|---|---|
| `00_resumen.md` | Resumen ejecutivo | Qué pasó, hallazgos, propuesta, cifras | |
| `01_introduccion.md` | 1. Introducción | Propósito, alcance, método de mapeo, fuentes | |
| `02_contexto.md` | 2. Contexto de la organización | Las siete preguntas del docente (numeral 4 de ISO 27001) | T1 contexto |
| `03_incidente.md` | 3. El incidente: hechos, anatomía y principios afectados | Hechos y supuestos, ARP e IP spoofing, cronología, ocho preguntas de clase, C-I-D-A-T | T2 hechos y supuestos, T3 ocho preguntas; F1 anatomía, F2 cronología |
| `04_act01_activos.md` | 4. Actividad 1: identificación de activos | 10 activos justificados | T4 |
| `05_act02_clasificacion.md` | 5. Actividad 2: clasificación de activos | Escala, CIA más A y T, etiquetas | T5 escala, T6 valoración |
| `06_act03_vulnerabilidades.md` | 6. Actividad 3: vulnerabilidades | V1 a V9 con mitigación | T7 |
| `07_act04_modelo_normativo.md` | 7. Actividad 4: modelo normativo | Ley, norma, marco, buena práctica; leyes con artículos; ISO, NIST, COBIT, ITIL; políticas; exigencia, control y evidencia | T8 a T12; F3 pirámide |
| `08_act05_riesgos.md` | 8. Actividad 5: gestión de riesgos | Método, cadena, inherente, tratamiento, residual | T13 escalas, T14 identificación, T15 valoración y tratamiento; F4 mapa de calor |
| `09_act06_controles.md` | 9. Actividad 6: controles | C1 a C16, SoA resumida, configuración de referencia | T16, T17, T18 SoA; F5 arquitectura |
| `10_act07_cierre_brechas.md` | 10. Actividad 7: cierre de brechas | Proceso, plan por horizontes, verificación, resiliencia | T19; F6 hoja de ruta |
| `11_act08_monitoreo.md` | 11. Actividad 8: monitoreo | Fuentes, casos de uso, indicadores, roles | T20, T21; F7 arquitectura de monitoreo |
| `12_act09_financiera.md` | 12. Actividad 9: afectación financiera | Costos directos e indirectos, escenarios, multas | T22, T23; F8 |
| `13_act10_reputacional.md` | 13. Actividad 10: afectación reputacional | Efectos, acciones, comunicación de 72 horas | T24, T25 |
| `14_act11_operacion_drp.md` | 14. Actividad 11: operación y DRP | Afectación, contingencias, BIA, DRP | T26, T27; F9 |
| `15_act12_divulgacion.md` | 15. Actividad 12: divulgación | Pasos legales y operativos, protección futura | T28, T29; F10 |
| `16_act13_modificacion.md` | 16. Actividad 13: modificación no autorizada | Tratamiento, mecanismos, ejemplo ejecutado | T30; F11, F12 |
| `17_plan_mejora.md` | 17. Plan integrado de mejora y tratamiento de riesgos | Hoja de ruta, PHVA, auditoría interna, revisión por la dirección | T31 |
| `18_conclusiones.md` | 18. Conclusiones | | |
| `19_referencias.md` | 19. Referencias | APA 7 | |
| `20_anexo_a_trazabilidad.md` | Anexo A | Trazabilidad con guía, rúbrica y clase | T32 |
| `21_anexo_b_politica.md` | Anexo B | Política de seguridad de la información (modelo) | |
| `22_anexo_c_demo.md` | Anexo C | Cómo reproducir la demostración de auditoría | |

## Figuras (`Lab6/diagramas/`)

1. `01_anatomia_ataque` secuencia: atacante, conmutador, servidor de aplicación, base de datos.
2. `02_cronologia` línea de tiempo: fases del ataque y plazos de respuesta (detección, 4 h, 24 h, 72 h, un mes).
3. `03_modelo_normativo` jerarquía: ley, norma, marco, buena práctica, política, normas internas, procedimientos, registros.
4. `04_mapa_calor` riesgo inherente y residual.
5. `05_arquitectura_segura` red propuesta con zonas y controles.
6. `06_hoja_ruta` gantt de cierre de brechas (0-30-60-90-180 días).
7. `07_monitoreo` fuentes, recolección, correlación, SOC y respuesta.
8. `08_impacto_financiero` costos por escenario.
9. `09_drp` fases del plan de recuperación con RTO y RPO.
10. `10_flujo_legal` notificaciones y plazos.
11. y 12. `Lab6/evidencias/` salidas de la demostración de auditoría de registros.

## Modelo financiero (actividad 9), estimación propia calculada por script

Escenarios bajo, base y alto con 50.000, 250.000 y 1.000.000 de afectados. Partidas: respuesta y forense; asesoría legal y regulatoria; notificación a afectados; refuerzo del centro de atención; servicio antifraude ofrecido; fraude reembolsado; refuerzo técnico urgente; auditorías extraordinarias; multa administrativa (0, 1,5 y 5 millones, con la referencia de Generali); interrupción operativa; pérdida de clientes; recaptación y reputación; litigios e indemnizaciones; ciberseguro. Totales esperados: cerca de 1,5, 8,1 y 35,4 millones de euros. Comparación: IBM 2026, sector financiero USD 6,3 millones.

## Pendientes antes de redactar

- Verificar datos públicos de Mapfre para la sección 2 (clientes, empleados, red de distribución, certificaciones).
- Verificar artículos del RD 43/2021 (6 y 7) y los arts. 249 y 264 del Código Penal español.
