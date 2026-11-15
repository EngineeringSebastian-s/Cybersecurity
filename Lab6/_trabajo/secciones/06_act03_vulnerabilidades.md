# 6. Actividad 3: identificación de vulnerabilidades

La guía pregunta qué vulnerabilidades de la infraestructura pudieron explotarse con la suplantación de IP y el ARP spoofing, y pide al menos tres con su mitigación. El material del curso llama vulnerabilidades explotadas a las "debilidades en los sistemas de información que los atacantes pueden aprovechar para comprometer la seguridad" (Ochoa Agudelo, 2026d).

El enunciado no las enumera, así que hay que deducirlas del propio ataque. Uso dos grados de certeza. Las vulnerabilidades V1 a V5 son condiciones necesarias: sin ellas el ataque que describe la guía no habría funcionado. Las V6 a V9 son probables: no son imprescindibles para el ataque, pero explican cómo llegó el atacante a la red interna, por qué tardó en detectarse y por qué el daño fue tan amplio.

| ID | Vulnerabilidad | Cómo la aprovechó el ataque | Cómo se habría mitigado | Control |
|---|---|---|---|---|
| V1 | Segmentación insuficiente | La base de datos compartía red local con equipos menos confiables. Desde uno de ellos el atacante alcanzó por ARP al servidor de aplicaciones y a la base de datos. | Zona de datos aislada tras un cortafuegos interno, alcanzable solo desde los servidores de aplicación. | C1 |
| V2 | Conmutadores sin protecciones de capa 2 | Los conmutadores aceptaron y propagaron respuestas ARP falsas sin contrastarlas con nada. | DHCP snooping, inspección dinámica de ARP, IP Source Guard y seguridad de puertos: el conmutador descarta la respuesta ARP que no coincide con su tabla de asignaciones. | C2 |
| V3 | Autorización basada en la dirección IP | La base de datos concedió acceso a quien se presentó con la dirección del servidor de aplicaciones. | Autenticación de cada servicio y de cada administrador con certificado, y retirada de las reglas de confianza por dirección. | C5 |
| V4 | Tráfico interno sin cifrar ni autenticar | El intermediario leyó consultas y respuestas con datos personales y pudo capturar credenciales. | TLS con autenticación mutua entre la aplicación y la base de datos. | C4 |
| V5 | Sin filtrado antisuplantación | Encaminadores y cortafuegos internos dejaron circular paquetes con una dirección de origen falsa. | Verificación de ruta inversa (uRPF) y filtros de entrada por interfaz, según la práctica BCP 38 (Ferguson y Senie, 2000). | C3 |
| V6 | Sin control de acceso a la red y con tomas activas sin vigilar | Un equipo no autorizado o comprometido operó dentro del segmento. | Autenticación 802.1X de cada equipo, tomas sin uso deshabilitadas y armarios de red cerrados. | C6, C14 |
| V7 | Registro y monitoreo insuficientes | Ni el envenenamiento ARP ni las consultas masivas generaron una alerta a tiempo. La detección llegó después del acceso. | Sensor de red con reglas de ARP, monitoreo de la actividad de la base de datos, casos de uso en el SIEM y relojes sincronizados. | C8, C9 |
| V8 | Privilegios excesivos y datos legibles | La cuenta de la aplicación podía consultar toda la base y los datos estaban en claro. | Mínimo privilegio por función, cifrado por campo y enmascaramiento. | C5, C7 |
| V9 | Debilidades de gobierno | Las normas de red y de acceso no se verificaban. Una prueba interna de intrusión habría encontrado V1 a V5. | Normas internas vigentes, pruebas de intrusión internas periódicas y auditoría interna. | C10, C15 |

*Tabla [[t:vulnerabilidades]].* Vulnerabilidades de la infraestructura, forma en que el ataque las aprovechó y mitigación propuesta. La columna de control remite al capítulo 9.

## 6.1 Tres barreras que faltaban a la vez

El ataque necesitó que fallaran varias cosas al mismo tiempo, y esa es la lectura más útil de la tabla. La inspección dinámica de ARP (V2) habría impedido que el atacante se colocara en medio, y sin esa posición la suplantación de IP sobre una conexión TCP no se sostiene. La autenticación con certificado en los dos extremos (V3 y V4) habría dejado al atacante con tráfico cifrado e incapaz de identificarse ante la base de datos, aunque hubiera logrado desviar el tráfico. La segmentación (V1) le habría quitado el acceso al segmento donde hablan la aplicación y la base de datos. Cualquiera de las tres barreras habría cortado la cadena. El principio de defensa en profundidad consiste en no depender de una sola.

El material de redes del curso describía ya las tres piezas. La segmentación "aísla los sistemas críticos, como servidores de bases de datos, de los usuarios finales, reduciendo el riesgo de acceso no autorizado o ataques laterales"; los certificados digitales verifican la identidad del servidor o del cliente para que la comunicación se haga "con la parte correcta"; e IPsec aporta "autenticación mutua entre las partes" en la capa de red (Ochoa Agudelo, 2026a). El incidente es, en buena medida, la consecuencia de no haber aplicado dentro del centro de datos lo que sí se aplica hacia Internet.

## 6.2 Debilidades de diseño y de configuración

Ninguna de las cinco condiciones necesarias es un fallo de programación con un parche pendiente. Son decisiones de diseño y de configuración: una red plana, unas funciones de seguridad del conmutador que vienen desactivadas de fábrica, una regla de acceso que se fía de la dirección. El catálogo de debilidades las tiene descritas desde hace años, como la transmisión de información sensible en claro (CWE-319) o la confianza en la dirección IP para autenticar (CWE-291), y el catálogo de técnicas de ataque recoge tanto el envenenamiento ARP (T1557.002) como la escucha de red (T1040) (MITRE, s. f.).

Esto cambia la forma de mitigarlas. El material del curso cita como medidas típicas los parches de seguridad y el refuerzo de contraseñas con autenticación multifactor (Ochoa Agudelo, 2026d), que siguen siendo necesarias para otras vulnerabilidades. Aquí el trabajo corresponde a dos controles distintos del Anexo A: la gestión de la configuración (8.9), que fija una línea base segura para conmutadores, cortafuegos y bases de datos y vigila que nadie la altere, y la gestión de vulnerabilidades técnicas (8.8), que debe hacerse de forma proactiva y no cuando el incidente ya ocurrió (ISO/IEC, 2022b).

## 6.3 Cómo se habrían encontrado antes

Una prueba de intrusión interna que incluyera la capa 2 habría reproducido el ataque en una tarde con herramientas de uso común, y una revisión de la configuración de los conmutadores contra una línea base habría mostrado las protecciones desactivadas sin necesidad de atacar nada. El ejemplo que el curso pone de la banca va en esa dirección: identificar los activos, clasificarlos por sensibilidad y hacer pruebas de penetración periódicas para detectar las vulnerabilidades y corregirlas (Ochoa Agudelo, 2026d).

Un auditor que quisiera comprobar hoy si estas vulnerabilidades siguen abiertas pediría cuatro cosas: la configuración vigente de los conmutadores del centro de datos, las reglas del cortafuegos interno, los parámetros de autenticación y cifrado de la base de datos y el informe de la última prueba de intrusión interna con el estado de sus hallazgos.
