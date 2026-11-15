# 5. Actividad 2: clasificación de activos

La guía pide clasificar cada activo según su confidencialidad, integridad y disponibilidad, con un valor alto, medio o bajo en función del impacto en el negocio si se ve comprometido. Es el enfoque cualitativo que describe el material del curso: los parámetros se expresan con términos como alto, medio o bajo y se apoyan en el conocimiento de quienes participan en el análisis (UNIR, s. f.). El docente lo resume así: los activos se clasifican "según su nivel de sensibilidad y su valor para la organización", y esa clasificación "facilita la aplicación de controles adecuados" (Ochoa Agudelo, 2026d).

## 5.1 Escala de valoración

Una valoración cualitativa solo es útil si quien la lee sabe qué significa cada nivel. La Tabla [[t:escala_cia]] fija el criterio que uso en este ejercicio. La pregunta es siempre la misma: qué le pasa al negocio si esa dimensión del activo se pierde.

| Valor | Impacto en el negocio si la dimensión se pierde |
|---|---|
| Alto (3) | Daño grave. Afecta a los derechos de muchos clientes, detiene un proceso esencial más de cuatro horas o expone a la compañía a sanción y a pérdidas superiores al millón de euros. |
| Medio (2) | Daño apreciable pero acotado. Afecta a un proceso o a un grupo limitado de personas, se recupera en la misma jornada y no hace previsible una sanción. |
| Bajo (1) | Molestia interna. No alcanza a los clientes ni al cumplimiento normativo. |

*Tabla [[t:escala_cia]].* Escala de valoración de los activos por impacto en el negocio.

## 5.2 Valoración de los diez activos

A las tres dimensiones de la guía añado dos que trae el material de análisis de riesgos del curso: la autenticidad, que garantiza la identidad de quien origina una información, y la trazabilidad, que permite determinar quién hizo qué y cuándo (Merino Bada, s. f.). Las incluyo porque el caso las pone en primer plano: la suplantación de IP y de ARP es un ataque a la autenticidad, y la auditoría de registros que pide la actividad 13 es trazabilidad. La columna de valor suma las tres dimensiones de la guía y sirve para ordenar los activos; la etiqueta indica cómo debe manejarse la información asociada.

| ID | Activo | C | I | D | A | T | Valor (C+I+D) | Etiqueta |
|---|---|---|---|---|---|---|---|---|
| A1 | Base de datos de clientes y pólizas | Alto | Alto | Alto | Alto | Alto | 9 | Restringida |
| A2 | Núcleo asegurador | Alto | Alto | Alto | Alto | Alto | 9 | Restringida |
| A5 | Identidades y credenciales | Alto | Alto | Alto | Alto | Alto | 9 | Reservada |
| A7 | Copias de seguridad y centro de respaldo | Alto | Alto | Alto | Medio | Medio | 9 | Restringida |
| A3 | Aplicaciones y canales digitales | Medio | Alto | Alto | Alto | Medio | 8 | Uso interno |
| A4 | Red interna del centro de datos | Medio | Alto | Alto | Alto | Medio | 8 | Uso interno |
| A6 | Registros de auditoría y monitoreo | Medio | Alto | Medio | Alto | Alto | 7 | Restringida |
| A8 | Centro de datos e instalaciones | Medio | Medio | Alto | Medio | Medio | 7 | Uso interno |
| A9 | Personas | Medio | Medio | Alto | Medio | Medio | 7 | Uso interno |
| A10 | Marca y confianza | Bajo | Alto | Alto | Alto | Bajo | 7 | Pública |

*Tabla [[t:valoracion_cia]].* Clasificación de los activos por confidencialidad (C), integridad (I), disponibilidad (D), autenticidad (A) y trazabilidad (T), ordenados por valor.

Cuatro activos alcanzan el valor máximo. La base de datos (A1) es alta en todo: su divulgación afecta a los derechos de los clientes, su alteración puede desviar el pago de una prestación a quien no corresponde y su caída detiene la compañía. El núcleo asegurador (A2) hereda esos valores porque es la puerta de la base de datos. Las credenciales (A5) valen lo que valen los sistemas que abren, y por eso reciben la etiqueta más estricta. Las copias de seguridad (A7) suelen pasarse por alto y contienen exactamente los mismos datos personales que la base de datos de producción.

La red (A4) merece un comentario. Su confidencialidad es media, porque el plano de la red no es un secreto comercial, pero su integridad y su autenticidad son altas: si alguien puede alterar las tablas que dicen qué equipo es cuál, todo lo que circula por ella queda expuesto. El incidente lo demostró. Un inventario que hubiera valorado la red solo por su disponibilidad no habría justificado las protecciones de capa 2 que faltaban.

Los registros de auditoría (A6) tienen disponibilidad media, ya que la operación puede seguir unas horas sin ellos, y en cambio integridad y trazabilidad altas. Un registro que puede modificarse no prueba nada, ni ante el equipo que investiga ni ante el regulador. La marca (A10) se valora baja en confidencialidad porque es pública por definición, y alta en integridad y disponibilidad: lo que la compañía dice de sí misma tiene que ser cierto, y perder la confianza equivale a no poder vender.

## 5.3 De la clasificación al manejo

La clasificación tiene que cambiar la forma de tratar el activo. El material del curso incluye el esquema de cuatro niveles de una gran empresa española, que liga cada nivel a la valoración de la confidencialidad y pide reflejar la etiqueta en el propio documento (Grupo Renfe, s. f.). Propongo para Mapfre un esquema equivalente, resumido en la Tabla [[t:etiquetas]], que debería quedar recogido en una norma interna de clasificación conforme a los controles 5.12 y 5.13 del Anexo A (ISO/IEC, 2022b).

| Etiqueta | Quién accede | Cómo se protege |
|---|---|---|
| Reservada | Personas designadas por nombre | Custodia en un gestor de secretos, cifrado obligatorio, rotación periódica. Nunca viaja por correo ni se anota en claro. |
| Restringida | Quien lo necesita para su función | Cifrado en tránsito y en reposo, acceso registrado, enmascaramiento en entornos que no sean de producción. |
| Uso interno | Empleados y colaboradores autorizados | No se publica ni se comparte con terceros sin acuerdo de confidencialidad. |
| Pública | Cualquiera | Sin restricción de lectura. Se protege su integridad para que nadie la altere. |

*Tabla [[t:etiquetas]].* Niveles de clasificación propuestos y reglas de manejo asociadas.

Con esta escala, los datos que el atacante interceptó eran información restringida que viajaba por la red sin cifrar. La clasificación, si hubiera existido y se hubiera aplicado, habría señalado por sí sola el incumplimiento.
