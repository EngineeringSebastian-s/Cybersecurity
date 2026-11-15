# 8. Actividad 5: gestión de riesgos de seguridad

La guía pide un análisis de riesgos para los activos críticos a partir del incidente de acceso no autorizado: definir los riesgos, evaluar su probabilidad y su impacto, priorizarlos y recomendar su mitigación. En clase se dijo que aquí está "el corazón de la ISO 27001", porque la norma no dice qué productos comprar, dice "identifique sus riesgos y determine cómo tratarlos" (Ochoa Agudelo, 2026c). El material del curso divide la gestión de riesgos en dos fases, el análisis y el tratamiento (UNIR, s. f.), y este capítulo sigue ese orden.

## 8.1 Método y escalas

Sigo el proceso de la norma ISO/IEC 27005:2022, que desarrolla para la seguridad de la información el esquema general de ISO 31000: establecer el contexto, identificar los riesgos, analizarlos, evaluarlos frente a un criterio y tratarlos (ISO/IEC, 2022c; ISO, 2018). El enfoque es cualitativo, como pide la guía. Para poder priorizar, cada nivel cualitativo lleva un número del 1 al 5 y el nivel de riesgo es el producto de la probabilidad por el impacto. La Tabla [[t:escalas_riesgo]] define ambos ejes.

| Valor | Probabilidad | Impacto |
|---|---|---|
| 1 | Muy baja. No se espera en cinco años. | Muy bajo. Sin efecto en los clientes ni en el servicio. |
| 2 | Baja. Podría ocurrir una vez en cinco años. | Bajo. Molestia interna que se resuelve en horas. |
| 3 | Media. Podría ocurrir una vez al año. | Medio. Afecta a un proceso o a miles de clientes, sin sanción previsible. |
| 4 | Alta. Puede ocurrir varias veces al año o ya hay indicios. | Alto. Afecta a los derechos de decenas de miles de clientes, detiene procesos esenciales o hace probable una sanción. |
| 5 | Muy alta. Ya ocurrió o es inminente. | Muy alto. Afecta a cientos de miles de clientes, compromete la continuidad o acarrea sanciones de varios millones. |

*Tabla [[t:escalas_riesgo]].* Escalas de probabilidad e impacto. El nivel de riesgo es su producto: de 1 a 4 bajo, de 5 a 9 medio, de 10 a 16 alto y de 17 a 25 crítico.

El criterio de aceptación es que ningún riesgo quede por encima de 9 después del tratamiento. Un riesgo residual de nivel medio o bajo lo acepta por escrito su propietario; uno mayor exige más controles o una decisión expresa de la Dirección.

## 8.2 Identificación de los riesgos

En clase se dio la cadena con que debe describirse un riesgo: activo, amenaza, vulnerabilidad, consecuencia y riesgo. El ejemplo fue una base de datos de clientes amenazada por un programa de secuestro, con copias de seguridad conectadas de forma permanente a la red, cuya consecuencia es la pérdida de disponibilidad y cuyo riesgo es la interrupción del servicio (Ochoa Agudelo, 2026c). La Tabla [[t:riesgos_id]] aplica esa misma cadena a los diez riesgos que se desprenden del incidente. Los activos y las vulnerabilidades remiten a los capítulos 4 y 6.

