# 15. Actividad 12: divulgación de acceso no autorizado a información confidencial

La guía pregunta qué pasos legales y operativos deben darse cuando se ha divulgado un acceso no autorizado a información confidencial, y pide explicar los procedimientos legales y cómo puede la empresa protegerse de futuras filtraciones.

## 15.1 Qué es, en términos jurídicos, lo que ocurrió

El incidente tiene tres calificaciones simultáneas y cada una abre un procedimiento distinto.

Es una violación de la seguridad de los datos personales, que el RGPD define como toda violación de la seguridad que ocasione la destrucción, pérdida o alteración de datos personales, o la comunicación o el acceso no autorizados a ellos (artículo 4.12). Esa calificación activa las obligaciones de los artículos 33 y 34.

Es también, con mucha probabilidad, un incidente grave relacionado con las TIC en el sentido de DORA, por el número de clientes afectados, la pérdida de confidencialidad de los datos y el impacto económico. Esa calificación obliga a notificar al supervisor de seguros.

Y es un delito del que la compañía es víctima: acceso ilícito a un sistema de información e interceptación de transmisiones de datos, tipificados en el artículo 197 bis del Código Penal.

## 15.2 Pasos legales

La Tabla [[t:legal]] ordena los pasos, con su destinatario, su plazo y la norma que los impone. La Figura [[f:legal]] muestra las decisiones que llevan a cada uno.

| Paso | Ante quién | Plazo | Norma |
|---|---|---|---|
| 1. Registrar la violación, sus efectos y las medidas, y evaluar el riesgo para las personas | Registro interno, a cargo del delegado de protección de datos | Inmediato | Artículo 33.5 del RGPD |
| 2. Notificar la violación: naturaleza, categorías y número aproximado de afectados y de registros, consecuencias probables, medidas adoptadas y contacto del delegado | Agencia Española de Protección de Datos | 72 horas desde que se tiene constancia; puede hacerse por fases si falta información | Artículo 33 del RGPD |
| 3. Comunicar la violación a los afectados en lenguaje claro | Clientes afectados | Sin dilación indebida, si es probable un alto riesgo | Artículo 34 del RGPD |
| 4. Notificar el incidente grave | Dirección General de Seguros y Fondos de Pensiones | Notificación inicial en 4 horas desde la clasificación y a más tardar 24 horas desde que se conoce; informe intermedio a las 72 horas de la inicial; informe final en un mes | Artículo 19 de DORA y artículo 5 del Reglamento Delegado (UE) 2025/301 |
| 5. Denunciar los hechos y aportar las evidencias | Policía Nacional o Guardia Civil | Cuanto antes | Artículos 197 bis y 249 del Código Penal |
| 6. Avisar al equipo de respuesta de referencia | INCIBE-CERT | Obligatorio si la compañía es operador de servicios esenciales; voluntario en otro caso | Artículo 19 del Real Decreto-ley 12/2018 |
| 7. Valorar si el incidente es información privilegiada y, en su caso, difundirla | Supervisor del mercado de valores | Tan pronto como sea posible | Artículo 17 del Reglamento (UE) 596/2014 |
| 8. Avisar a los terceros con obligación contractual | Encargados del tratamiento, reaseguradores y aseguradora del ciberriesgo | Según cada contrato | Artículos 28 y 33.2 del RGPD |
| 9. Atender las solicitudes y reclamaciones de los afectados | Clientes | Un mes para responder al ejercicio de derechos | Artículos 12 y 82 del RGPD |

*Tabla [[t:legal]].* Pasos legales tras la violación de datos, con destinatario, plazo y norma.

![](diagramas/10_flujo_legal.png)

*Figura [[f:legal]].* Decisiones y plazos de notificación tras detectar la violación de datos.

Tres observaciones sobre la tabla.

Los relojes son distintos y corren a la vez. El plazo más corto es el del supervisor financiero: cuatro horas desde que el incidente se clasifica como grave, muy por debajo de las 72 horas de protección de datos. Un procedimiento interno que solo tenga presente el plazo de 72 horas llega tarde a la primera obligación.

La comunicación a los clientes del paso 3 admite una excepción que interesa para el futuro. No es necesaria si el responsable había aplicado medidas que hacen los datos ininteligibles para quien no esté autorizado, como el cifrado (artículo 34.3.a). En el caso los datos viajaban en claro, de modo que la excepción no aplica y hay que comunicar.

