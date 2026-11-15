# Indicaciones del docente en clase

Síntesis de las tres grabaciones de clase (transcripciones completas en `material/transcripciones/`). Recoge lo que el docente, Edwin Ochoa, pidió o enfatizó y que condiciona cómo debe hacerse el Ejercicio Práctico de Políticas de Seguridad (Laboratorio 6). Las marcas `[hh:mm:ss]` remiten al momento del video.

## Clase del 4 de noviembre de 2026, primera parte

Video `2026-11-04 18-43-20.mp4` (34 min). Tema: marco normativo colombiano en ciberseguridad (Tema 10), Ley 1581 de 2012.

### Indicaciones que condicionan el informe

1. **Hablar con propiedad de normas, leyes y artículos** `[00:00:00]`. "Tiene que empezar a hablar con propiedad de las normas, de la normatividad, de mencionar leyes, de mencionar artículos, de todo lo que le estoy dejando en la plataforma". El informe debe citar la ley y el artículo concretos, y apoyarse en el material de Polivirtual (videos, PDF, la norma ISO y el PDF de UNIR) `[00:01:22]`.
2. **Leyes de Colombia y de Europa, más estándares** `[00:02:35]`. La clase anuncia "leyes en Colombia y leyes en Europa" e "integración profunda de los estándares internacionales como la ISO, la NIST, la COBIT". Confirma el marco doble (Colombia y Unión Europea) sobre estándares internacionales.
3. **No meter todo en el mismo saco: ley, norma, marco y buena práctica son cosas distintas** `[00:09:50]` a `[00:13:11]`. "Una de las confusiones más frecuentes en ciberseguridad es meter todo en el mismo saco".
   - **Ley:** "es obligatoria dentro de su ámbito de aplicación".
   - **Norma (ISO 27001):** "establece requisitos para un sistema de gestión".
   - **Marco o framework (NIST):** "proporciona una estructura para gestionar riesgos de ciberseguridad".
   - **COBIT:** "se enfoca principalmente en gobierno y gestión de información y tecnología".
   - **ITIL:** "se enfoca en gestión de servicios TI".
   - "¿Pueden trabajar juntas? Sí, pero no quiere decir que equivalgan a lo mismo". "Una empresa madura puede utilizar varios de estos elementos simultáneamente" `[00:14:18]`.
4. **Mapa general de la normatividad** `[00:13:11]`. Legislación colombiana: protección de datos; delitos informáticos; acceso a la información pública; sector financiero, salud y telecomunicaciones. Marcos: gobierno y gestión con COBIT; gestión de seguridad con ISO; gestión de riesgos cibernéticos con NIST; gestión de servicios TI con ITIL.
5. **Conectar la ley con los controles técnicos** `[00:28:22]` a `[00:30:08]`. Tabla "exigencia y control TI" que el docente dictó y dejó en el chat:

   | Exigencia de la ley | Control TI |
   |---|---|
   | Protección de la información | Cifrado |
   | Acceso autorizado | IAM |
   | Control de usuarios | RBAC |
   | Trazabilidad | Logs |
   | Prevención de accesos | MFA |
   | Protección de infraestructura | Firewall |
   | Recuperación | Backups |
   | Detección | SIEM o EDR |
   | Gestión de riesgos | ISO o NIST |
   | Evidencia | Auditoría |

   "La norma establece la responsabilidad y la tecnología ayuda a demostrar y ejecutar el control".
6. **Pensar como en una auditoría** `[00:31:45]`. "A la hora de una auditoría me van a preguntar: si la ley usted la está aplicando, cómo la implementó y qué seguridad está utilizando". Tres cosas distintas y de estricto cumplimiento: la aplicabilidad, el uso y la seguridad que se le brinda a los datos, con trazabilidad de cada evento.
7. **La protección de datos es también arquitectura de seguridad** `[00:18:24]` a `[00:19:40]`. Preguntas que la organización debe hacerse por cada dato: para qué lo recolecto, si es necesario, cómo lo voy a proteger, quién puede acceder, cuánto tiempo lo conservo y con quién lo comparto. "Esto ya no es solamente una pregunta jurídica, es una pregunta de arquitectura de seguridad".

### Contenido teórico dictado

