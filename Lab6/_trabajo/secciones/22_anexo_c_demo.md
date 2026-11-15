# Anexo C. Demostración de auditoría de registros

La demostración del capítulo 16 es un programa de unas doscientas líneas que solo usa la biblioteca estándar de Python y una base de datos en memoria. No necesita instalación ni conexión, y todos los nombres, documentos y cuentas que contiene son ficticios.

## Cómo reproducirla

```
python Lab6/controles/auditoria_registros/demo_auditoria.py
```

La salida completa de la ejecución usada en este informe está en `Lab6/evidencias/salidas/00_demo_auditoria_completa.txt`.

## Qué contiene

El programa crea tres tablas. La tabla de pólizas tiene cuatro registros de ejemplo. La tabla de contexto de sesión guarda quién está conectado, desde qué dirección, con qué programa y con qué tique de cambio. La tabla de auditoría recibe una fila por cada cambio en los campos críticos: beneficiario, cuenta de cobro, capital asegurado y estado.

El mecanismo es un disparador por cada campo crítico. Este es el del beneficiario, abreviado:

```sql
CREATE TRIGGER audita_beneficiario
AFTER UPDATE OF beneficiario ON polizas
WHEN OLD.beneficiario IS NOT NEW.beneficiario
BEGIN
  INSERT INTO auditoria_polizas
    (fecha_hora, usuario, ip_origen, aplicacion, tique_cambio,
     id_poliza, campo, valor_anterior, valor_nuevo,
     hash_anterior, hash_registro)
  SELECT c.fecha_hora, c.usuario, c.ip_origen, c.aplicacion,
         c.tique_cambio, OLD.id_poliza, 'beneficiario',
         OLD.beneficiario, NEW.beneficiario, previo.h,
         sha256(previo.h || '|' || c.fecha_hora || '|' || ...)
  FROM contexto_sesion c, (ultimo hash del registro) previo;
END;
```

Cada fila guarda el hash de la anterior y calcula el suyo con ese valor y con sus propios datos. Otros dos disparadores impiden modificar o borrar filas del registro. Las dos consultas de auditoría son estas:

```sql
-- Regla A: cambios en campos críticos sin tique de autorización
SELECT * FROM auditoria_polizas WHERE tique_cambio IS NULL;

-- Regla B: cambios fuera de horario o hechos sin la aplicación
SELECT usuario, ip_origen, aplicacion, COUNT(*) AS cambios
FROM auditoria_polizas
WHERE time(fecha_hora) NOT BETWEEN '08:00:00' AND '20:00:00'
   OR aplicacion <> 'core-polizas'
GROUP BY usuario, ip_origen, aplicacion;
```

## Límites del ejemplo

Es una maqueta. En producción el contexto de la sesión lo proporciona la auditoría nativa del gestor de base de datos y no una tabla que la aplicación rellena, el registro se envía en tiempo real a un almacén que el administrador de la base de datos no controla, y las reglas viven en el SIEM. El ejemplo conserva lo esencial del mecanismo: registrar el contexto y el valor anterior, encadenar los registros y consultar por lo que no encaja.
