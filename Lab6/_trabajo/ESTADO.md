# ESTADO del Laboratorio 6 (checkpoint)

Fuente de verdad para retomar el trabajo. Se actualiza al cerrar cada paso, antes de empezar el siguiente.

- Plan aprobado: `C:\Users\Sebastian-EDU\.claude-personal\plans\necesito-realizar-el-laboratorio-async-perlis.md` (incluye el resumen de la guía y la rúbrica, no hace falta releer el PDF).
- Iniciado: 13/11/2026.

## Cómo retomar

1. Leer este archivo completo.
2. Continuar por el primer paso sin marcar. Los pasos marcados ya tienen su salida en disco: no repetirlos.
3. Antes de redactar: cargar las skills `humanizer:humanizer` y `anthropic-skills:ing-docs`.
4. Las fuentes ya resumidas están en `Lab6/_trabajo/notas/`. Los textos crudos están en `material/_texto/` y `material/transcripciones/`. No leer PDF como imagen ni volver a transcribir.
5. Los scripts son idempotentes: si se relanzan, saltan lo que ya existe.

## Pasos

### F0. Preparación
- [x] Estructura `Lab6/{guias,diagramas,anexos,_trabajo}` y guía movida a `Lab6/guias/`
- [x] `.gitignore`: `/material/*.mp4` y `/material/_audio/`
- [x] Este archivo, lista `lab6-mapfre` en claude-mem y memoria `lab6-mapfre-estado.md`

### F1. Videos a texto (local, en segundo plano)
- [x] Entorno `contexto-claude/tools/.venv-transcripcion` (faster-whisper 1.2.1 + CUDA, 2,2 GB)
- [x] `contexto-claude/tools/transcribir_video.py` escrito y probado (modelo turbo en GPU, 7,7 veces tiempo real)
- [x] Transcripción `2026-11-04 18-43-20.mp4` (34 min, 3.576 palabras)
- [x] Transcripción `2026-11-04 20-02-51.mp4` (46 min, 5.802 palabras)
- [x] Transcripción `2026-11-06 18-25-16.mp4` (1 h 44 min, 12.220 palabras; último segmento en 01:44:30)
- [x] Pantallas (fotogramas clave + OCR) de los 3 videos: 27, 55 y 311 pantallas; `pantallas.md` y `hojas/`
- [x] `material/transcripciones/README.md`
- Para regenerar (no hace falta; saltan lo ya hecho): ver los comandos en `material/transcripciones/README.md`.

### F2. Material a texto (local)
- [x] `contexto-claude/tools/ocr_windows.ps1` y `extraer_texto_material.py`
- [x] `material/_texto/*.txt` y `material/_texto/INDICE.md` (31 documentos; 240 páginas por OCR)

### F3. Lectura y síntesis
- [x] `Lab6/guias/instrucciones_clase.md` (las 3 clases sintetizadas, con marca de tiempo y lista de verificación)
- [x] Nota `notas/01_fuentes_A_docente.md`: Presentación Unidad 3 - M1, Marco Normativo Colombiano, Unidad Temática 3
- [x] Nota `notas/02_riesgos_UNIR_y_redes_U2.md`: Análisis de Riesgos (UNIR), Unidad 2 - M1 (redes), Tema UNIR de riesgos
- [x] Nota `notas/03_Ley1581_y_temario_Renfe.md`: artículos de la Ley 1581 y clasificación de la información de Renfe
- [x] NIST CSF 2.0 y guía NQA ISO 27001: consultados; lo útil quedó en `instrucciones_clase.md` (numerales 4 a 10, PHVA, Anexo A) y no requiere nota aparte
- [x] **`Lab6/_trabajo/ESQUEMA.md`** (esquema definitivo: supuestos S1 a S8, activos A1 a A10, vulnerabilidades V1 a V9, riesgos R1 a R10 con valores, controles C1 a C16 con Anexo A, evidencia e indicador, lista de secciones, figuras y modelo financiero). LEERLO antes de redactar cualquier sección.

### F4. Fuentes externas
- [x] `Lab6/_trabajo/fuentes_verificadas.md` (F01 a F21 verificadas; lo estable sin búsqueda queda listado al final)

### F5. Diagramas (`Lab6/diagramas/`, `.mmd` + `.png`)
- [x] 10 figuras en `Lab6/diagramas/` revisadas visualmente: 01 anatomía del ataque, 02 cronología, 03 modelo normativo, 04 mapa de calor, 05 arquitectura segura, 06 hoja de ruta, 07 monitoreo, 08 impacto financiero, 09 DRP, 10 flujo legal.
  - Mermaid: `python -I contexto-claude/tools/lab6_diagramas.py Lab6` (escribe los `.mmd` y renderiza; salta lo que está al día).
  - Gráficos de datos (04 y 08): `python -I contexto-claude/tools/lab6_modelo.py Lab6` y luego `lab6_graficos.py Lab6`. Las cifras exactas de riesgos y costos están en `Lab6/_trabajo/datos/tablas_generadas.md`: usarlas tal cual en el informe.
