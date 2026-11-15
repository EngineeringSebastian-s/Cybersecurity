# 7. Actividad 4: modelo normativo de seguridad

La guía pide un modelo normativo que contemple las mejores prácticas y los estándares internacionales, y que explique cómo las políticas y normativas internas ayudan a prevenir incidentes similares. El material del curso define el modelo normativo como "el conjunto de marcos regulatorios y normas que guían las políticas de seguridad de la información en una organización" (Ochoa Agudelo, 2026d).

El modelo que propongo tiene dos mitades, que la Figura [[f:modelo]] muestra una junto a la otra. La mitad externa reúne lo que la compañía debe cumplir o decide seguir. La mitad interna es lo que la compañía escribe y aplica en su casa para cumplirlo: una política, unas normas, unos procedimientos y los registros que prueban que todo eso se hace.

![](diagramas/03_modelo_normativo.png)

*Figura [[f:modelo]].* Modelo normativo propuesto: el marco externo de leyes, norma, marcos y buenas prácticas se traduce en una normativa interna que termina en evidencias auditables.

## 7.1 Ley, norma, marco y buena práctica

En clase el docente insistió en no meter todo en el mismo saco, porque una de las confusiones más frecuentes en ciberseguridad es tratar como equivalentes cosas que cumplen funciones distintas (Ochoa Agudelo, 2026c). La Tabla [[t:capas]] ordena el marco externo con esa distinción y con las palabras con que se explicó.

| Capa | Qué es | Instrumentos para Mapfre | Qué aporta al caso |
|---|---|---|---|
| Ley | "Es obligatoria dentro de su ámbito de aplicación." | RGPD, LOPDGDD, Reglamento DORA, Real Decreto-ley 12/2018, Real Decreto 43/2021, Código Penal | Fija el deber de proteger, los plazos de notificación y las sanciones. |
| Norma | "Establece requisitos para un sistema de gestión." Se puede certificar. | ISO/IEC 27001:2022 para la seguridad de la información; ISO 22301 para la continuidad | Ordena la gestión: contexto, riesgo, controles, medición, auditoría y mejora. |
| Marco | "Proporciona una estructura para gestionar." | NIST CSF 2.0 para el riesgo de ciberseguridad; COBIT 2019 para el gobierno y la gestión de TI; ITIL 4 para la gestión de servicios | Organiza capacidades, reparte responsabilidades e integra la seguridad en la operación diaria. |
| Buena práctica | Indica cómo implementar. | ISO/IEC 27002:2022, CIS Controls, BCP 38, guías de los fabricantes | Baja al detalle técnico: qué activar en un conmutador o en la base de datos. |

*Tabla [[t:capas]].* Las cuatro capas del marco externo, con la definición dada en clase.

Las cuatro capas pueden trabajar juntas sin ser equivalentes, y "una empresa madura puede utilizar varios de estos elementos simultáneamente" (Ochoa Agudelo, 2026c). La ley dice qué resultado se exige. La norma dice cómo organizarse para lograrlo de forma demostrable. El marco y la buena práctica dicen con qué piezas.

## 7.2 Las leyes y sus artículos

Hablar con propiedad de la normativa exige citar la ley y el artículo. La Tabla [[t:leyes]] recoge las normas que aplican a una aseguradora española con el incidente descrito.