- **Ley 1581 de 2012** `[00:05:13]`: "la piedra angular en Colombia"; aplica obligatoriamente a toda organización pública o privada que recolecte, almacene o procese datos. Garantiza el derecho fundamental a la protección de datos y la autodeterminación informativa `[00:16:24]`. Antes de 2012 "no había regulaciones" `[00:04:10]`.
- **Consentimiento previo, expreso e informado** `[00:06:43]`. **Derechos ARCO**: acceso, rectificación, cancelación y oposición `[00:08:38]`.
- **SIC**: máxima autoridad, vigila e impone multas `[00:09:50]`.
- **El dato no es de la empresa** `[00:14:18]`: que una empresa almacene un dato no significa que deje de pertenecer a su titular.
- **Responsable y encargado** `[00:19:40]` a `[00:22:37]`: el responsable decide finalidades y condiciones; el encargado trata por cuenta del responsable. Con un proveedor en la nube, la empresa sigue siendo responsable. Según la SIC (Ley 1581 y Decreto 1074 de 2015), el encargado no puede ampliar por iniciativa propia las finalidades `[00:22:37]` a `[00:26:28]`.
- **Pilares de la Ley 1581** `[00:26:28]`: consentimiento, derechos del titular y responsabilidad del responsable (medidas adecuadas).

## Clase del 4 de noviembre de 2026, segunda parte

Video `2026-11-04 20-02-51.mp4` (46 min). Tema: ISO 27001 frente a NIST, Ley 1266, Ley 1273, Ley 1712, estándares internacionales y análisis de riesgos (documento de UNIR).

### Indicaciones que condicionan el informe

1. **La lógica de ISO 27001 es la secuencia del ejercicio** `[00:30:37]`. Ejemplo del docente con "una empresa que maneja información de 2 millones de clientes": la organización "identifica sus activos, analiza riesgos, define controles, establece políticas, asigna responsabilidades, monitorea resultados, realiza auditorías y mejoras continuas". Es el mismo orden de las actividades de la guía.
2. **Demostrar, no solo tener controles** `[00:32:59]`. "La ISO 27001 no pregunta únicamente qué controles tiene, sino que pregunta cómo gestionas sistemáticamente el riesgo y cómo puedes demostrarlo".
3. **Cada norma tiene su ámbito** `[00:30:37]`. "Cada ley se tipifica según dónde la voy a poner a operar, dónde aplica"; "no es que cualquier ley me sirva para lo mismo".
4. **ISO y NIST son válidas a la vez; se elige según el propósito** `[00:10:21]`. Si la empresa va a contratar, tener proveedores o vender servicios, "la ISO es la que me audita y me garantiza el cumplimiento de todos los estándares".
5. **El desconocimiento de la ley no exime de cumplirla** `[00:21:04]`. Las leyes son "de estricto cumplimiento legal".
6. **Usar los documentos de la plataforma** `[00:42:15]` y `[00:44:44]`. "Estos documentos ahí los tienen para que se alimenten y para que los descarguen".

### Contenido teórico dictado

