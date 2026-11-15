# 12. Actividad 9: afectación financiera

La guía pide estimar el impacto financiero del incidente, con los costos de recuperación y las multas, y listar los costos directos e indirectos. El enunciado habla de "pérdidas económicas significativas debido al fraude" sin dar cifras, y Mapfre no ha publicado ninguna porque el caso es un escenario de estudio. La estimación que sigue es propia. No pretende acertar un importe: busca el orden de magnitud y, sobre todo, saber qué partidas pesan más, que es lo que orienta dónde invertir.

## 12.1 Cómo se construye la estimación

El modelo trabaja con tres escenarios definidos por dos variables que el caso deja abiertas: cuántos clientes resultaron afectados y cuántos días duró la degradación del servicio (supuestos S5 y S7). El escenario bajo supone 50.000 afectados y un día; el base, 250.000 y tres días; el alto, un millón y siete días. Cada partida se calcula con un supuesto explícito, que figura en la tabla para que cualquiera pueda discutirlo o cambiarlo.

Llamo costos directos a los desembolsos que el incidente obliga a hacer de inmediato: la respuesta, las notificaciones, las compensaciones, el refuerzo técnico y las multas. Llamo indirectos a los efectos sobre el negocio, que llegan después y son más difíciles de atribuir: lo que se deja de ganar durante la parada, los clientes que se van y lo que cuesta recuperarlos.

## 12.2 Costos directos e indirectos

| Código | Concepto | Supuesto de cálculo | Bajo | Base | Alto |
|---|---|---|---|---|---|
| D1 | Respuesta al incidente y análisis forense | Equipo externo de respuesta y peritaje | 250 | 600 | 1.500 |
| D2 | Asesoría jurídica y gestión regulatoria | Notificaciones, requerimientos y defensa | 100 | 300 | 900 |
| D3 | Notificación a los afectados | 1,2 euros por afectado | 60 | 300 | 1.200 |
| D4 | Refuerzo del centro de atención al cliente | Personal y líneas adicionales | 150 | 400 | 1.000 |
| D5 | Servicio antifraude ofrecido a los clientes | 6 euros por cliente que lo acepta (10, 15 y 20 %) | 30 | 225 | 1.200 |
| D6 | Reembolso de fraudes a clientes | 0,05, 0,1 y 0,2 % de los afectados, con 1.800 euros de pérdida media | 45 | 450 | 3.600 |
| D7 | Refuerzo técnico urgente (red, cifrado y monitoreo) | Equipos, licencias y servicios de implantación | 400 | 1.200 | 3.000 |
| D8 | Auditorías de seguridad extraordinarias | Auditoría independiente y prueba de intrusión | 80 | 200 | 500 |
| D9 | Multa administrativa | Archivo, sanción media y sanción del orden de la impuesta a Generali | 0 | 1.500 | 5.000 |
| D10 | Franquicia y encarecimiento del ciberseguro | Franquicia del siniestro y subida de la prima | 50 | 250 | 750 |
| | **Subtotal de costos directos** | | **1.165** | **5.425** | **18.650** |
| I1 | Interrupción operativa | Margen no realizado por día de servicio degradado (1, 3 y 7 días) | 150 | 450 | 1.400 |
| I2 | Pérdida de clientes | Bajas del 0,5, 1,5 y 3 % de los afectados, con 120 euros de margen anual durante 3 años | 90 | 1.350 | 10.800 |
| I3 | Recaptación comercial y campaña de reputación | Campañas, incentivos a mediadores y comunicación | 100 | 600 | 2.500 |
| I4 | Reclamaciones e indemnizaciones | Indemnizaciones del artículo 82 del RGPD y litigios | 0 | 300 | 2.000 |
| | **Subtotal de costos indirectos** | | **340** | **2.700** | **16.700** |
| | **Total estimado** | | **1.505** | **8.125** | **35.350** |

*Tabla [[t:costos]].* Costos directos e indirectos del incidente en tres escenarios, en miles de euros. Estimación propia con supuestos explícitos; no son cifras de la compañía.

![](diagramas/08_impacto_financiero.png)

*Figura [[f:financiero]].* Costo total estimado por escenario y partidas del escenario base ordenadas de mayor a menor.

## 12.3 Qué dicen las cifras

El incidente cuesta entre 1,5 y 35,4 millones de euros según su alcance, con 8,1 millones en el escenario base. Equivale a entre 30 y 35 euros por cliente afectado en los tres escenarios. Como referencia externa, el informe anual de IBM sitúa en 4,99 millones de dólares el costo medio mundial de una brecha de datos y en 6,3 millones el del sector financiero, el segundo más alto de los que analiza (IBM, 2026). El escenario base queda en ese mismo orden de magnitud, lo que da cierta confianza en los supuestos.

