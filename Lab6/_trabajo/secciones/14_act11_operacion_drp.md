# 14. Actividad 11: afectación a la operación del negocio

La guía pide analizar cómo afectó el ataque a la operación, qué acciones de contingencia debieron tomarse y proponer un plan de recuperación ante desastres (DRP) que asegure la continuidad operativa.

## 14.1 Cómo afectó el ataque a la operación

El enunciado dice que la operación se interrumpió "mientras se solucionaba el problema y se realizaban auditorías de seguridad". La parada no la causó el atacante, que no borró ni cifró nada. La causó la respuesta: para contener un acceso de este tipo hay que aislar el segmento de la base de datos, cambiar las credenciales con que se conectan las aplicaciones y conservar los equipos para el análisis forense, y mientras tanto las aplicaciones que dependen de esos datos no funcionan o funcionan a medias.

Con la base de datos de clientes fuera de servicio se detienen o se ralentizan la emisión y modificación de pólizas, el cobro de recibos, la tramitación de siniestros y el pago de prestaciones, el portal y la aplicación de clientes y las herramientas de los mediadores. El efecto se nota en tres plazos. De inmediato, colas en el centro de atención y ventas que no se cierran. En los días siguientes, prestaciones que se pagan tarde a familias que las esperan. Después, semanas de trabajo para cargar en el sistema lo que se tramitó a mano y para revisar que los datos están como deben.

La duración de la parada depende de una decisión de diseño anterior al incidente. Con una red segmentada se aísla solo la zona afectada. Con una red plana, la única forma de estar seguro es apagar mucho más de lo necesario. El curso plantea esa misma disyuntiva como ejemplo de decisión bajo presión: "¿apagamos todo el centro de datos o solo una sucursal?" (Ochoa Agudelo, 2026e).

## 14.2 Contingencias que debieron tomarse

El incidente real de 2020 sirve de comparación. Aquella noche, la compañía activó el Comité de Crisis dieciséis minutos después de iniciarse el cifrado y los planes de continuidad veintiséis minutos después; en tres horas y media empezó a reforzar con personal los centros de atención, y el lunes siguiente abrió sus oficinas con normalidad (AEPD, 2021). Con ese listón, las contingencias que el caso de marzo exigía son ocho:

1. Declarar el incidente y reunir al Comité de Crisis en la primera hora, con poder para decidir qué se aísla.
2. Aislar la zona de datos y no el centro de datos completo.
3. Preservar las evidencias antes de restaurar nada. El curso recuerda el orden: primero lo más volátil, la memoria, después los discos, con imagen forense, cálculo de hash y cadena de custodia (Ochoa Agudelo, 2026e).
4. Dar por comprometidas todas las credenciales que circularon por el segmento y cambiarlas.
5. Levantar el servicio en un entorno de recuperación limpio, con credenciales nuevas y la configuración de red ya corregida.
6. Activar los procedimientos manuales para lo que no puede esperar, que en una aseguradora de vida son los siniestros y el pago de prestaciones.
7. Reforzar el centro de atención y dar instrucciones a la red de mediadores.
8. Validar la integridad de los datos antes de reabrir, porque quien pudo leer la base de datos también pudo modificarla.

## 14.3 Análisis de impacto en el negocio

El plan de recuperación parte de un análisis de impacto en el negocio (BIA), que fija para cada proceso cuánto tiempo puede estar detenido y cuántos datos puede permitirse perder. El tiempo objetivo de recuperación (RTO) es el plazo máximo para restablecer el proceso. El punto objetivo de recuperación (RPO) es la antigüedad máxima de los datos que se recuperan. La Tabla [[t:bia]] propone los valores para el servicio de pólizas de vida.

| Proceso | Impacto si se detiene | RTO | RPO | Alternativa manual |
|---|---|---|---|---|
| Pago de prestaciones y tramitación de siniestros | Familias que esperan un capital; reclamaciones | 4 horas | 15 minutos | Expediente en papel con doble firma y pago autorizado a mano |
| Atención al cliente (teléfono y oficinas) | Clientes sin respuesta en plena crisis | 2 horas | No aplica | Guion de atención y registro manual de solicitudes |
| Emisión y modificación de pólizas | Ventas detenidas; mediadores sin herramienta | 8 horas | 1 hora | Solicitud en formulario y emisión diferida |
| Portal y aplicación de clientes | Imagen pública; más carga sobre el teléfono | 8 horas | 1 hora | Derivación al teléfono y a las oficinas |
| Cobro de primas y recibos | Tesorería y devoluciones | 24 horas | 1 hora | Aplazamiento de las remesas |
| Información al supervisor y cierre contable | Incumplimiento de plazos regulatorios | 72 horas | 24 horas | Comunicación previa del retraso |

