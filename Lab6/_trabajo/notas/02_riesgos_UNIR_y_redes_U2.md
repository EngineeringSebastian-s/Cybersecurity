# Notas: análisis de riesgos (UNIR) y redes (Unidad 2 - M1). Leídas completas el 13/11/2026

## 1. `Análisis de Riesgos.pdf` (UNIR, Cristina Merino Bada; 43 diapositivas, por OCR)

Citar como: Merino Bada, C. (s. f.). *Análisis de riesgos* [Diapositivas]. Universidad Internacional de La Rioja. Material del curso.

- **Temario (d2):** Tema 6 Seguridad de la información y gestión de riesgos; Tema 7 UNE-ISO 31000:2018; Tema 8 Metodologías de análisis de riesgos; Tema 9 Evaluación de riesgos de TI; Tema 10 Respuesta y monitorización.
- **La información (d6-d7):** "uno de los activos más importantes con los que cuentan las organizaciones"; es inmaterial y reside en las personas, los documentos escritos y los sistemas informáticos.
- **Cuatro preguntas (d10):** ¿qué?, ¿dónde?, ¿cómo?, ¿cuándo?
- **Dimensiones de la seguridad (d12-d18):** Confidencialidad [C], Integridad [I], Disponibilidad [D], Autenticidad [A], Trazabilidad [T].
  - Confidencialidad: que la información no sea conocida por personas, organizaciones o procesos sin la autorización necesaria.
  - Integridad: que la información no se haya transformado ni modificado de forma no autorizada durante su procesamiento, transporte o almacenamiento, y poder detectar fácilmente las modificaciones.
  - Disponibilidad: que la información sea accesible cuando los usuarios autorizados la necesiten.
  - Autenticidad: garantizar la identidad del usuario que origina una información; conocer con certeza quién la envía o genera. **(La suplantación de IP y de ARP ataca esta dimensión.)**
  - Trazabilidad: poder determinar en todo momento quién hizo qué y en qué momento. **(Base de la auditoría de registros de la actividad 13.)**
- **¿Dónde? (d22-d23):** en los Sistemas de Información y Comunicaciones: personas, datos, procedimientos y recursos técnicos; hay que proteger todos sus elementos según sus características y vulnerabilidades.
- **¿Cómo? (d24-d25):** con salvaguardas (controles) que minimicen la probabilidad de que la amenaza se materialice, disminuyan el impacto, permitan una recuperación rápida y se ajusten con la experiencia de incidentes anteriores.
- **¿Cuándo? (d26):** durante todo el ciclo de vida: captura, almacenamiento, proceso, transmisión, utilización y destrucción.
- **Análisis y gestión de riesgos (d27, d39-d40):** permite conocer a qué se está expuesto, identificar los riesgos que impedirían lograr los objetivos, determinar su magnitud y señalar las áreas que requieren salvaguardas. "La mitigación total de los riesgos es imposible"; el objetivo es tratar el riesgo "hasta disminuir el riesgo residual a los niveles asumibles por la dirección".
- **Amenazas (d38, taxonomía ENISA):** actividad maliciosa: robo de identidad, acceso no autorizado a sistemas, ataques de suplantación de DNS, código malicioso, ingeniería social, escalada de privilegios.
- **Lenguaje común (d42):** glosario CCN-STIC-401 y glosario de ISACA.

## 2. `Presentación Unidad 2 - M1.pdf` (Ochoa, 2026): "Arquitectura de sistemas y redes en ciberseguridad"

