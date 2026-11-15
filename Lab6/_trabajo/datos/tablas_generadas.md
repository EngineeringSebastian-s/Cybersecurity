# Tablas generadas por lab6_modelo.py (no editar a mano)

## Riesgos: valoración inherente y residual

| ID | Riesgo | P | I | Inherente | Tratamiento | P res. | I res. | Residual |
|---|---|---|---|---|---|---|---|---|
| R1 | Interceptación de datos en tránsito | 5 | 5 | 25 Crítico | Mitigar | 2 | 4 | 8 Medio |
| R2 | Acceso a la base de datos con IP suplantada | 5 | 5 | 25 Crítico | Evitar y mitigar | 1 | 5 | 5 Medio |
| R3 | Fraude a clientes con los datos sustraídos | 4 | 5 | 20 Crítico | Mitigar y transferir | 2 | 4 | 8 Medio |
| R4 | Modificación no autorizada de pólizas | 3 | 5 | 15 Alto | Mitigar | 1 | 5 | 5 Medio |
| R5 | Interrupción de la operación | 4 | 4 | 16 Alto | Mitigar | 2 | 3 | 6 Medio |
| R6 | Sanción regulatoria y reclamaciones | 4 | 4 | 16 Alto | Mitigar y transferir | 2 | 4 | 8 Medio |
| R7 | Daño reputacional y pérdida de clientes | 4 | 5 | 20 Crítico | Mitigar | 2 | 4 | 8 Medio |
| R8 | Robo de credenciales en tránsito | 4 | 4 | 16 Alto | Mitigar | 2 | 3 | 6 Medio |
| R9 | Detección tardía y pérdida de trazabilidad | 4 | 4 | 16 Alto | Mitigar y aceptar el residual | 1 | 3 | 3 Bajo |
| R10 | Equipo no autorizado en la red interna | 3 | 4 | 12 Alto | Mitigar y aceptar el residual | 1 | 4 | 4 Bajo |

Inherente por nivel: {'Crítico': 4, 'Alto': 6}. Residual por nivel: {'Medio': 8, 'Bajo': 2}.
Suma de puntuaciones: inherente 181, residual 61 (reducción del 66 %).

## Costos del incidente por escenario (miles de euros)

| Código | Concepto | Supuesto de cálculo | Bajo | Base | Alto |
|---|---|---|---|---|---|
| D1 | Respuesta al incidente y análisis forense | Equipo externo de respuesta y peritaje | 250 | 600 | 1.500 |
| D2 | Asesoría jurídica y gestión regulatoria | Notificaciones, requerimientos y defensa | 100 | 300 | 900 |
| D3 | Notificación a los afectados | 1,2 euros por afectado | 60 | 300 | 1.200 |
| D4 | Refuerzo del centro de atención al cliente | Personal y líneas adicionales | 150 | 400 | 1.000 |
| D5 | Servicio antifraude ofrecido a los clientes | 6 euros por cliente que lo acepta (10, 15 y 20 %) | 30 | 225 | 1.200 |
| D6 | Reembolso de fraudes a clientes | 0,05, 0,1 y 0,2 % de afectados con 1.800 euros de pérdida media | 45 | 450 | 3.600 |
| D7 | Refuerzo técnico urgente (red, cifrado y monitoreo) | Equipos, licencias y servicios de implantación | 400 | 1.200 | 3.000 |
| D8 | Auditorías de seguridad extraordinarias | Auditoría independiente y prueba de intrusión | 80 | 200 | 500 |
| D9 | Multa administrativa | Archivo, sanción media y sanción del orden de la de Generali | 0 | 1.500 | 5.000 |
| D10 | Franquicia y encarecimiento del ciberseguro | Franquicia del siniestro y subida de prima | 50 | 250 | 750 |
| | **Subtotal de costos directos** | | **1.165** | **5.425** | **18.650** |
| I1 | Interrupción operativa | Margen no realizado por día (1, 3 y 7 días) | 150 | 450 | 1.400 |
| I2 | Pérdida de clientes | Bajas del 0,5, 1,5 y 3 % con 120 euros de margen anual durante 3 años | 90 | 1.350 | 10.800 |
| I3 | Recaptación comercial y campaña de reputación | Campañas, incentivos a mediadores y comunicación | 100 | 600 | 2.500 |
| I4 | Reclamaciones e indemnizaciones | Indemnizaciones del art. 82 del RGPD y litigios | 0 | 300 | 2.000 |
| | **Subtotal de costos indirectos** | | **340** | **2.700** | **16.700** |
| | **Total estimado** | | **1.505** | **8.125** | **35.350** |

Escenarios: bajo: 50.000 afectados, 1 día(s) de servicio degradado; base: 250.000 afectados, 3 día(s) de servicio degradado; alto: 1.000.000 afectados, 7 día(s) de servicio degradado
Peso de los costos indirectos: bajo 23 %; base 33 %; alto 47 %
Costo por afectado: bajo 30,1 euros; base 32,5 euros; alto 35,4 euros