- [x] Demostración de auditoría de registros (actividad 13): `Lab6/controles/auditoria_registros/demo_auditoria.py` ejecutada; salida en `Lab6/evidencias/salidas/` (00 completa, 01, 02, 03) y capturas `Lab6/evidencias/01_registro_auditoria.png`, `02_consultas_deteccion.png`, `03_integridad_y_reversion.png`

### F6. Redacción (`Lab6/_trabajo/secciones/NN_*.md`)
Convenciones al redactar: tablas y figuras con clave `[[t:clave]]` y `[[f:clave]]` (el ensamblador las numera); pie debajo (`*Tabla [[t:x]].* ...`); imágenes sin ancho (`![](diagramas/NN.png)`); citas APA en el texto con las claves de `19_referencias.md`; sin rayas largas.
- [x] `02_contexto.md`
- [x] `03_incidente.md`
- [x] `04_act01_activos.md`
- [x] `05_act02_clasificacion.md`
- [x] `06_act03_vulnerabilidades.md`
- [x] `07_act04_modelo_normativo.md`
- [x] `08_act05_riesgos.md`
- [x] `09_act06_controles.md`
- [x] `10_act07_cierre_brechas.md`
- [x] `11_act08_monitoreo.md`
- [x] `12_act09_financiera.md`
- [x] `13_act10_reputacional.md`
- [x] `14_act11_operacion_drp.md`
- [x] `15_act12_divulgacion.md`
- [x] `16_act13_modificacion.md`
- [x] `17_plan_mejora.md`
- [x] `18_conclusiones.md`
- [x] `19_referencias.md`
- [x] `20_anexo_a_trazabilidad.md`
- [x] `21_anexo_b_politica.md`
- [x] `22_anexo_c_demo.md`
- [x] `00_resumen.md` y `01_introduccion.md`

### F7. Ensamblado y render
- [x] `contexto-claude/tools/build_lab6.py` (ensambla, numera tablas y figuras)
- [x] Informe `.md`, `.docx` y `.pdf` en `Lab6/` (primer render 15/11: 94 páginas). Rehacer: `python contexto-claude/tools/build_lab6.py Lab6 "15 de noviembre de 2026"` y luego `EXTRA_POST=tablas_compactas.py bash contexto-claude/tools/build_informe.sh Lab6 "Informe*N*6*.md" word "Políticas de Seguridad Informática" "15/11/2026" "POLÍTICAS DE SEGURIDAD INFORMÁTICA" "FD-GC195"`

### F8. Validación y corrección
- [x] Ciclo 1 (`validacion/ciclo_1.md`)
- [x] Ciclo 2 (`validacion/ciclo_2.md`): sin hallazgos abiertos; PDF final de 98 páginas

### F9. Presentación
- [x] PPTX de 10 diapositivas y su PDF (`python contexto-claude/tools/build_lab6_pptx.py Lab6`)
- [x] `Lab6/GUIDE.md` (guion de 582 palabras, 6 min 30 s)

### F10. Cierre
- [x] Memoria del proyecto y este archivo actualizados; resumen al usuario. Pendiente solo de decisiones del usuario: fecha de portada (15/11/2026) y commit.

## Decisiones tomadas

- Autor: Sebastián López Osorno, **Grupo 02**, semestre 2026-02 (la guía trae "Grupo 11" prellenado; se mantiene 02 como en Lab1 a Lab5).
- Nombre del entregable: `Informe de Laboratorio N.° 6 - Diplomado Ciberseguridad - Sebastián López Osorno`. La guía lo llama "Ejercicio Práctico N.° 5 de Políticas de Seguridad" (Taller N.° 5, 10 %).
- Membrete: asignatura "Políticas de Seguridad Informática", módulo "POLÍTICAS DE SEGURIDAD INFORMÁTICA", código FD-GC195.
- Marco normativo provisional: eje España/UE (empresa del caso) con espejo colombiano (marco del curso). Se confirma con los videos.
- El caso es un escenario académico: los datos reales de Mapfre solo se usan con fuente verificada y los supuestos se declaran como tales.
- Sin subagentes y sin commits (el usuario hace sus propios commits).
- Redacción: prosa ampliada, sin rayas largas, reglas de humanizer.

- **Plazo:** en la clase del 6/11 el docente dijo que la actividad cerraba el martes 10/11/2026 a las 22:00. Se avisó al usuario el 13/11. Portada con la fecha real de terminación salvo que el usuario indique otra.
- **Convenciones del autor (skill ing-docs):** guion de exposición en `Lab6/GUIDE.md`; evidencias numeradas en `Lab6/evidencias/`; artefactos de control en `Lab6/controles/` (como en Lab5). La carpeta `anexos/` no se usa.
- **Presentación:** la guía escrita pide una de 5 a 7 minutos; en clase el docente solo habló de la exposición final con póster. Se prepara igual (PPTX y `GUIDE.md`).

## Bitácora

- 13/11/2026: plan aprobado; F0 cerrada.
- 13/11/2026 (madrugada): F1 y F2 cerradas (3 clases transcritas, 31 documentos a texto). F3 cerrada: notas, `instrucciones_clase.md` y `ESQUEMA.md`. Siguiente: terminar F4 (dos verificaciones pendientes), luego F5 diagramas y F6 redacción.