- **Seguridad en redes (d2):** protección de la infraestructura de red contra accesos no autorizados, ataques y actividades maliciosas; asegura la confidencialidad, integridad y disponibilidad de los datos que viajan por la red. Topología: su diseño influye directamente en la seguridad. Firewall: controla el tráfico según reglas.
- **Segmentación (d3, d5, d6):** dividir la red en subredes para limitar el alcance del atacante. "Aísla los sistemas críticos, como servidores de bases de datos, de los usuarios finales, reduciendo el riesgo de acceso no autorizado o ataques laterales." Ejemplo AWS: separa el tráfico de administración del de usuario.
- **Firewall de próxima generación, NGFW (d4-d5):** inspección profunda de paquetes; ejemplo IBM para proteger servidores y bases de datos.
- **VPN (d3-d5):** conexión segura sobre redes no seguras, cifrando los datos; evita la interceptación.
- **TLS/SSL (d14-d16):** confidencialidad e integridad mediante cifrado; cifrado simétrico y asimétrico; los certificados digitales verifican la identidad del servidor o del cliente, "asegurando que la comunicación se realice con la parte correcta". **(Contramedida directa al intermediario por ARP spoofing.)**
- **IPsec (d17-d18):** protege la comunicación IP en capa 3; AH y ESP dan cifrado y autenticación mutua entre las partes; túneles entre sedes. **(Contramedida a la suplantación de IP: autentica el origen del paquete.)**
- **Nube (d27):** control de acceso y cifrado de datos en reposo y en tránsito.

## 3. `-Tema-UNIR-Ciberseguridad-normatividad.pdf` (UNIR, "Tema 4: Analizando los riesgos de las infraestructuras críticas"; pp. 3-30 leídas)

Citar como: Universidad Internacional de La Rioja. (s. f.). *Tema 4: Analizando los riesgos de las infraestructuras críticas* [Diapositivas]. Material del curso.

- **Gestión de riesgos (p4):** "proceso sistemático para estimar la magnitud de los riesgos a los que está expuesta una organización". Tiene dos fases: análisis de riesgos (identificar y definir los riesgos) y tratamiento de riesgos (seleccionar e implementar salvaguardas para conocer, prevenir, impedir, reducir o controlar los riesgos).
- **Punto de partida (p6):** identificar formalmente los elementos a proteger o con valor para la organización, los activos, y valorarlos según requisitos de seguridad: confidencialidad, integridad y disponibilidad.
- **Enfoques (p7-p9):** cuantitativo (probabilidades y frecuencia de la amenaza); cualitativo (estimaciones de pérdida potencial con términos "alto", "medio" o "bajo"; tiene en cuenta el conocimiento del personal); basado en conocimiento (reutilizar el método de sistemas similares). **La guía del Lab6 pide el cualitativo.**
- **Tratamiento (p10):** para cada riesgo se elige una opción: reducir el riesgo; compartir o transferir el riesgo; eliminar o mitigar el riesgo; aceptar el riesgo. De ahí sale el riesgo residual.
- **Estándares y metodologías que enumera (p11-p29):** ISO/IEC 13335; ISO/IEC 27001/27002 ("un total de 93 controles", es decir, ya la versión 2022); ISO/IEC 27005 (gestión de riesgos de seguridad de la información, complementa 27001 y 27002); NIST SP 800-30 (guía de análisis y gestión de riesgos; segunda fase: mitigación al menor costo hasta niveles aceptables); AS/NZS 4360; MAGERIT v3 (metodología española, abierta, obligatoria para las Administraciones Públicas); OCTAVE (Carnegie Mellon, tres fases: perfiles de amenaza por activo, vulnerabilidades de la infraestructura, estrategia y planes); MEHARI (CLUSIF); CRAMM; ISO/IEC 15443; ISO/IEC 20000 e ITIL (conocimiento actualizado de los activos y sus dependencias, gestión de la configuración); COBIT (proceso de evaluación de riesgos, criterios de confidencialidad, integridad y disponibilidad); MARISMA y la herramienta eMARISMA (Universidad de Castilla-La Mancha).
- **Tabla comparativa (p30):** compara metodologías por tipo de análisis, criterios (C, I, D, autenticidad) y elementos del modelo (activos, vulnerabilidades, amenazas, salvaguardas).