- **Video comparativo ISO 27001 y NIST CSF (canal ErgoHackers)** `[00:00:00]` a `[00:10:21]`. NIST CSF: funciones identificar, proteger, detectar, responder y recuperar; gratuito, no certificable, nacido para agencias federales de Estados Unidos. ISO 27001: internacional, orientada a riesgos, certificable por un tercero (con costo). Coincidencias: ambos se orientan al ciberriesgo (impacto y probabilidad, BIA), piden controles para mitigar y monitoreo continuo con indicadores clave de riesgo (KRI). Pueden coexistir. El video usa las versiones antiguas (14 dominios y 114 controles; cinco funciones).
- **Ley 1266 de 2008, habeas data financiero** `[00:12:01]` a `[00:14:36]`: información financiera, crediticia, comercial y de servicios. "La ciberseguridad no es solo cuidar bases de datos corporativas, también persigue el delito y protege el sistema financiero".
- **Ley 1273 de 2009** `[00:14:36]` a `[00:23:30]`: incorporó al Código Penal colombiano el bien jurídico "de la protección de la información y de los datos"; capítulo de los atentados contra la confidencialidad, la integridad y la disponibilidad de los datos y de los sistemas informáticos. El docente leyó en la página de Función Pública el **artículo 269A, acceso abusivo a un sistema informático**: quien sin autorización o por fuera de lo acordado acceda en todo o en parte a un sistema informático, protegido o no con una medida de seguridad, o se mantenga dentro de él contra la voluntad de quien tenga derecho a excluirlo, incurre en prisión de 48 a 96 meses y multa de 100 a 1.000 salarios mínimos legales mensuales vigentes `[00:20:05]`.
- **Ley 1712 de 2014** `[00:25:06]`: acceso a la información pública.
- **Circular Externa 003 de la SIC** `[00:27:09]`: tratamiento de datos sensibles (el docente dice "2007"; la diapositiva dice 2017).
- **ISO 27001** `[00:28:18]` a `[00:29:29]`: "el estándar de oro en seguridad de la información"; requisitos para crear, implementar, mantener y mejorar continuamente el SGSI; se basa en la gestión de riesgos (identificar, analizar, tratar, monitorear) y en el ciclo PHVA (planear, hacer, verificar, actuar).
- **NIST** `[00:29:29]` a `[00:30:37]`: cinco funciones (identificar, proteger, detectar, responder y recuperar); "sumamente práctico para diseñar planes de respuesta ante incidentes".
- **Recomendaciones de cumplimiento** `[00:32:59]`: evaluar la recolección de datos, tener mecanismos de alerta y respuesta, capacitación continua (phishing, malware, ransomware), notificar incidentes.
- **Análisis de riesgos, documento de UNIR** `[00:34:41]` a `[00:43:14]`: la gestión de riesgos tiene dos fases, análisis y tratamiento; los activos se valoran por confidencialidad, integridad y disponibilidad; enfoques cuantitativo, cualitativo (alto, medio, bajo) y basado en conocimiento; opciones de tratamiento: reducir, compartir o transferir, eliminar o mitigar, y aceptar; estándares: ISO 13335, ISO 27001 y 27002 ("un total de 93 controles"), NIST, COBIT, MAGERIT v3 y MARISMA.

Nota para el informe: la clase menciona las cinco funciones clásicas del NIST y el video usa ISO 27001:2013. El material de Polivirtual trae el CSF 2.0 (seis funciones, con Gobernar) y el documento de UNIR ya habla de 93 controles (ISO 27002:2022). El informe usa las versiones vigentes y deja la equivalencia.

## Clase del 6 de noviembre de 2026

Video `2026-11-06 18-25-16.mp4` (1 h 44 min, día de la guía). Temas: cumplimiento de normativas y auditoría de riesgos (Tema 4.4), normativa española y europea, video de los controles tecnológicos de ISO 27001:2022 y recorrido por los numerales 4 a 10 de la norma. **Es la clase donde el docente presenta el ejercicio y da las pautas para hacerlo.**

### Datos de la actividad

- **Dónde está** `[00:00:00]`: Polivirtual, Módulo 2, Unidad 3, al final: "Ejercicio práctico número 5, Políticas de Seguridad".
- **Plazo** `[00:10:09]` y `[01:39:29]`: "hasta el martes está abierta a las 10 de la noche"; "le queda sábado, domingo, lunes y el martes hasta las 10 de la noche". La clase fue el viernes 6, de modo que el cierre anunciado fue el **martes 10 de noviembre de 2026 a las 22:00**.
- **Extensión** `[00:00:00]` y `[01:43:42]`: "es larga, yo creo que de las actividades más largas"; "no se descuide con el ejercicio, es largo, compréndalo muy bien antes de comenzar a montar".
- **Documentación necesaria** `[00:01:52]`: "es una actividad que se necesita mucha documentación para responderla": la ISO, la Ley 1581, las leyes de la clase pasada y lo de esta clase. En Polivirtual, junto al ejercicio, están la Ley 1581, la guía NQA de ISO 27001, el tema de UNIR y el video "ISO 27001 vs NIST CSF". El docente envió además por WhatsApp la ISO 27001 y la 27002 `[00:10:09]`.
- **Exposición** `[01:39:29]` a `[01:42:02]`: lo que el docente comenta es la exposición final del diplomado con póster, en grupos de tres (quizá cuatro), con temas del microcurrículo y rúbrica aún sin definir. No habló de exponer este ejercicio; la presentación de 5 a 7 minutos solo figura en la guía escrita.

### Indicaciones directas sobre cómo hacer el ejercicio