No cumplir estos pasos es en sí una infracción. La ley orgánica española tipifica como grave no notificar la violación a la autoridad o no comunicarla al afectado cuando procede, y como leve notificarla tarde o de forma incompleta (artículos 73 y 74 de la LOPDGDD). El precedente de 2020 enseña el camino contrario: la compañía avisó al supervisor de seguros y a los equipos nacionales de respuesta al día siguiente del ataque, notificó a la Agencia al segundo día y presentó denuncia al tercero, y la resolución calificó esa actuación de "diligente reacción" (AEPD, 2021).

En Colombia los pasos equivalentes serían informar a la Superintendencia de Industria y Comercio (artículo 17 n de la Ley 1581 de 2012) mediante el reporte del incidente en el Registro Nacional de Bases de Datos dentro de los quince días hábiles siguientes a su detección, avisar a los titulares, denunciar ante la Fiscalía los delitos de acceso abusivo, interceptación de datos informáticos y violación de datos personales (artículos 269A, 269C y 269F de la Ley 1273 de 2009) y reportar el incidente a la Superintendencia Financiera conforme a sus circulares de ciberseguridad.

## 15.3 Pasos operativos

Los pasos legales dependen de que la operación haga bien los suyos. Son siete.

1. Contener sin destruir la evidencia. Se aísla el segmento y no se apagan ni se reinstalan los equipos hasta tener su imagen forense. La adquisición sigue el orden de volatilidad, calcula el hash de cada imagen y abre la cadena de custodia desde el primer momento (Ochoa Agudelo, 2026e). Sin esa cadena, la denuncia del paso 5 pierde valor.
2. Determinar el alcance. Hay que saber qué datos se vieron, de cuántos clientes y desde cuándo. Esa información la piden tanto la Agencia como el supervisor de seguros, y sale de los registros de la red y de la base de datos. Es el momento en que se paga o se cobra la calidad del monitoreo.
3. Cambiar credenciales y certificados y cerrar las sesiones abiertas de todas las cuentas que circularon por el segmento.
4. Proteger a los clientes del uso de sus datos. El atacante conoce nombre, dirección, documento y póliza, que son justo los datos con que un centro de atención suele verificar la identidad de quien llama. Mientras dure el riesgo, las operaciones sensibles, como un cambio de beneficiario o de cuenta de cobro, exigen una verificación reforzada por un segundo canal.
5. Vigilar la aparición de los datos en foros y mercados ilegales y las campañas de fraude que usen el nombre de la compañía.
6. Documentar cada decisión en la bitácora del incidente, con hora y responsable. Es el registro que exige el artículo 33.5 y la base del informe final a los supervisores.
7. Cerrar con lecciones aprendidas, la última fase del procedimiento de respuesta que enseña el curso, con el análisis de lo que faltó para evitar la reincidencia.

## 15.4 Cómo protegerse de futuras filtraciones

La protección tiene una parte técnica, una organizativa y una jurídica.

En lo técnico, los controles del capítulo 9 atacan la filtración en tres puntos. Impiden que el atacante llegue a los datos (segmentación, control de acceso a la red y mínimo privilegio). Impiden que los lea si llega (cifrado en tránsito, cifrado por campo y enmascaramiento). Y detectan la salida (monitoreo de la base de datos y prevención de fuga). El segundo punto tiene además el efecto legal ya comentado: con los datos cifrados, la violación puede no requerir comunicación a los afectados.

En lo organizativo, la medida más barata es tener menos datos. El principio de limitación del plazo de conservación obliga a suprimir los datos que ya no son necesarios, y el control 8.10 del Anexo A pide un procedimiento para hacerlo. El precedente de Generali es ilustrativo, porque los datos filtrados eran de antiguos clientes (Europa Press, 2025). A eso se suman la evaluación de impacto del tratamiento de datos de vida (artículo 35 del RGPD), la protección de datos desde el diseño en cada sistema nuevo (artículo 25) y la formación de quienes manejan los datos.

En lo jurídico, tres piezas. Contratos de encargado del tratamiento con cláusulas de seguridad, derecho de auditoría y obligación de avisar sin demora (artículo 28 del RGPD). Un procedimiento de notificación con plantillas preparadas y ensayado en simulacros, para que los plazos de 4, 24 y 72 horas se cumplan sin improvisar. Y una póliza de ciberriesgo que cubra los costos de respuesta y las reclamaciones.

Ante un auditor, este capítulo se acredita con el registro interno de violaciones, los justificantes de cada notificación con su hora, el informe forense con la cadena de custodia y las actas del Comité de Crisis.
