# -*- coding: utf-8 -*-
"""
Demostración reproducible de auditoría de registros para detectar cambios no autorizados en datos de pólizas.
Laboratorio 6, actividad 13. Solo usa la biblioteca estándar de Python (sqlite3 y hashlib).

Qué muestra:
  1. Una tabla de pólizas y un registro de auditoría alimentado por disparadores: cada cambio en un campo crítico
     deja quién, cuándo, desde dónde, con qué aplicación, con qué tique de cambio y el valor anterior y el nuevo.
  2. Cambios legítimos (hechos por la aplicación y con tique) y cambios no autorizados hechos de madrugada por un
     atacante que usa la cuenta de servicio y la dirección IP suplantada del servidor de aplicaciones.
  3. Consultas de auditoría que separan unos de otros sin fiarse de la dirección IP.
  4. Un registro de solo anexado y encadenado por hash: si alguien borra o altera una fila, la cadena se rompe.
  5. La reversión de los cambios indebidos con los valores anteriores, que también queda auditada.

Todos los nombres, documentos y cuentas son ficticios. En un sistema real el contexto de sesión lo aporta la
auditoría nativa del gestor de base de datos y el registro se envía en tiempo real a un almacén inmutable.

Uso: python demo_auditoria.py
"""
import hashlib
import sqlite3
import sys

APLICACION_AUTORIZADA = "core-polizas"

ESQUEMA = """
CREATE TABLE polizas (
    id_poliza TEXT PRIMARY KEY, titular TEXT, beneficiario TEXT, iban_cobro TEXT,
    capital_asegurado INTEGER, estado TEXT);

-- Contexto de la sesión: quién, desde dónde, con qué aplicación y con qué tique de cambio.
CREATE TABLE contexto_sesion (
    id INTEGER PRIMARY KEY CHECK (id = 1), fecha_hora TEXT, usuario TEXT, ip_origen TEXT,
    aplicacion TEXT, tique_cambio TEXT);
INSERT INTO contexto_sesion VALUES (1, NULL, NULL, NULL, NULL, NULL);

CREATE TABLE auditoria_polizas (
    id INTEGER PRIMARY KEY AUTOINCREMENT, fecha_hora TEXT, usuario TEXT, ip_origen TEXT, aplicacion TEXT,
    tique_cambio TEXT, id_poliza TEXT, campo TEXT, valor_anterior TEXT, valor_nuevo TEXT,
    hash_anterior TEXT, hash_registro TEXT);

-- El registro es de solo anexado: una cuenta normal no puede modificarlo ni borrarlo.
CREATE TRIGGER auditoria_sin_update BEFORE UPDATE ON auditoria_polizas
BEGIN SELECT RAISE(ABORT, 'el registro de auditoría es de solo anexado'); END;
CREATE TRIGGER auditoria_sin_delete BEFORE DELETE ON auditoria_polizas
BEGIN SELECT RAISE(ABORT, 'el registro de auditoría es de solo anexado'); END;
"""

DISPARADOR = """
CREATE TRIGGER audita_{campo} AFTER UPDATE OF {campo} ON polizas
WHEN OLD.{campo} IS NOT NEW.{campo}
BEGIN
    INSERT INTO auditoria_polizas (fecha_hora, usuario, ip_origen, aplicacion, tique_cambio, id_poliza, campo,
                                   valor_anterior, valor_nuevo, hash_anterior, hash_registro)
    SELECT c.fecha_hora, c.usuario, c.ip_origen, c.aplicacion, c.tique_cambio, OLD.id_poliza, '{campo}',
           OLD.{campo}, NEW.{campo}, previo.h,
           sha256(previo.h || '|' || c.fecha_hora || '|' || c.usuario || '|' || c.ip_origen || '|' ||
                  c.aplicacion || '|' || COALESCE(c.tique_cambio, '') || '|' || OLD.id_poliza || '|{campo}|' ||
                  OLD.{campo} || '|' || NEW.{campo})
    FROM contexto_sesion c,
         (SELECT COALESCE((SELECT hash_registro FROM auditoria_polizas ORDER BY id DESC LIMIT 1), 'INICIO') AS h) previo;
END;
"""
CAMPOS_CRITICOS = ("beneficiario", "iban_cobro", "capital_asegurado", "estado")

