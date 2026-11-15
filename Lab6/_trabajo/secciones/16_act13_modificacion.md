# 16. Actividad 13: modificación no autorizada de datos

La guía pide proponer cómo debe tratarse la modificación no autorizada de datos, qué mecanismos de auditoría y control pueden implementarse, y dar un ejemplo de auditoría de registros que identifique cambios no autorizados en los datos almacenados.

## 16.1 Por qué hay que tratarla aunque el caso no la describa

El enunciado habla de interceptación y de acceso, no de cambios. Pero quien se coloca en medio de una conversación puede alterarla, y quien entra a la base de datos con la identidad de la aplicación puede escribir igual que leer. El material del curso define la integridad como la garantía de que la información "no se ha transformado ni modificado de forma no autorizada durante su procesamiento, transporte o almacenamiento", y añade que debe ser posible "detectar fácilmente las posibles modificaciones" (Merino Bada, s. f.). La segunda parte de la definición es la que ocupa este capítulo.

En un seguro de vida la modificación más dañina es también la más discreta: cambiar el beneficiario de una póliza, la cuenta donde se cobra o el capital asegurado. Nadie lo nota hasta el día en que hay que pagar, que puede llegar años después. Las normas lo contemplan de forma expresa. El RGPD cuenta la alteración entre las formas de violación de la seguridad de los datos (artículo 4.12) y exige que los datos sean exactos (artículo 5.1.d). La ley colombiana obliga a conservar la información en condiciones que impidan "su adulteración" (artículo 17 d de la Ley 1581 de 2012). El catálogo MITRE ATT&CK lo recoge como manipulación de datos almacenados, técnica T1565.001 (MITRE, s. f.).

## 16.2 Cómo se trata una modificación no autorizada

Propongo un procedimiento de ocho pasos, que es una especialización del procedimiento general de incidentes.

1. Detectar y confirmar. La alerta llega por una regla de monitoreo, por la conciliación diaria o por la queja de un cliente. Se confirma comparando el cambio con la solicitud que debería respaldarlo.
2. Contener. Se suspende la cuenta o la sesión que hizo el cambio y se bloquean los pagos y las operaciones sobre las pólizas afectadas hasta aclarar su estado.
3. Preservar la evidencia. Se copia el registro de auditoría y se abre la cadena de custodia antes de tocar ningún dato.
4. Determinar el alcance con el registro: qué campos, de qué pólizas, desde cuándo y con qué cuenta.
5. Restaurar los valores correctos a partir del valor anterior que guarda el registro o, si el daño es amplio, de una copia a un punto en el tiempo. La corrección se hace con un tique de incidente y con la validación de una segunda persona.
6. Confirmar con el cliente, por un canal seguro, los datos sensibles restaurados cuando haya duda sobre cuál era el valor legítimo.
7. Notificar. Una alteración ilícita de datos personales es una violación de la seguridad de los datos, de modo que se aplican los pasos del capítulo 15.
8. Corregir la causa y registrar las lecciones aprendidas.

## 16.3 Mecanismos de auditoría y control

Ningún mecanismo basta por sí solo. La Tabla [[t:mecanismos]] reúne los que propongo, con su función y el control del Anexo A que desarrollan.

| Mecanismo | Función | Qué aporta | Anexo A |
|---|---|---|---|
| Registro de auditoría de cambios, por disparadores o con la auditoría nativa del gestor | Detectivo | Quién cambió qué, cuándo, desde dónde, con qué programa, y el valor anterior y el nuevo | 8.15 |
| Registro de solo anexado, encadenado por hash y con copia en un almacén inmutable | Preventivo y detectivo | Impide y delata la manipulación del propio registro | 8.15, 5.33 |
| Tique de cambio obligatorio y doble validación en los campos críticos | Preventivo | Ningún cambio de beneficiario, cuenta o capital depende de una sola persona | 5.3, 8.32 |
| Segregación de funciones y mínimo privilegio | Preventivo | La cuenta de la aplicación no sirve fuera de la aplicación; quien administra la base de datos no administra el registro | 5.3, 8.2, 8.3 |
| Reglas de detección en el SIEM | Detectivo | Alerta en minutos ante cambios sin tique, fuera de horario o con un cliente no autorizado | 8.16 |
| Conciliación diaria entre cambios registrados y solicitudes de clientes | Detectivo | Descubre lo que escapó a las reglas automáticas | 5.36 |
| Confirmación al cliente de cada cambio sensible por un canal independiente | Detectivo | El titular es el último control sobre sus propios datos | 5.34 |
| Copias con recuperación a un punto en el tiempo | Correctivo | Permite volver al estado anterior a la modificación | 8.13 |
| Relojes sincronizados | Soporte | Hace fiable el orden de los hechos | 8.17 |
| Revisión periódica del registro por auditoría interna | Detectivo | Comprueba que el mecanismo sigue funcionando | 5.35 |

