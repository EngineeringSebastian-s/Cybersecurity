# 11. Actividad 8: monitoreo de seguridad

La guía pide diseñar un plan de monitoreo que tenga en cuenta el incidente y que proponga herramientas y técnicas para detectar accesos no autorizados y actividades maliciosas. El punto de partida es lo que el caso deja ver: el equipo de TI detectó los accesos cuando ya se habían producido. La compañía tenía capacidad de vigilancia, y la resolución de la AEPD describe un Centro de Control General que en 2020 detectó por monitorización el fallo de sus aplicaciones siete minutos después de iniciarse el cifrado (AEPD, 2021). Lo que el incidente de marzo revela es un punto ciego concreto: el tráfico entre equipos dentro del centro de datos y la actividad de la base de datos.

## 11.1 Objetivos del plan

El plan se propone detectar cinco cosas que el 10 de marzo no se detectaron a tiempo: el envenenamiento ARP y la suplantación de IP en el momento en que ocurren; los accesos a la base de datos que se salen del patrón normal; el uso anómalo de cuentas de servicio y de administración; los cambios no autorizados en los datos y en la configuración, y la presencia de equipos desconocidos en la red. Fija además dos metas medibles: detectar en menos de quince minutos cualquiera de los casos críticos y contenerlo en menos de una hora.

## 11.2 Arquitectura de monitoreo

La Figura [[f:monitoreo]] muestra el recorrido de un evento. Las fuentes generan registros, que viajan cifrados y con la hora sincronizada a un almacén que no admite modificaciones. El SIEM los correlaciona con los casos de uso definidos y, cuando una condición se cumple, lanza una alerta que atiende el centro de operaciones de seguridad. Si la alerta se confirma, pasa al equipo de respuesta, y si hay datos personales afectados, al delegado de protección de datos y a la Asesoría Jurídica, que tienen los plazos de notificación en la mano.

![](diagramas/07_monitoreo.png)

*Figura [[f:monitoreo]].* Arquitectura del plan de monitoreo: fuentes de registro, recolección, correlación, operación y mejora.

Tres controles del Anexo A sostienen esta arquitectura. El 8.15 exige generar, proteger, almacenar y analizar los registros. El 8.16 pide vigilar las redes y los sistemas para detectar comportamientos anómalos. El 8.17 obliga a sincronizar los relojes con una fuente de tiempo fiable para que todos los registros compartan la misma hora (ISO/IEC, 2022b). El último parece menor y no lo es: sin relojes sincronizados no se puede reconstruir en qué orden ocurrieron un envenenamiento ARP en un conmutador y una sesión en la base de datos.

## 11.3 Herramientas y técnicas

La norma no impone productos, así que la Tabla [[t:herramientas]] describe cada herramienta por su función. La tercera columna indica qué habría visto en el incidente.

| Herramienta o técnica | Qué vigila | Qué habría visto en el caso |
|---|---|---|
| Inspección dinámica de ARP con registro en los conmutadores | Respuestas ARP que no coinciden con la tabla de asignaciones | El envenenamiento en el instante de producirse, con el puerto de origen |
| Sensor de red en el segmento de datos, con vigilancia de las parejas IP y MAC | Cambios de la dirección física asociada a una IP crítica y direcciones duplicadas | La IP de la base de datos anunciándose desde otra tarjeta de red |
| Registros del cortafuegos interno y del filtrado antisuplantación | Flujos denegados y paquetes con origen inválido | Paquetes con la IP del servidor de aplicaciones llegando por una interfaz que no le corresponde |
| Monitoreo de la actividad de la base de datos (auditoría nativa) | Quién consulta qué, cuánto, a qué hora y con qué programa | Consultas masivas fuera de patrón y un cliente distinto de la aplicación |
| SIEM con reglas de correlación | La relación entre eventos de fuentes distintas | Una anomalía ARP seguida de una sesión nueva en la base de datos desde esa misma dirección |
| Análisis de comportamiento de cuentas | Usos inusuales de cuentas de servicio y de administración | La cuenta de la aplicación activa de madrugada |
| Control de integridad de la configuración | Cambios en conmutadores, cortafuegos y base de datos respecto a la línea base | Una protección desactivada |
| Control de acceso a la red y registros de acceso físico | Equipos nuevos en la red y entradas a las salas técnicas | Un equipo desconocido en el segmento del centro de datos |
| Registros señuelo en la base de datos | Lecturas de pólizas ficticias que ninguna operación legítima consulta | Una extracción masiva, que inevitablemente los toca |