| Norma | Artículos | Qué exige | Relación con el incidente |
|---|---|---|---|
| Reglamento (UE) 2016/679, RGPD | 5.1.f y 5.2; 24, 25 y 32; 33 y 34; 35; 82 y 83 | Integridad y confidencialidad de los datos y capacidad de demostrarlo. Medidas técnicas y organizativas apropiadas al riesgo, entre ellas el cifrado y la verificación periódica de su eficacia. Notificación a la autoridad en 72 horas y comunicación a los afectados si el riesgo es alto. Evaluación de impacto. Indemnización y multas de hasta 20 millones de euros o el 4 % del volumen de negocio. | Datos sin cifrar en tránsito y acceso autorizado por dirección IP son difíciles de defender como medidas apropiadas al riesgo. |
| Ley Orgánica 3/2018, LOPDGDD | 72.1.a; 73 d, f, g, r y s; 74 m y n; 78 | Tipifica como muy grave tratar datos vulnerando los principios del artículo 5 del RGPD. Como graves, no adoptar las medidas de seguridad del artículo 32, quebrantarlas por falta de diligencia, no notificar la violación a la autoridad y no comunicarla al afectado cuando se requiere. Como leves, notificar tarde o de forma incompleta y no documentar la violación. | Concreta a qué tipo de infracción se expone la compañía y en cuánto tiempo prescribe. |
| Reglamento (UE) 2022/2554, DORA, y Reglamento Delegado (UE) 2025/301 | 5 a 16; 17 a 19; 24 a 27; 28 a 30; artículo 5 del delegado | Marco de gestión del riesgo tecnológico aprobado por el órgano de dirección: identificar, proteger, detectar, responder y recuperar. Clasificación de incidentes y notificación de los graves a la autoridad competente: inicial en 4 horas desde la clasificación y a más tardar 24 horas desde que se conoce, intermedia a las 72 horas y final en un mes. Pruebas de resiliencia. Gestión del riesgo de proveedores. | La aseguradora debe notificar a la Dirección General de Seguros y Fondos de Pensiones y demostrar que su marco funciona. |
| Real Decreto-ley 12/2018 y Real Decreto 43/2021 | 16 y 19 del real decreto-ley; 6 y 7 del real decreto | Medidas de seguridad en diez frentes (riesgos, proveedores, catálogo de medidas organizativas, tecnológicas y físicas, personal, incidentes, continuidad, mejora continua, interconexión y registro de la actividad de los usuarios). Declaración de aplicabilidad firmada por el responsable de seguridad e incluida en la política que aprueba la Dirección. Notificación de incidentes al CSIRT de referencia. | Aplican si la compañía está designada operador de servicios esenciales. Su estructura coincide con la de un sistema de gestión. |
| Ley Orgánica 10/1995, Código Penal | 197 bis.1 y 197 bis.2; 249; 264; 197 quinquies | Castiga el acceso a un sistema vulnerando sus medidas de seguridad con prisión de seis meses a dos años, y la interceptación de transmisiones no públicas de datos con prisión de tres meses a dos años o multa. Tipifica las estafas por medios informáticos y los daños informáticos. Prevé la responsabilidad de las personas jurídicas. | Califica la conducta de los atacantes. La compañía es víctima y debe denunciar. |
| Reglamento (UE) 596/2014, abuso de mercado | 17 | Obliga al emisor cotizado a difundir la información privilegiada tan pronto como sea posible. | Solo aplica si el incidente puede influir de forma apreciable en la cotización. |

*Tabla [[t:leyes]].* Leyes aplicables en España y la Unión Europea, con los artículos que interesan al caso.

Dos precisiones sobre vigencia. La Directiva NIS 2 debía transponerse antes del 17 de octubre de 2024 y a finales de octubre de 2026 España seguía sin ley de transposición, por lo que el Real Decreto-ley 12/2018 continúa en vigor (Cuatrecasas, 2026). Y las directrices de seguridad tecnológica que el supervisor europeo de seguros había dictado bajo Solvencia II quedaron revocadas el 17 de enero de 2025 porque DORA cubre por completo sus objetivos (EIOPA, 2024). Para una aseguradora, el texto de referencia en resiliencia digital es hoy DORA.

## 7.3 El mismo incidente bajo la ley colombiana

El diplomado se cursa en Colombia y el docente recordó que estas normas europeas "las traemos y las aplicamos" aquí (Ochoa Agudelo, 2026c). Si la base de datos afectada fuera la de una filial colombiana, el análisis cambiaría de artículos pero no de lógica, como muestra la Tabla [[t:espejo]].

