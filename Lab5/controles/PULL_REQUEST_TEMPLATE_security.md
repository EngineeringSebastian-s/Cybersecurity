## Caso

- **Origen:** <!-- Snyk Open Source / Snyk Code / Snyk Container / Snyk IaC / CodeQL / Dependabot / cargo-audit / secret scanning, con número de alerta o Finding ID -->
- **Identificadores:** <!-- CVE, CWE, ID de Snyk -->
- **Severidad reportada y vector CVSS 3.1:**
- **Riesgo real en SmartPot:** <!-- alcanzabilidad, condiciones, activo expuesto, impacto C/I/D -->

## Causa raíz

<!-- defecto de diseño, implementación, configuración o dependencia; archivo y líneas -->

## Cambio

<!-- estrategia y por qué corrige la causa raíz y no solo el síntoma -->

## Verificación (obligatoria)

- [ ] Reescaneo con la misma herramienta que reportó el hallazgo, pegando el resumen **antes** y **después**.
- [ ] Si el hallazgo vive en una imagen: escaneo de la imagen construida (`snyk container test`), no solo del manifiesto.
- [ ] Pruebas del repositorio en verde (unitarias, `validate.sh`, E2E según el servicio).
- [ ] Si una corrección propuesta por un agente de IA no hizo desaparecer el hallazgo, se documenta y se descarta.
- [ ] Sin secretos en el diff; `[skip deploy]` si no debe desplegarse.

> Lección del Lab5: #8 de SmartPot-DB-Postgre se fusionó con «18/18 en validate.sh» pero sin reescanear; las 117
> alertas de `gosu` siguieron abiertas hasta esta auditoría.