*Tabla [[t:mecanismos]].* Mecanismos de auditoría y control frente a la modificación no autorizada de datos.

Estos mecanismos realizan la dimensión de trazabilidad que el curso añade a la tríada clásica: poder determinar en todo momento quién hizo qué y en qué momento lo hizo (Merino Bada, s. f.).

## 16.4 Ejemplo de auditoría de registros

Para que el ejemplo no se quede en una descripción, lo construí y lo ejecuté. Es una base de datos de demostración con cuatro pólizas ficticias y un registro de auditoría alimentado por disparadores, que anota cada cambio en los campos críticos junto con el contexto de la sesión. El programa completo y la forma de reproducirlo están en el Anexo C. Las tres figuras siguientes son la salida real de esa ejecución.

El escenario reproduce lo que pudo pasar en Mapfre. El día 9 y la mañana del 10 de marzo la aplicación hace tres cambios legítimos, cada uno con su tique. En la madrugada del 10, un atacante que ha capturado la cuenta de servicio de la aplicación y que suplanta la dirección IP de su servidor cambia el beneficiario y la cuenta de cobro de una póliza y multiplica por cuatro el capital de otra. La Figura [[f:demo_registro]] muestra el registro de auditoría con los seis cambios.

![](evidencias/01_registro_auditoria.png)

*Figura [[f:demo_registro]].* Registro de auditoría tras los cambios. Los registros 3, 4 y 5 son los no autorizados: mismo usuario y misma dirección IP que los legítimos, pero de madrugada, con otro programa cliente y sin tique.

A simple vista, los seis registros tienen el mismo usuario y la misma dirección IP. Esa es la lección que enlaza el ejemplo con el caso: cuando la dirección está suplantada y la credencial está robada, ni una ni otra distinguen al atacante. La Figura [[f:demo_consultas]] muestra las dos consultas de auditoría que sí lo distinguen.

![](evidencias/02_consultas_deteccion.png)

*Figura [[f:demo_consultas]].* Consultas de auditoría. La regla A busca cambios sin tique de autorización; la regla B, cambios fuera del horario de operación o hechos sin la aplicación.

La regla A devuelve exactamente los tres cambios indebidos, porque ninguno tiene tique. La regla B los agrupa en un hallazgo: tres cambios en dos pólizas entre las 02:47:19 y las 02:49:40, hechos con un cliente SQL que no es la aplicación. El auditor concluye lo que el propio programa imprime: la dirección de origen no sirve como prueba, y lo que delata el cambio es la falta de tique, la hora y el programa usado. Por eso el registro tiene que guardar ese contexto y no solo el usuario y la dirección.

Queda un problema. Un atacante con suficientes privilegios puede intentar borrar sus huellas. La Figura [[f:demo_integridad]] muestra cómo responde el registro.

![](evidencias/03_integridad_y_reversion.png)

*Figura [[f:demo_integridad]].* Integridad del registro de auditoría y reversión de los cambios indebidos.

La verificación inicial recorre la cadena de hash y la encuentra íntegra. El intento de borrar los registros con una cuenta normal queda bloqueado, porque el registro es de solo anexado. Cuando el borrado se hace con privilegios de administrador, tras eliminar la protección, la verificación siguiente falla en el registro 5: cada registro incluye el hash del anterior, y al faltar el 4 la cadena ya no cuadra. El contraste con la copia enviada al almacén inmutable indica qué registro falta y permite recuperarlo. Es el mismo principio que el curso presenta al hablar de blockchain, un libro al que solo se puede añadir y que resulta extremadamente difícil de cambiar (Yepes, s. f.).

La última parte de la figura es el tratamiento. Los tres cambios indebidos se revierten con el valor anterior que el registro había guardado, bajo el tique de incidente INC-2026-0031, y las propias reversiones quedan registradas. El registro termina con ocho anotaciones y las pólizas afectadas vuelven a su estado legítimo.

En un sistema de producción el contexto de la sesión lo aporta la auditoría nativa del gestor de base de datos, el registro se envía en tiempo real a un almacén que el administrador de la base de datos no controla y las dos reglas del ejemplo son casos de uso del SIEM, como el sexto de la Tabla [[t:casosuso]]. Un auditor comprobaría el mecanismo de la forma más directa: haciendo un cambio de prueba sin tique y midiendo cuánto tarda en saltar la alerta.