1. **Mapear antes de escribir** `[00:10:09]`, `[00:15:16]`, `[01:03:18]`. "Mapee desde hoy cómo la va a realizar"; "uno primero la mapea para que sepa qué documentos va a utilizar en ella"; mapear es tomar nota de las palabras clave de la norma.
2. **Empezar por el contexto de la empresa (numeral 4 de ISO 27001)** `[01:01:09]` a `[01:02:17]`. "El ejercicio de la empresa es una empresa que existe en España, el ejercicio es real, no es una empresa que yo me inventé". Preguntas que el estudiante debe responder antes de proponer nada: **¿qué hace la empresa?, ¿qué información maneja?, ¿quiénes son sus clientes?, ¿qué sistema utiliza?, ¿qué leyes debe cumplir?, ¿qué proveedores tiene? y ¿qué amenazas enfrenta?** Advertencia literal: "no me haga con pendejadas porque le pongo una pendejada de nota también, porque este tema sí me lo sé de pe a pa". "No es lo mismo proteger una tienda de ropa que un banco": el sistema se adapta al contexto, no al contrario `[01:03:18]`.
3. **Los controles salen del mapeo de la empresa y de sus riesgos** `[01:19:17]`. "En la parte del ejercicio que le mencione la implementación de los controles usted ya tiene que tener la inferencia de lo que le vengo mencionando: qué mapeo estoy haciendo de la empresa, qué es esa empresa, dónde está ubicada"; "yo no le voy a cantar todo el ejercicio, le estoy dando pautas para que lo delibere, lo mapee".
4. **Cadena del riesgo** `[01:06:50]` a `[01:09:32]`. Formato del ejemplo del docente: **activo** (base de datos de clientes), **amenaza** (ransomware), **vulnerabilidad** (copias de seguridad conectadas permanentemente a la red), **consecuencia** (pérdida de disponibilidad), **riesgo** (interrupción del servicio y pérdida de la información) y **controles** (copias aisladas, MFA, segmentación, EDR, control de privilegios, pruebas de recuperación) `[01:12:42]`.
5. **Cuatro opciones de tratamiento** `[01:12:42]`: evitar (no realizar la actividad que genera el riesgo), mitigar (controles para reducirlo), transferir (compartirlo con terceros, por ejemplo con un seguro o un contrato) y aceptar (la organización decide asumirlo dentro de sus criterios de aceptación).
6. **Riesgo inherente y riesgo residual** `[01:14:26]`. El inherente es el de antes de los controles; el residual permanece después ("puede pasar de alto a medio, pero no desapareció"); la norma pide que los responsables acepten el residual.
7. **Declaración de aplicabilidad (SoA)** `[01:16:42]` a `[01:19:17]`. "Uno de los conceptos que sí o sí usted debe aprender"; indica los controles necesarios, su justificación y las razones para incluir o excluir. No se implementan todos los controles de la norma: primero se identifican los riesgos y luego se eligen los controles según el sistema, el tamaño y las dependencias de la empresa; eso es lo que se audita.
8. **Anexo A en sus cuatro grupos, versión 2022** `[01:21:07]`: A.5 organizacionales (políticas, roles, proveedores, incidentes, continuidad, cumplimiento), A.6 de personas (selección, capacitación, concienciación, responsabilidades, contratos), A.7 físicos (acceso físico, instalaciones, protección de equipos, vigilancia) y A.8 tecnológicos (control de acceso, autenticación, criptografía, copias de seguridad, registros, monitoreo, vulnerabilidades, seguridad de redes, desarrollo seguro).
9. **Pensar como auditor, no como hacker** `[01:34:35]`. "Usted tiene que pensar como un auditor en estos casos de políticas de seguridad". Evidencias que pediría un auditor: política aprobada, configuración técnica, registros, usuarios, revisiones, resultados de auditoría, capacitaciones e indicadores. "No basta con decir que un control existe, hay que poder demostrar que está implementado y que funciona".
10. **Plantilla de análisis de un incidente** `[01:32:47]`. Caso de clase (empresa XYZ, phishing, credenciales, servidor con base de datos, extracción) y sus preguntas: ¿qué activo estaba en riesgo?, ¿qué amenaza ocurrió?, ¿qué vulnerabilidad permitió el ataque?, ¿qué principio de la tríada se afectó?, ¿qué controles deberían existir?, ¿qué debería hacer el SGSI?, ¿qué evidencias debería conservar la empresa? y ¿qué debería revisar después del incidente?
11. **Indicadores** `[01:29:08]`. Para saber si un control funciona se mide; ejemplo con MFA: porcentaje de cuentas con MFA, número de accesos bloqueados, incidentes relacionados con credenciales, usuarios con privilegios excesivos y tiempo de respuesta a incidentes.
12. **Dónde poner el énfasis** `[01:39:29]`. "Yo dedicaría más tiempo al riesgo, al SoA, al anexo A, a la auditoría, a la evidencia, a los incidentes, a la mejora continua, que a explicar controles individuales". "No se trata de memorizar sino de implementar".
13. **Fuentes** `[01:39:29]`. "Léalo aparte de la norma, lea los documentos que tiene ahí, básese en la clase pasada, básese en esta clase".

