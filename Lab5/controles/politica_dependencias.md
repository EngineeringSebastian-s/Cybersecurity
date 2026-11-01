# Política de actualización y control de dependencias de SmartPot

Propuesta derivada del Laboratorio 5. Formaliza lo que ya se hace en la organización y cierra los huecos encontrados.

## 1. Fuentes de alerta

| Fuente                         | Alcance                                              | Frecuencia                          |
| ------------------------------ | ---------------------------------------------------- | ----------------------------------- |
| Dependabot (version + security) | Maven, Go modules, npm/pnpm, uv, Cargo, Actions, Docker | Semanal por repositorio            |
| Snyk Open Source + `snyk monitor` | Dependencias resueltas de cada servicio             | En cada PR, en cada push a `main` y semanal |
| Snyk Container                 | Imagen construida (no el manifiesto)                 | En cada PR que toque el `Dockerfile` |
| Snyk IaC                       | `docker/**` y `kubernetes/**` de `.github`           | En cada PR y antes de desplegar     |
| cargo-audit                    | Firmware y simulador en Rust                         | En cada PR y semanal                |

## 2. Plazos de corrección (SLA)

El plazo sale del riesgo real, no solo de la severidad del escáner: severidad × alcanzabilidad × exposición.

| Severidad | Alcanzable o expuesto a Internet | No alcanzable o solo en herramientas locales |
| --------- | -------------------------------- | ------------------------------------------- |
| Crítica   | 48 horas                         | 7 días                                      |
| Alta      | 7 días                           | 30 días                                     |
| Media     | 30 días                          | siguiente ciclo de mantenimiento            |
| Baja      | siguiente ciclo                  | aceptación documentada                      |

## 3. Reglas

1. Un PR por causa raíz, desde `security/<origen>/<problema>`, con la plantilla de seguridad y el reescaneo pegado.
2. Los pins de seguridad (`jackson-bom.version`, `logback.version`, `toolchain`) llevan comentario con motivo y
   condición de retiro; Dependabot los revisa cada semana.
3. Los ignores en `.snyk` llevan `reason` con la mitigación concreta y `expires` (máximo 12 meses).
4. Las versiones mayores (Java 25, Python 3.15, TimescaleDB 2.31) no se fusionan desde Dependabot sin un PR propio que
   ajuste imagen, CI y migraciones.
5. Las acciones de GitHub se fijan por SHA cuando reciben secretos (`snyk/actions/setup`).
6. Un workflow que despliega a producción no se dispara a sí mismo al cambiar (incidente evitado el 2026-11-01).
7. El cumplimiento se verifica sobre el artefacto publicado: imagen en GHCR y, para Java, el contenido real del JAR.