| Aspecto | España y Unión Europea | Colombia |
|---|---|---|
| Ley de protección de datos | RGPD y LOPDGDD | Ley 1581 de 2012; Ley 1266 de 2008 para la información financiera y crediticia |
| Autoridad | Agencia Española de Protección de Datos | Superintendencia de Industria y Comercio (SIC) |
| Deber de seguridad | Artículo 32 del RGPD | Artículos 4 g y 17 d de la Ley 1581: impedir la adulteración, pérdida, consulta, uso o acceso no autorizado o fraudulento |
| Aviso a la autoridad | 72 horas (artículo 33 del RGPD) | Artículo 17 n de la Ley 1581; reporte al Registro Nacional de Bases de Datos en 15 días hábiles |
| Aviso a los afectados | Sin dilación indebida si el riesgo es alto (artículo 34 del RGPD) | A los titulares, en un plazo razonable (Ochoa Agudelo, 2026b) |
| Sanción administrativa | Hasta 20 millones de euros o el 4 % del volumen de negocio | Multas de hasta 2.000 salarios mínimos mensuales, suspensión de hasta seis meses y cierre (artículo 23 de la Ley 1581) |
| Supervisor financiero | Dirección General de Seguros y Fondos de Pensiones, con DORA | Superintendencia Financiera, con las Circulares Externas 007 de 2018 y 033 de 2020 |
| Delito de acceso | Artículo 197 bis.1 del Código Penal | Artículo 269A de la Ley 1273 de 2009: prisión de 48 a 96 meses y multa de 100 a 1.000 salarios mínimos |
| Delito de interceptación | Artículo 197 bis.2 del Código Penal | Artículo 269C de la Ley 1273 de 2009 |

*Tabla [[t:espejo]].* Correspondencia entre el marco español y europeo y el colombiano para el mismo incidente.

La comparación deja dos diferencias. El plazo colombiano de aviso a la autoridad es mucho más largo que el europeo, de modo que un procedimiento interno diseñado para cumplir las 72 horas cumple de sobra el otro. En cambio, las penas de prisión colombianas por acceso abusivo son más altas, hasta ocho años, como se leyó en clase al revisar el artículo 269A (Ochoa Agudelo, 2026c).

## 7.4 La norma y los marcos, cada uno en su papel

ISO/IEC 27001 es la columna del modelo. Es la norma que establece cómo implantar, mantener y mejorar un sistema de gestión de seguridad de la información, y "no pregunta únicamente qué controles tiene, sino cómo gestionas sistemáticamente el riesgo y cómo puedes demostrarlo" (Ochoa Agudelo, 2026c). Sus numerales 4 a 10 marcan el recorrido de este informe: el contexto de la organización está en el capítulo 2; el liderazgo se concreta en la política que aprueba la Dirección; la planificación es el análisis de riesgos del capítulo 8 y la declaración de aplicabilidad del capítulo 9; el soporte incluye la formación; la operación son los controles y el cierre de brechas; la evaluación del desempeño corresponde al monitoreo, los indicadores y la auditoría interna, y la mejora es el plan del capítulo 17. La versión vigente es la de 2022, con 93 controles en cuatro grupos. La guía de implantación del curso describe la de 2013, con 114 controles en 14 dominios (NQA, s. f.), y la estructura de los numerales 4 a 10 es la misma en ambas.

El marco de ciberseguridad del NIST organiza las capacidades por funciones. En clase se citaron las cinco clásicas, identificar, proteger, detectar, responder y recuperar; la versión 2.0, que es la que está en la plataforma del curso, antepone una sexta, gobernar (NIST, 2024). Sirve para comprobar que no queda ninguna función vacía. En el caso, la compañía tenía capacidad de protección hacia el exterior y de respuesta, y un hueco en la detección dentro de la red. El video comparativo visto en clase lo sitúa bien: ISO se certifica y sirve para demostrar cumplimiento ante clientes y reguladores; NIST es gratuito y muy práctico para diseñar la respuesta, y los dos pueden coexistir (ErgoHackers, s. f.).