### Contenido teórico dictado

- **Normativa europea y española proyectada (diapositivas de UNIR, "Normativa en materia de ciberseguridad")** `[00:01:52]` a `[00:10:09]`:
  - Directiva (UE) 2016/1148 (NIS): lograr un elevado nivel común de seguridad de las redes y sistemas de información; aplica a operadores de servicios esenciales y proveedores de servicios digitales.
  - Directiva NIS 2: deroga la anterior desde el 18 de octubre de 2024; transposición a más tardar el 17 de octubre de 2024.
  - **Real Decreto-ley 12/2018**, de seguridad de las redes y sistemas de información: regula la seguridad de las redes usadas para prestar servicios esenciales (sectores estratégicos del anexo de la Ley 8/2011) y servicios digitales, y establece un sistema de notificación de incidentes (art. 19). CSIRT de referencia: CCN-CERT (sector público), INCIBE-CERT (entidades privadas y ciudadanos) y ESPDEF-CERT.
  - **Real Decreto 43/2021**, de 26 de enero, que lo desarrolla. Medidas de seguridad (art. 6.2): análisis y gestión de riesgos; gestión de riesgos de terceros o proveedores; catálogo de medidas organizativas, tecnológicas y físicas; gestión del personal y profesionalidad; adquisición de productos o servicios de seguridad; detección y gestión de incidentes; planes de recuperación y continuidad de las operaciones; mejora continua; interconexión de sistemas; registro de la actividad de los usuarios. "La relación de medidas adoptadas se formalizará en un documento denominado Declaración de Aplicabilidad de medidas de seguridad, que será suscrito por el responsable de seguridad de la información y que se incluirá en la política de seguridad que apruebe la Dirección". Los operadores designan un responsable de la seguridad de la información como punto de contacto con la autoridad y el CSIRT.
  - El docente equipara la autoridad española con la SIC en Colombia: "nosotros de estas leyes las traemos y las aplicamos en Colombia" `[00:07:40]`.