POLIZAS = [
    ("VID-2024-000187", "Lucía Herrero Vidal", "Andrés Pastor Gil", "ES91 **** **** 1332", 60000, "vigente"),
    ("VID-2024-000245", "Ignacio Vera Cano", "Marta Solís Rey", "ES76 **** **** 0419", 90000, "vigente"),
    ("VID-2025-000310", "Marta Solís Rey", "Ignacio Vera Cano", "ES12 **** **** 7750", 120000, "vigente"),
    ("VID-2025-000402", "Andrés Pastor Gil", "Lucía Herrero Vidal", "ES45 **** **** 2206", 45000, "vigente"),
]


def titulo(texto):
    print()
    print("=" * 96)
    print(texto)
    print("=" * 96)


def sesion(con, fecha_hora, usuario, ip, aplicacion, tique):
    con.execute("UPDATE contexto_sesion SET fecha_hora=?, usuario=?, ip_origen=?, aplicacion=?, tique_cambio=?",
                (fecha_hora, usuario, ip, aplicacion, tique))


def cambia(con, poliza, campo, valor):
    con.execute(f"UPDATE polizas SET {campo}=? WHERE id_poliza=?", (valor, poliza))


def imprime_registro(filas):
    for r in filas:
        tique = r["tique_cambio"] or "(sin tique)"
        print(f"[{r['id']}] {r['fecha_hora']} | {r['usuario']} | IP {r['ip_origen']} | {r['aplicacion']} | {tique}")
        print(f"     {r['id_poliza']} · {r['campo']}: {r['valor_anterior']} -> {r['valor_nuevo']}"
              f"   hash {r['hash_registro'][:12]}…")