COBIT se ocupa del gobierno: quién decide, quién responde y cómo se rinden cuentas sobre la tecnología (ISACA, 2018). Aporta lo que el incidente echó en falta, un responsable claro del riesgo de la red interna. ITIL ordena la prestación de los servicios de TI (AXELOS, 2019), y dos de sus prácticas tocan el caso de lleno: la gestión de cambios, para que nadie desactive una protección sin aprobación ni registro, y la gestión de incidentes, que conecta la mesa de servicio con el equipo de respuesta.

## 7.5 La normativa interna

La mitad interna del modelo es una jerarquía documental de cuatro niveles. La política general enuncia el compromiso y los principios. Las normas internas fijan reglas obligatorias por materia. Los procedimientos dicen quién hace qué, cuándo y con qué herramienta. Los registros dejan la evidencia. La Tabla [[t:politicas]] propone el juego de documentos y señala qué habría evitado cada uno.

| Política o norma interna | Qué establece | Anexo A | Qué habría evitado |
|---|---|---|---|
| Política de seguridad de la información | Compromiso de la Dirección, objetivos, funciones y revisión anual | 5.1, 5.2, 5.4 | Que la red interna no tuviera un responsable definido |
| Norma de clasificación y manejo | Cuatro etiquetas y sus reglas de tratamiento | 5.10, 5.12, 5.13 | Que información restringida viajara sin cifrar |
| Norma de control de acceso e identidades | Mínimo privilegio, autenticación fuerte, prohibición de autorizar por dirección IP, revisión trimestral | 5.15 a 5.18, 8.2, 8.3, 8.5 | V3 y V8 |
| Norma de seguridad de redes | Zonas, protecciones de capa 2 obligatorias, filtrado antisuplantación, control de acceso a la red | 8.20, 8.21, 8.22 | V1, V2, V5 y V6 |
| Norma de criptografía | Cifrado en tránsito y en reposo, gestión de certificados y claves | 8.24 | V4 |
| Norma de registro y monitoreo | Qué se registra, cuánto se conserva, sincronización de relojes y revisión | 8.15, 8.16, 8.17 | V7 |
| Procedimiento de gestión de incidentes | Clasificación, funciones, plazos legales y plantillas de notificación | 5.24 a 5.28, 6.8 | Notificaciones tardías |
| Plan de continuidad y recuperación | Análisis de impacto, tiempos objetivo y pruebas | 5.29, 5.30, 8.13, 8.14 | Interrupción prolongada |
| Norma de cambios y configuración | Línea base segura, aprobación y trazabilidad de cada cambio | 8.9, 8.32 | Protecciones desactivadas sin que nadie lo sepa |
| Norma de seguridad con proveedores | Cláusulas, evaluación y acceso de terceros | 5.19 a 5.22 | Accesos de terceros sin control |
| Norma de seguridad física | Acceso a salas técnicas, cableado y tomas de red | 7.1 a 7.4, 7.8, 7.12 | V6 |
| Plan de formación y concienciación | Formación por perfil y simulaciones | 6.3 | Errores de configuración y de manejo |

*Tabla [[t:politicas]].* Políticas y normas internas propuestas, con los controles del Anexo A que desarrollan y la debilidad que habrían evitado. El Anexo B de este informe contiene el texto modelo de la política general.

## 7.6 Cómo previenen las políticas un incidente como este

Una política previene por cuatro vías, y las cuatro se ven en el caso.

La primera es que convierte una buena práctica en una obligación interna que se puede verificar. Activar la inspección de ARP es hoy una recomendación del fabricante que un administrador puede seguir o no. Si la norma de seguridad de redes la declara obligatoria en todos los conmutadores del centro de datos, su ausencia pasa a ser un incumplimiento que una auditoría detecta.