*Tabla [[t:herramientas]].* Herramientas y técnicas de monitoreo propuestas y lo que cada una habría detectado en el incidente.

El SIEM es la pieza que une las demás. El video visto en clase advierte que la norma no obliga a tenerlo y que un control de registro puede evidenciarse de otras formas, aunque añade que una herramienta así, bien implantada, facilita mucho el cumplimiento de los controles 8.15 y 8.16. En una aseguradora con centro de control propio y obligación de detectar bajo el artículo 10 de DORA, la cuestión es qué casos de uso tiene cargados.

## 11.4 Casos de uso de detección

Un SIEM sin casos de uso es un almacén de registros caro. La Tabla [[t:casosuso]] define los ocho que cubren el ataque del caso, con la condición que dispara la alerta, su severidad y la primera acción.

| Caso de uso | Fuente | Condición de alerta | Severidad | Respuesta inicial |
|---|---|---|---|---|
| Cambio de la dirección física asociada a la IP de un servidor crítico | Sensor de red y conmutador | La pareja IP y MAC de la base de datos o del servidor de aplicaciones cambia | Crítica | Aislar el puerto de origen y abrir incidente |
| Descartes de la inspección de ARP | Conmutador | Más de diez descartes por minuto en un puerto | Alta | Bloquear el puerto y revisar el equipo conectado |
| Paquetes con origen inválido | Encaminador y cortafuegos | Cualquier descarte con una dirección de origen de la zona de datos | Alta | Localizar la interfaz de entrada e investigar |
| Conexión a la base de datos sin certificado válido o desde fuera de la zona de aplicaciones | Base de datos y cortafuegos | Intento rechazado | Alta | Bloquear el origen y analizarlo |
| Consulta masiva o fuera de horario | Monitoreo de la base de datos | Más registros de clientes de los que usa una operación normal, o actividad de una cuenta de servicio entre las 22:00 y las 6:00 | Crítica | Suspender la sesión y avisar al propietario del dato |
| Cambio en un campo crítico sin tique | Registro de auditoría de cambios | Tique de cambio vacío | Crítica | Revertir con el valor anterior y escalar (capítulo 16) |
| Equipo no registrado en la red del centro de datos | Control de acceso a la red | Autenticación fallida repetida en una toma | Media | Localizar la toma y revisar el acceso físico |
| Hueco en la cadena del registro de auditoría | Almacén de registros | La verificación de integridad falla | Crítica | Preservar la copia íntegra e investigar quién lo alteró |

*Tabla [[t:casosuso]].* Casos de uso de detección derivados del incidente.

El primero y el quinto habrían bastado para detectar el ataque el mismo día. El primero es propio de este tipo de ataque: la dirección física de un servidor de base de datos no cambia casi nunca, así que cualquier cambio merece una alerta crítica con muy pocos falsos positivos.

## 11.5 Indicadores y organización

Para saber si el monitoreo funciona hay que medirlo. En clase se puso el ejemplo del doble factor, que se mide con el porcentaje de cuentas cubiertas, los accesos bloqueados, los incidentes de credenciales, los usuarios con privilegios excesivos y el tiempo de respuesta (Ochoa Agudelo, 2026c). La Tabla [[t:kpi]] aplica la misma lógica al plan.

| Indicador | Meta | Revisión |
|---|---|---|
| Tiempo medio de detección de los casos críticos | Menos de 15 minutos | Mensual |
| Tiempo medio de contención | Menos de 1 hora | Mensual |
| Activos críticos que envían registros al SIEM | 100 % | Mensual |
| Alertas críticas atendidas dentro de plazo | 95 % o más | Mensual |
| Simulaciones de ataque detectadas | 100 % de las pruebas trimestrales | Trimestral |
| Registros conservados durante el periodo definido | 100 % | Semestral |

*Tabla [[t:kpi]].* Indicadores del plan de monitoreo.

La operación se reparte en tres niveles. El centro de operaciones de seguridad atiende las alertas las 24 horas y hace el primer análisis. El equipo de respuesta a incidentes, el CSIRT que el curso sitúa en la fase de preparación (Ochoa Agudelo, 2026e), se ocupa de la contención y la erradicación. El delegado de protección de datos y la Asesoría Jurídica deciden las notificaciones. Los casos de uso se revisan cada mes y después de cada incidente, y cada trimestre se lanza un ataque simulado para comprobar que las alertas saltan. Lo que un auditor pediría es el plan aprobado, la lista de casos de uso, una muestra de alertas con su tratamiento y los resultados de esas simulaciones.