- **Otras metodologías del documento de UNIR** `[00:12:01]`: MEHARI (puntos de control de vulnerabilidades y monitorización para la mejora continua), ISO 20000 e ITIL (conocimiento actualizado de todos los activos), COBIT (evaluación de riesgos; confidencialidad, integridad y disponibilidad).
- **Video de los 34 controles tecnológicos de ISO 27001:2022 (bloque 8 del Anexo A)** `[00:15:16]` a `[00:43:05]`. "Ese video le va a ayudar mucho para que desarrolle la actividad" `[00:13:41]`. Ideas: la norma no impone una herramienta ni una marca; los controles se evidencian de varias maneras siempre que respondan al análisis de riesgo; los controles físicos son "los grandes olvidados". Controles citados: 8.2 privilegios de acceso, 8.3 restricción de acceso por necesidad de conocer, 8.4 código fuente, 8.5 autenticación segura (doble factor), 8.6 capacidad, 8.7 código malicioso, 8.8 vulnerabilidades técnicas (de forma proactiva), 8.9 gestión de la configuración, 8.10 eliminación de la información, 8.11 enmascaramiento de datos, 8.12 prevención de fuga de datos, 8.13 copias de seguridad (cifradas, periódicas, en otra ubicación), 8.14 redundancia, 8.15 registro de eventos, 8.16 seguimiento de actividades, 8.17 sincronización de relojes, 8.18 programas de utilidad con privilegios, 8.19 instalación de software, 8.20 seguridad de redes, 8.21 seguridad de los servicios de red, 8.22 segregación de redes, 8.23 filtrado web, 8.24 uso de la criptografía, 8.25 a 8.34 desarrollo seguro, cambios y pruebas (8.32 gestión del cambio con trazabilidad de quién pide, aprueba y ejecuta). Cierra con la declaración de aplicabilidad.
- **Qué es ISO 27001** `[00:43:05]` a `[00:46:20]`: "no es un antivirus, no es un firewall, no es una herramienta informática"; es la norma para establecer, implementar, mantener y mejorar continuamente un SGSI, en organizaciones de cualquier tamaño y sector. La palabra clave es gestión: identificar riesgos, decidir su tratamiento, implementar controles, medirlos, auditarse y mejorar.
- **Tríada** `[00:47:53]` a `[00:55:19]`: confidencialidad (la nómina solo la consulta quien está autorizado), integridad (si un atacante cambia el salario de un empleado en la base de datos hay un problema de integridad), disponibilidad (un hospital con el sistema caído). Un ransomware afecta sobre todo la disponibilidad y puede comprometer las otras dos.
- **No es solo tecnología** `[00:55:19]` a `[00:57:37]`: personas, procesos y tecnología; error común: creer que la seguridad es responsabilidad exclusiva de sistemas.
- **Numerales 4 a 10** `[00:57:37]` a `[01:32:47]`: 4 contexto; 5 liderazgo (la alta dirección aporta compromiso y recursos; "la política debe establecerse, comunicarse y mantenerse", no basta un PDF que nadie conoce); 6 planificación ("aquí está el corazón de la ISO 27001: gestión del riesgo"); 7 soporte (recursos, competencia, conciencia, comunicación); 8 operación (ejecutar lo planificado); 9 evaluación del desempeño (seguimiento y medición, auditoría interna, revisión por la dirección; la auditoría "no consiste en buscar culpables", busca evidencia con objetividad e imparcialidad); 10 mejora (no conformidad: se identifica, se corrige, se analiza la causa, se aplican acciones correctivas y se verifica su eficacia).
- **Las diez ideas** `[01:36:24]`: es una norma de gestión; establece el SGSI; protege la confidencialidad, integridad y disponibilidad; la seguridad se alinea con el negocio; el enfoque central es el riesgo; la alta dirección da liderazgo y recursos; los controles se seleccionan según riesgos y necesidades; la SoA documenta la aplicabilidad; hay que medir, auditar y revisar; mejora continua. "La pregunta realmente importante es: ¿la organización conoce sus riesgos, ha decidido cómo tratarlos, ha implementado controles adecuados, puede demostrar que funcionan, los audita y los mejora?". "ISO 27001 es contexto, riesgo, control, implementación, medición, auditoría, mejora continua".

## Lista de verificación derivada de las clases

Se usa en el ciclo de validación de cobertura.

- [ ] Cada norma citada lleva su artículo o numeral concreto.
- [ ] El modelo normativo distingue ley, norma, marco y buena práctica, con ISO 27001, NIST, COBIT e ITIL cada uno en su papel.
- [ ] Hay leyes de Colombia y de Europa (incluidos el Real Decreto-ley 12/2018 y el Real Decreto 43/2021 vistos en clase).
- [ ] Existe una tabla que conecta exigencia legal, control TI y evidencia de auditoría.
- [ ] Se usa el material de Polivirtual como fuente citada.
- [ ] El informe abre con el contexto de la empresa y responde las siete preguntas (qué hace, qué información maneja, clientes, sistemas, leyes, proveedores, amenazas).
- [ ] Los riesgos siguen la cadena activo, amenaza, vulnerabilidad, consecuencia, riesgo y controles.
- [ ] Hay riesgo inherente y residual, y una de las cuatro opciones de tratamiento por riesgo (evitar, mitigar, transferir, aceptar).
- [ ] Hay una declaración de aplicabilidad con controles del Anexo A de 2022 (A.5, A.6, A.7 y A.8), su justificación y las exclusiones.
- [ ] Cada control indica la evidencia con que se demuestra ante un auditor.
- [ ] Hay indicadores para medir si los controles funcionan.
- [ ] El incidente se analiza con las ocho preguntas del caso de clase.
- [ ] El énfasis está en riesgo, SoA, Anexo A, auditoría, evidencia, incidentes y mejora continua.