La segunda es que asigna responsables. Las definiciones del curso lo recogen: las políticas son "documentos formales que definen los procedimientos, normas y reglas que deben seguir los usuarios y los sistemas", y los controles administrativos "involucran a personas y sus responsabilidades" (Ochoa Agudelo, 2026d). Con un propietario de la red y otro del dato, la decisión de dejar una regla de acceso basada en la dirección IP tiene nombre y firma.

La tercera es que obliga a revisar. Una norma que exige revisar los accesos cada trimestre y probar la red una vez al año encuentra la desviación antes que el atacante.

La cuarta es que enlaza con la ley. El Real Decreto 43/2021 pide que la relación de medidas se formalice en una declaración de aplicabilidad incluida en la política de seguridad que aprueba la Dirección, y DORA exige que el órgano de dirección apruebe el marco de gestión del riesgo tecnológico. La política es el documento donde la obligación legal se vuelve decisión de la empresa.

Hay un límite que el caso también enseña. Una política guardada en un cajón no protege a nadie. En palabras del docente, la política "debe establecerse, comunicarse y mantenerse", y no basta con tenerla en un PDF que nadie conoce (Ochoa Agudelo, 2026c). Es muy probable que una compañía del tamaño de Mapfre tuviera una política de seguridad el 10 de marzo. Lo que faltaba era la comprobación de que la configuración real de la red la cumplía.

## 7.7 De la exigencia legal al control y a la evidencia

El docente propuso en clase conectar cada exigencia de la ley con el control tecnológico que la cumple, porque "la norma establece la responsabilidad y la tecnología ayuda a demostrar y ejecutar el control" (Ochoa Agudelo, 2026c). La Tabla [[t:exigencia]] aplica esa tabla al caso y le añade lo que pediría un auditor.

| Exigencia | Dónde se exige | Control en Mapfre | Evidencia para el auditor |
|---|---|---|---|
| Protección de la información | Art. 32.1.a del RGPD; art. 4 g de la Ley 1581 | Cifrado en tránsito y en reposo (C4, C7) | Parámetros de cifrado e inventario de certificados |
| Acceso autorizado | Art. 32 del RGPD; art. 9 de DORA | Gestión de identidades y accesos (C5) | Altas y bajas aprobadas; revisión trimestral |
| Control de usuarios | Art. 5.1.f del RGPD | Roles con mínimo privilegio (C5) | Matriz de roles vigente |
| Trazabilidad | Art. 33.5 del RGPD; art. 6 del RD 43/2021 | Registros de auditoría protegidos (C8, C9) | Registros, retención y verificación de integridad |
| Prevención de accesos | Art. 32 del RGPD | Doble factor y bastión para administradores (C5) | Informe de cobertura del doble factor |
| Protección de la infraestructura | Art. 9 de DORA; art. 6 del RD 43/2021 | Cortafuegos interno, segmentación y capa 2 (C1, C2, C3) | Reglas y configuración vigentes |
| Recuperación | Art. 32.1.c del RGPD; arts. 11 y 12 de DORA | Copias de seguridad y plan de recuperación (C12) | Informes de pruebas de restauración |
| Detección | Art. 10 de DORA | SIEM, sensor de red y monitoreo de la base de datos (C8) | Alertas generadas y atendidas |
| Gestión de riesgos | Art. 6 de DORA; numeral 6 de ISO/IEC 27001 | Metodología de riesgos y marco NIST | Registro de riesgos aprobado |
| Evidencia | Arts. 5.2 y 24 del RGPD | Auditoría interna e independiente (C15) | Informes de auditoría y plan de acciones |

*Tabla [[t:exigencia]].* De la exigencia legal al control tecnológico y a su evidencia, siguiendo la tabla dictada en clase.