Tres partidas concentran la mitad del escenario base: la multa (1,5 millones), la pérdida de clientes (1,35 millones) y el refuerzo técnico urgente (1,2 millones). Ninguna de las tres es el costo de responder al ataque. Son la sanción por no haber tenido medidas adecuadas, el precio de la confianza perdida y la inversión que se había aplazado.

El peso de los costos indirectos crece con la gravedad: representan el 23 % en el escenario bajo, el 33 % en el base y el 47 % en el alto. En el escenario alto la pérdida de clientes sola, con 10,8 millones, supera a cualquier otra partida y duplica la multa. Cuanto mayor es la brecha, más se parece el problema financiero a un problema de reputación, y por eso el capítulo siguiente trata la comunicación como una medida de contención de costos.

## 12.4 Costos de recuperación

La recuperación técnica en sentido estricto reúne tres partidas: la respuesta y el análisis forense, el refuerzo técnico urgente y las auditorías extraordinarias. Suman 730.000 euros en el escenario bajo, 2 millones en el base y 5 millones en el alto, cerca de una cuarta parte del total en el escenario base. Si se añade lo que cuesta atender a los afectados (notificación, centro de atención, servicio antifraude y reembolsos), la cifra del escenario base sube a 3,4 millones.

El refuerzo técnico urgente merece una observación. Es, en esencia, el plan de cierre de brechas del capítulo 10 ejecutado con prisa. Aun suponiendo que prevenir hubiera costado lo mismo, 1,2 millones, el incidente del escenario base cuesta casi siete veces más. El mismo informe de IBM calcula que las organizaciones que usan de forma amplia la automatización y la inteligencia artificial en sus operaciones de seguridad ahorran cerca de 2 millones de dólares por brecha (IBM, 2026), un dato que respalda la inversión en detección del capítulo 11.

## 12.5 Multas

El RGPD fija dos techos. Las infracciones de las obligaciones del responsable, entre ellas las medidas de seguridad del artículo 32 y las notificaciones de los artículos 33 y 34, pueden sancionarse con hasta 10 millones de euros o el 2 % del volumen de negocio anual mundial, la cifra que sea mayor (artículo 83.4). Las infracciones de los principios del artículo 5, incluido el de integridad y confidencialidad, llegan a 20 millones o el 4 % (artículo 83.5). Para un grupo que ingresó 34.501 millones de euros en 2025 (MAPFRE, 2026d), esos porcentajes equivalen a 690 y 1.380 millones. Son techos teóricos. Las sanciones reales en España quedan muy por debajo, como muestra la Tabla [[t:multas]].

| Referencia | Hechos | Resultado |
|---|---|---|
| Techo legal del RGPD | Infracción del artículo 5 o de los artículos 25, 32, 33 y 34 | Hasta 20 millones de euros o el 4 % del volumen de negocio; hasta 10 millones o el 2 % |
| Generali España | Ciberataque de 2022 con filtración de datos de antiguos clientes | Multa de 5 millones de euros, reducida a 4 millones por pronto pago, por los artículos 5.1.f, 25, 32 y 35 del RGPD (Europa Press, 2025) |
| Mapfre España | Ataque con programa de secuestro en agosto de 2020 | Archivo de las actuaciones sin sanción: la compañía tenía medidas razonables y reaccionó con diligencia (AEPD, 2021) |

*Tabla [[t:multas]].* Techo legal y dos precedentes españoles en el sector asegurador.

Los dos precedentes son del mismo sector y tienen resultados opuestos. La diferencia no está en la gravedad del ataque. Está en lo que la autoridad encontró al investigar: medidas previas adecuadas, detección rápida, notificación en plazo y transparencia en un caso; deficiencias en la seguridad y en la evaluación de impacto en el otro. Por eso el modelo usa 0, 1,5 y 5 millones como multa de cada escenario. La ley orgánica española añade criterios para graduar la sanción, como el carácter continuado de la infracción o la vinculación de la actividad del infractor con el tratamiento de datos (artículo 76 de la LOPDGDD), y este último pesa en contra de una aseguradora, cuyo negocio consiste en tratar datos personales.

Si la base de datos fuera de una filial colombiana, la Superintendencia de Industria y Comercio podría imponer multas de hasta 2.000 salarios mínimos mensuales, sucesivas mientras persista el incumplimiento, además de suspender las actividades de tratamiento hasta por seis meses (artículo 23 de la Ley 1581 de 2012).

## 12.6 Lo que el modelo no cuantifica

Cuatro efectos quedan fuera de la tabla porque no hay base razonable para ponerles cifra. El primero es la reacción de la cotización, que afecta al valor de la compañía y no a su cuenta de resultados. El segundo es el costo de oportunidad: durante meses, la dirección y los equipos de tecnología dedican a la crisis el tiempo que tenían para otros proyectos. El tercero es el mayor escrutinio del supervisor, con requerimientos e inspecciones que consumen recursos durante años. El cuarto es el efecto sobre los mediadores, que pueden desviar negocio hacia otras compañías si sus clientes desconfían. Todos empujan el costo real por encima de la estimación.
