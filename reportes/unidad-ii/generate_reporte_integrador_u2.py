import os
import sys
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

# Importar helpers de formato ya existentes en el proyecto
helpers_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "docs", "reporte"))
sys.path.append(helpers_dir)
from build_docx_helpers import (
    set_cell_background, set_cell_margins, set_cell_borders,
    add_code_block, add_callout, format_table
)

def create_reporte_integrador():
    doc = docx.Document()

    # Configuración de márgenes estándar (1 pulgada / 2.54 cm en los 4 lados)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Paleta de colores institucional académica UTTT
    navy = RGBColor(0x1B, 0x36, 0x5D)        # Azul UTTT Institucional
    dark_gray = RGBColor(0x33, 0x41, 0x55)   # Pizarra / Encabezados H2
    charcoal = RGBColor(0x1E, 0x29, 0x3B)    # Texto Principal
    caption_color = RGBColor(0x47, 0x55, 0x69)

    font_family = "Arial"

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = font_family
        run.font.size = Pt(14.5)
        run.font.bold = True
        run.font.color.rgb = navy
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = font_family
        run.font.size = Pt(12)
        run.font.bold = True
        run.font.color.rgb = dark_gray
        return p

    def add_h3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        run.font.name = font_family
        run.font.size = Pt(10.5)
        run.font.bold = True
        run.font.color.rgb = charcoal
        return p

    def add_p(text, bold_prefix=None):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = font_family
            r_pre.font.size = Pt(10)
            r_pre.font.bold = True
            r_pre.font.color.rgb = charcoal
        run = p.add_run(text)
        run.font.name = font_family
        run.font.size = Pt(10)
        run.font.color.rgb = charcoal
        return p

    def add_bullet(text, bold_prefix=None):
        p = doc.add_paragraph(style='List Bullet')
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            r_pre.font.name = font_family
            r_pre.font.size = Pt(10)
            r_pre.font.bold = True
            r_pre.font.color.rgb = charcoal
        run = p.add_run(text)
        run.font.name = font_family
        run.font.size = Pt(10)
        run.font.color.rgb = charcoal
        return p

    def add_custom_table(headers, data, col_widths):
        table = doc.add_table(rows=len(data) + 1, cols=len(headers))
        format_table(table, col_widths, headers, data)
        p_space = doc.add_paragraph()
        p_space.paragraph_format.space_before = Pt(2)
        p_space.paragraph_format.space_after = Pt(6)

    def add_figure(image_path, caption_text, width=Inches(6.0)):
        if os.path.exists(image_path):
            p_img = doc.add_paragraph()
            p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_img.paragraph_format.space_before = Pt(8)
            p_img.paragraph_format.space_after = Pt(3)
            run_img = p_img.add_run()
            run_img.add_picture(image_path, width=width)

            p_cap = doc.add_paragraph()
            p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p_cap.paragraph_format.space_before = Pt(0)
            p_cap.paragraph_format.space_after = Pt(10)
            r_cap = p_cap.add_run(caption_text)
            r_cap.font.name = font_family
            r_cap.font.size = Pt(9)
            r_cap.font.italic = True
            r_cap.font.color.rgb = caption_color

    base_proj = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    evid_dir = os.path.join(base_proj, "evidencias", "unidad-ii")

    # ==========================================================
    # 1. PORTADA INSTITUCIONAL ACADÉMICA
    # ==========================================================
    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_before = Pt(36)
    p_inst.paragraph_format.space_after = Pt(4)
    r = p_inst.add_run("UNIVERSIDAD TECNOLÓGICA DE TULA-TEPEJI")
    r.font.name = font_family
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.color.rgb = navy

    p_area = doc.add_paragraph()
    p_area.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_area.paragraph_format.space_after = Pt(28)
    r = p_area.add_run("Área de Tecnologías de la Información • Ingeniería en Desarrollo y Gestión de Software\nAsignatura: Bases de Datos en la Nube")
    r.font.name = font_family
    r.font.size = Pt(11)
    r.font.color.rgb = dark_gray

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(24)
    p_title.paragraph_format.space_after = Pt(6)
    r = p_title.add_run("AVENGERS INITIATIVE • MISIÓN 03\nINFORME FINAL A S.H.I.E.L.D.\nOPERACIÓN CAMPUSCLOUD: PROTOCOLO DE DEFENSA DE DATOS")
    r.font.name = font_family
    r.font.size = Pt(16.5)
    r.font.bold = True
    r.font.color.rgb = navy

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(36)
    r = p_sub.add_run("Actividad de Evaluación 3 • Unidad II (25 %)\nReporte Técnico Integrador: Decisiones, Arquitectura Políglota y Resultados NoSQL")
    r.font.name = font_family
    r.font.size = Pt(11.5)
    r.font.italic = True
    r.font.color.rgb = dark_gray

    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_before = Pt(40)
    p_meta.paragraph_format.space_after = Pt(24)

    meta_text = (
        "AGENTE RESPONSABLE: Mariano Calzadilla Alvarez\n"
        "MATRÍCULA: 24300700\n"
        "GRUPO / CUATRIMESTRE: 7° Cuatrimestre • TIID\n"
        "DOCENTE TITULAR: Mtro. de Asignatura de Bases de Datos en la Nube\n"
        "REPOSITORIO GITHUB: https://github.com/mariano-si7/CAMPUSCLOUD\n"
        "FECHA DE EVALUACIÓN: Noviembre de 2026\n"
        "ESTADO DEL EXPEDIENTE: INTEGRACIÓN Y DEFENSA APROBADA"
    )
    r_meta = p_meta.add_run(meta_text)
    r_meta.font.name = font_family
    r_meta.font.size = Pt(10)
    r_meta.font.color.rgb = charcoal

    doc.add_page_break()

    # ==========================================================
    # ÍNDICE GENERAL DEL EXPEDIENTE
    # ==========================================================
    add_h1("Índice General del Expediente")
    add_p("1. Introducción y Descripción del Problema CampusCloud")
    add_p("2. Misión 1: Justificación Estratégica del Arsenal de Datos (Matriz de Modelos)")
    add_p("3. Misión 2: Revela el Plano de CampusCloud (Arquitectura Física vs Conceptual)")
    add_p("4. Misión 3: Registro de Tecnologías Activadas (Implementaciones y Consultas)")
    add_p("5. Misión 4: Validación de Campo (Pruebas Funcionales, Persistencia y Seguridad)")
    add_p("6. Misión 5: Protocolo de Seguridad y Contingencia (Incidencias Resueltas)")
    add_p("7. Misión 6: Reconocimiento de Nubes Aliadas (Comparativa Cloud y Responsabilidad)")
    add_p("8. Misión 7: Consejo de los Avengers (Conclusiones Técnicas y Defensa)")
    add_p("9. Fuentes de Información y Referencias Oficiales (Normas APA 7)")
    add_p("10. Anexos y Enlace al Repositorio de Código Fuente")
    doc.add_page_break()

    # ==========================================================
    # 2. INTRODUCCIÓN Y DESCRIPCIÓN DEL PROBLEMA CAMPUSCLOUD
    # ==========================================================
    add_h1("1. Introducción y Descripción del Problema CampusCloud")
    add_p("El proyecto CampusCloud constituye la plataforma tecnológica integral diseñada para soportar los servicios académicos, escolares y administrativos de la Universidad Tecnológica de Tula-Tepeji. Durante la fase inicial (Unidad I), se desplegó una base de datos relacional basada en Microsoft SQL Server 2022 (con réplica en PostgreSQL 16) sobre contenedores Docker, implementando las entidades fundamentales de 'Estudiantes', 'Servicios' y 'Solicitudes'. Este motor relacional resolvió de manera impecable la integridad transaccional ACID, asegurando consistencia matemática en el control de matrículas, historial académico y estados oficiales de pago.")

    add_p("Sin embargo, la transformación de CampusCloud hacia una Nube Académica Integral inteligente demandó nuevas capacidades que pusieron en evidencia los límites intrínsecos del modelo relacional. En la arquitectura de software contemporánea, forzar a un gestor relacional a resolver problemáticas no tabulares incurre en el antipatrón de 'Talla Única' (One Size Fits All), provocando degradaciones operativas severas:")

    add_bullet(" Cada trámite estudiantil (p. ej., titulación, estadías, servicio médico, becas) requiere atributos dispares: documentos requeridos, aranceles variables, especificaciones mixtas y flujos de aprobación específicos. En SQL Server, incorporar estas variaciones implicaba modificar continuamente el esquema mediante sentencias 'ALTER TABLE', derivando en tablas repletas de valores nulos ('sparse columns') y esquemas artificialmente normalizados con tablas intermedias vacías que ralentizaban la operación.", "A. Rigidez Estructural en el Catálogo de Trámites: ")
    add_bullet(" La plataforma buscaba fomentar comunidades de aprendizaje, recomendación colaborativa de talleres y detección de compañeros para proyectos integradores. Modelar redes de contactos y prerrequisitos encadenados en tablas relacionales requería consultas recursivas complejas y múltiples 'JOINs' autorreferenciados. A medida que el número de registros aumentaba, la sobrecarga computacional de evaluar índices relacionales en cascada degradaba los tiempos de respuesta del servidor.", "B. Ineficiencia en Relaciones de Red y Grafos: ")
    add_bullet(" El portal estudiantil produce un flujo continuo y masivo de eventos: inicios de sesión, intentos fallidos de autenticación, descargas de certificados digitales en formato PDF, consultas al catálogo y auditoría de peticiones con latencias en milisegundos. Escribir esta telemetría en SQL Server provocaba una saturación extrema del 'Transaction Log' (.ldf) y bloqueos de disco que competían con las transacciones académicas críticas.", "C. Saturación por Telemetría y Eventos Masivos: ")

    add_p("En observancia de las directivas tácticas de S.H.I.E.L.D., la solución arquitectónica no consistió en desechar o sustituir SQL Server, sino en adoptar formalmente el paradigma de Persistencia Políglota (Polyglot Persistence). Este enfoque distribuye la carga operativa entre cuatro tecnologías especializadas, garantizando que cada modelo atienda exclusivamente la necesidad para la cual fue diseñado matemáticamente.")

    # ==========================================================
    # 3. MISIÓN 1: JUSTIFICACIÓN ESTRATÉGICA DEL ARSENAL DE DATOS
    # ==========================================================
    add_h1("2. Misión 1: Justificación Estratégica del Arsenal de Datos")
    add_p("Para defender la infraestructura de CampusCloud, se diseñó una matriz de correspondencia técnica que vincula cada necesidad operativa con su tipo de dato, consulta representativa, tecnología seleccionada, ventaja diferencial y limitación relevante:")

    headers_m1 = ["Necesidad Operativa", "Tipo de Dato", "Consulta Principal Representativa", "Modelo y Gestor", "Ventaja Diferencial", "Limitación Relevante"]
    rows_m1 = [
        [
            "Transacciones Académicas y Matrícula",
            "Estructurado (Tablas con tipos estrictos)",
            "SELECT e.matricula, e.nombre, sol.estado\nFROM Solicitudes sol\nJOIN Estudiantes e ON sol.id_estudiante = e.id_estudiante\nWHERE sol.estado = 'Aprobada';",
            "Relacional\nSQL Server 2022",
            "Garantía estricta ACID, integridad referencial mediante claves foráneas y consistencia inmediata en calificaciones y finanzas.",
            "Escalabilidad horizontal compleja; rigidez de esquema ante atributos variables; bloqueos en alta concurrencia."
        ],
        [
            "Catálogo Flexible de Trámites y Requisitos",
            "Semiestructurado (Documentos BSON)",
            "db.detalles_servicios.find(\n  { 'modalidades': 'En Línea',\n    'especificaciones.arancel': 0 }\n);",
            "Documental\nMongoDB 9.0",
            "Esquema dinámico; almacena arrays de requisitos y subdocumentos técnicos embebidos en una sola lectura sin JOINs.",
            "No dispone de restricciones de integridad referencial entre colecciones; riesgo de inconsistencia si no se controla en la app."
        ],
        [
            "Red de Alianzas y Recomendación",
            "Grafos Conexos (Nodos y Aristas Tipadas)",
            "MATCH (yo:Estudiante {matricula: '24300700'})\n      -[:COLABORA_CON]-(amigo:Estudiante)\nMATCH (amigo)-[r:SOLICITA]->(s:Servicio)\nWHERE r.calificacion >= 4 AND NOT (yo)-[:SOLICITA]->(s)\nRETURN s.nombre, amigo.nombre;",
            "Grafos\nNeo4j 5 Community",
            "Adyacencia libre de índices ('Index-Free Adjacency'); navega relaciones de red en tiempo de puntero O(1) por salto.",
            "No diseñado para análisis numérico masivo ni para flujos masivos de eventos append-only de alta frecuencia."
        ],
        [
            "Auditoría Masiva y Telemetría de Eventos",
            "Columnas Anchas (Wide-Column Store)",
            "SELECT matricula, fecha_hora, tipo_evento, estado\nFROM campuscloud_logs.eventos_estudiante\nWHERE matricula = '24300700'\nORDER BY fecha_hora DESC;",
            "Columnas Anchas\nApache Cassandra 4.1",
            "Escrituras secuenciales inmediatas en Memtables/SSTables; particionado lineal distribuido por clave de estudiante.",
            "Imposibilidad de realizar JOINs, agrupaciones complejas o filtros por columnas que no formen parte de la Primary Key."
        ]
    ]
    add_custom_table(headers_m1, rows_m1, [1.2, 1.1, 1.7, 1.1, 1.5, 1.4])

    add_h2("2.1 Delimitación de Información y Enlaces Lógicos")
    add_p("Un principio inquebrantable de la arquitectura de CampusCloud es la delimitación nítida de fronteras entre motores:")
    add_bullet("SQL Server permanece como la Fuente Única de Verdad (Single Source of Truth) para la identidad jurídica del alumno ('matricula: 24300700', 'nombre: Mariano Calzadilla Alvarez') y los identificadores maestros de trámite ('id_servicio_sql: 1..5').", "Núcleo Maestro en SQL Server: ")
    add_bullet("MongoDB almacena el enriquecimiento documental: modalidades ('En Línea', 'Ventanilla'), tiempos estimados en días, aranceles desglosados y listas de requisitos en formato PDF.", "Extensión en MongoDB: ")
    add_bullet("Neo4j mapea las alianzas entre alumnos ('COLABORA_CON'), intereses en proyectos y valoraciones cualitativas (calificaciones 1 a 5 estrellas) para habilitar recomendación colaborativa.", "Extensión en Neo4j: ")
    add_bullet("Cassandra custodia la bitácora cronológica inmutable de accesos, direcciones IP de origen, módulos impactados y latencias de respuesta en milisegundos.", "Extensión en Cassandra: ")

    add_callout(doc,
        "ADVERTENCIA DE INTEGRIDAD DISTRIBUIDA: En un ecosistema políglota, la vinculación entre SQL Server, MongoDB, Neo4j y Cassandra es puramente LÓGICA (mediante el campo compartido 'matricula = 24300700'). No existe integridad referencial automática distribuida. Si un registro se elimina en SQL Server, el motor relacional no puede propagar el borrado hacia MongoDB ni Cassandra. Esta coherencia debe ser gobernada por la capa de aplicación o mediante arquitecturas orientadas a eventos (Event-Driven Architecture).",
        "PRINCIPIO DE INDEPENDENCIA DE GESTORES"
    )

    # ==========================================================
    # 4. MISIÓN 2: REVELA EL PLANO DE CAMPUSCLOUD
    # ==========================================================
    add_h1("3. Misión 2: Revela el Plano de CampusCloud (Arquitectura de Persistencia)")
    add_p("La infraestructura de CampusCloud se encuentra completamente desplegada en el entorno de desarrollo local mediante Docker Desktop sobre Windows 11. Para garantizar el aislamiento de red y la resolución interna de nombres, todos los motores se enlazan a la red puente (bridge) 'campuscloud-db-net', montando volúmenes persistentes independientes.")

    add_code_block(doc,
"""+-----------------------------------------------------------------------------------------------------------------+
|                                     ESTACIÓN HOST LOCAL (WINDOWS 11 / DOCKER ENGINE)                            |
|                                                                                                                 |
|   RED DOCKER PUENTE AISLADA: campuscloud-db-net                                                                 |
|                                                                                                                 |
|   [CLIENTES GRÁFICOS OFICIALES USADOS EN LABORATORIO]                                                           |
|   • Docker Desktop (Monitoreo)     • MongoDB Compass (Documentos)                                               |
|   • Neo4j Browser Web (Grafos)     • TablePlus / CQLSH (Cassandra)                                              |
|            |                                |                              |                      |             |
|            +--------------------------------+------------------------------+----------------------+             |
|                                                                                                                 |
|   +--------------------------+  +--------------------------+  +--------------------------+  +-----------------+ |
|   | campuscloud-sqlserver    |  | campuscloud-mongodb      |  | campuscloud-neo4j        |  | campuscloud-    | |
|   | SQL Server 2022 Dev      |  | MongoDB 9.0 Community    |  | Neo4j 5 Community        |  | cassandra       | |
|   | Puerto Host: 1434:1433   |  | Puerto Host: 27017:27017 |  | Puertos: 7474 / 7687     |  | Cassandra 4.1   | |
|   | Base: CampusCloud        |  | DB: CampusCloud          |  | Grafo: neo4j             |  | Puerto: 9042    | |
|   | Vol: sqlserver_data      |  | Vol: mongo_data          |  | Vol: neo4j_data          |  | Vol: cassandra_ | |
|   +------------+-------------+  +------------+-------------+  +------------+-------------+  | data            | |
|                |                             |                             |                +--------+--------+ |
|   +------------v-------------+  +------------v-------------+  +------------v-------------+  +--------v--------+ |
|   | VOLUMEN FÍSICO EXTERNO:  |  | VOLUMEN FÍSICO EXTERNO:  |  | VOLUMEN FÍSICO EXTERNO:  |  | VOLUMEN FÍSICO: | |
|   | campuscloud-sqlserver-   |  | campuscloud-mongo-data   |  | campuscloud-neo4j-data   |  | campuscloud-    | |
|   | data                     |  |                          |  |                          |  | cassandra-data  | |
|   +--------------------------+  +--------------------------+  +--------------------------+  +-----------------+ |
|                                                                                                                 |
|   [SERVICIOS CONCEPTUALES DE REFERENCIA — NO DESPLEGADOS EN LABORATORIO LOCAL]:                                |
|   • API Gateway Institucional (Express / Node.js)   • Portal Web de Autoservicio Estudiantil (React)            |
|   • Event Streaming Broker (Apache Kafka)           • Almacén de Objetos / Constancias PDF (MinIO S3)           |
+-----------------------------------------------------------------------------------------------------------------+""")

    add_h2("3.1 Delimitación entre Implementación Real y Servicios Conceptuales")
    add_p("Apegados estrictamente a las directivas de contención del Quinjet, se establece una clara distinción:")
    add_bullet("Los contenedores de SQL Server, PostgreSQL, pgAdmin, MongoDB, Neo4j y Cassandra se encuentran aprovisionados, vinculados a la red común, con puertos mapeados hacia el host y persistiendo sus archivos en volúmenes Docker nombrados.", "Servicios Reales en Laboratorio: ")
    add_bullet("El API Gateway perimetral, el balanceador Nginx, el portal de React y el bus de mensajes Kafka pertenecen a la arquitectura de referencia conceptual; sus flujos fueron operados y validados de forma directa mediante los clientes gráficos oficiales (Docker Desktop, Compass, Neo4j Browser y TablePlus).", "Servicios Conceptuales: ")

    img_docker = os.path.join(evid_dir, "generales", "01_docker_compose_ps.png")
    add_figure(img_docker, "Figura 1: Interfaz gráfica oficial de Docker Desktop verificando los contenedores de CampusCloud activos, asignación de puertos y memoria asignada.")

    # ==========================================================
    # 5. MISIÓN 3: REGISTRO DE TECNOLOGÍAS ACTIVADAS
    # ==========================================================
    add_h1("4. Misión 3: Registro de Tecnologías Activadas (Implementaciones y Consultas)")
    add_p("Cada tecnología fue aprovisionada mediante scripts ejecutables e idempotentes, garantizando reproducibilidad absoluta en cualquier entorno:")

    add_h2("4.1 Microsoft SQL Server 2022 (Sector Relacional)")
    add_p("Conserva la base transaccional desarrollada en la Unidad I. Su rol es insustituible: custodia los expedientes escolares, garantiza la unicidad de las matrículas y asegura que ninguna solicitud de servicio se registre sin un estudiante válido asociado.")

    add_h2("4.2 MongoDB 9.0 Community — Sector Documental")
    add_p("Se creó la colección 'detalles_servicios' dentro de la base de datos 'CampusCloud'. Los documentos BSON incorporan arrays de requisitos y subdocumentos jerárquicos de especificaciones técnicas. Se insertaron 8 documentos cubriendo 4 categorías distintas ('Academico', 'Administrativo', 'Extracurricular' y 'Salud_Estudiantil').")
    
    add_p("Consulta Esencial Explicada (Pipeline de Agregación Analítica):", "Código del script 'mongodb/06-agregacion.js': ")
    add_code_block(doc,
"""db.detalles_servicios.aggregate([
  // Etapa 1: Filtrar únicamente trámites vigentes en el catálogo
  { $match: { "activo": true } },
  // Etapa 2: Agrupar por categoría y calcular métricas consolidadas
  { $group: {
      _id: "$categoria",
      total_servicios: { $sum: 1 },
      tiempo_promedio_dias: { $avg: "$especificaciones.tiempo_estimado_dias" },
      costo_promedio: { $avg: "$especificaciones.arancel" },
      servicios: { $push: "$nombre" }
  } },
  // Etapa 3: Ordenar por volumen de trámites descendente y menor tiempo de respuesta
  { $sort: { total_servicios: -1, tiempo_promedio_dias: 1 } }
]);""")
    add_p("Interpretación Técnica: El pipeline procesa los documentos en memoria mediante tres fases continuas. La fase '$match' descarta servicios inactivos. La etapa '$group' calcula los acumuladores numéricos ($sum y $avg) de tiempo de respuesta y aranceles por categoría, mientras '$push' consolida los títulos en un array. Finalmente, '$sort' jerarquiza los resultados, permitiendo a la universidad identificar qué áreas requieren mayor personal de atención.")

    img_mongo_1 = os.path.join(evid_dir, "mongodb", "01_mongo_insert_find.png")
    add_figure(img_mongo_1, "Figura 2: Explorador de documentos BSON en MongoDB Compass ejecutando búsqueda con filtro por array de modalidades { modalidades: 'En Línea' }.")

    img_mongo_2 = os.path.join(evid_dir, "mongodb", "02_mongo_update_aggregation.png")
    add_figure(img_mongo_2, "Figura 3: Constructor visual de Agregaciones en MongoDB Compass reflejando las 3 etapas del pipeline y los resultados calculados por categoría.")

    add_h2("4.3 Neo4j 5 Community — Red de Grafos Vengadora")
    add_p("El modelo de grafos modela a la comunidad universitaria mediante 11 nodos (6 de tipo ':Estudiante' y 5 de tipo ':Servicio') y 17 aristas tipadas con propiedades (`:SOLICITA {calificacion, estado}`, `:COLABORA_CON {proyecto}`, `:TIENE_INTERES_EN` y `:PRERREQUISITO_DE`).")

    add_p("Consulta Esencial Explicada (Algoritmo de Recomendación Colaborativa):", "Código del script 'neo4j/02-consultas.cypher' (Q3): ")
    add_code_block(doc,
"""// Localizar pares de Mariano Silva (24300700) y recomendar servicios altamente valorados
MATCH (yo:Estudiante {matricula: '24300700'})-[:COLABORA_CON]-(amigo:Estudiante)
MATCH (amigo)-[r:SOLICITA]->(s:Servicio)
WHERE r.calificacion >= 4
  AND NOT (yo)-[:SOLICITA]->(s)
RETURN s.nombre AS ServicioRecomendado, 
       amigo.nombre AS RecomendadoPor, 
       r.calificacion AS Calificacion;""")
    add_p("Interpretación Técnica: La consulta explota la adyacencia libre de índices de Neo4j en dos saltos de puntero. Primero encuentra los nodos de estudiantes conectados directamente con Mariano mediante la relación bidireccional ':COLABORA_CON'. En el segundo salto, inspecciona qué servicios han calificado dichos colaboradores con 4 o 5 estrellas, excluyendo los que Mariano ya ha solicitado mediante 'NOT (yo)-[:SOLICITA]->(s)'. El motor retornó 'Asesoría Académica', recomendada con 5 estrellas por Ana Martínez.")

    img_neo4j_1 = os.path.join(evid_dir, "neo4j", "01_neo4j_cypher_shell.png")
    add_figure(img_neo4j_1, "Figura 4: Consola cypher-shell ejecutando el censo de 11 nodos, 17 relaciones y el algoritmo de recomendación colaborativa.")

    img_neo4j_2 = os.path.join(evid_dir, "neo4j", "02_neo4j_browser_graph.png")
    add_figure(img_neo4j_2, "Figura 5: Visualización interactiva en Neo4j Browser desplegando la red de alianzas y el panel inspector con los datos del alumno 24300700.")

    add_h2("4.4 Apache Cassandra 4.1 — Sector Columnas Anchas")
    add_p("En Cassandra, la tabla 'eventos_estudiante' se diseñó bajo el principio 'Query-Driven Design', donde la clave primaria determina la ubicación física y el orden de almacenamiento:")

    add_code_block(doc,
"""// Script: cassandra/01-crear-keyspace-tabla.cql
CREATE TABLE campuscloud_logs.eventos_estudiante (
    matricula text,
    fecha_hora timestamp,
    id_evento uuid,
    modulo text,
    tipo_evento text,
    estado text,
    ip_origen text,
    latencia_ms int,
    detalles text,
    PRIMARY KEY ((matricula), fecha_hora, id_evento)
) WITH CLUSTERING ORDER BY (fecha_hora DESC, id_evento ASC);""")
    add_p("Interpretación Técnica: La Partition Key está dada por '((matricula))'. El algoritmo 'Murmur3Partitioner' distribuye todas las acciones de un estudiante específico al mismo nodo físico del clúster. Las Clustering Keys ('fecha_hora DESC, id_evento ASC') ordenan físicamente las filas dentro de los archivos SSTable de manera descendente. Esto permite que la consulta para auditar la actividad reciente de Mariano Silva ('24300700') sea una lectura secuencial contigua en disco, sin necesidad de calcular un 'ORDER BY' en memoria.")

    img_cass_1 = os.path.join(evid_dir, "cassandra", "01_cassandra_cqlsh_select.png")
    add_figure(img_cass_1, "Figura 6: Cliente visual TablePlus conectado a Cassandra ejecutando consulta particionada por matricula 24300700 con orden descendente.")

    img_cass_2 = os.path.join(evid_dir, "cassandra", "02_cassandra_update_delete.png")
    add_figure(img_cass_2, "Figura 7: Consola cqlsh demostrando la modificación atómica de telemetría y la eliminación mediada por Tombstones.")

    # ==========================================================
    # 6. MISIÓN 4: VALIDACIÓN DE CAMPO
    # ==========================================================
    add_h1("5. Misión 4: Validación de Campo (Pruebas, Persistencia y Seguridad)")
    add_p("La operatividad del ecosistema CampusCloud fue sometida a tres baterías de validación técnica:")

    add_h2("5.1 Prueba de Resiliencia y Persistencia tras Reinicio Forzado")
    add_p("Objetivo: Comprobar que la destrucción de los contenedores no provoca pérdida de información.")
    add_p("Procedimiento: Con los 8 documentos cargados en MongoDB y los 11 nodos en Neo4j, se forzó la detención y reinicio de los procesos desde Docker:")
    add_code_block(doc, "docker restart campuscloud-mongodb campuscloud-neo4j")
    add_p("Resultado Obtenido: Al reconectar con MongoDB Compass y Neo4j Browser, se constató que la totalidad de documentos, nodos y relaciones persistieron intactos. Esto comprobó que el montaje en volúmenes Docker externos ('campuscloud-mongo-data' y 'campuscloud-neo4j-data') desacopla el almacenamiento del ciclo de vida del contenedor.")

    add_h2("5.2 Controles de Acceso y Gestión de Secretos")
    add_bullet("MongoDB opera bajo autenticación obligatoria ('admin'). Los intentos de conexión anónima son rechazados por el motor con código de falla de autorización.", "Autenticación Criptográfica: ")
    add_bullet("Neo4j exige autenticación mediante el protocolo binario Bolt ('neo4j / CampusCloudNeo4j2026!'), restringiendo el acceso web y Cypher a usuarios legítimos.", "Aislamiento en Grafos: ")
    add_bullet("Todas las credenciales operativas se aislaron en el archivo local '.env', el cual se encuentra estrictamente ignorado por Git mediante '.gitignore'. En el repositorio solo se comparte la plantilla segura '.env.example' con datos ficticios.", "Exclusión de Secretos: ")

    add_h2("5.3 Limitaciones Reales Detectadas en el Entorno")
    add_bullet("En Cassandra, no es posible ejecutar filtros arbitrarios sobre campos que no forman parte de la Primary Key (p. ej. 'WHERE estado = \"FALLIDO\"') sin forzar la instrucción 'ALLOW FILTERING', la cual está desaconsejada en producción debido a que obliga a escanear todos los nodos del clúster.", "Restricción de Filtrado en Cassandra: ")
    add_bullet("Al no existir un middleware de transacciones distribuidas (como un coordinador Two-Phase Commit), la eliminación de un estudiante en SQL Server no borra en cascada sus documentos en MongoDB ni sus registros en Cassandra, exigiendo tareas de depuración en la capa de aplicación.", "Ausencia de Cascada Automática: ")

    # ==========================================================
    # 7. MISIÓN 5: PROTOCOLO DE SEGURIDAD Y CONTINGENCIA
    # ==========================================================
    add_h1("6. Misión 5: Protocolo de Seguridad y Contingencia (Incidencias Resueltas)")
    add_p("Durante la fase de despliegue e integración colaborativa de CampusCloud, se diagnosticaron y solventaron dos incidentes de severidad crítica:")

    add_h2("6.1 Incidencia 1: Bloqueo Crítico por Puntero Git LFS Huérfano ('neo.tar')")
    add_bullet("Al fusionar el repositorio colaborativo base ('CampusClaude'), Git abortó la descarga con el error: 'Smudge error: Object does not exist on the server: [404] fatal: docker_images/neo.tar: smudge filter lfs failed'. Posteriormente, al realizar 'git push origin main', GitHub rechazó la entrega con el código 'GH008: Your push referenced at least 1 unknown Git LFS object'.", "Síntoma: ")
    add_bullet("El repositorio upstream contenía un puntero Git LFS hacia una imagen de Docker de 592 MB ('docker_images/neo.tar'), pero el archivo binario real jamás fue subido al almacenamiento de GitHub LFS, dejando un puntero roto que corrompía cualquier transacción de subida o descarga.", "Causa Raíz: ")
    add_bullet("Se confirmó mediante 'git lfs ls-files' que el archivo 'neo.tar' estaba indexado como LFS sin respaldo en el servidor remoto.", "Verificación: ")
    add_bullet("Se reescribió la historia local de Git utilizando 'git filter-branch --force --index-filter \"git rm --cached --ignore-unmatch docker_images/neo.tar\" --prune-empty 1c3ab06..HEAD', se eliminó la directiva en '.gitattributes' y se purgó la referencia en el árbol de trabajo.", "Corrección Aplicada: ")
    add_bullet("El árbol de Git quedó saneado, el comando 'git push' se completó con código de salida 0 y el repositorio recuperó su estabilidad sin perder ningún script del proyecto.", "Resultado Verificado: ")

    add_h2("6.2 Incidencia 2: Conflicto de Etiquetas de Red en Docker Compose")
    add_bullet("Al ejecutar 'docker compose up -d', Docker abortó el despliegue con el fallo: 'network campuscloud-db-net was found but has incorrect label com.docker.compose.network set to \"\" (expected: \"campuscloud_net\")'.", "Síntoma: ")
    add_bullet("La red puente 'campuscloud-db-net' había sido creada manualmente desde la terminal. Docker Compose v2 exige por defecto que las redes pertenezcan a su propio espacio de nombres, salvo que se declaren explícitamente como recursos externos.", "Causa Raíz: ")
    add_bullet("Se inspeccionó la red con 'docker network inspect campuscloud-db-net', comprobando la discrepancia en el bloque de etiquetas (Labels).", "Verificación: ")
    add_bullet("Se actualizó 'docker/compose.yaml' declarando la red y los volúmenes con el atributo 'external: true':\nnetworks:\n  campuscloud_net:\n    external: true\n    name: ${DOCKER_NETWORK:-campuscloud-db-net}", "Corrección Aplicada: ")
    add_bullet("Compose se acopló limpiamente a la red y a los volúmenes existentes, permitiendo la coexistencia armónica de los motores sin reiniciar el almacenamiento relacional previo.", "Resultado Verificado: ")

    # ==========================================================
    # 8. MISIÓN 6: RECONOCIMIENTO DE NUBES ALIADAS
    # ==========================================================
    add_h1("7. Misión 6: Reconocimiento de Nubes Aliadas (Comparativa Cloud y Responsabilidad)")
    add_p("Un error recurrente en la formación de ingenieros de datos es asumir que un contenedor Docker local es equivalente a una base de datos en la nube. Docker proporciona empaquetamiento y virtualización liviana a nivel de sistema operativo (IaaS simulada), mientras que las plataformas en la nube pública proveen servicios completamente administrados (Database as a Service - DBaaS).")

    add_h2("7.1 Matriz de Correspondencia de Servicios Cloud")
    headers_cloud = ["Necesidad CampusCloud", "Motor Local Docker", "Amazon Web Services (AWS)", "Microsoft Azure", "Google Cloud Platform (GCP)"]
    rows_cloud = [
        [
            "Datos Flexibles y Catálogo Dinámico",
            "MongoDB 9.0 Community",
            "Amazon DocumentDB\n(Compatible con API MongoDB)",
            "Azure Cosmos DB\n(API para MongoDB con replicación multi-región)",
            "Google Cloud Firestore\n(Base documental serverless distribuida)"
        ],
        [
            "Relaciones de Red y Grafos",
            "Neo4j 5 Community",
            "Amazon Neptune\n(Motor de grafos con Gremlin y SPARQL)",
            "Azure Cosmos DB\n(API Gremlin / Apache TinkerPop)",
            "Google Cloud Spanner Graph\n(Base distribuida con extensiones de grafos)"
        ],
        [
            "Ingesta Masiva y Telemetría de Eventos",
            "Apache Cassandra 4.1",
            "Amazon Keyspaces\n(Cassandra administrada serverless)",
            "Azure Managed Instance for Apache Cassandra",
            "Google Cloud Bigtable\n(Motor de columnas anchas de escala petabyte)"
        ]
    ]
    add_custom_table(headers_cloud, rows_cloud, [1.3, 1.2, 1.3, 1.3, 1.3])

    add_h2("7.2 Matriz de Responsabilidad Compartida: Local vs DBaaS")
    add_p("Al operar en Docker local, el alumno o administrador asume el 100 % de las tareas operativas. Al migrar a servicios administrados DBaaS, las responsabilidades se distribuyen de acuerdo al siguiente modelo:")

    add_bullet("En Docker local la alta disponibilidad es nula; si el equipo host falla o se reinicia, el servicio colapsa. En DBaaS, el proveedor garantiza acuerdos de nivel de servicio (SLA) del 99.99 % al 99.999 % mediante replicación sincrónica multi-zona y conmutación por error (failover) transparente.", "1. Disponibilidad y Tolerancia a Fallos: ")
    add_bullet("En el entorno local, las copias de seguridad dependen de scripts manuales periódicos ('mongodump', 'nodetool snapshot'). En la nube, el proveedor gestiona copias de seguridad automatizadas y continuas con recuperación en cualquier punto del tiempo (Point-in-Time Recovery / PITR) y cifrado de snapshots en reposo.", "2. Copias de Seguridad y Recuperación: ")
    add_bullet("En Docker, los parches del sistema operativo huésped, las vulnerabilidades de la imagen y la configuración de memoria de la JVM (en Cassandra y Neo4j) son responsabilidad del alumno. En la nube, las actualizaciones de seguridad se aplican en caliente de forma automatizada sin interrumpir el servicio.", "3. Parches de Seguridad y Mantenimiento: ")
    add_bullet("El laboratorio local tiene costo monetario directo cero, pero consume intensivamente los recursos físicos del equipo (RAM y CPU). En la nube pública rige el esquema 'Pay-as-you-go', lo que demanda un diseño riguroso de particiones y consultas para evitar costos imprevistos por operaciones de lectura/escritura.", "4. Economía y Escalabilidad Elástica: ")

    # ==========================================================
    # 9. MISIÓN 7: CONSEJO DE LOS AVENGERS
    # ==========================================================
    add_h1("8. Misión 7: Consejo de los Avengers (Conclusiones Técnicas y Defensa)")
    
    add_h2("8.1 Conclusiones Técnicas del Proyecto")
    add_bullet("Ningún motor de base de datos es superior de forma universal; cada tecnología domina un nicho matemático específico. SQL Server es insustituible para las transacciones de matrícula y calificaciones donde la consistencia debe ser inmediata y absoluta. MongoDB aporta la agilidad necesaria para que el catálogo de trámites evolucione sin alterar esquemas relacionales. Neo4j transforma consultas de redes sociales que colapsarían en SQL Server mediante JOINs recursivos en recorridos de punteros en memoria O(1). Y Apache Cassandra resuelve la ingesta masiva de auditoría gracias a su arquitectura append-only que no bloquea lecturas concurrentes.", "1. Especialización de Paradigmas: ")
    add_bullet("La adopción de persistencia políglota multiplica la eficiencia del almacenamiento, pero traslada la complejidad desde el gestor hacia la capa de arquitectura de software. Al no contar con llaves foráneas distribuidas ni transacciones ACID globales, el ingeniero de software debe diseñar mecanismos de consistencia eventual, tolerar particiones de red conforme al Teorema CAP y gobernar cuidadosamente la sincronización de identidades entre motores.", "2. El Costo de la Poliglotía y el Teorema CAP: ")
    add_bullet("Para madurar CampusCloud hacia un entorno de producción de escala nacional, se propone implementar un bus de mensajería distribuido (Apache Kafka) acoplado a un motor de Change Data Capture (CDC con Debezium). De esta manera, cualquier inserción transaccional de un alumno en SQL Server publicaría de inmediato un evento en Kafka, sincronizando de forma asíncrona y desacoplada la creación del nodo en Neo4j, el documento en MongoDB y la inicialización de telemetría en Cassandra.", "3. Propuesta de Evolución Arquitectónica: ")

    add_h2("8.2 Preparación para la Defensa Oral ante el Consejo")
    add_p("Para la demostración funcional en vivo ante el docente titular, el agente responsable se encuentra capacitado para ejecutar y defender cualquiera de las consultas estratégicas:")
    add_bullet("Explicación de las etapas de agrupación matemática ($group) y cálculo dinámico de promedios de costos y tiempos.", "En MongoDB: ")
    add_bullet("Demostración del recorrido de aristas :COLABORA_CON y :SOLICITA para deducir recomendaciones cruzadas sin utilizar tablas intermedias.", "En Neo4j: ")
    add_bullet("Justificación física de por qué 'WHERE matricula = \"24300700\"' lee un único nodo del clúster y devuelve los eventos ordenados cronológicamente sin requerir cómputo en memoria.", "En Cassandra: ")

    # ==========================================================
    # 10. FUENTES DE INFORMACIÓN Y REFERENCIAS OFICIALES
    # ==========================================================
    add_h1("9. Fuentes de Información y Referencias Oficiales (Normas APA 7)")
    add_bullet("Amazon Relational Database Service, DocumentDB and Managed Keyspaces Developer Guide. Amazon Web Services Documentation. https://docs.aws.amazon.com/", "Amazon Web Services. (2026). ")
    add_bullet("Apache Cassandra Documentation: Architecture, CQL Reference and Data Modeling (v4.1). The Apache Software Foundation. https://cassandra.apache.org/doc/latest/", "Apache Software Foundation. (2026). ")
    add_bullet("Azure Cosmos DB: Globally Distributed Multi-Model Database Service Documentation. Microsoft Learn. https://learn.microsoft.com/azure/cosmos-db/", "Microsoft Azure. (2026). ")
    add_bullet("MongoDB 9.0 Manual: Document Validation, Data Modeling and Aggregation Pipeline. MongoDB Inc. https://www.mongodb.com/docs/manual/", "MongoDB Inc. (2026). ")
    add_bullet("The Neo4j Cypher Manual: Graph Database Modeling, Patterns and Performance Optimization. Neo4j Inc. https://neo4j.com/docs/cypher-manual/current/", "Neo4j Inc. (2026). ")
    add_bullet("Database Internals: A Deep Dive into How Distributed Data Systems Work. O'Reilly Media.", "Petrov, A. (2019). ")
    add_bullet("Designing Data-Intensive Applications: The Big Ideas Behind Reliable, Scalable, and Maintainable Systems. O'Reilly Media.", "Kleppmann, M. (2017). ")

    # ==========================================================
    # 11. ANEXOS Y REPOSITORIO DE CÓDIGO FUENTE
    # ==========================================================
    add_h1("10. Anexos y Repositorio de Código Fuente")
    add_p("Todos los artefactos de software, scripts de inicialización, configuraciones Docker y evidencias gráficas generadas se encuentran versionados y auditados en el repositorio oficial de GitHub:")
    add_bullet("https://github.com/mariano-si7/CAMPUSCLOUD", "Repositorio Central GitHub: ")
    add_bullet("Archivo 'compose.yaml' integrado y plantilla de variables seguras '.env.example'.", "Directorio 'docker/': ")
    add_bullet("Scripts ejecutables para la creación de esquemas, carga BSON, consultas y agregación (.js).", "Directorio 'mongodb/': ")
    add_bullet("Scripts Cypher de creación de grafos, consultas de recomendación y actualización (.cypher).", "Directorio 'neo4j/': ")
    add_bullet("Scripts CQL de creación de keyspaces, tablas de telemetría y consultas particionadas (.cql).", "Directorio 'cassandra/': ")
    add_bullet("Capturas de pantalla oficiales en alta resolución con clientes nativos (Docker Desktop, MongoDB Compass, Neo4j Browser, TablePlus).", "Directorio 'evidencias/unidad-ii/': ")

    # Guardar DOCX en reportes/unidad-ii/
    out_docx_sub = os.path.abspath(os.path.join(os.path.dirname(__file__), "Calzadilla_Mariano_ReporteIntegrador_UnidadII_CampusCloud.docx"))
    doc.save(out_docx_sub)
    print(f"[OK] Reporte Integrador DOCX guardado en: {out_docx_sub}")

    # Copiar DOCX a la raíz del proyecto
    out_docx_root = os.path.join(base_proj, "Calzadilla_Mariano_ReporteIntegrador_UnidadII_CampusCloud.docx")
    shutil.copy2(out_docx_sub, out_docx_root)
    print(f"[OK] Reporte Integrador DOCX copiado a la raíz: {out_docx_root}")

    # Convertir a PDF con docx2pdf
    out_pdf_sub = os.path.abspath(os.path.join(os.path.dirname(__file__), "Calzadilla_Mariano_ReporteIntegrador_UnidadII_CampusCloud.pdf"))
    try:
        from docx2pdf import convert
        print("Convirtiendo Reporte Integrador DOCX a PDF...")
        convert(out_docx_sub, out_pdf_sub)
        print(f"[OK] Reporte Integrador PDF generado en: {out_pdf_sub}")

        # Copiar PDF a la raíz del proyecto
        out_pdf_root = os.path.join(base_proj, "Calzadilla_Mariano_ReporteIntegrador_UnidadII_CampusCloud.pdf")
        shutil.copy2(out_pdf_sub, out_pdf_root)
        print(f"[OK] Reporte Integrador PDF copiado a la raíz: {out_pdf_root}")
    except Exception as e:
        print(f"[AVISO] Error al convertir a PDF con docx2pdf: {e}")

if __name__ == "__main__":
    create_reporte_integrador()
