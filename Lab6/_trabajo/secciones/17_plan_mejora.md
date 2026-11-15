# 17. Plan integrado de mejora y tratamiento de riesgos

Los capítulos anteriores responden cada actividad por separado. Este los une en un solo plan, con responsables, plazos e indicadores, y lo somete al ciclo de mejora que exige la norma.

## 17.1 Seis preguntas para saber si hay un sistema de gestión

Al cerrar la clase sobre ISO/IEC 27001, el docente dejó una pregunta que sirve de criterio de evaluación: "¿la organización conoce sus riesgos, ha decidido cómo tratarlos, ha implementado controles adecuados, puede demostrar que funcionan, los audita y los mejora?" (Ochoa Agudelo, 2026c). La Tabla [[t:seispreguntas]] compara la situación que el caso deja entrever el 10 de marzo con la que resulta del plan. La columna central es una inferencia a partir del enunciado.

| Pregunta | Situación el 10 de marzo | Con el plan | Capítulo |
|---|---|---|---|
| ¿Conoce sus riesgos? | El riesgo de la red interna no estaba valorado | Registro de diez riesgos, cada uno con propietario | 8 |
| ¿Ha decidido cómo tratarlos? | Sin plan de tratamiento para esos riesgos | Opción de tratamiento y controles por riesgo, con residual aceptado | 8 |
| ¿Ha implementado controles adecuados? | Protección hacia el exterior; el interior de la red sin proteger | Dieciséis controles y una declaración de aplicabilidad | 9 y 10 |
| ¿Puede demostrar que funcionan? | La detección fue posterior al acceso | Evidencia e indicador para cada control | 9 y 11 |
| ¿Los audita? | Las vulnerabilidades V1 a V5 no se habían encontrado | Pruebas de intrusión internas y auditoría interna | 10 |
| ¿Los mejora? | Sin datos | Ciclo de mejora con revisión por la Dirección | 17 |

*Tabla [[t:seispreguntas]].* Las seis preguntas de un sistema de gestión, antes y después del plan.

## 17.2 Líneas de mejora

La Tabla [[t:plan]] agrupa las propuestas del informe en nueve líneas. Los plazos se cuentan desde la detección del incidente.

| Línea | Acciones | Responsable | Plazo | Indicador de éxito |
|---|---|---|---|---|
| 1. Gobierno | Aprobar la política y las normas internas, designar propietarios de activos y de riesgos y reunir un comité de seguridad cada trimestre | Dirección General y CISO | 30 días | Política aprobada y comunicada a toda la plantilla |
| 2. Red interna | Ejecutar el plan de cierre de brechas: capa 2, segmentación, filtrado antisuplantación y control de acceso a la red | Área de Redes | 90 días | Todos los puertos protegidos; prueba de intrusión sin hallazgos críticos |
| 3. Identidad y datos | Autenticación con certificado, mínimo privilegio, cifrado por campo y enmascaramiento | Dirección de Tecnología | 90 días | Todas las conexiones a la base de datos con TLS mutuo; ninguna cuenta con privilegios excesivos |
| 4. Detección | Casos de uso en el SIEM, almacén inmutable de registros y relojes sincronizados | SOC | 30 días | Detección de los casos críticos en menos de 15 minutos |
| 5. Respuesta y notificación | Procedimiento de incidentes, plantillas para cada autoridad y simulacros | CISO y delegado de protección de datos | 60 días | Todas las notificaciones dentro de plazo en los simulacros |
| 6. Continuidad | Análisis de impacto, plan de recuperación y calendario de pruebas | Dirección de Operaciones y Dirección de Tecnología | 120 días | Tiempos objetivo alcanzados en la prueba |
| 7. Integridad de los datos | Auditoría de cambios con doble validación, conciliación diaria y confirmación al cliente | Dirección de Operaciones | 90 días | Ningún cambio crítico sin tique |
| 8. Personas y terceros | Formación por perfil, cláusulas de seguridad con proveedores y póliza de ciberriesgo | Recursos Humanos y Asesoría Jurídica | 180 días | Personal formado y proveedores críticos evaluados |
| 9. Verificación | Auditoría interna, revisión por la Dirección, actualización de la declaración de aplicabilidad y certificación del alcance | Auditoría Interna | 180 días para la auditoría; 12 meses para la certificación | Certificación ISO/IEC 27001 del servicio |

*Tabla [[t:plan]].* Plan integrado de mejora, con responsable, plazo e indicador de éxito.

Las líneas 1 y 4 van primero porque condicionan a las demás. Sin propietarios no hay quien apruebe los cambios ni quien acepte el riesgo residual, y sin detección no se puede comprobar que los controles nuevos funcionan.

## 17.3 El ciclo de mejora

La norma ISO/IEC 27001 se apoya en el ciclo de planificar, hacer, verificar y actuar (NQA, s. f.), y el plan lo sigue.

Planificar es lo que hacen el análisis de riesgos, la declaración de aplicabilidad y este plan. Hacer es implantar los controles y cerrar las brechas en los plazos fijados. Verificar tiene tres instrumentos, que son los del numeral 9 de la norma: el seguimiento y la medición con los indicadores de los capítulos 9 y 11, que se revisan cada mes; la auditoría interna, una vez al año, y la revisión por la Dirección, semestral durante el primer año. Actuar es tratar cada desviación como una no conformidad: se identifica, se corrige, se analiza su causa, se aplica una acción correctiva y se comprueba su eficacia.

Sobre la auditoría interna conviene retener lo que se dijo en clase: no consiste en buscar culpables, consiste en obtener evidencia para determinar si el sistema cumple los requisitos y funciona, con objetividad e imparcialidad (Ochoa Agudelo, 2026c). Si la auditoría se vive como una caza de responsables, los equipos ocultan los problemas, y un problema oculto en la configuración de la red es exactamente lo que originó este incidente.

## 17.4 Lo que el plan consigue y lo que deja pendiente

El plan baja la suma de las puntuaciones de riesgo de 181 a 61 y deja los diez riesgos dentro del criterio de aceptación. En términos económicos, su costo técnico es del orden de la partida de refuerzo urgente del capítulo 12, mientras que el incidente cuesta varias veces más en cualquiera de los escenarios.

Quedan ocho riesgos residuales de nivel medio. Sus propietarios los aceptan por escrito y se revisan al año, o antes si cambia la arquitectura o hay otro incidente. La revisión por la Dirección decide entonces si el nivel sigue siendo asumible. Queda también abierto el alcance: este trabajo cubre el servicio de pólizas de vida, y la misma red plana puede existir en otros servicios de la compañía. La primera recomendación a la Dirección es extender el análisis al resto del centro de datos.
