# Guía de ejecución — Laboratorio 2: WordPress y `wp-cron.php`

**Práctica integradora Kali Linux #3 — Diplomado en Ciberseguridad**
Prueba **controlada** de disponibilidad y análisis de resiliencia (sustituto de `cron-kill`).

> **Alcance y autorización.** Esta sección es una **prueba de carga y análisis de resiliencia en
> laboratorio** contra un contenedor WordPress **local propio** (`http://localhost`), desplegado por ti
> con Docker. No es una guía para afectar servicios reales. Según la regla ética de la práctica, **cada
> resultado debe ir acompañado de su mitigación defensiva**. El objetivo pedagógico es observar la
> relación entre **concurrencia, recursos y disponibilidad**, no maximizar el daño.

> **Sustituto de `cron-kill` (indicación del docente).** La máquina `cron-kill` ya no está disponible.
> En su lugar se despliega WordPress con el `docker-compose.yaml` entregado por el profesor. Cambia el
> **despliegue** y la **URL** (`http://localhost` en vez de `172.17.0.2`); el resto de la práctica queda
> **igual**: al ejecutar la prueba de carga, las estadísticas de rendimiento se verán elevadas y el sitio
> dejará de responder por la saturación de peticiones.

---

## Cómo usar este documento

- Necesitarás **dos terminales**: una para la prueba de carga y otra para el monitoreo en vivo.
- El `docker-compose.yaml` ya está en esta carpeta (`Lab3/`).
- Nombra tus capturas con el código `L2-XX` para mapearlas a las "Figura X" del informe.

### Mapa de capturas (resumen)

| Código | Fase | Qué captura |
|--------|------|-------------|
| L2-01 | Despliegue | `docker compose up -d` + contenedores arriba |
| L2-02 | Verificación web | `http://localhost` respondiendo (línea base) |
| L2-03 | Exposición wp-cron | `http://localhost/wp-cron.php` accesible |
| L2-04 | Monitoreo previo | `docker stats` / `top` en reposo (línea base de recursos) |
| L2-05 | Prueba de carga | Salida de ApacheBench (`ab`) |
| L2-06 | Monitoreo durante | `docker stats` con CPU/MEM elevadas |
| L2-07 | Efecto visible | Navegador lento / sin respuesta |
| L2-08 | Recuperación | Servicio recuperado tras finalizar la prueba |

---

## Fase 0 — Preparación

Herramientas necesarias en Kali: el plugin de Docker Compose y ApacheBench (`ab`).

```bash
cd ~/Documentos/.../Lab3     # ubícate donde está el docker-compose.yaml
ls docker-compose.yaml       # confirma que existe

sudo systemctl start docker
sudo apt update
sudo apt install -y docker-compose-plugin apache2-utils
```

- `docker-compose-plugin` habilita `docker compose` (v2, con espacio).
- `apache2-utils` aporta `ab` (ApacheBench), la herramienta de prueba de carga.

> Si tu Kali solo tiene el binario antiguo, el equivalente es `docker-compose` (con guion, v1). En esta
> guía se usa `docker compose` (v2); si usas v1, reemplaza mentalmente los comandos.

### Qué hace el `docker-compose.yaml` (para explicar en el informe)

- Levanta dos servicios: `db` (MySQL 5.7) y `wordpress` (imagen oficial, puerto `80:80`).
- El servicio `wordpress` tiene **límites de recursos**: `cpus: '0.50'` y `memory: 512M`.
- Ese límite es el **aislamiento del laboratorio**: al estar acotado a medio núcleo y 512 MB, el
  contenedor **satura rápido y de forma visible** durante la prueba, sin comprometer tu equipo anfitrión.

---

## Fase 1 — Despliegue del contenedor WordPress

```bash
sudo docker compose up -d
sudo docker compose ps
sudo docker ps
```

- **Propósito:** desplegar WordPress + base de datos en segundo plano (`-d`).
- **Qué esperar:** dos contenedores en estado `Up` (nombres tipo `lab3-wordpress-1` y `lab3-db-1`),
  con el puerto `0.0.0.0:80->80/tcp` publicado.

**📸 Captura L2-01** — despliegue y contenedores arriba con la IP/puerto. *(Aprendizaje: aislamiento del laboratorio.)*

---

## Fase 2 — Verificación web (línea base de disponibilidad)

```bash
curl -I http://localhost
```

Abre también `http://localhost` en el navegador.