*Tabla [[t:bia]].* Análisis de impacto en el negocio: procesos, tiempos objetivo y alternativa manual.

El orden de la tabla es el orden de recuperación. El pago de prestaciones va primero aunque no sea el proceso con más volumen, porque es la promesa que la compañía vende.

## 14.4 Plan de recuperación ante desastres

### Objetivo y alcance

Restablecer el servicio de pólizas de vida dentro de los tiempos de la Tabla [[t:bia]] tras cualquier incidente que deje inservible o no fiable la base de datos de clientes, el núcleo asegurador o la red que los une.

### Activación

El plan se activa cuando un incidente afecta a los activos A1 o A2 durante más de una hora, o cuando la contención exige aislar la zona de datos. Lo declara el Comité de Crisis a propuesta del responsable de seguridad.

### Funciones

El curso enumera la composición del Comité de Crisis: Dirección General, área legal, tecnología, recursos humanos y comunicación (Ochoa Agudelo, 2026e). La Tabla [[t:drp_roles]] reparte las responsabilidades.

| Función | Quién | Responsabilidad en el plan |
|---|---|---|
| Comité de Crisis | Dirección General, Asesoría Jurídica, Tecnología, Recursos Humanos y Comunicación | Declara el desastre, fija prioridades, autoriza gastos y aprueba los mensajes |
| Dirección de la recuperación | Dirección de Tecnología | Coordina la ejecución técnica y reporta al Comité |
| Seguridad y respuesta | CISO y equipo de respuesta a incidentes | Contiene, preserva las evidencias y certifica que el entorno recuperado está limpio |
| Equipos de recuperación | Redes, bases de datos y aplicaciones | Ejecutan los procedimientos de restauración |
| Protección de datos | Delegado de protección de datos | Evalúa la violación y gestiona las notificaciones |
| Negocio | Responsables de siniestros, emisión y atención | Activan los procedimientos manuales y validan los datos recuperados |

*Tabla [[t:drp_roles]].* Funciones y responsabilidades en el plan de recuperación.

### Estrategias de recuperación

Son cinco. Copias de seguridad cifradas con la regla de tres copias en dos soportes y una fuera del centro principal, una de ellas sin conexión permanente a la red; el ejemplo de clase era justamente el de unas copias conectadas de forma permanente, que un atacante alcanza igual que alcanza los datos de producción (Ochoa Agudelo, 2026c). Réplica de la base de datos en un centro de respaldo. Un entorno de recuperación aislado, con sus propias credenciales, donde levantar el servicio sin arrastrar lo que estuviera comprometido. Recuperación a un punto en el tiempo, que permite volver al estado anterior a una modificación indebida. Y acuerdos con los proveedores que garanticen su apoyo en los plazos del plan.

### Fases

La Figura [[f:drp]] muestra las seis fases de la recuperación tecnológica y las dos líneas que corren en paralelo, la continuidad del negocio y la comunicación.

![](diagramas/09_drp.png)

*Figura [[f:drp]].* Fases del plan de recuperación ante desastres y líneas paralelas de continuidad del negocio y de comunicación.

La quinta fase, la validación, es la que este caso hace imprescindible. Reabrir el servicio con datos que pudieron ser alterados cambiaría una parada de días por un problema de meses. Antes de reabrir se comparan los datos recuperados con la última copia de confianza y se revisa el registro de cambios del capítulo 16.

### Pruebas y mantenimiento

Un plan que no se prueba es una hipótesis. Propongo una restauración de copias cada trimestre, con medición del tiempo real; un simulacro de mesa cada semestre, que el curso incluye en la fase de anticipación (Ochoa Agudelo, 2026e), y una prueba de conmutación al centro de respaldo una vez al año. El plan se revisa tras cada prueba, tras cada incidente y cuando cambia la arquitectura. DORA respalda esta exigencia: sus artículos 11 y 12 obligan a tener una política de continuidad de las TIC, planes de respuesta y recuperación probados de forma periódica y políticas de copia de seguridad.

### Evidencias

Un auditor pediría el análisis de impacto aprobado, el plan vigente, los informes de las pruebas con los tiempos alcanzados frente a los objetivos y el registro de las mejoras introducidas después de cada una. Los controles del Anexo A que este plan desarrolla son el 5.29, el 5.30, el 8.13 y el 8.14 (ISO/IEC, 2022b), y la norma de referencia para el sistema de continuidad completo es ISO 22301 (ISO, 2019).