| ID | Riesgo | Activo | Amenaza | Vulnerabilidad | Consecuencia |
|---|---|---|---|---|---|
| R1 | Interceptación de datos personales en tránsito por un intermediario | A1, A4 | ARP spoofing | V1, V2, V4 | Pérdida de confidencialidad y violación de datos personales |
| R2 | Acceso no autorizado a la base de datos con la IP de un servidor de confianza | A1, A2 | Suplantación de IP | V3, V5 | Consulta y extracción masiva de datos |
| R3 | Fraude a clientes con los datos sustraídos | A1, A10 | Uso fraudulento de los datos | V8 | Pérdidas económicas e indemnizaciones |
| R4 | Modificación no autorizada de datos de pólizas | A1, A2 | Manipulación de beneficiarios, cuentas o capitales | V3, V7, V8 | Pérdida de integridad y pagos indebidos |
| R5 | Interrupción de la operación durante la contención y las auditorías | A2, A3, A4 | Indisponibilidad | V9 | Emisión, cobros y siniestros detenidos |
| R6 | Sanción regulatoria y reclamaciones | A10 | Incumplimiento de medidas o de plazos | V7, V9 | Multas e indemnizaciones |
| R7 | Daño reputacional y pérdida de clientes y mediadores | A10 | Divulgación pública de la brecha | V9 | Cancelaciones y menor nueva producción |
| R8 | Robo de credenciales de servicio o de administración en tránsito | A5 | Captura de credenciales | V4, V8 | Movimiento lateral y persistencia del atacante |
| R9 | Detección tardía e imposibilidad de reconstruir lo ocurrido | A6 | Registros insuficientes o alterables | V7 | Pérdida de trazabilidad y alcance indeterminado |
| R10 | Conexión de un equipo no autorizado a la red interna | A4, A8 | Acceso físico o equipo comprometido | V6 | Punto de partida de nuevos ataques |

*Tabla [[t:riesgos_id]].* Identificación de los riesgos con la cadena activo, amenaza, vulnerabilidad y consecuencia.

## 8.3 Valoración y priorización

La Tabla [[t:riesgos_val]] valora cada riesgo tal como estaba el día del incidente, antes de aplicar controles. Es el riesgo inherente. El orden de la tabla es el orden de prioridad.

| Prioridad | ID | Riesgo | P | I | Riesgo inherente |
|---|---|---|---|---|---|
| 1 | R1 | Interceptación de datos en tránsito | 5 | 5 | 25 Crítico |
| 2 | R2 | Acceso a la base de datos con IP suplantada | 5 | 5 | 25 Crítico |
| 3 | R3 | Fraude a clientes con los datos sustraídos | 4 | 5 | 20 Crítico |
| 4 | R7 | Daño reputacional y pérdida de clientes | 4 | 5 | 20 Crítico |
| 5 | R5 | Interrupción de la operación | 4 | 4 | 16 Alto |
| 6 | R6 | Sanción regulatoria y reclamaciones | 4 | 4 | 16 Alto |
| 7 | R8 | Robo de credenciales en tránsito | 4 | 4 | 16 Alto |
| 8 | R9 | Detección tardía y pérdida de trazabilidad | 4 | 4 | 16 Alto |
| 9 | R4 | Modificación no autorizada de pólizas | 3 | 5 | 15 Alto |
| 10 | R10 | Equipo no autorizado en la red interna | 3 | 4 | 12 Alto |

*Tabla [[t:riesgos_val]].* Valoración del riesgo inherente y orden de prioridad.

Los dos primeros riesgos reciben la probabilidad máxima porque ya se materializaron: son el incidente. El fraude (R3) y el daño reputacional (R7) también ocurrieron según el enunciado; se valoran con probabilidad 4 porque lo que se mide es que sigan produciéndose mientras los datos estén en manos de terceros. La modificación de datos (R4) es el único riesgo del grupo alto que no consta como ocurrido. Se le asigna probabilidad media y el impacto más alto, porque un beneficiario cambiado en una póliza de vida solo se descubre cuando hay que pagar la prestación, y entonces el daño ya no tiene arreglo sencillo.

Ningún riesgo queda en nivel medio o bajo. Cuatro son críticos y seis altos, de modo que los diez requieren tratamiento y ninguno puede aceptarse tal como está. La parte izquierda de la Figura [[f:calor]] muestra esa concentración en la esquina superior derecha de la matriz.

![](diagramas/04_mapa_calor.png)

*Figura [[f:calor]].* Mapa de calor de los riesgos R1 a R10 antes y después de los controles propuestos.

## 8.4 Tratamiento y riesgo residual

Terminado el análisis hay que elegir una opción de tratamiento para cada riesgo. Las cuatro que se vieron en clase son evitar, que es dejar de hacer la actividad que genera el riesgo; mitigar, que es reducirlo con controles; transferir, que es compartirlo con un tercero mediante un seguro o un contrato, y aceptar, que es asumirlo dentro de los criterios fijados (Ochoa Agudelo, 2026c). La Tabla [[t:riesgos_trat]] indica la opción elegida, la recomendación de mitigación y el riesgo que queda después.