def verifica_cadena(con):
    """Recalcula la cadena de hash de principio a fin y dice dónde se rompe, si se rompe."""
    previo, total = "INICIO", 0
    for r in con.execute("SELECT * FROM auditoria_polizas ORDER BY id"):
        base = "|".join([previo, r["fecha_hora"], r["usuario"], r["ip_origen"], r["aplicacion"],
                         r["tique_cambio"] or "", r["id_poliza"], r["campo"],
                         str(r["valor_anterior"]), str(r["valor_nuevo"])])
        esperado = hashlib.sha256(base.encode("utf-8")).hexdigest()
        if r["hash_anterior"] != previo or r["hash_registro"] != esperado:
            return f"CADENA ROTA en el registro [{r['id']}]: falta o se alteró un registro anterior"
        previo, total = r["hash_registro"], total + 1
    return f"Cadena íntegra: {total} registros verificados"


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    con = sqlite3.connect(":memory:")
    con.row_factory = sqlite3.Row
    con.create_function("sha256", 1, lambda s: hashlib.sha256(s.encode("utf-8")).hexdigest())
    con.executescript(ESQUEMA)
    for campo in CAMPOS_CRITICOS:
        con.executescript(DISPARADOR.format(campo=campo))
    con.executemany("INSERT INTO polizas VALUES (?, ?, ?, ?, ?, ?)", POLIZAS)

    titulo("1. CAMBIOS DEL DÍA 9 Y DE LA MADRUGADA DEL 10 DE MARZO")
    # Cambios legítimos: los hace la aplicación, en horario de oficina y con tique de cambio aprobado.
    sesion(con, "2026-03-09 10:14:07", "app_polizas", "10.10.20.15", APLICACION_AUTORIZADA, "CHG-2026-0412")
    cambia(con, "VID-2024-000245", "beneficiario", "Lucía Herrero Vidal")
    sesion(con, "2026-03-09 16:42:31", "app_polizas", "10.10.20.15", APLICACION_AUTORIZADA, "CHG-2026-0415")
    cambia(con, "VID-2025-000402", "iban_cobro", "ES45 **** **** 9914")
    # Cambios no autorizados: misma cuenta de servicio y misma IP (suplantada), pero de madrugada, con un
    # cliente SQL que no es la aplicación y sin tique.
    sesion(con, "2026-03-10 02:47:19", "app_polizas", "10.10.20.15", "cliente-sql", None)
    cambia(con, "VID-2025-000310", "beneficiario", "Tercero no vinculado")
    sesion(con, "2026-03-10 02:48:02", "app_polizas", "10.10.20.15", "cliente-sql", None)
    cambia(con, "VID-2025-000310", "iban_cobro", "ES00 **** **** 6666")
    sesion(con, "2026-03-10 02:49:40", "app_polizas", "10.10.20.15", "cliente-sql", None)
    cambia(con, "VID-2024-000187", "capital_asegurado", 250000)
    # Un cambio legítimo más, ya en la mañana del día 10.
    sesion(con, "2026-03-10 09:05:12", "app_polizas", "10.10.20.15", APLICACION_AUTORIZADA, "CHG-2026-0420")
    cambia(con, "VID-2024-000245", "estado", "suspendida")
    print("Registro de auditoría completo (una fila por cada cambio en un campo crítico):")
    imprime_registro(con.execute("SELECT * FROM auditoria_polizas ORDER BY id").fetchall())

    titulo("2. CONSULTAS DE AUDITORÍA: ¿QUÉ CAMBIOS NO ESTÁN AUTORIZADOS?")
    print("Regla A. Cambios en campos críticos sin tique de cambio aprobado:")
    print("  SELECT * FROM auditoria_polizas WHERE tique_cambio IS NULL;")
    sin_tique = con.execute("SELECT * FROM auditoria_polizas WHERE tique_cambio IS NULL").fetchall()
    imprime_registro(sin_tique)
    print()
    print("Regla B. Cambios fuera del horario de operación (08:00 a 20:00) o hechos sin la aplicación:")
    print("  SELECT ... WHERE time(fecha_hora) NOT BETWEEN '08:00:00' AND '20:00:00' OR aplicacion <> 'core-polizas';")
    resumen = con.execute("""
        SELECT usuario, ip_origen, aplicacion, date(fecha_hora) AS dia, COUNT(*) AS cambios,
               MIN(time(fecha_hora)) AS desde, MAX(time(fecha_hora)) AS hasta, COUNT(DISTINCT id_poliza) AS polizas
        FROM auditoria_polizas
        WHERE time(fecha_hora) NOT BETWEEN '08:00:00' AND '20:00:00' OR aplicacion <> ?
        GROUP BY usuario, ip_origen, aplicacion, dia""", (APLICACION_AUTORIZADA,)).fetchall()
    for r in resumen:
        print(f"  HALLAZGO: {r['cambios']} cambios en {r['polizas']} pólizas el {r['dia']} entre las {r['desde']} y "
              f"las {r['hasta']}")
        print(f"            usuario {r['usuario']}, IP {r['ip_origen']}, aplicación {r['aplicacion']}")
    print()
    print("Lectura del auditor: la IP coincide con la del servidor de aplicaciones porque fue suplantada, así que")
    print("la dirección de origen no sirve como prueba. Delatan el cambio la falta de tique, la hora y el cliente.")

    titulo("3. INTEGRIDAD DEL PROPIO REGISTRO DE AUDITORÍA")
    print("Verificación inicial ->", verifica_cadena(con))
    print()
    print("Intento de borrar las huellas con una cuenta normal:")
    print("  DELETE FROM auditoria_polizas WHERE tique_cambio IS NULL;")
    try:
        con.execute("DELETE FROM auditoria_polizas WHERE tique_cambio IS NULL")
    except sqlite3.DatabaseError as e:
        print(f"  BLOQUEADO: {e}")
    print()
    print("Intento con privilegios de administrador (se elimina la protección y se borra el registro [4]):")
    copia = [dict(r) for r in con.execute("SELECT * FROM auditoria_polizas ORDER BY id")]   # copia en el SIEM
    con.execute("DROP TRIGGER auditoria_sin_delete")
    con.execute("DELETE FROM auditoria_polizas WHERE id = 4")
    print("Verificación posterior ->", verifica_cadena(con))
    faltan = sorted({r["id"] for r in copia} - {r["id"] for r in con.execute("SELECT id FROM auditoria_polizas")})
    print(f"Contraste con la copia enviada al almacén inmutable: falta el registro {faltan}; se recupera de la copia.")

    titulo("4. TRATAMIENTO: REVERSIÓN CON LOS VALORES ANTERIORES (TAMBIÉN AUDITADA)")
    sesion(con, "2026-03-10 11:30:00", "app_polizas", "10.10.20.15", APLICACION_AUTORIZADA, "INC-2026-0031")
    for r in sin_tique:
        cambia(con, r["id_poliza"], r["campo"], r["valor_anterior"])
        print(f"  Revertido {r['id_poliza']} · {r['campo']}: {r['valor_nuevo']} -> {r['valor_anterior']}"
              f"   (tique INC-2026-0031)")
    print()
    print("Estado final de las pólizas afectadas:")
    for r in con.execute("SELECT * FROM polizas WHERE id_poliza IN ('VID-2025-000310', 'VID-2024-000187')"):
        print(f"  {r['id_poliza']} | beneficiario: {r['beneficiario']} | cobro: {r['iban_cobro']} | "
              f"capital: {r['capital_asegurado']} | {r['estado']}")
    total = con.execute("SELECT COUNT(*) FROM auditoria_polizas").fetchone()[0]
    print(f"Registros de auditoría tras la reversión: {total} (las reversiones quedan registradas con su tique).")


if __name__ == "__main__":
    main()
