# 4. Actividad 1: identificación de activos

La guía pide listar al menos cinco activos críticos y justificar su importancia para la operación. El material del curso define la identificación como el proceso de reconocer todos los activos de información de la organización, "como servidores, bases de datos, aplicaciones y dispositivos de red" (Ochoa Agudelo, 2026d), y el análisis de riesgos parte siempre de ahí: de los elementos que tienen valor para la organización y que por eso hay que proteger (Universidad Internacional de La Rioja [UNIR], s. f.). La norma lo convierte en un control concreto, el 5.9 del Anexo A, que exige un inventario de la información y de los activos asociados, cada uno con un propietario (ISO/IEC, 2022b).

Para el servicio de pólizas de vida identifico diez activos. Los cinco primeros son los que el incidente tocó de forma directa; los otros cinco sostienen la detección, la recuperación y la confianza, y sin ellos el análisis de riesgos quedaría cojo. Cada activo tiene un propietario, que es el cargo que responde por su protección y que más adelante acepta el riesgo residual.

| ID | Activo | Tipo | Propietario | Por qué es crítico para la operación |
|---|---|---|---|---|
| A1 | Base de datos de clientes y pólizas de vida | Información | Dirección de Negocio Vida | Guarda la identidad de los clientes, sus pólizas, beneficiarios y datos de cobro. Sin ella no se puede emitir, cobrar ni pagar una prestación. Fue el objetivo del ataque. |
| A2 | Sistema central de gestión de pólizas (núcleo asegurador) | Aplicación | Dirección de Operaciones | Ejecuta la emisión, los cobros y la tramitación de siniestros. Es el único camino legítimo para leer y modificar A1. |
| A3 | Aplicaciones y canales digitales (servidores de aplicación, portal y aplicación móvil, interfaces de mediadores) | Aplicación y servicio | Dirección de Tecnología | Por ellos entra la mayor parte de las operaciones y son lo que el cliente y el mediador ven de la compañía. |
| A4 | Red interna del centro de datos (conmutadores, encaminadores, cortafuegos, VLAN) | Infraestructura | Área de Redes | Une las aplicaciones con los datos y su diseño decide quién puede hablar con la base de datos. Fue el medio del ataque. |
| A5 | Identidades y credenciales (directorio, cuentas de servicio y de administración) | Información y servicio | Dirección de Seguridad (CISO) | Abren la base de datos. Quien las obtiene actúa con los permisos de la aplicación o del administrador. |
| A6 | Registros de auditoría y plataforma de monitoreo | Información | Centro de operaciones de seguridad (SOC) | Permiten detectar el ataque, acotar su alcance y demostrar al regulador qué ocurrió. |
| A7 | Copias de seguridad y centro de respaldo | Información e infraestructura | Dirección de Tecnología | Son la vía de recuperación si los datos se alteran o el centro principal queda aislado. Contienen los mismos datos personales que A1. |
| A8 | Centro de proceso de datos e instalaciones (salas técnicas, cableado, tomas de red) | Instalación | Seguridad Corporativa | Aloja servidores, conmutadores y cableado. El acceso físico a una toma de red basta para iniciar un ataque como el del caso. |
| A9 | Personas (equipos de TI y seguridad, empleados y red de mediadores) | Personas | Recursos Humanos | Aplican o incumplen las políticas y son quienes responden cuando ocurre un incidente. |
| A10 | Marca y confianza de clientes y supervisores | Intangible | Dirección General | Un seguro de vida es una promesa a muchos años. El cliente que duda de la custodia de sus datos cancela o no contrata. |

*Tabla [[t:activos]].* Inventario de activos críticos del servicio de pólizas de vida, con su propietario y su justificación.

El inventario mezcla a propósito activos de naturaleza distinta. La norma de gestión de riesgos distingue los activos primarios, que son la información y los procesos de negocio, de los activos de soporte, que son el hardware, el software, las redes, las personas y los emplazamientos (ISO/IEC, 2022c). Quedarse solo con servidores y bases de datos, como invita a hacer la primera lectura del caso, dejaría fuera dos cosas que el incidente dañó: la capacidad de reconstruir lo ocurrido (A6) y la confianza del cliente (A10).

Los activos dependen unos de otros y esa cadena explica el alcance del daño. La base de datos (A1) solo es tan segura como la red que la conecta (A4) y como las credenciales que la abren (A5). El ataque entró por el eslabón de soporte, la red, y terminó afectando al activo primario, los datos, y al intangible, la marca. Un inventario que registra esas dependencias permite ver que proteger A1 exige invertir en A4 y A5, que es justo lo que proponen los controles del capítulo 9.

Ante un auditor, este control se demuestra con el inventario vigente, en el que cada fila tiene propietario, ubicación y clasificación, y con el acta de su última revisión. La guía de implantación del curso lo recomendaba ya para la versión anterior de la norma: si la evaluación de riesgos recorre de forma sistemática la lista de activos y asigna un responsable a cada uno, se cumplen dos requisitos en un mismo ejercicio (NQA, s. f.).