| ID | Opción | Recomendación de mitigación | P | I | Riesgo residual | Lo acepta |
|---|---|---|---|---|---|---|
| R1 | Mitigar | Segmentar, proteger la capa 2, cifrar con autenticación mutua y vigilar la red (C1, C2, C4, C8) | 2 | 4 | 8 Medio | Dirección de Tecnología |
| R2 | Evitar y mitigar | Eliminar la autorización por dirección IP y el acceso directo a la base de datos; filtrado antisuplantación y autenticación con certificado (C3, C5, C1) | 1 | 5 | 5 Medio | CISO |
| R3 | Mitigar y transferir | Cifrar y enmascarar los datos, avisar pronto a los afectados y contratar cobertura de ciberriesgo (C7, C11, C16) | 2 | 4 | 8 Medio | Dirección de Negocio Vida |
| R4 | Mitigar | Mínimo privilegio, auditoría de cambios con doble validación y copias verificadas (C5, C9, C12) | 1 | 5 | 5 Medio | Dirección de Operaciones |
| R5 | Mitigar | Plan de recuperación probado y procedimiento de incidentes (C12, C11) | 2 | 3 | 6 Medio | Dirección de Operaciones |
| R6 | Mitigar y transferir | Normativa interna aplicada, notificación en plazo y cláusulas con proveedores (C10, C11, C16) | 2 | 4 | 8 Medio | Delegado de protección de datos y Asesoría Jurídica |
| R7 | Mitigar | Comunicación transparente y formación (C11, C13) | 2 | 4 | 8 Medio | Dirección General |
| R8 | Mitigar | Cifrado del tráfico, credenciales con rotación y bastión, detección de usos anómalos (C4, C5, C8) | 2 | 3 | 6 Medio | CISO |
| R9 | Mitigar y aceptar el residual | Registros protegidos, relojes sincronizados y casos de uso de detección (C8, C9) | 1 | 3 | 3 Bajo | SOC |
| R10 | Mitigar y aceptar el residual | Control de acceso a la red, seguridad física y protecciones de capa 2 (C6, C14, C2) | 1 | 4 | 4 Bajo | Área de Redes |

*Tabla [[t:riesgos_trat]].* Opción de tratamiento, recomendación de mitigación y riesgo residual de cada riesgo.

Las cuatro opciones aparecen en el plan. Se evita el riesgo R2 en su origen, porque la compañía deja de autorizar conexiones por dirección IP y retira el acceso directo a la base de datos desde otros segmentos: la actividad que generaba el riesgo desaparece. Se mitigan los diez con los controles del capítulo 9. Se transfiere una parte de R3 y de R6 con una póliza de ciberriesgo y con cláusulas que reparten la responsabilidad con los proveedores. Y se aceptan los residuales de R9 y R10, que quedan en nivel bajo.

Con los controles aplicados, la suma de las puntuaciones baja de 181 a 61, una reducción del 66 %. Ocho riesgos quedan en nivel medio y dos en bajo, todos dentro del criterio de aceptación. El residual no desaparece. Como se explicó en clase, un riesgo que pasa de alto a medio sigue latente, y por eso la norma pide que los responsables lo acepten de forma expresa (Ochoa Agudelo, 2026c). En R2 y R4 el impacto sigue siendo el máximo aunque la probabilidad sea mínima, porque si un atacante vuelve a entrar a la base de datos el daño es el mismo; lo que cambian los controles es lo difícil que resulta llegar.

Ante un auditor, este capítulo se sostiene con cuatro documentos: la metodología de riesgos aprobada, el registro de riesgos con un propietario por riesgo, el plan de tratamiento con fechas y el acta en que cada propietario acepta su residual. El registro se revisa una vez al año y siempre que cambien los sistemas o haya un incidente, que son los supuestos que la guía de implantación del curso señala para repetir la evaluación (NQA, s. f.).