- **Primera vez:** WordPress mostrará el **instalador** (`/wp-admin/install.php`). Complétalo (elige
  idioma, título del sitio, usuario y contraseña de administrador). Esto deja el sitio operativo y hace
  que `wp-cron.php` tenga tareas reales que procesar, de modo que la saturación sea más evidente.
- **Propósito:** confirmar que el servicio responde **antes** de la prueba (tu punto de comparación).

**📸 Captura L2-02** — página de WordPress visible / cabecera `HTTP/1.1 200 OK`. *(Aprendizaje: línea base de disponibilidad.)*

---

## Fase 3 — Exposición de `wp-cron.php`

```bash
curl -I http://localhost/wp-cron.php
```

Ábrelo también en el navegador: `http://localhost/wp-cron.php` (se verá una **página en blanco**, lo
cual es normal: el endpoint responde y ejecuta tareas programadas).

- **Propósito:** comprobar que el pseudo-cron de WordPress es **accesible públicamente** y entender su
  función. WordPress usa `wp-cron.php` para ejecutar tareas programadas **en cada visita**; expuesto a
  ejecución repetida, se convierte en un vector de **consumo excesivo de recursos**.

**📸 Captura L2-03** — respuesta del endpoint `wp-cron.php`. *(Aprendizaje: exposición pública de procesos internos.)*

---

## Fase 4 — Monitoreo previo (línea base de recursos)

*(Deja esta terminal abierta y visible durante toda la prueba.)*

```bash
sudo docker stats
#   (o, para ver el sistema completo:)   top      # o   htop
```

- **Propósito:** registrar CPU y memoria **en reposo**, antes de la carga.
- **Qué esperar:** el contenedor `wordpress` con un uso de CPU bajo (cercano a 0 %) y memoria estable.

**📸 Captura L2-04** — `docker stats` / `top` en reposo. *(Aprendizaje: medición antes/después.)*

---

## Fase 5 — Prueba de carga controlada (núcleo del laboratorio)

*(En la segunda terminal, mientras `docker stats` sigue visible en la primera.)*

```bash
ab -n 5000 -c 50 -k -H "Accept-Encoding: gzip, deflate" http://localhost/wp-cron.php
```

- **Propósito:** ApacheBench envía solicitudes HTTP **controladas** al endpoint de tu laboratorio.
  - `-n 5000` → total de solicitudes.
  - `-c 50` → concurrencia (solicitudes simultáneas).
  - `-k` → mantiene conexiones abiertas (keep-alive).
  - `-H "Accept-Encoding: gzip, deflate"` → añade una cabecera HTTP.
- **Qué interpretar en la salida:** `Requests per second`, `Time per request`, `Failed requests` y los
  tiempos de respuesta. Observa si aparecen fallos, lentitud o saturación.

> **Equipo con pocos recursos.** Usa la versión reducida que sugiere la guía:
> ```bash
> ab -n 300 -c 10 http://localhost/wp-cron.php
> ```
> La finalidad es observar la relación concurrencia–recursos–disponibilidad, **no** maximizar el daño.

**📸 Captura L2-05** — salida completa de `ab`. *(Aprendizaje: agotamiento de recursos.)*

---

## Fase 6 — Monitoreo durante la prueba

Mientras `ab` se ejecuta, mira la terminal de `docker stats`:

- **Qué esperar:** el contenedor `wordpress` dispara su **CPU** (tiende al límite de 0.5 núcleo → se ve
  saturado) y sube el uso de **memoria**. Relaciona esa subida con la concurrencia (`-c`) de la prueba.

**📸 Captura L2-06** — `docker stats` con CPU/MEM elevadas durante la carga. *(Aprendizaje: impacto operacional.)*

---

## Fase 7 — Efecto visible sobre la disponibilidad

Con la prueba todavía en curso (o repitiéndola), intenta abrir/recargar `http://localhost` en el navegador.

- **Qué esperar:** la página carga **lenta**, se queda "esperando a localhost" o **no responde**. Esa es
  la evidencia de afectación de **disponibilidad** (denegación de servicio reproducida en laboratorio).

**📸 Captura L2-07** — navegador lento/bloqueado/sin respuesta. *(Aprendizaje: denegación de servicio en laboratorio.)*

---

## Fase 8 — Recuperación

Al terminar `ab`, el servicio debería volver a responder. Verifícalo:

```bash
curl -I http://localhost
```

Si quedó degradado, reinicia el servicio:

```bash
sudo docker compose restart wordpress
# o reinicia todo el stack:
sudo docker compose restart
```

**📸 Captura L2-08** — servicio recuperado (`HTTP/1.1 200 OK` / página de nuevo visible). *(Aprendizaje: resiliencia y continuidad.)*

> **📸 Captura L2-09 (opcional, recomendada).** Vuelve a mirar `docker stats` ya recuperado: el uso de
> CPU/MEM regresa a la línea base. Con esto cierras el ciclo **antes (L2-04) → durante (L2-06) → después**,
> que es justo lo que puntúa el criterio "medición antes/después".

### Limpieza (al finalizar la práctica)

```bash
sudo docker compose down        # detiene y elimina los contenedores
sudo docker compose down -v     # además elimina el volumen de datos (db_data)
```

---

## Fase 9 — Mitigaciones (obligatorio en el informe)

Cada hallazgo debe cerrarse con su control defensivo:

| Control defensivo | Qué previene | Cómo explicarlo en el informe |
|-------------------|--------------|-------------------------------|
| Deshabilitar el pseudo-cron público y usar **cron real** del servidor | Que cada visita dispare tareas costosas | `define('DISABLE_WP_CRON', true);` en `wp-config.php` y una tarea `cron` del sistema que llame a `wp-cron.php` por horario controlado |
| **Rate limiting** en servidor web / proxy / WAF | Peticiones repetitivas desde una misma fuente | Límites por IP, por ruta y por intervalo de tiempo |
| **Restringir el acceso** a `wp-cron.php` cuando aplique | Exposición directa del endpoint | Validar que no rompa tareas legítimas del sitio |
| **Monitoreo** de logs, CPU, RAM y errores HTTP | Detectar saturación temprana | Indicadores: `5xx`, latencia, CPU/mem altas, conexiones simultáneas |
| **Caché**, CDN y endurecimiento de WordPress | Reducir carga dinámica | No sustituye la corrección de configuración, pero mejora la resiliencia |

## Extras — perfil avanzado (opcional)

> **Mismo alcance:** contenedor WordPress **local** (`http://localhost`). Enfoque de **resiliencia y
> medición**, no de maximizar la carga (misma intensidad del laboratorio). Capturas con código `L2-A#`.

### A. Espacio de trabajo
```bash
mkdir -p ~/lab3-wp/{logs,ab,shots}
cd ~/lab3-wp
```

### B. Línea base medible con curl (objetiva)
```bash
cat > curl-format.txt <<'EOF'
tiempo_conexion: %{time_connect}s
ttfb:            %{time_starttransfer}s
tiempo_total:    %{time_total}s
codigo_http:     %{http_code}
EOF
curl -w "@curl-format.txt" -o /dev/null -s http://localhost/ | tee logs/baseline.txt
curl -s -o /dev/null -w "%{http_code} %{time_total}s\n" http://localhost/wp-cron.php
```
- **Por qué (pro):** mide TTFB y tiempo total de forma objetiva, no solo "se siente lento".

**📸 L2-A1** — métricas curl en reposo.

### C. Reconocimiento del WordPress con wpscan
```bash
wpscan --url http://localhost --no-update --enumerate vp,u    # versión, plugins vulnerables, usuarios
```
- **Por qué:** `wpscan` es el escáner estándar de WordPress; enumera versión, plugins y usuarios = superficie de ataque del sitio (token de API opcional solo para datos de CVE).

**📸 L2-A2** — salida de wpscan.

### D. Monitoreo continuo a CSV (serie temporal antes/durante/después)
```bash
CID=$(docker compose ps -q wordpress)
( echo "ts,cpu,mem"; while true; do \
    echo "$(date +%T),$(docker stats --no-stream --format '{{.CPUPerc}},{{.MemPerc}}' $CID)"; \
    sleep 2; done ) | tee logs/stats.csv
```
- **Por qué (pro):** genera una **serie temporal** de CPU/memoria graficable (antes→durante→después), muy superior a una sola captura. (Déjalo corriendo en una terminal aparte durante la prueba; corta con `Ctrl+C`.)

**📸 L2-A3** — stats.csv poblándose durante la prueba.

### E. Prueba de carga con datos graficables + corroboración con otra herramienta
```bash
# ApacheBench guardando datos crudos (-g) y percentiles de latencia (-e):
ab -n 5000 -c 50 -k -g ab/ab.tsv -e ab/ab_percentiles.csv http://localhost/wp-cron.php | tee ab/ab_resumen.txt
# Corroborar con wrk (otra herramienta = rigor metodológico; si falta: sudo apt install wrk):
wrk -t4 -c50 -d30s http://localhost/wp-cron.php | tee logs/wrk.txt
```
- **Por qué:** `-g/-e` dejan datos para graficar latencias; `wrk` confirma el resultado con una herramienta distinta.

**📸 L2-A4** — ab con percentiles. **📸 L2-A5** — wrk.

### F. Evidencia desde los logs del servidor
```bash
docker compose logs --since 5m wordpress > logs/wp_container.log
docker compose exec wordpress sh -c "tail -n 40 /var/log/apache2/access.log 2>/dev/null"
docker compose exec wordpress sh -c "tail -n 40 /var/log/apache2/error.log  2>/dev/null"
```
- **Por qué:** correlaciona la saturación con las peticiones/errores reales (5xx, timeouts) = "monitoreo de logs" de la tabla de mitigación.

**📸 L2-A6** — tormenta de peticiones en el access.log.

### G. Validación de la mitigación (antes/después) — el paso que más suma
```bash
# Desactiva el pseudo-cron público (añade la constante tras <?php en wp-config.php):
docker compose exec wordpress bash -c 'grep -q DISABLE_WP_CRON wp-config.php || sed -i "1a define(\"DISABLE_WP_CRON\", true);" wp-config.php'
# Repite la MISMA prueba y compara el consumo con el de la fase 6:
ab -n 5000 -c 50 -k http://localhost/wp-cron.php | tee ab/ab_mitigado.txt
```
- **Por qué (pro):** demuestra **empíricamente** que la mitigación funciona (la CPU ya no se dispara igual). Eleva directamente el criterio "Análisis de riesgos y mitigación" (20 pts). *(Para revertir: quita esa línea del `wp-config.php`.)*

**📸 L2-A7** — comparación de CPU/stats con `DISABLE_WP_CRON` activo.

### H. Integridad de la evidencia
```bash
sha256sum ab/* logs/* > logs/HASHES.txt
```

> **En el informe:** estos extras van a **Anexos**; además, cita el paso **G** en la sección 2.3 de
> mitigaciones, porque **demuestra** el control (no solo lo describe).

## Preguntas de análisis (resuélvelas en el informe)

1. ¿Por qué `wp-cron.php` no es necesariamente un *bug*, sino un problema de **diseño/configuración**
   cuando queda expuesto a ejecución repetida?
2. ¿Qué diferencia hay entre **disponibilidad, confidencialidad e integridad** en este laboratorio?
3. ¿Qué evidencia permite afirmar que el servicio se **saturó**: salida de `ab`, navegador, CPU/RAM o
   logs? Justifícalo.
4. ¿Por qué una prueba de carga **autorizada** mejora la resiliencia digital de una organización?
5. Propón **tres controles** concretos y explica cuál implementarías primero.

## Datos a anotar durante la ejecución (insumo para el informe)

Además de las capturas, apunta estos valores **reales**. Son el insumo que necesito para redactar el
informe con tus cifras y no con las de ejemplo de la guía:

- **Portada:** nombre, documento, grupo (02) y fecha de entrega.
- **Fase 1:** nombres reales de los contenedores (salida de `docker compose ps`).
- **Fase 2:** usuario y clave de administrador de WordPress que creaste (son de laboratorio; en el
  informe se ocultan, pero me sirven para describir el paso).
- **Fases 4 y 6:** % de **CPU** y **memoria** del contenedor `wordpress` **en reposo** y **durante** la prueba.
- **Fase 5 (`ab`):** de la salida anota `Complete requests`, `Failed requests`, `Requests per second`
  y `Time per request`.
- **Fase 7:** cómo se vio el efecto (lento / "esperando a localhost" / error) y cuánto tardó en recuperarse.

## Formato por comando (tabla del profesor, para cada paso)

| Paso | Comando ejecutado | Propósito técnico | Resultado observado | Explicación del estudiante (≥5 líneas) |
|------|-------------------|-------------------|---------------------|----------------------------------------|
| … | … | … | … | Relaciona el resultado con el riesgo y su mitigación |

> Recuerda: cada pantallazo lleva título **"Figura X. Evidencia del comando ejecutado"** y una
> explicación de **mínimo 5 líneas**. El Laboratorio 2 se califica por la **relación entre recursos,
> disponibilidad y controles** — no olvides cerrar siempre con la mitigación.
